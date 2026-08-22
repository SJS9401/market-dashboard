#!/usr/bin/env python3
"""KRX 일별 시총 상위 300 종목 히스토리 백필 (2026-08-22, 순환매 종목 단위 스캔용).

각 거래일에 '그날' 시총 상위 300만 저장 (생존편향·look-ahead 회피).
수익률은 KRX FLUC_RT (기준가 대비 — 분할·증자 조정 반영).

출력: data/kr_top300_history.json.gz
  { updated, last_date, codes: {code: name},
    dates: ["YYYYMMDD", ...],
    days: [ {code: [rt(%), trdval(억)]}, ... ] }   # dates 와 1:1
resume: 기존 gz last_date 다음부터 MAX_DAYS 거래일 처리.
가드: 평일 연속 20일 빈 응답이면 API 한도/장애로 보고 저장 후 중단.
"""
import gzip, json, os, time, urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
OUT = SCRIPT_DIR / "data" / "kr_top300_history.json.gz"
HOST = "https://data-dbg.krx.co.kr"
EPS = ("/svc/apis/sto/stk_bydd_trd", "/svc/apis/sto/ksq_bydd_trd")
AUTH_KEY = os.environ.get("KRX_AUTH_KEY") or ""
START = "20140101"
MAX_DAYS = int(os.environ.get("MAX_DAYS", "900"))
TOPN = 300
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
    rows, fail = [], 0
    for ep in EPS:
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
        rows.extend(ob)
        time.sleep(0.15)
    return rows if fail < 2 else None


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
            rows = fetch_day(bas)
            if rows and len(rows) > 1200:
                empty_streak = 0
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
                day = {}
                for cap, code, name, rt, tv in recs[:TOPN]:
                    day[code] = [round(rt, 2), int(tv / 1e8)]
                    if code not in h["codes"]:
                        h["codes"][code] = name
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
                    log(f"[ABORT] 20 consecutive empty weekdays at {bas} — rate limit? saving & stop")
                    break
        cur += timedelta(days=1)
    h["updated"] = datetime.now(KST).strftime("%Y-%m-%d %H:%M")
    h["last_date"] = h["dates"][-1] if h["dates"] else None
    OUT.write_bytes(gzip.compress(json.dumps(h, ensure_ascii=False, separators=(",", ":")).encode("utf-8"), 6))
    log(f"saved {done} days, total {len(h['dates'])}, last={h.get('last_date')}, "
        f"codes={len(h['codes'])}, size={OUT.stat().st_size/1e6:.1f}MB")


if __name__ == "__main__":
    main()
