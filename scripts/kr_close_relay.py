# -*- coding: utf-8 -*-
"""kr_close_relay.py v2 — probe2: investor 조합 스캔 + ETF 제외 마스크 스캔"""
import json, os, time, urllib.request, urllib.parse
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))
BASE = "https://openapi.koreainvestment.com:9443"
APPKEY = os.environ["KIS_APP_KEY"]
APPSECRET = os.environ["KIS_APP_SECRET"]
PROBE = os.environ.get("PROBE", "0") == "1"

INDEX_CODES = {
    "코스피":    {"code": "0001"},
    "코스닥":    {"code": "1001"},
    "코스피200": {"code": "2001"},
    "코스닥150": {"code": "3003"},
}
TR_INDEX = "FHPUP02100000"
TR_VOLRANK = "FHPST01710000"
TR_INVESTOR = "FHPTJ04030000"

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

def is_etf_etn_spac(name):
    n = name.replace(" ", "")
    return n.startswith(ETF_PREFIX) or "스팩" in n or n.endswith("ETN") or "레버리지" in n or "인버스" in n

def volrank(tk, exls):
    return kis_get(tk, "/uapi/domestic-stock/v1/quotations/volume-rank", TR_VOLRANK, {
        "FID_COND_MRKT_DIV_CODE": "J", "FID_COND_SCR_DIV_CODE": "20171",
        "FID_INPUT_ISCD": "0000", "FID_DIV_CLS_CODE": "0",
        "FID_BLNG_CLS_CODE": "3",
        "FID_TRGT_CLS_CODE": "111111111", "FID_TRGT_EXLS_CLS_CODE": exls,
        "FID_INPUT_PRICE_1": "", "FID_INPUT_PRICE_2": "", "FID_VOL_CNT": "", "FID_INPUT_DATE_1": ""})

def main():
    tk = token()
    out = {"generated_at": datetime.now(KST).isoformat(), "base_date": None,
           "indices": {}, "value_top20": [], "investor": {}, "notes": []}

    for name, cfg in INDEX_CODES.items():
        try:
            d = kis_get(tk, "/uapi/domestic-stock/v1/quotations/inquire-index-price", TR_INDEX,
                        {"FID_COND_MRKT_DIV_CODE": "U", "FID_INPUT_ISCD": cfg["code"]})
            o = d.get("output", {})
            out["indices"][name] = {"close": o.get("bstp_nmix_prpr"), "chg_pct": o.get("bstp_nmix_prdy_ctrt"),
                                    "value_krw_mn": o.get("acml_tr_pbmn"), "code": cfg["code"]}
        except Exception as e:
            out["notes"].append(f"지수 {name} 실패: {e}")
        time.sleep(0.4)

    # ===== PROBE2-A: ETF 제외 마스크 스캔 =====
    if PROBE:
        for mask in ["1111111111", "0000000011", "0000001100", "0000110000"]:
            try:
                d = volrank(tk, mask)
                names = [r.get("hts_kor_isnm") for r in d.get("output", [])][:10]
                print(f"MASK {mask}: {names}")
            except Exception as e:
                print(f"MASK {mask}: ERR {e}")
            time.sleep(0.6)

    # Top 20 (기본 마스크 + 이름 필터)
    try:
        d = volrank(tk, "0000000000")
        rank = 0
        for r in d.get("output", []):
            nm = r.get("hts_kor_isnm", "")
            if is_etf_etn_spac(nm):
                continue
            rank += 1
            out["value_top20"].append({"rank": rank, "name": nm, "code": r.get("mksc_shrn_iscd"),
                                       "close": r.get("stck_prpr"), "chg_pct": r.get("prdy_ctrt"),
                                       "value_krw": r.get("acml_tr_pbmn")})
            if rank >= 20:
                break
        if rank < 20:
            out["notes"].append(f"거래대금 순위 {rank}건만 확보 (30행-ETF)")
    except Exception as e:
        out["notes"].append(f"Top20 실패: {e}")
    time.sleep(0.6)

    # ===== PROBE2-B: investor 조합 스캔 =====
    if PROBE:
        combos = [("999","S001"),("999","Q001"),("999","S002"),("999","K200"),
                  ("999","F001"),("999","O001"),("999","P001"),("999","Q150"),
                  ("101","S001"),("999","KSP")]
        for a, b in combos:
            try:
                d = kis_get(tk, "/uapi/domestic-stock/v1/quotations/inquire-investor-time-by-market",
                            TR_INVESTOR, {"FID_INPUT_ISCD": a, "FID_INPUT_ISCD_2": b})
                rows = d.get("output", [])
                r0 = rows[0] if rows else {}
                nz = any(v not in ("0", 0, "", None) for v in r0.values())
                print(f"INV {a}/{b}: rt={d.get('rt_cd')} rows={len(rows)} nonzero={nz} "
                      f"frgn_ntby_tr_pbmn={r0.get('frgn_ntby_tr_pbmn')} prsn={r0.get('prsn_ntby_tr_pbmn')} "
                      f"orgn={r0.get('orgn_ntby_tr_pbmn')} scrt={r0.get('scrt_ntby_tr_pbmn')} "
                      f"ivtr={r0.get('ivtr_ntby_tr_pbmn')} fund={r0.get('fund_ntby_tr_pbmn')} "
                      f"pe={r0.get('pe_fund_ntby_tr_pbmn')} etc_corp={r0.get('etc_corp_ntby_tr_pbmn')}")
            except Exception as e:
                print(f"INV {a}/{b}: ERR {e}")
            time.sleep(0.6)

    out["base_date"] = datetime.now(KST).strftime("%Y-%m-%d")
    os.makedirs("data", exist_ok=True)
    with open("data/kr_close_latest.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"[OK] indices={len(out['indices'])} top20={len(out['value_top20'])} notes={out['notes']}")

if __name__ == "__main__":
    main()
