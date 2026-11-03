#!/usr/bin/env python3
"""KRX OpenAPI 일별 시가총액 히스토리 백필 (2026-11-03, 섹터 시총 합산 카드용).

각 거래일 코스피·코스닥 전종목 시세(stk_bydd_trd / ksq_bydd_trd)에서
  - 시장 전체 시총 합계 (억원)
  - 시장별 그날 시총 상위 TOPN + 섹터 구성 종목(MEMBERS) 시총 (억원)
을 저장한다. (그날 기준 상위 → 생존편향 없음. 연도별 Tier 2 탭에도 재사용)

출력: data/kr_mcap_history.json.gz
  { updated, last_date, codes: {code: name}, mkt: {code: "K"|"Q"},
    dates: ["YYYYMMDD", ...], tot: [[kospi억, kosdaq억], ...],
    days: [ {code: cap억}, ... ] }   # dates 와 1:1
resume: 기존 gz last_date 다음부터 MAX_DAYS 거래일 처리.
가드: 평일 연속 20일 빈 응답 → 한도/장애로 보고 저장 후 중단 (START 이전 구간 미제공이면 START 를 앞당겨 건너뜀).
"""
import gzip, json, os, time, urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
OUT = SCRIPT_DIR / "data" / "kr_mcap_history.json.gz"
HOST = "https://data-dbg.krx.co.kr"
EPS = (("K", "/svc/apis/sto/stk_bydd_trd"), ("Q", "/svc/apis/sto/ksq_bydd_trd"))
AUTH_KEY = os.environ.get("KRX_AUTH_KEY") or ""
START = os.environ.get("START", "20100104")
MAX_DAYS = int(os.environ.get("MAX_DAYS", "1200"))
TOPN = 150
KST = timezone(timedelta(hours=9))

MEMBERS = set("""
000720 006360 047040 375500 000210 009540 329180 010140 042660 010620 011200 028670
010120 267260 298040 103590 034020 052690 051600 015760 012450 079550 047810 064350 103140
005380 000270 012330 005490 004020 051910 011170 011780 009830 010950 096770 005930 000660
373220 006400 086520 247540 066970 003670 068270 091990 207940 128940 008930 000100 096530
196170 215600 017670 030200 032640 032500 050890 088800 039560 010170 043260 073490 218410
035420 035720 036570 264450 178320
006800 071050 016360 005940 039490 003540 090430 002790 051900 192820 161890 214150 214450 335890
278470 145020 017800 021240 005610 026960
097950 001800 271560 004370 007310 003230 049770 051500 031440 005300 004990 280360 001680 005180 000250
""".split())
MVER = 3   # MEMBERS 목록 버전 — 올리면 과거 날짜를 다시 받아 빠진 구성 종목 시총을 채움 (리필)


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


def fetch(ep, bas):
    req = urllib.request.Request(f"{HOST}{ep}?basDd={bas}",
                                 headers={"AUTH_KEY": AUTH_KEY, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8")).get("OutBlock_1") or []


def save(h):
    h["updated"] = datetime.now(KST).strftime("%Y-%m-%d %H:%M")
    h["last_date"] = h["dates"][-1] if h["dates"] else None
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(gzip.compress(json.dumps(h, ensure_ascii=False, separators=(",", ":")).encode("utf-8"), 6))


def main():
    if not AUTH_KEY:
        raise SystemExit("KRX_AUTH_KEY missing")
    if OUT.exists():
        h = json.loads(gzip.decompress(OUT.read_bytes()).decode("utf-8"))
    else:
        h = {"codes": {}, "mkt": {}, "dates": [], "tot": [], "days": []}
    cur = (datetime.strptime(h["dates"][-1], "%Y%m%d") + timedelta(days=1)) if h["dates"] \
        else datetime.strptime(START, "%Y%m%d")
    end = datetime.now(KST).replace(tzinfo=None)
    done, empty_streak, calls = 0, 0, 0
    while cur <= end and done < MAX_DAYS:
        if cur.weekday() < 5:
            bas = cur.strftime("%Y%m%d")
            day, tot, ok = {}, [0, 0], True
            for i, (mk, ep) in enumerate(EPS):
                try:
                    rows = fetch(ep, bas)
                    calls += 1
                except Exception as e:
                    log(f"  {mk} {bas} fail: {e}")
                    rows = []
                time.sleep(0.12)
                if not rows:
                    ok = False
                    break
                recs = []
                for r in rows:
                    code = short(r.get("ISU_CD", ""))
                    cap = num(r.get("MKTCAP"))
                    if not code or not cap or cap <= 0:
                        continue
                    recs.append((cap, code, str(r.get("ISU_NM", "")).strip()))
                tot[i] = int(sum(c for c, _, _ in recs) / 1e8)
                recs.sort(reverse=True)
                for rank, (cap, code, name) in enumerate(recs):
                    if rank < TOPN or code in MEMBERS:
                        day[code] = int(cap / 1e8)
                        h["codes"][code] = name
                        h["mkt"][code] = mk
            if ok and tot[0] > 0:
                empty_streak = 0
                h["dates"].append(bas)
                h["tot"].append(tot)
                h["days"].append(day)
                h.setdefault("mver", [1] * (len(h["dates"]) - 1)).append(MVER)
                done += 1
                if done % 100 == 0:
                    log(f"  {bas} done={done} calls={calls}")
                    save(h)
            else:
                empty_streak += 1
                if empty_streak >= 20:
                    if not h["dates"]:
                        log(f"[INFO] no data up to {bas} — START 이전 미제공 구간, 계속 진행")
                        empty_streak = 0
                    else:
                        log(f"[ABORT] 20 consecutive empty weekdays at {bas} — rate limit? saving & stop")
                        break
        cur += timedelta(days=1)
    # ---- 리필: MEMBERS 가 늘어난 뒤 과거 날짜의 빠진 구성 종목 채우기 (남은 예산만큼) ----
    mv = h.setdefault("mver", [1] * len(h["dates"]))
    if len(mv) < len(h["dates"]):
        mv.extend([1] * (len(h["dates"]) - len(mv)))
    fails = 0
    for i, bas in enumerate(h["dates"]):
        if done >= MAX_DAYS or fails >= 20:
            break
        if mv[i] >= MVER:
            continue
        ok = True
        for mk, ep in EPS:
            try:
                rows = fetch(ep, bas); calls += 1
            except Exception as e:
                log(f"  refill {mk} {bas} fail: {e}"); rows = []
            time.sleep(0.12)
            if not rows:
                ok = False; break
            for r in rows:
                code = short(r.get("ISU_CD", ""))
                cap = num(r.get("MKTCAP"))
                if code in MEMBERS and cap and cap > 0:
                    h["days"][i][code] = int(cap / 1e8)
                    h["codes"].setdefault(code, str(r.get("ISU_NM", "")).strip())
                    h["mkt"][code] = mk
        if ok:
            mv[i] = MVER; done += 1; fails = 0
            if done % 100 == 0:
                log(f"  refill {bas} done={done} calls={calls}"); save(h)
        else:
            fails += 1
    save(h)
    log(f"saved {done} days, total {len(h['dates'])}, first={h['dates'][0] if h['dates'] else None}, "
        f"last={h.get('last_date')}, codes={len(h['codes'])}, calls={calls}, size={OUT.stat().st_size/1e6:.1f}MB")


if __name__ == "__main__":
    main()
