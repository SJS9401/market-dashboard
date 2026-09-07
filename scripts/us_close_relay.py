# -*- coding: utf-8 -*-
"""us_close_relay.py v1 — 미국장 마감 릴레이 (KIS 해외주식 → data/us_close_latest.json)
검증된 TR (로컬 kis_mcp_server.py 이식): trade-pbmn HHDFS76320010 / price-detail HHDFS76200200 / new-highlow HHDFS76300000
수집: ① 거래대금 순위 3거래소 합산 (ETF 플래그) ② 분류체계 70종 개별 시세 (EXCD 자가 발견) ③ 52주 신고가 랭킹
⚠ probe 확인 사항: rate가 정규장 기준인지(시간외 포함 함정 — 국내 KIS 전례), tamt 단위(USD)"""
import json, os, time, urllib.request, urllib.parse
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))
BASE = "https://openapi.koreainvestment.com:9443"
APPKEY = os.environ["KIS_APP_KEY"]
APPSECRET = os.environ["KIS_APP_SECRET"]
PROBE = os.environ.get("PROBE", "0") == "1"

SYMBOLS = ["NVDA","AMD","AVGO","MRVL","ALAB","CRDO","MU","SNDK","WDC","STX","INTC","ARM",
           "TSM","GFS","UMC","AMAT","LRCX","KLAC","ASML","TXN","ADI","NXPI","ON","MPWR",
           "AMKR","ENTG","LITE","COHR","AAOI","FN","CIEN","NOK","ERIC","ANET","CSCO",
           "CRWV","NBIS","ORCL","IBM","SNOW","MDB","DELL","SMCI","HPE",
           "MSFT","AMZN","GOOGL","GOOG","META","PLTR","NFLX","CRM","NOW","ADBE","CRWD","PANW","ZS",
           "MSTR","MARA","RIOT","CLSK","COIN","HOOD","IREN","APLD","WULF","CORZ","CIFR",
           "TSLA","AAPL","SPCX","CBRS"]
ETF_SET = {"SPY","QQQ","QQQM","IWM","DIA","VOO","IVV","VTI","SPLG","TQQQ","SQQQ","SOXL","SOXS",
           "SPXL","SPXS","UVXY","VXX","UVIX","TSLL","TSLZ","TSLQ","NVDL","NVDD","NVDU","NVDQ",
           "AMDL","GGLL","MSTU","MSTX","MSTZ","CONL","BITX","BITU","IBIT","FBTC","GBTC","ETHA","ETHU",
           "GLD","SLV","TLT","TMF","HYG","LQD","EEM","SMH","SOXX","XLF","XLE","XLK","ARKK",
           "JEPI","JEPQ","SCHD","YINN","YANG","LABU","FNGU","BULZ","PLTU","AVGX","AVL","CRWL"}

def http_get(path, tr, params, timeout=15):
    url = BASE + path + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "Content-Type": "application/json", "authorization": f"Bearer {TK}",
        "appkey": APPKEY, "appsecret": APPSECRET, "tr_id": tr, "custtype": "P"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())

def token():
    req = urllib.request.Request(BASE + "/oauth2/tokenP",
        data=json.dumps({"grant_type": "client_credentials", "appkey": APPKEY, "appsecret": APPSECRET}).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())["access_token"]

def main():
    global TK
    TK = token()
    out = {"generated_at": datetime.now(KST).isoformat(),
           "units": {"trading_amount": "USD(tamt 원시값 — probe 검증)", "volume": "주"},
           "rank_value": [], "stocks": {}, "new_highs": [], "notes": []}

    all_rank = {}
    for excd in ["NYS", "NAS", "AMS"]:
        try:
            d = http_get("/uapi/overseas-stock/v1/ranking/trade-pbmn", "HHDFS76320010",
                         {"EXCD": excd, "NDAY": "0", "VOL_RANG": "0", "AUTH": "", "KEYB": "", "PRC1": "", "PRC2": ""})
            rows = d.get("output2", [])
            if PROBE:
                print("RANK " + excd + ": rows=" + str(len(rows)) + " head=" + str([(r.get('symb'), r.get('tamt')) for r in rows[:3]]))
            for it in rows:
                sym = it.get("symb", "")
                if not sym:
                    continue
                tamt = float(it.get("tamt", "0") or 0)
                if sym in all_rank:
                    all_rank[sym]["tamt"] += tamt
                else:
                    all_rank[sym] = {"symbol": sym, "name": it.get("ename", "") or it.get("name", ""),
                                     "price": it.get("last", "0"), "change_rate": it.get("rate", "0"),
                                     "volume": it.get("tvol", "0"), "tamt": tamt, "excd": excd,
                                     "is_etf": sym in ETF_SET}
        except Exception as e:
            out["notes"].append("rank " + excd + " 실패: " + str(e))
        time.sleep(0.4)
    ranked = sorted(all_rank.values(), key=lambda x: x["tamt"], reverse=True)[:60]
    for i, s in enumerate(ranked, 1):
        s["rank"] = i
        s["tamt"] = round(s["tamt"])
    out["rank_value"] = ranked

    excd_cache = {}
    for sym in SYMBOLS:
        got = None
        for excd in ["NAS", "NYS", "AMS"]:
            try:
                d = http_get("/uapi/overseas-price/v1/quotations/price-detail", "HHDFS76200200",
                             {"AUTH": "", "EXCD": excd, "SYMB": sym}, timeout=10)
                o = d.get("output", {}) or {}
                if o.get("last") not in ("", "0", None):
                    got = {"last": o.get("last"), "rate": o.get("rate") or o.get("t_xrat") or o.get("prdy_ctrt"),
                           "diff": o.get("diff"), "tvol": o.get("tvol"), "tamt": o.get("tamt"),
                           "high": o.get("high"), "low": o.get("low"), "open": o.get("open"),
                           "h52p": o.get("h52p"), "l52p": o.get("l52p"), "excd": excd}
                    excd_cache[sym] = excd
                    break
            except Exception:
                pass
            time.sleep(0.25)
        out["stocks"][sym] = got
        if got is None:
            out["notes"].append(sym + " 시세 미확보")
        time.sleep(0.25)
    if PROBE:
        print("EXCD map:", json.dumps(excd_cache))
        for s in ["NVDA", "MU", "SNDK", "TSLA"]:
            print("DETAIL " + s + ": " + json.dumps(out['stocks'].get(s), ensure_ascii=False))

    for excd in ["NYS", "NAS", "AMS"]:
        try:
            d = http_get("/uapi/overseas-stock/v1/ranking/new-highlow", "HHDFS76300000",
                         {"EXCD": excd, "MINX": "0", "VOL_RANG": "0", "GUBN": "1", "GUBN2": "1", "KEYB": "", "AUTH": ""})
            for it in d.get("output2", []):
                sym = it.get("symb", "")
                if not sym:
                    continue
                out["new_highs"].append({"symbol": sym, "name": it.get("ename", "") or it.get("name", ""),
                                         "price": it.get("last"), "change_rate": it.get("rate"),
                                         "tamt": it.get("tamt"), "exchange": excd, "is_etf": sym in ETF_SET})
        except Exception as e:
            out["notes"].append("new-high " + excd + " 실패: " + str(e))
        time.sleep(0.4)
    out["new_highs"] = sorted(out["new_highs"], key=lambda x: float(x.get("tamt") or 0), reverse=True)[:80]

    out["base_date_note"] = "미국 직전 영업일 데이터 (휴장일엔 그 전 영업일 스냅샷 — 데일리가 rank 대표 종목 등락률로 날짜 검증)"

    os.makedirs("data", exist_ok=True)
    with open("data/us_close_latest.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    ok_syms = sum(1 for v in out["stocks"].values() if v)
    print("[OK] rank=" + str(len(out['rank_value'])) + " stocks=" + str(ok_syms) + "/" + str(len(SYMBOLS)) + " new_highs=" + str(len(out['new_highs'])) + " notes=" + str(out['notes'][:5]))

if __name__ == "__main__":
    main()
