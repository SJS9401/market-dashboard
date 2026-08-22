#!/usr/bin/env python3
"""KRX 일별 코스피 시총 상위 200 + 코스닥 상위 150 백필 (2026-08-23, K200/Q150 근사 유니버스).

각 거래일 '그날' 시장별 시총 상위를 저장 (look-ahead·생존편향 없음). 수익률 = FLUC_RT.
출력: data/kr_k200q150_history.json.gz
  { updated, last_date, codes: {code: [name, mkt]},   # mkt 0=KOSPI 1=KOSDAQ
    dates: [...], days: [ {code: [rt(%), trdval(억)]}, ... ] }
resume: last_date 다음부터 MAX_DAYS 거래일. 가드: 평일 연속 20일 빈 응답 시 저장 후 중단.
"""
import gzip, json, os, time, urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
OUT = SCRIPT_DIR / "data" / "kr_k200q150_history.json.gz"
HOST = "https://data-dbg.krx.co.kr"
EPS = (("/svc/apis/sto/stk_bydd_trd", 0), ("/svc/apis/sto/ksq_bydd_trd", 1))
AUTH_KEY = os.environ.get("KRX_AUTH_KEY") or ""
START = "20140101"
MAX_DAYS = int(os.environ.get("MAX_DAYS", "900"))
TOPN = {0: 200, 1: 150}
KST = timezone(timedelta(hours=9))


def log(m):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {m}", flush=True)


def num(v):
    try:
        return float(str(v).replace(",", ""))
    except Exception:
        return None


def short(s):
    s = str(s).strip()
    return s if len(s) == 6 else (s[3:9] if len(s) == 12 else s)


def fetch_day(bas):
    out, fail = {0: [], 1: []}, 0
    for ep, mkt in EPS:
        req = urllib.request.Request(f"{HOST}{ep}?basDd={bas}",
                                     headers={"AUTH_KEY": AUTH_KEY, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                ob = json.loads(r.read().decode("utf-8")).get("OutBlock_1") or []
        except Exception as e:
            log(f"  {ep} {bas} fail: {e}")
            fail += 1
            continue
        if not ob:
            fail += 1
            continue
        out[mkt] = ob
        time.sleep(0.15)
    return out if fail < 2 else None


def main():
    if not AUTH_KEY:
        raise SystemExit("KRX_AUTH_KEY missing")
    if OUT.exists():
        h = json.loads(gzip.decompress(OUT.read_bytes()).decode("utf-8"))
    else:
        h = {"codes": {}, "dates": [], "days": []}
    cur = (datetime.strptime(h["dates"][-1], "%Y%m%d") + timedelta(days=1)) if h["dates"] \
        else datetime.strptime(START, "%Y%m%d")
    end = datetime.now(KST).replace(tzinfo=None)
    done, empty_streak = 0, 0
    while cur <= end and done < MAX_DAYS:
        if cur.weekday() < 5:
            bas = cur.strftime("%Y%m%d")
            mk = fetch_day(bas)
            total = sum(len(v) for v in mk.values()) if mk else 0
            if mk and total > 1200:
                empty_streak = 0
                day = {}
                for mkt, rows in mk.items():
                    recs = []
                    for r in rows:
                        code = short(r.get("ISU_CD", ""))
                        cap = num(r.get("MKTCAP"))
                        rt = num(r.get("FLUC_RT"))
                        tv = num(r.get("ACC_TRDVAL")) or 0
                        if not code or not cap or cap <= 0 or rt is None:
                            continue
                        recs.append((cap, code, str(r.get("ISU_NM", "")).strip(), rt, tv))
                    recs.sort(reverse=True)
                    for cap, code, name, rt, tv in recs[:TOPN[mkt]]:
                        day[code] = [round(rt, 2), int(tv / 1e8)]
                        if code not in h["codes"]:
                            h["codes"][code] = [name, mkt]
                h["dates"].append(bas)
                h["days"].append(day)
                done += 1
                if done % 50 == 0:
                    log(f"  {bas} done={done}")
                    OUT.write_bytes(gzip.compress(json.dumps(h, ensure_ascii=False,
                                    separators=(",", ":")).encode("utf-8"), 6))
            else:
                empty_streak += 1
                if empty_streak >= 20:
                    log(f"[ABORT] 20 empty weekdays at {bas} — saving & stop")
                    break
        cur += timedelta(days=1)
    h["updated"] = datetime.now(KST).strftime("%Y-%m-%d %H:%M")
    h["last_date"] = h["dates"][-1] if h["dates"] else None
    OUT.write_bytes(gzip.compress(json.dumps(h, ensure_ascii=False, separators=(",", ":")).encode("utf-8"), 6))
    log(f"saved {done} days, total {len(h['dates'])}, last={h.get('last_date')}, "
        f"codes={len(h['codes'])}, size={OUT.stat().st_size/1e6:.1f}MB")


if __name__ == "__main__":
    main()
