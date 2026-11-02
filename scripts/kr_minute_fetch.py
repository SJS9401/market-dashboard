# -*- coding: utf-8 -*-
"""kr_minute_fetch.py — 주도주 모멘텀 스터디용 분봉 수집 (2026-11-02 BT)
KIS 「주식일별분봉조회」 FHKST03010230 (1분봉, 1회 120건, 과거 약 1년 보관) → 3분·15분 합성.
MODE=probe : 보관 한도·지수 분봉 가능 여부만 로그로 확인 (저장 없음)
MODE=fetch : CODES 종목의 1분봉을 DAYS 일치 받아 data/momentum/<code>_1m.json 에 저장 (이미 있는 날짜는 건너뜀)
"""
import json, os, sys, time, urllib.request, urllib.parse
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))
BASE = "https://openapi.koreainvestment.com:9443"
APPKEY = os.environ["KIS_APP_KEY"]; APPSECRET = os.environ["KIS_APP_SECRET"]
MODE = os.environ.get("MODE", "probe")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(ROOT, "data", "momentum")

def log(*a): print(datetime.now(KST).strftime("[%H:%M:%S]"), *a, flush=True)

def http(method, path, headers=None, body=None, params=None):
    url = BASE + path + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None, headers=headers or {}, method=method)
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())

def token():
    return http("POST", "/oauth2/tokenP", {"Content-Type": "application/json"},
                {"grant_type": "client_credentials", "appkey": APPKEY, "appsecret": APPSECRET})["access_token"]

def kis_get(tk, path, tr, params):
    h = {"Content-Type": "application/json", "authorization": f"Bearer {tk}", "appkey": APPKEY,
         "appsecret": APPSECRET, "tr_id": tr, "custtype": "P"}
    for k in range(4):
        try:
            return http("GET", path, h, params=params)
        except Exception as e:
            log(f"  retry {k+1}: {e}"); time.sleep(1.5 * (k + 1))
    return {}

P_DAILY_MIN = "/uapi/domestic-stock/v1/quotations/inquire-time-dailychartprice"
P_INDEX_MIN = "/uapi/domestic-stock/v1/quotations/inquire-time-indexchartprice"

def day_minutes(tk, code, ymd, mkt="J"):
    """그 날 1분봉 전부 (15:30 부터 거꾸로 120건씩)"""
    bars, hh = {}, "153000"
    for _ in range(6):
        d = kis_get(tk, P_DAILY_MIN, "FHKST03010230", {"FID_COND_MRKT_DIV_CODE": mkt, "FID_INPUT_ISCD": code,
            "FID_INPUT_HOUR_1": hh, "FID_INPUT_DATE_1": ymd, "FID_PW_DATA_INCU_YN": "Y", "FID_FAKE_TICK_INCU_YN": ""})
        rows = [r for r in (d.get("output2") or []) if r.get("stck_bsop_date") == ymd and r.get("stck_cntg_hour")]
        if not rows: break
        for r in rows:
            t = r["stck_cntg_hour"]
            bars[t] = [float(r["stck_oprc"]), float(r["stck_hgpr"]), float(r["stck_lwpr"]), float(r["stck_prpr"]),
                       int(float(r.get("cntg_vol") or 0)), int(float(r.get("acml_tr_pbmn") or 0))]
        first = min(r["stck_cntg_hour"] for r in rows)
        if first <= "090000": break
        t = datetime.strptime(first, "%H%M%S") - timedelta(minutes=1)
        hh = t.strftime("%H%M%S")
        time.sleep(0.08)
    return bars

def probe():
    tk = token()
    today = datetime.now(KST)
    for days in (7, 200, 330, 360, 365, 372, 380, 400, 450, 500):
        dt = today - timedelta(days=days)
        while dt.weekday() >= 5: dt -= timedelta(days=1)
        ymd = dt.strftime("%Y%m%d")
        d = kis_get(tk, P_DAILY_MIN, "FHKST03010230", {"FID_COND_MRKT_DIV_CODE": "J", "FID_INPUT_ISCD": "000660",
            "FID_INPUT_HOUR_1": "153000", "FID_INPUT_DATE_1": ymd, "FID_PW_DATA_INCU_YN": "Y", "FID_FAKE_TICK_INCU_YN": ""})
        o2 = d.get("output2") or []
        dates = sorted({r.get("stck_bsop_date") for r in o2})
        log(f"stock 000660 req {ymd} ({days}d ago): rt={d.get('rt_cd')} msg={d.get('msg1','').strip()[:40]} n={len(o2)} dates={dates[:3]} first={o2[-1].get('stck_cntg_hour') if o2 else None} last={o2[0].get('stck_cntg_hour') if o2 else None}")
        time.sleep(0.2)
    # 지수 분봉: 1) 일별분봉 TR 에 U 시장  2) 업종 분봉 TR
    ymd = (today - timedelta(days=30)).strftime("%Y%m%d")
    for mkt, code in (("U", "0001"), ("U", "1001")):
        d = kis_get(tk, P_DAILY_MIN, "FHKST03010230", {"FID_COND_MRKT_DIV_CODE": mkt, "FID_INPUT_ISCD": code,
            "FID_INPUT_HOUR_1": "153000", "FID_INPUT_DATE_1": ymd, "FID_PW_DATA_INCU_YN": "Y", "FID_FAKE_TICK_INCU_YN": ""})
        o2 = d.get("output2") or []
        log(f"index via dailymin {mkt}/{code} {ymd}: rt={d.get('rt_cd')} msg={d.get('msg1','').strip()[:50]} n={len(o2)} sample={o2[:1]}")
    for itv in ("60", "900"):
        d = kis_get(tk, P_INDEX_MIN, "FHKUP03500200", {"FID_COND_MRKT_DIV_CODE": "U", "FID_ETC_CLS_CODE": "0",
            "FID_INPUT_ISCD": "0001", "FID_INPUT_HOUR_1": itv, "FID_PW_DATA_INCU_YN": "Y"})
        o2 = d.get("output2") or []
        log(f"index minute TR itv={itv}: rt={d.get('rt_cd')} msg={d.get('msg1','').strip()[:50]} n={len(o2)} keys={list(o2[0].keys()) if o2 else None} first={o2[-1] if o2 else None} last={o2[0] if o2 else None}")
    # KODEX200 (069500) 1년 전 — 지수 대용 가능 여부
    d = kis_get(tk, P_DAILY_MIN, "FHKST03010230", {"FID_COND_MRKT_DIV_CODE": "J", "FID_INPUT_ISCD": "069500",
        "FID_INPUT_HOUR_1": "153000", "FID_INPUT_DATE_1": (today - timedelta(days=300)).strftime("%Y%m%d"), "FID_PW_DATA_INCU_YN": "Y", "FID_FAKE_TICK_INCU_YN": ""})
    log("KODEX200 300d:", len(d.get("output2") or []))
    # 하루 전체 수집 테스트
    dt = today - timedelta(days=10)
    while dt.weekday() >= 5: dt -= timedelta(days=1)
    b = day_minutes(tk, "005930", dt.strftime("%Y%m%d"))
    ks = sorted(b); log(f"full day 005930 {dt:%Y%m%d}: {len(b)} bars {ks[:1]}~{ks[-1:]} sample={b[ks[-1]] if ks else None}")

def fetch():
    codes = os.environ.get("CODES", "005930,000660").split(",")
    days = int(os.environ.get("DAYS", "400"))
    os.makedirs(OUTDIR, exist_ok=True)
    tk = token(); today = datetime.now(KST).date()
    for code in codes:
        code = code.strip(); path = os.path.join(OUTDIR, f"{code}_1m.json")
        store = json.load(open(path)) if os.path.exists(path) else {"code": code, "fields": ["o", "h", "l", "c", "v", "amt_cum"], "days": {}}
        empty_run = 0; got = 0
        for k in range(1, days + 1):
            dt = today - timedelta(days=k)
            if dt.weekday() >= 5: continue
            ymd = dt.strftime("%Y%m%d")
            if ymd in store["days"]: continue
            b = day_minutes(tk, code, ymd)
            if not b:
                empty_run += 1
                if empty_run >= 15: log(f"{code}: {ymd} 이전 데이터 없음 — 중단"); break
                continue
            empty_run = 0; store["days"][ymd] = [[t] + v for t, v in sorted(b.items())]; got += 1
            if got % 20 == 0:
                log(f"{code}: {got} days (last {ymd})"); json.dump(store, open(path, "w"), separators=(",", ":"))
        store["updated"] = datetime.now(KST).isoformat(timespec="seconds")
        json.dump(store, open(path, "w"), separators=(",", ":"))
        log(f"{code}: saved {len(store['days'])} days → {path} ({os.path.getsize(path)//1024} KB)")

# ── 3분·15분 합성 + 일봉 (페이지용 경량 파일) ─────────────────────────────
#   1분봉 시각 = 그 1분의 시작(090000~152900) + 153000(종가 단일가). 봉 라벨 = 구간 시작 시각.
#   15:30 단일가 1분봉은 직전 구간(15:15~ / 15:27~)에 합친다 → 키움 분봉과 같은 봉 수.
#   거래대금 = 누적 거래대금(acml_tr_pbmn) 차분. 시간은 KST 벽시계를 UTC 초로 저장(차트가 그대로 표시).
def agg(days, n):
    out = []
    for ymd in sorted(days):
        rows = days[ymd]; groups = {}; prev_cum = 0
        for t, o, h, l, c, v, cum in rows:
            hh, mm = int(t[:2]), int(t[2:4]); m = (hh - 9) * 60 + mm
            if m >= 390: m = 389
            if m < 0: continue
            g = (m // n) * n
            amt = max(0, cum - prev_cum) if cum else 0; prev_cum = cum or prev_cum
            b = groups.get(g)
            if b is None: groups[g] = [o, h, l, c, v, amt]
            else: b[1] = max(b[1], h); b[2] = min(b[2], l); b[3] = c; b[4] += v; b[5] += amt
        base = int(datetime(int(ymd[:4]), int(ymd[4:6]), int(ymd[6:]), 9, 0, tzinfo=timezone.utc).timestamp())
        for g in sorted(groups):
            o, h, l, c, v, a = groups[g]
            out.append([base + g * 60, o, h, l, c, v, round(a / 1e8, 2)])   # 거래대금 억원
    return out

def build():
    import glob
    for path in glob.glob(os.path.join(OUTDIR, "*_1m.json")):
        st = json.load(open(path)); code = st["code"]
        for n in (3, 15):
            bars = agg(st["days"], n)
            json.dump({"code": code, "tf": f"{n}m", "fields": ["t", "o", "h", "l", "c", "v", "amt_eok"], "bars": bars},
                      open(os.path.join(OUTDIR, f"{code}_{n}m.json"), "w"), separators=(",", ":"))
            log(f"build {code} {n}m: {len(bars)} bars")
    # 일봉: 나스닥·코스피·코스닥·종목 (yfinance, 2015~)
    try:
        import yfinance as yf
        syms = {"IXIC": "^IXIC", "KOSPI": "^KS11", "KOSDAQ": "^KQ11"}
        for path in glob.glob(os.path.join(OUTDIR, "*_1m.json")):
            c = json.load(open(path))["code"]
            if c not in ("069500", "229200"): syms[c] = c + ".KS"
        for c in os.environ.get("DAILY_EXTRA", "").split(","):
            if c.strip(): syms[c.strip()] = c.strip() + ".KS"
        daily = {}
        for k, y in syms.items():
            h = yf.Ticker(y).history(start="2015-01-01", interval="1d", auto_adjust=False)
            rows = [[str(i.date()), round(float(r.Open), 2), round(float(r.High), 2), round(float(r.Low), 2), round(float(r.Close), 2), int(r.Volume)]
                    for i, r in h.iterrows() if r.Close == r.Close and r.Open > 0]
            daily[k] = rows; log(f"daily {k}: {len(rows)} rows, last {rows[-1] if rows else None}")
        json.dump({"updated": datetime.now(KST).isoformat(timespec="seconds"), "fields": ["d", "o", "h", "l", "c", "v"], "series": daily},
                  open(os.path.join(OUTDIR, "daily.json"), "w"), separators=(",", ":"))
    except Exception as e:
        log("daily build error", e)

if __name__ == "__main__":
    if MODE == "probe": probe()
    elif MODE == "build": build()
    else: fetch(); build()
