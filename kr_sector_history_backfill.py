#!/usr/bin/env python3
"""KRX 일별 업종 집계 히스토리 백필 (2026-08-22 신설, 순환매 스캔 Phase 1).

KRX OpenAPI stk/ksq_bydd_trd 일별 전종목 시세를 현재 업종 매핑(data/kr_marketmap.json,
네이버 78업종 — 소급 적용 = 생존편향 있음, 한계로 명시)으로 시총가중 집계.

출력: data/kr_sector_history.json
  { updated, start, last_date, sectors: [...업종, "_ALL", "_KOSPI", "_KOSDAQ"],
    dates: ["YYYYMMDD", ...],
    ret: [[%...] per sector],   # 시총가중 일별 수익률, 소수 3자리, null=해당일 종목 없음
    val: [[억원...] per sector] } # 거래대금 합
resume 방식: 기존 JSON의 last_date 다음 날부터 이어서 최대 MAX_DAYS 거래일 처리 후 저장.
(GitHub Actions 에서 여러 번 dispatch 하면 순차적으로 완성된다)
"""
import json, os, time, urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
OUT_PATH = DATA_DIR / "kr_sector_history.json"
MAP_PATH = DATA_DIR / "kr_marketmap.json"

HOST = "https://data-dbg.krx.co.kr"
EPS = ("/svc/apis/sto/stk_bydd_trd", "/svc/apis/sto/ksq_bydd_trd")
AUTH_KEY = os.environ.get("KRX_AUTH_KEY") or ""
START_DATE = "20140101"
MAX_DAYS = int(os.environ.get("MAX_DAYS", "900"))   # 거래일 기준 청크
# 스키마 변경(_KOSPI/_KOSDAQ 신설)으로 전 구간 재빌드가 필요할 때는 env 청크를 무시하고 한 번에 끝낸다.
# 3,100 거래일 x 2 endpoint x 0.15s sleep ~= 20분 (workflow timeout 120분)
REBUILD_MAX_DAYS = 3600
PSEUDO = ["_ALL", "_KOSPI", "_KOSDAQ"]
KST = timezone(timedelta(hours=9))


def log(m):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {m}", flush=True)


def num(v):
    try:
        return float(str(v).replace(",", ""))
    except Exception:
        return None


def short_code(s):
    s = str(s).strip()
    return s if len(s) == 6 else (s[3:9] if len(s) == 12 else s)


def fetch_day(bas_dd):
    rows, fail = [], 0
    for ep, mkt in zip(EPS, ("kp", "kq")):
        req = urllib.request.Request(f"{HOST}{ep}?basDd={bas_dd}",
                                     headers={"AUTH_KEY": AUTH_KEY, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                ob = json.loads(r.read().decode("utf-8")).get("OutBlock_1") or []
        except Exception as e:
            log(f"  {ep} {bas_dd} fail: {e}")
            fail += 1
            continue
        if not ob:
            fail += 1
            continue
        for r in ob:
            r["_mkt"] = mkt      # 2026-09-13: 코스피/코스닥 거래대금 분리용
        rows.extend(ob)
        time.sleep(0.15)
    return rows if fail < 2 else None


def main():
    if not AUTH_KEY:
        raise SystemExit("[ERROR] KRX_AUTH_KEY missing")
    mp = json.loads(MAP_PATH.read_text(encoding="utf-8"))
    map_sectors = list(mp["sectors"])

    # kr_marketmap.json 은 매일 재생성되며 sectors 배열의 "순서"가 바뀔 수 있다
    # (2026-09-08 진단: idx 55 에서 핸드셋 <-> 생명보험 뒤바뀜 -> 구 assert 가
    #  8/22 이후 매일 실패시켜 데이터가 8/21 에 멈춰 있었다).
    # 기존 파일이 있으면 그 순서를 canonical 로 고정하고, 종목 -> 섹터 인덱스를
    # "이름" 기준으로 remap 한다. map 인덱스를 그대로 쓰면 과거 열과 어긋난다.
    hist = None
    rebuild = False
    if OUT_PATH.exists():
        hist = json.loads(OUT_PATH.read_text(encoding="utf-8"))
        if "_KOSPI" not in hist.get("sectors", []):
            # 구 스키마 (_ALL 만 존재) — 시장 분리값이 과거에 없으므로 전 구간 재빌드
            log("[migrate] _KOSPI/_KOSDAQ 없음 -> 전 구간 재빌드")
            hist = None
            rebuild = True
            sectors = map_sectors
        else:
            sectors = [x for x in hist["sectors"] if x not in PSEUDO]
            assert set(sectors) == set(map_sectors), (
                f"sector set changed (hist {len(sectors)} vs map {len(map_sectors)}) "
                f"— rebuild from scratch")
    else:
        sectors = map_sectors

    n_sec = len(sectors)
    ALL, KP, KQ = n_sec, n_sec + 1, n_sec + 2   # 의사섹터 인덱스
    n_col = n_sec + len(PSEUDO)
    name2idx = {n: i for i, n in enumerate(sectors)}
    code2sec = {}
    for st in mp["stocks"]:
        si = st[3]
        if si is None or si < 0 or si >= len(map_sectors):
            continue
        ci = name2idx.get(map_sectors[si])
        if ci is not None:
            code2sec[st[0]] = ci
    log(f"mapping: {len(code2sec)} stocks -> {n_sec} sectors (canonical order)")

    if hist is None:
        hist = {"start": START_DATE, "sectors": sectors + PSEUDO,
                "dates": [], "ret": [[] for _ in range(n_col)],
                "val": [[] for _ in range(n_col)]}

    cur = (datetime.strptime(hist["dates"][-1], "%Y%m%d") + timedelta(days=1)) if hist["dates"] \
        else datetime.strptime(START_DATE, "%Y%m%d")
    end = datetime.now(KST).replace(tzinfo=None)
    done = 0
    limit = REBUILD_MAX_DAYS if rebuild else MAX_DAYS
    unmapped_caps = {}
    while cur <= end and done < limit:
        if cur.weekday() < 5:
            bas = cur.strftime("%Y%m%d")
            rows = fetch_day(bas)
            if rows and len(rows) > 1200:
                sw = [0.0] * n_col
                swr = [0.0] * n_col
                sv = [0.0] * n_col
                for r in rows:
                    code = short_code(r.get("ISU_CD", ""))
                    cap = num(r.get("MKTCAP"))
                    rt = num(r.get("FLUC_RT"))
                    tv = num(r.get("ACC_TRDVAL")) or 0
                    if not cap or cap <= 0 or rt is None:
                        continue
                    mkt_i = KP if r.get("_mkt") == "kp" else (KQ if r.get("_mkt") == "kq" else None)
                    si = code2sec.get(code)
                    if si is None:
                        unmapped_caps[code] = cap
                        si_list = (ALL,)
                    else:
                        si_list = (si, ALL)
                    if mkt_i is not None:
                        si_list = si_list + (mkt_i,)
                    for i in si_list:
                        sw[i] += cap
                        swr[i] += cap * rt
                        sv[i] += tv
                hist["dates"].append(bas)
                for i in range(n_col):
                    hist["ret"][i].append(round(swr[i] / sw[i], 3) if sw[i] > 0 else None)
                    hist["val"][i].append(int(sv[i] / 1e8))
                done += 1
                if done % 50 == 0:
                    log(f"  {bas} done={done} rows={len(rows)}")
                    OUT_PATH.write_text(json.dumps(hist, ensure_ascii=False, separators=(",", ":")),
                                        encoding="utf-8")  # checkpoint
        cur += timedelta(days=1)

    hist["updated"] = datetime.now(KST).strftime("%Y-%m-%d %H:%M")
    hist["last_date"] = hist["dates"][-1] if hist["dates"] else None
    OUT_PATH.write_text(json.dumps(hist, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    log(f"saved {done} new days, total {len(hist['dates'])}, last={hist.get('last_date')}, "
        f"unmapped~{len(unmapped_caps)} codes, size={OUT_PATH.stat().st_size/1e6:.1f}MB")


if __name__ == "__main__":
    main()
