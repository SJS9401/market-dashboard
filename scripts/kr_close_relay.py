# -*- coding: utf-8 -*-
"""
kr_close_relay.py — 한국장 마감 데이터 릴레이 (KIS OpenAPI → data/kr_close_latest.json)
목적: daily-preview-cloud의 2-K [전일 한국장 리뷰]가 읽는 마감 확정치 생성
  1) 지수 4종: 코스피 / 코스피200 / 코스닥 / 코스닥150 — 종가·등락률(·현물 2종 거래대금)
  2) 거래대금 Top 20 (ETF·ETN·스팩 제외, 코스피+코스닥 통합)
  3) 투자자별 매매동향: 코스피 / 코스닥 / 코스피200선물 / 코스닥150선물
     × 개인·외국인·기관계·금융투자·투신·연기금등·사모펀드·기타법인 (억원)

⚠ 최초 셋업: PROBE=1 로 수동 실행 → Actions 로그의 원시 응답으로 TR·필드 검증 후
   아래 CONFIG의 '검증 필요' 항목을 확정한다 (추정 금지 원칙).
   참고 코드: 로컬 kis-market/kis_mcp_server.py (거래대금 순위 호출 패턴 검증됨)
"""
import json, os, sys, time, urllib.request, urllib.parse
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))
BASE = "https://openapi.koreainvestment.com:9443"
APPKEY = os.environ["KIS_APP_KEY"]
APPSECRET = os.environ["KIS_APP_SECRET"]
PROBE = os.environ.get("PROBE", "0") == "1"

# ===== CONFIG (probe로 검증 후 확정) =====
INDEX_CODES = {  # 업종·지수 코드 — 코스피200·코스닥150 코드는 probe 검증 필요
    "코스피":    {"code": "0001", "verified": True},
    "코스닥":    {"code": "1001", "verified": True},
    "코스피200": {"code": "2001", "verified": False},
    "코스닥150": {"code": "3003", "verified": False},  # 후보: 3003 / 1167
}
TR_INDEX = "FHPUP02100000"      # 국내업종 현재지수
TR_VOLRANK = "FHPST01710000"    # 거래량순위 (FID_BLNG_CLS_CODE=3 → 거래금액순 — probe 확인)
TR_INVESTOR_STOCK = "FHPTJ04030000"  # 시장별 투자자매매동향(시세) — probe 확인
TR_INVESTOR_FUT = "TODO_PROBE"  # 선물 투자자별 — probe에서 TR 확정

ETF_PREFIX = ("KODEX", "TIGER", "PLUS", "ACE", "SOL", "RISE", "KIWOOM", "KOSEF",
              "HANARO", "ARIRANG", "WON", "TIMEFOLIO", "에셋플러스", "KCGI", "DAISHIN343")

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
    d = http("GET", path, h, params=params)
    if PROBE:
        print(f"\n===== PROBE {tr} {params} =====")
        print(json.dumps(d, ensure_ascii=False)[:3000])
    return d

def is_etf_etn_spac(name):
    n = name.replace(" ", "")
    return n.startswith(ETF_PREFIX) or "스팩" in n or n.endswith("ETN") or "레버리지" in n or "인버스" in n

def main():
    tk = token()
    out = {"generated_at": datetime.now(KST).isoformat(), "base_date": None,
           "indices": {}, "value_top20": [], "investor": {}, "notes": []}

    for name, cfg in INDEX_CODES.items():
        try:
            d = kis_get(tk, "/uapi/domestic-stock/v1/quotations/inquire-index-price", TR_INDEX,
                        {"FID_COND_MRKT_DIV_CODE": "U", "FID_INPUT_ISCD": cfg["code"]})
            o = d.get("output", {})
            out["indices"][name] = {
                "close": o.get("bstp_nmix_prpr"), "chg_pct": o.get("bstp_nmix_prdy_ctrt"),
                "value_krw_mn": o.get("acml_tr_pbmn"),
                "code": cfg["code"], "verified": cfg["verified"]}
        except Exception as e:
            out["indices"][name] = {"error": str(e)}
            out["notes"].append(f"지수 {name} 수집 실패: {e}")
        time.sleep(0.3)

    try:
        d = kis_get(tk, "/uapi/domestic-stock/v1/quotations/volume-rank", TR_VOLRANK, {
            "FID_COND_MRKT_DIV_CODE": "J", "FID_COND_SCR_DIV_CODE": "20171",
            "FID_INPUT_ISCD": "0000", "FID_DIV_CLS_CODE": "0",
            "FID_BLNG_CLS_CODE": "3",
            "FID_TRGT_CLS_CODE": "111111111", "FID_TRGT_EXLS_CLS_CODE": "0000000000",
            "FID_INPUT_PRICE_1": "", "FID_INPUT_PRICE_2": "", "FID_VOL_CNT": "", "FID_INPUT_DATE_1": ""})
        rows = d.get("output", [])
        rank = 0
        for r in rows:
            nm = r.get("hts_kor_isnm", "")
            if is_etf_etn_spac(nm):
                continue
            rank += 1
            out["value_top20"].append({
                "rank": rank, "name": nm, "code": r.get("mksc_shrn_iscd"),
                "close": r.get("stck_prpr"), "chg_pct": r.get("prdy_ctrt"),
                "value_krw_mn": r.get("acml_tr_pbmn")})
            if rank >= 20:
                break
        if rank < 20:
            out["notes"].append(f"거래대금 순위 {rank}건만 확보")
    except Exception as e:
        out["notes"].append(f"거래대금 Top20 수집 실패: {e}")

    if TR_INVESTOR_FUT == "TODO_PROBE":
        out["notes"].append("investor 블록 미활성 — probe 후 TR 확정 필요")
    if PROBE:
        try:
            kis_get(tk, "/uapi/domestic-stock/v1/quotations/inquire-investor-time-by-market",
                    TR_INVESTOR_STOCK, {"FID_INPUT_ISCD": "0001", "FID_INPUT_ISCD_2": "KSP"})
        except Exception as e:
            print(f"PROBE investor(stock) 실패: {e}")

    out["base_date"] = datetime.now(KST).strftime("%Y-%m-%d")
    out["notes"].append("base_date=실행일 기준 — 지수 응답의 영업일 필드 확인 후 교체 권장")

    os.makedirs("data", exist_ok=True)
    with open("data/kr_close_latest.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    with open(f"data/kr_close_{out['base_date'].replace('-', '')}.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"[OK] indices={len(out['indices'])} top20={len(out['value_top20'])} notes={out['notes']}")

if __name__ == "__main__":
    main()
