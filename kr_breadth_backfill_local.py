#!/usr/bin/env python3
"""
KR Breadth Backfill — KRX OpenAPI raw HTTP 방식
==========================================
Phase B — 종목별 일별매매정보 endpoint를 활용해 KR ADR + NH/NL 동시 산출.
pykrx 의존 X → 미국 IP에서도 동작 → GitHub Actions 자동화 가능.

데이터 소스 (probe 검증 완료 — 핵심 필드 8/8):
  - KOSPI:  /svc/apis/sto/stk_bydd_trd  (~950 종목)
  - KOSDAQ: /svc/apis/sto/ksq_bydd_trd  (~1820 종목)

산출:
  ADR(20일)   = Σ(20일 상승종목수) / Σ(20일 하락종목수) × 100
  NH%(252일) = 그 날 close ≥ rolling-252 max인 종목 비율 (%)
  NL%(252일) = 그 날 close ≤ rolling-252 min인 종목 비율 (%)

출력 — data/kr_breadth.json:
  {
    "generated_at": "...Z",
    "source": "KRX OpenAPI - 종목별 일별매매정보 (KOSPI + KOSDAQ)",
    "data": [
      {"date": "YYYY-MM-DD", "adv": ..., "dec": ..., "unc": ...,
       "adr": ..., "nh_pct": ..., "nl_pct": ..., "n_traded": ...},
      ...
    ]
  }

CLI:
  py kr_breadth_backfill_local.py --probe                          # 1일치 응답 확인
  py kr_breadth_backfill_local.py --backfill 20100104 20260428    # 풀 백필 (사용자 로컬 권장)
  py kr_breadth_backfill_local.py --update                        # 최근 260영업일만 incremental (Actions용)

전제: .krx_auth_key 또는 KRX_AUTH_KEY 환경변수
필요 패키지: pandas (rolling 계산)
"""
import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
OUT_PATH = DATA_DIR / "kr_breadth.json"

AUTH_KEY = os.environ.get("KRX_AUTH_KEY") or ""
KEY_FILE = SCRIPT_DIR / ".krx_auth_key"
if not AUTH_KEY and KEY_FILE.exists():
    AUTH_KEY = KEY_FILE.read_text(encoding="utf-8").strip()

HOST = "https://data-dbg.krx.co.kr"
KOSPI_EP  = "/svc/apis/sto/stk_bydd_trd"
KOSDAQ_EP = "/svc/apis/sto/ksq_bydd_trd"
WINDOW_ADR = 20
WINDOW_52W = 252


# ---------------- HTTP ----------------

def http_get(url, headers, timeout=30):
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        return e.code, (e.read().decode("utf-8", errors="replace") if e.fp else "")
    except Exception as e:
        return -1, str(e)


def call_endpoint(endpoint, bas_dd):
    if not AUTH_KEY:
        raise RuntimeError("KRX_AUTH_KEY 미설정")
    url = f"{HOST}{endpoint}?basDd={bas_dd}"
    headers = {"AUTH_KEY": AUTH_KEY, "Accept": "application/json"}
    return http_get(url, headers)


def fetch_one_day(bas_dd):
    """KOSPI + KOSDAQ 한 일자 fetch — 통합 종목 list 반환. 둘 다 실패 시 None."""
    rows = []
    fail = 0
    for ep in (KOSPI_EP, KOSDAQ_EP):
        status, body = call_endpoint(ep, bas_dd)
        if status != 200:
            fail += 1
            continue
        try:
            j = json.loads(body)
        except Exception:
            fail += 1
            continue
        ob = j.get("OutBlock_1") or []
        rows.extend(ob)
        time.sleep(0.05)  # rate limit 보호
    if fail == 2:
        return None  # 양쪽 다 실패 → 휴일 또는 API 장애
    return rows


def aggregate_day(rows):
    """일자별 advance/decline/unchanged + 종목별 close 매핑.
    거래 정지(거래량=0) / 이상치(close=0) 종목 제외.
    """
    adv = dec = unc = 0
    close_map = {}
    for r in rows:
        try:
            rt = float(str(r.get("FLUC_RT", "0")).replace(",", ""))
            close = int(str(r.get("TDD_CLSPRC", "0")).replace(",", ""))
            isu = r.get("ISU_CD", "")
            vol = int(str(r.get("ACC_TRDVOL", "0")).replace(",", ""))
        except Exception:
            continue
        if not isu or close <= 0 or vol <= 0:
            continue
        if rt > 0:
            adv += 1
        elif rt < 0:
            dec += 1
        else:
            unc += 1
        close_map[isu] = close
    return adv, dec, unc, close_map


# ---------------- Probe ----------------

def cmd_probe():
    bas_dd = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
    while datetime.strptime(bas_dd, "%Y%m%d").weekday() >= 5:
        bas_dd = (datetime.strptime(bas_dd, "%Y%m%d") - timedelta(days=1)).strftime("%Y%m%d")
    print(f"[probe] basDd={bas_dd}")
    print(f"[probe] AUTH_KEY length: {len(AUTH_KEY)}")
    rows = fetch_one_day(bas_dd)
    if rows is None:
        print("[probe] FAIL — 양쪽 endpoint 모두 실패")
        sys.exit(1)
    adv, dec, unc, cm = aggregate_day(rows)
    print(f"[probe] 종목수 (KOSPI+KOSDAQ 통합 거래 종목): {adv + dec + unc}")
    print(f"[probe] adv={adv}  dec={dec}  unc={unc}")
    if dec > 0:
        print(f"[probe] 당일 ADR proxy: {round(adv/dec*100, 2)} (정상 80~120)")
    print(f"[probe] close map size: {len(cm)}")


# ---------------- Backfill ----------------

def trading_days(start_yyyymmdd, end_yyyymmdd):
    cur = datetime.strptime(start_yyyymmdd, "%Y%m%d")
    end = datetime.strptime(end_yyyymmdd, "%Y%m%d")
    while cur <= end:
        if cur.weekday() < 5:
            yield cur.strftime("%Y%m%d")
        cur += timedelta(days=1)


def fetch_range(start_yyyymmdd, end_yyyymmdd, existing_dates=None):
    """기간 내 모든 영업일 fetch. existing_dates에 있는 일자는 스킵."""
    days = list(trading_days(start_yyyymmdd, end_yyyymmdd))
    total = len(days)
    daily = []  # [{date, adv, dec, unc, close_map}, ...]
    skip = fail = 0
    print(f"[*] {total} 영업일 fetch 시작 ({start_yyyymmdd} → {end_yyyymmdd})")
    t0 = time.time()
    for i, bas_dd in enumerate(days, 1):
        date_str = f"{bas_dd[:4]}-{bas_dd[4:6]}-{bas_dd[6:]}"
        if existing_dates and date_str in existing_dates:
            skip += 1
            continue
        rows = fetch_one_day(bas_dd)
        if rows is None:
            fail += 1
            continue
        adv, dec, unc, cm = aggregate_day(rows)
        if adv + dec + unc == 0:
            continue  # 휴장
        daily.append({"date": date_str, "adv": adv, "dec": dec, "unc": unc, "close_map": cm})
        if i % 50 == 0 or i == total:
            elapsed = int(time.time() - t0)
            print(f"  [{i:5d}/{total}] {bas_dd}  fetched={len(daily)}  skip={skip}  fail={fail}  ({elapsed}s)")
    return daily


def compute_breadth(daily):
    """ADR(20) + NH/NL(252) 계산."""
    try:
        import pandas as pd
    except ImportError:
        print("[install] pandas 설치 중...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "pandas",
                               "--break-system-packages"])
        import pandas as pd

    if not daily:
        return []
    daily_sorted = sorted(daily, key=lambda x: x["date"])
    dates = [d["date"] for d in daily_sorted]

    # close DataFrame (sparse — 종목 × 일자)
    all_isu = sorted({k for d in daily_sorted for k in d["close_map"].keys()})
    close_df = pd.DataFrame(index=dates, columns=all_isu, dtype=float)
    for d in daily_sorted:
        for isu, c in d["close_map"].items():
            close_df.at[d["date"], isu] = c

    # ADR (20일 누적 비율)
    adv_s = pd.Series([d["adv"] for d in daily_sorted], index=dates, dtype=float)
    dec_s = pd.Series([d["dec"] for d in daily_sorted], index=dates, dtype=float)
    sum_adv = adv_s.rolling(WINDOW_ADR, min_periods=WINDOW_ADR).sum()
    sum_dec = dec_s.rolling(WINDOW_ADR, min_periods=WINDOW_ADR).sum()
    adr_s = (sum_adv / sum_dec.replace(0, float("nan")) * 100).round(2)

    # NH/NL (252일 rolling max/min vs close)
    roll_max = close_df.rolling(WINDOW_52W, min_periods=60).max()
    roll_min = close_df.rolling(WINDOW_52W, min_periods=60).min()
    nh_mask = (close_df >= roll_max - 1e-6) & close_df.notna()
    nl_mask = (close_df <= roll_min + 1e-6) & close_df.notna()
    valid = close_df.notna().sum(axis=1)
    nh_pct = (nh_mask.sum(axis=1) / valid.replace(0, float("nan")) * 100).round(2)
    nl_pct = (nl_mask.sum(axis=1) / valid.replace(0, float("nan")) * 100).round(2)

    import math
    def _safe(v):
        if v is None: return None
        try:
            f = float(v)
            return None if math.isnan(f) else round(f, 2)
        except Exception:
            return None

    out = []
    for i, d in enumerate(daily_sorted):
        v = int(valid.iloc[i]) if not pd.isna(valid.iloc[i]) else 0
        out.append({
            "date": d["date"],
            "adv": d["adv"],
            "dec": d["dec"],
            "unc": d["unc"],
            "n_traded": v,
            "adr":    _safe(adr_s.iloc[i]),
            "nh_pct": _safe(nh_pct.iloc[i]),
            "nl_pct": _safe(nl_pct.iloc[i]),
        })
    return out


def save(records):
    obj = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "KRX OpenAPI - 종목별 일별매매정보 (KOSPI + KOSDAQ)",
        "windows": {"adr": WINDOW_ADR, "nh_nl": WINDOW_52W},
        "n_rows": len(records),
        "data": records,
    }
    tmp = OUT_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False), encoding="utf-8")
    tmp.replace(OUT_PATH)
    print(f"[OK] SAVED → {OUT_PATH}  ({len(records)} rows)")


def cmd_backfill(start_yyyymmdd, end_yyyymmdd, overwrite=False):
    """풀 백필 — 사용자 로컬 1회 권장 (10년치 약 60~80분).
    overwrite=False 면 기존 파일에 있는 일자는 스킵.
    """
    existing = {}
    if not overwrite and OUT_PATH.exists():
        prev = json.loads(OUT_PATH.read_text(encoding="utf-8"))
        for r in prev.get("data", []):
            existing[r["date"]] = r
        print(f"[*] 기존 {len(existing)} 일자 발견")
    daily = fetch_range(start_yyyymmdd, end_yyyymmdd, existing_dates=set(existing.keys()))
    if not daily and not existing:
        print("[ERROR] 신규/기존 데이터 모두 없음")
        sys.exit(1)
    # NH/NL warmup 위해 기존 + 신규 합쳐서 재계산
    # 기존 close_map 데이터는 보존 안 됨 (집계만 저장) → 재계산 정확도 위해 풀 fetch 권장
    # 다만 기존이 있고 신규가 적으면 incremental: 기존 records는 그대로 두고 신규만 추가
    # 단순화: 신규만 compute_breadth + 기존 records와 merge
    if existing and daily:
        new_records = compute_breadth(daily)
        merged = list(existing.values())
        for r in new_records:
            existing[r["date"]] = r
        merged_sorted = sorted(existing.values(), key=lambda x: x["date"])
        save(merged_sorted)
    elif daily:
        records = compute_breadth(daily)
        save(records)
    else:
        print("[*] 신규 fetch 없음 — 기존 데이터 유지")


def cmd_update():
    """최근 260영업일만 fetch → NH/NL warmup 포함 정확 계산 → 신규 일자만 append.
    Actions에서 매일 실행 권장. 약 5~10분.
    기존 파일 없으면 fallback으로 최근 260일치 백필 (1년치 데이터 즉시 확보).
    """
    today = datetime.now()
    # 영업일 기준으로 260일 전 (캘린더 약 374일 전부터 시작해서 260 영업일까지)
    start = (today - timedelta(days=400)).strftime("%Y%m%d")
    end = today.strftime("%Y%m%d")
    print(f"[update] 최근 260영업일 fetch: {start} → {end}")
    if not OUT_PATH.exists():
        print(f"[update] 기존 파일 없음 — fallback: 최근 260일치 풀 백필 모드로 진행")

    # 기존 records 로드
    existing = {}
    if OUT_PATH.exists():
        prev = json.loads(OUT_PATH.read_text(encoding="utf-8"))
        for r in prev.get("data", []):
            existing[r["date"]] = r
        print(f"[update] 기존 {len(existing)} 일자")

    # update 모드는 기존 일자도 fetch (NH/NL warmup용 close 데이터 필요)
    daily = fetch_range(start, end, existing_dates=None)  # 모두 fetch
    if not daily:
        print("[update] fetch 결과 없음")
        return

    new_records = compute_breadth(daily)
    # existing에 없는 일자만 추가 (또는 NH/NL이 None이었던 기존 일자 갱신)
    added = 0
    for r in new_records:
        if r["date"] not in existing:
            existing[r["date"]] = r
            added += 1
        else:
            # 기존 일자 — NH/NL이 None이었으면 새로 계산된 값으로 업데이트
            old = existing[r["date"]]
            if (old.get("nh_pct") is None and r.get("nh_pct") is not None) or \
               (old.get("adr") is None and r.get("adr") is not None):
                existing[r["date"]] = r
                added += 1
    merged_sorted = sorted(existing.values(), key=lambda x: x["date"])
    save(merged_sorted)
    print(f"[update] 신규/갱신 {added} 일자 추가됨")


def main():
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--probe", action="store_true", help="1일치 응답 확인")
    g.add_argument("--backfill", nargs=2, metavar=("START", "END"),
                   help="기간 풀 백필 YYYYMMDD YYYYMMDD")
    g.add_argument("--update", action="store_true",
                   help="최근 260영업일 fetch + 신규 일자 append (Actions용)")
    p.add_argument("--overwrite", action="store_true", help="기존 파일 무시하고 처음부터")
    args = p.parse_args()

    if args.probe:
        cmd_probe()
    elif args.backfill:
        cmd_backfill(args.backfill[0], args.backfill[1], overwrite=args.overwrite)
    elif args.update:
        cmd_update()


if __name__ == "__main__":
    main()
