# -*- coding: utf-8 -*-
"""kr_price_probe.py — 일회성 확인용 (2026-10-16 BT 승인)
KIS 시세 API 가 「정규장(KRX)」 종가를 주는 조합을 찾는다. 결과를 로그에 찍기만 하고 파일은 쓰지 않는다.
기준값: 삼성전자 10/15 정규장 종가 210,000(기사). ※ 10/14 234,500(키움)은 통합가로 보인다 — 1차 결과 J 일별 232,000
조회: 시장구분 J / NX / UN × (현재가 시세 FHKST01010100, 일별 시세 FHKST01010400, 기간별 차트 FHKST03010100)
v2 (같은 날): 저녁(애프터마켓 이후)에도 정규장 종가를 뽑을 수 있는지 — 체결(FHKST01010300)·시간대별 체결(FHPST01060000)
1차 결과(10/16 09:4x): J 일별은 아침엔 정규장 종가(10/15 210,000)지만, 10/15 22:21 릴레이 때는 통합가 207,500이었다
"""
import json, os, time, urllib.request, urllib.parse

BASE = "https://openapi.koreainvestment.com:9443"
APPKEY = os.environ["KIS_APP_KEY"]
APPSECRET = os.environ["KIS_APP_SECRET"]
CODES = {"005930": "삼성전자", "000660": "SK하이닉스", "009150": "삼성전기", "250030": "진코스텍"}
MARKETS = ("J", "NX", "UN")


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


def get(tk, path, tr, params):
    h = {"Content-Type": "application/json", "authorization": f"Bearer {tk}",
         "appkey": APPKEY, "appsecret": APPSECRET, "tr_id": tr, "custtype": "P"}
    try:
        return http("GET", path, h, params=params)
    except Exception as e:
        return {"rt_cd": "EXC", "msg1": f"{type(e).__name__}: {str(e)[:80]}"}
    finally:
        time.sleep(0.4)


def pick(o, keys):
    return " ".join(f"{k}={o.get(k)}" for k in keys if k in o)


def main():
    tk = token()
    for code, name in CODES.items():
        print(f"\n===== {name} ({code}) =====")
        for mk in MARKETS:
            d = get(tk, "/uapi/domestic-stock/v1/quotations/inquire-price", "FHKST01010100",
                    {"FID_COND_MRKT_DIV_CODE": mk, "FID_INPUT_ISCD": code})
            o = d.get("output") or {}
            print(f"[현재가 {mk}] rt={d.get('rt_cd')} {str(d.get('msg1') or '')[:40]} | "
                  + pick(o, ["stck_prpr", "prdy_vrss", "prdy_ctrt", "stck_sdpr", "stck_prdy_clpr",
                             "stck_oprc", "stck_hgpr", "stck_lwpr", "acml_vol", "acml_tr_pbmn"]))
            for adj in (("0", "1") if mk == "J" else ("0",)):
                d = get(tk, "/uapi/domestic-stock/v1/quotations/inquire-daily-price", "FHKST01010400",
                        {"FID_COND_MRKT_DIV_CODE": mk, "FID_INPUT_ISCD": code,
                         "FID_PERIOD_DIV_CODE": "D", "FID_ORG_ADJ_PRC": adj})
                rows = (d.get("output") or [])[:4]
                print(f"[일별 {mk} adj={adj}] rt={d.get('rt_cd')} {str(d.get('msg1') or '')[:40]} | "
                      + " ; ".join(f"{x.get('stck_bsop_date')} 종가{x.get('stck_clpr')} 대비{x.get('prdy_vrss')} "
                                   f"{x.get('prdy_ctrt')}%" for x in rows))
            d = get(tk, "/uapi/domestic-stock/v1/quotations/inquire-daily-itemchartprice", "FHKST03010100",
                    {"FID_COND_MRKT_DIV_CODE": mk, "FID_INPUT_ISCD": code, "FID_INPUT_DATE_1": "20261008",
                     "FID_INPUT_DATE_2": "20261016", "FID_PERIOD_DIV_CODE": "D", "FID_ORG_ADJ_PRC": "0"})
            o1 = d.get("output1") or {}
            # v2 — 최근 체결 틱 (시장구분별)
            dc = get(tk, "/uapi/domestic-stock/v1/quotations/inquire-ccnl", "FHKST01010300",
                     {"FID_COND_MRKT_DIV_CODE": mk, "FID_INPUT_ISCD": code})
            ticks = (dc.get("output") or [])[:3]
            print(f"[체결 {mk}] rt={dc.get('rt_cd')} | " + " ; ".join(
                f"{x.get('stck_cntg_hour')} {x.get('stck_prpr')}" for x in ticks))
            # v2 — 15:31 이전 마지막 체결 (정규장 종가 후보)
            dt = get(tk, "/uapi/domestic-stock/v1/quotations/inquire-time-itemconclusion", "FHPST01060000",
                     {"FID_COND_MRKT_DIV_CODE": mk, "FID_INPUT_ISCD": code, "FID_INPUT_HOUR_1": "153100"})
            t2 = (dt.get("output2") or [])[:3]
            print(f"[시간대 {mk} ≤15:31] rt={dt.get('rt_cd')} {str(dt.get('msg1') or '')[:30]} | " + " ; ".join(
                f"{x.get('stck_cntg_hour')} {x.get('stck_prpr')}" for x in t2))
            rows = (d.get("output2") or [])[:4]
            print(f"[차트 {mk}] rt={d.get('rt_cd')} {str(d.get('msg1') or '')[:40]} | "
                  + pick(o1, ["stck_prpr", "prdy_ctrt", "stck_prdy_clpr"]) + " | "
                  + " ; ".join(f"{x.get('stck_bsop_date')} 종가{x.get('stck_clpr')} 대비{x.get('prdy_vrss')} "
                               f"락{x.get('flng_cls_code')} 분할{x.get('mod_yn')}" for x in rows))


if __name__ == "__main__":
    main()
