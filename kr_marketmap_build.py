#!/usr/bin/env python3
"""한국 마켓맵 데이터 빌더 — 코스피/코스닥 트리맵용 (2026-08-20 신설).

TradingView 임베드 위젯이 KRX 데이터 미지원이라 자체 구축 (BT 결정).

데이터 소스:
  1) KRX OpenAPI stk_bydd_trd / ksq_bydd_trd — 종목별 종가·등락률·시가총액
     (kr_breadth 파이프라인과 동일 엔드포인트·인증. Actions secrets KRX_AUTH_KEY)
  2) 네이버 금융 업종 페이지 — 업종 분류 (KRX API 에는 업종 정보 없음)
     finance.naver.com/sise/sise_group.naver?type=upjong (목록, euc-kr)
     → sise_group_detail.naver?type=upjong&no=N (업종별 종목코드)
     네이버-on-Actions 는 kr_futures_flow 에서 검증됨.

기간 수익률: 당일 + 5개 앵커일(1주/1개월/3개월/6개월/1년 전 거래일) 종가 스냅샷으로 계산.
  달력일 기준 이동 후 휴일이면 하루씩 후퇴 (최대 7일).

출력: data/kr_marketmap.json
  { updated, base_date, anchor_dates: {p:날짜},
    sectors: [업종명...],
    stocks: [[code, name, mkt(0=KP,1=KQ), sector_idx(-1=미분류), mktcap_eok,
              r1d, r1w, r1m, r3m, r6m, r1y], ...] }   # r은 %, null 가능

사용법:
  py kr_marketmap_build.py --probe    # KRX 필드/네이버 파싱 확인
  py kr_marketmap_build.py --build    # 풀 빌드 (cron 용)
"""
import argparse
import json
import re
import time
import urllib.request
import urllib.error
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
OUT_PATH = DATA_DIR / "kr_marketmap.json"

HOST = "https://data-dbg.krx.co.kr"
KOSPI_EP = "/svc/apis/sto/stk_bydd_trd"
KOSDAQ_EP = "/svc/apis/sto/ksq_bydd_trd"

AUTH_KEY = os.environ.get("KRX_AUTH_KEY") or ""
KEY_FILE = SCRIPT_DIR / ".krx_auth_key"
if not AUTH_KEY and KEY_FILE.exists():
    AUTH_KEY = KEY_FILE.read_text(encoding="utf-8").strip()

NAVER_UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36",
            "Referer": "https://finance.naver.com/sise/"}

# 기간: (키, 달력일 오프셋)
PERIODS = [("1w", 7), ("1m", 30), ("3m", 91), ("6m", 182), ("1y", 365)]

KST = timezone(timedelta(hours=9))


def _log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


# ---------------- KRX ----------------

def krx_fetch_day(bas_dd):
    """KOSPI+KOSDAQ 한 일자. rows(list of dict, _mkt 태깅) 또는 None(휴일/장애)."""
    if not AUTH_KEY:
        raise SystemExit("[ERROR] KRX_AUTH_KEY 미설정")
    rows = []
    fail = 0
    for mkt, ep in ((0, KOSPI_EP), (1, KOSDAQ_EP)):
        url = f"{HOST}{ep}?basDd={bas_dd}"
        req = urllib.request.Request(url, headers={"AUTH_KEY": AUTH_KEY, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                j = json.loads(r.read().decode("utf-8"))
        except Exception as e:
            _log(f"  krx {ep} {bas_dd} fail: {e}")
            fail += 1
            continue
        ob = j.get("OutBlock_1") or []
        if not ob:
            fail += 1
            continue
        for row in ob:
            row["_mkt"] = mkt
        rows.extend(ob)
        time.sleep(0.1)
    return rows if fail < 2 else None


def latest_trading_day(max_back=7):
    """오늘(KST)부터 후퇴하며 첫 거래일 + rows 반환."""
    d = datetime.now(KST).date()
    for _ in range(max_back):
        bas = d.strftime("%Y%m%d")
        rows = krx_fetch_day(bas)
        if rows:
            return bas, rows
        d -= timedelta(days=1)
    raise SystemExit("[ERROR] 최근 거래일 탐색 실패")


def anchor_close_map(base_date, offset_days, max_back=7):
    """base_date - offset 달력일에서 후퇴하며 첫 거래일의 {code: close} 맵."""
    d = datetime.strptime(base_date, "%Y%m%d").date() - timedelta(days=offset_days)
    for _ in range(max_back):
        bas = d.strftime("%Y%m%d")
        rows = krx_fetch_day(bas)
        if rows:
            m = {}
            for r in rows:
                code = _short_code(r.get("ISU_CD", ""))
                try:
                    close = float(str(r.get("TDD_CLSPRC", "0")).replace(",", ""))
                except Exception:
                    continue
                if code and close > 0:
                    m[code] = close
            return bas, m
        d -= timedelta(days=1)
    return None, {}


def _short_code(isu_cd):
    """KRX ISU_CD → 6자리 단축코드. 12자리 표준코드(KR7005930003)면 4:10 추출."""
    s = str(isu_cd).strip()
    if len(s) == 6:
        return s
    if len(s) == 12 and s.startswith("KR"):
        return s[3:9]
    return s[-6:] if len(s) >= 6 else s


def _num(v):
    try:
        return float(str(v).replace(",", ""))
    except Exception:
        return None


# ---------------- 네이버 업종 ----------------

def naver_get(url):
    req = urllib.request.Request(url, headers=NAVER_UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode("euc-kr", errors="replace")


def fetch_sector_map():
    """{종목코드: 업종명}. 네이버 업종 목록 → 각 업종 상세."""
    html = naver_get("https://finance.naver.com/sise/sise_group.naver?type=upjong")
    groups = re.findall(r"sise_group_detail\.naver\?type=upjong&no=(\d+)\">([^<]+)</a>", html)
    _log(f"  네이버 업종 {len(groups)}개")
    sector_of = {}
    for no, name in groups:
        name = name.strip()
        try:
            d = naver_get(f"https://finance.naver.com/sise/sise_group_detail.naver?type=upjong&no={no}")
        except Exception as e:
            _log(f"  업종 {name} fail: {e}")
            continue
        for code in re.findall(r"/item/main\.naver\?code=(\d{6})", d):
            sector_of.setdefault(code, name)
        time.sleep(0.08)
    _log(f"  업종 매핑 종목 {len(sector_of)}개")
    return sector_of


# ---------------- Build ----------------

def cmd_probe():
    print(f"[probe] AUTH_KEY len={len(AUTH_KEY)}")
    bas, rows = latest_trading_day()
    print(f"[probe] 최근 거래일 {bas}, rows={len(rows)}")
    r0 = rows[0]
    print("[probe] 첫 row keys:", sorted(r0.keys()))
    print("[probe] 첫 row:", json.dumps(r0, ensure_ascii=False)[:400])
    kp = [r for r in rows if r["_mkt"] == 0]
    print(f"[probe] KOSPI {len(kp)} / KOSDAQ {len(rows)-len(kp)}")
    html = naver_get("https://finance.naver.com/sise/sise_group.naver?type=upjong")
    groups = re.findall(r"sise_group_detail\.naver\?type=upjong&no=(\d+)\">([^<]+)</a>", html)
    print(f"[probe] 네이버 업종 {len(groups)}개, 앞 5개: {groups[:5]}")


def cmd_build():
    run_start = datetime.now(KST)
    _log("== kr_marketmap build ==")
    base_date, rows = latest_trading_day()
    _log(f"기준일 {base_date}, 종목 {len(rows)}")

    anchors = {}
    anchor_maps = {}
    for key, off in PERIODS:
        ad, amap = anchor_close_map(base_date, off)
        anchors[key] = ad
        anchor_maps[key] = amap
        _log(f"앵커 {key}: {ad} ({len(amap)}종목)")

    sector_of = fetch_sector_map()

    sectors = []
    sector_idx = {}
    stocks = []
    skipped = 0
    for r in rows:
        code = _short_code(r.get("ISU_CD", ""))
        name = str(r.get("ISU_NM", "")).strip()
        close = _num(r.get("TDD_CLSPRC"))
        rt = _num(r.get("FLUC_RT"))
        mktcap = _num(r.get("MKTCAP"))
        vol = _num(r.get("ACC_TRDVOL")) or 0
        if not code or not name or not close or close <= 0 or not mktcap or mktcap <= 0:
            skipped += 1
            continue
        # 스팩/우선주 노이즈 최소 필터는 하지 않음 — 한경도 전종목 표시
        sec = sector_of.get(code)
        if sec is None:
            si = -1
        else:
            if sec not in sector_idx:
                sector_idx[sec] = len(sectors)
                sectors.append(sec)
            si = sector_idx[sec]
        rets = [rt if rt is not None else None]
        for key, _off in PERIODS:
            prev = anchor_maps[key].get(code)
            rets.append(round((close / prev - 1) * 100, 2) if prev and prev > 0 else None)
        stocks.append([code, name, r["_mkt"], si,
                       int(round(mktcap / 1e8)),  # 억원
                       *[None if x is None else round(x, 2) for x in rets]])

    out = {
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "base_date": base_date,
        "anchor_dates": anchors,
        "periods": ["1d"] + [k for k, _ in PERIODS],
        "sectors": sectors,
        "stocks": stocks,
    }
    # sanity: 코스피 500+ 코스닥 800+ 필수, 업종 매핑률 60%+
    kp_n = sum(1 for s in stocks if s[2] == 0)
    kq_n = len(stocks) - kp_n
    mapped = sum(1 for s in stocks if s[3] >= 0)
    _log(f"KOSPI {kp_n} / KOSDAQ {kq_n} / 업종매핑 {mapped}/{len(stocks)} / skip {skipped}")
    assert kp_n > 500 and kq_n > 800, "종목 수 이상 — 저장 중단"
    assert mapped / max(1, len(stocks)) > 0.6, "업종 매핑률 저조 — 저장 중단"

    tmp = OUT_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    json.loads(tmp.read_text(encoding="utf-8"))
    tmp.replace(OUT_PATH)
    _log(f"저장 {OUT_PATH} ({OUT_PATH.stat().st_size/1024:.0f}KB, {(datetime.now(KST)-run_start).seconds}s)")


def main():
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--probe", action="store_true")
    g.add_argument("--build", action="store_true")
    args = p.parse_args()
    if args.probe:
        cmd_probe()
    else:
        cmd_build()


if __name__ == "__main__":
    main()
