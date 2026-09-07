# -*- coding: utf-8 -*-
"""kr_close_relay.py v3 — 한국장 마감 릴레이 (KIS → data/kr_close_latest.json)
확정: 지수코드(0001/1001/2001/3003), 거래대금순 BLNG=3, ETF·ETN 제외 마스크 0000001100,
      투자자별 시장구분 KSP/KSQ(+0001/1001), 단위: 지수 거래대금 백만원 / 순위 거래대금 원 / 투자자 백만원
미확정(자가 발견): 선물(K2I)·코스닥150선물(KQI)의 업종구분 — 후보 순회 후 nonzero 채택, notes에 기록"""
import json, os, time, urllib.request, urllib.parse
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))
BASE = "https://openapi.koreainvestment.com:9443"
APPKEY = os.environ["KIS_APP_KEY"]
APPSECRET = os.environ["KIS_APP_SECRET"]
PROBE = os.environ.get("PROBE", "0") == "1"

INDEX_CODES = {"코스피": "0001", "코스닥": "1001", "코스피200": "2001", "코스닥150": "3003"}
TR_INDEX, TR_VOLRANK, TR_INVESTOR = "FHPUP02100000", "FHPST01710000", "FHPTJ04030000"

INVESTOR_TARGETS = {
    "코스피":        [("KSP", "0001")],
    "코스닥":        [("KSQ", "1001")],
    "선물(코스피200)": [("K2I", "0001"), ("K2I", "F001"), ("K2I", "2001"), ("K2I", "0002"), ("K2I", "K200")],
    "코스닥150선물":  [("KQI", "1001"), ("KQI", "0001"), ("KQI", "3003"), ("KQI", "Q150")],
}
FIELDS = {"개인": "prsn", "외국인": "frgn", "기관계": "orgn", "금융투자": "scrt",
          "투신": "ivtr", "연기금등": "fund", "사모펀드": "pe_fund", "기타법인": "etc_corp"}

ETF_PREFIX = ("KODEX", "TIGER", "PLUS", "ACE", "SOL", "RISE", "KIWOOM", "KOSEF",
              "HANARO", "ARIRANG", "WON", "TIMEFOLIO", "에셋플러스", "KCGI")

def http(method, path, headers=None, body=None, params=None):
    url = BASE + path + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None,
                                 headers=headers or {}, method=method)
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())

def token():
    d = http("POST", "/oauth2/tokenP", {"Content-Type": "application/json"},
             {"grant_type": "client_credentials", "appkey": APPKEY, "appsecret": APPSECRET})
    return d["access_token"]

def kis_get(tk, path, tr, params):
    h = {"Content-Type": "application/json", "authorization": f"Bearer {tk}",
         "appkey": APPKEY, "appsecret": APPSECRET, "tr_id": tr, "custtype": "P"}
    return http("GET", path, h, params=params)

def is_excluded(name):
    n = name.replace(" ", "")
    return n.startswith(ETF_PREFIX) or "스팩" in n or n.endswith("ETN") or "레버리지" in n or "인버스" in n

def main():
    tk = token()
    out = {"generated_at": datetime.now(KST).isoformat(),
           "base_date": datetime.now(KST).strftime("%Y-%m-%d"),
           "units": {"indices.value": "백만원", "top20.value": "원", "investor": "억원(백만원/100 반올림)"},
           "indices": {}, "value_top20": [], "investor": {}, "notes": []}

    for name, code in INDEX_CODES.items():
        try:
            d = kis_get(tk, "/uapi/domestic-stock/v1/quotations/inquire-index-price", TR_INDEX,
                        {"FID_COND_MRKT_DIV_CODE": "U", "FID_INPUT_ISCD": code})
            o = d.get("output", {})
            row = {"close": o.get("bstp_nmix_prpr"), "chg_pct": o.get("bstp_nmix_prdy_ctrt")}
            if name in ("코스피", "코스닥"):
                row["value_krw_mn"] = o.get("acml_tr_pbmn")
            out["indices"][name] = row
        except Exception as e:
            out["notes"].append(f"지수 {name} 실패: {e}")
        time.sleep(0.4)

    try:
        d = kis_get(tk, "/uapi/domestic-stock/v1/quotations/volume-rank", TR_VOLRANK, {
            "FID_COND_MRKT_DIV_CODE": "J", "FID_COND_SCR_DIV_CODE": "20171",
            "FID_INPUT_ISCD": "0000", "FID_DIV_CLS_CODE": "0", "FID_BLNG_CLS_CODE": "3",
            "FID_TRGT_CLS_CODE": "111111111", "FID_TRGT_EXLS_CLS_CODE": "0000001100",
            "FID_INPUT_PRICE_1": "", "FID_INPUT_PRICE_2": "", "FID_VOL_CNT": "", "FID_INPUT_DATE_1": ""})
        rank = 0
        for r in d.get("output", []):
            nm = r.get("hts_kor_isnm", "")
            if is_excluded(nm):
                continue
            rank += 1
            out["value_top20"].append({"rank": rank, "name": nm, "code": r.get("mksc_shrn_iscd"),
                                       "close": r.get("stck_prpr"), "chg_pct": r.get("prdy_ctrt"),
                                       "value_krw": r.get("acml_tr_pbmn")})
            if rank >= 20:
                break
        if rank < 20:
            out["notes"].append(f"거래대금 순위 {rank}건만 확보")
    except Exception as e:
        out["notes"].append(f"Top20 실패: {e}")
    time.sleep(0.5)

    for target, cands in INVESTOR_TARGETS.items():
        picked = None
        for a, b in cands:
            try:
                d = kis_get(tk, "/uapi/domestic-stock/v1/quotations/inquire-investor-time-by-market",
                            TR_INVESTOR, {"FID_INPUT_ISCD": a, "FID_INPUT_ISCD_2": b})
                rows = d.get("output", [])
                r0 = rows[0] if rows else {}
                vals = {k: r0.get(f"{f}_ntby_tr_pbmn") for k, f in FIELDS.items()}
                if any(v not in ("0", 0, "", None) for v in vals.values()):
                    picked = (a, b)
                    out["investor"][target] = {k: round(int(v) / 100) for k, v in vals.items()}
                    out["investor"][target]["_combo"] = f"{a}/{b}"
                    break
                if PROBE:
                    print(f"PROBE {target} {a}/{b}: all-zero")
            except Exception as e:
                if PROBE:
                    print(f"PROBE {target} {a}/{b}: ERR {e}")
            time.sleep(0.6)
        if not picked:
            out["investor"][target] = None
            out["notes"].append(f"투자자별 {target} 미확보 (전 후보 zero — 업종구분 미확정 또는 휴장)")

    os.makedirs("data", exist_ok=True)
    with open("data/kr_close_latest.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    with open(f"data/kr_close_{out['base_date'].replace('-', '')}.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    inv_ok = [k for k, v in out["investor"].items() if v]
    print(f"[OK] indices={len(out['indices'])} top20={len(out['value_top20'])} investor={inv_ok} notes={out['notes']}")

if __name__ == "__main__":
    main()
