# -*- coding: utf-8 -*-
"""kr_close_relay.py v5 — 한국장 마감 릴레이 (KIS → data/kr_close_latest.json)
확정: 지수코드(0001/1001/2001/3003), 거래대금순 BLNG=3, ETF·ETN 제외 마스크 0000001100,
투자자별: 코스피 KSP/0001, 코스닥 KSQ/1001, 선물 K2I/F001. 코스닥150선물 = KRX 상품코드 106 힌트로 후보 확장(자가 발견)"""
import json, os, re, time, urllib.request, urllib.parse
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
    "선물(코스피200)": [("K2I", "F001"), ("K2I", "0001")],
    "코스닥150선물":  [("K2I", "F002"), ("K2I", "F003"), ("K2I", "F004"), ("K2I", "106"), ("KQI", "F001"), ("KQI", "106"), ("KQI", "F002")],
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

# ── 국고채 3Y·10Y 최종호가수익률 (2026-09-30 신설) ─────────────────────────────
# 데일리 프리뷰가 tradingeconomics 웹페이지를 긁어 국고채를 받던 것(지연·캐시에 취약, 9/30 데일리에서
# 9/29 종가 미수집)을 KIS 「금리 종합(국내채권/금리)」 로 대체해 kr_close JSON 에 같이 싣는다.
#   /uapi/domestic-stock/v1/quotations/comp-interest   TR HHPST070200C0
#   (구 TR FHPST07020000 은 KIS 공지상 삭제 예정이라 신 TR 만 쓴다)
#   DATA_GB 1 = 장외 최종호가(금투협 고시 = 시장 표준 지표금리) / 3 = 장내 국고채(KTS 체결)
#   1 을 먼저 보고 비면 3 으로 폴백. 둘 다 비면 bonds=None + notes — 다른 항목 저장은 막지 않는다.
# 응답 필드(신 TR): indicator_nm(금리명) bond_cntg_ert(수익률 %) prdy_vrss_sign prdy_vrss(전일대비 %p)
#   prdy_ctrt date_time bond_stnd_iscd. 목록이 output1/output2 어느 쪽인지 문서가 불명확해 둘 다 훑는다.
#   PROBE=1 이면 원문을 로그에 남긴다.
TR_BOND_RATES = "HHPST070200C0"
BOND_TARGETS = {"국고3Y": r"국고.*?(?<!\d)3\s*년", "국고10Y": r"국고.*?(?<!\d)10\s*년"}
_SIGN_NEG = {"4", "5"}          # KIS prdy_vrss_sign: 1상한 2상승 3보합 4하한 5하락

def _bond_name(r):
    return str(r.get("indicator_nm") or r.get("hts_kor_isnm") or "").strip()

def _signed(val, sign):
    s = str(val if val is not None else "").strip().replace(",", "")
    if not s:
        return None
    try:
        v = float(s)
    except ValueError:
        return None
    if str(sign or "").strip() in _SIGN_NEG and v > 0:
        v = -v
    return v

def fetch_bonds(tk, out):
    out["bonds"] = None
    rows, used = [], None
    for gb in ("1", "3"):
        try:
            d = kis_get(tk, "/uapi/domestic-stock/v1/quotations/comp-interest", TR_BOND_RATES,
                        {"FID_COND_MRKT_DIV_CODE": "I", "FID_COND_SCR_DIV_CODE": "20702",
                         "FID_DIV_CLS_CODE": "0", "FID_DIV_CLS_CODE1": "1", "DATA_GB": gb})
            if PROBE:
                print(f"PROBE bonds DATA_GB={gb}: " + json.dumps(d, ensure_ascii=False)[:4000])
            cand = []
            for key in ("output1", "output2", "output"):
                v = d.get(key)
                if isinstance(v, list):
                    cand += [r for r in v if isinstance(r, dict)]
                elif isinstance(v, dict):
                    cand.append(v)
            if any(re.search(p, _bond_name(r)) for r in cand for p in BOND_TARGETS.values()):
                rows, used = cand, gb
                break
            out["notes"].append(f"국고채 금리 DATA_GB={gb}: 국고 3년/10년 항목 없음 (rt_cd={d.get('rt_cd')}, {len(cand)}행)")
        except Exception as e:
            out["notes"].append(f"국고채 금리 DATA_GB={gb} 실패: {e}")
        time.sleep(0.3)
    if not rows:
        out["notes"].append("국고채 금리 미확보 — bonds=None (데일리는 폴백 소스 사용)")
        return
    bonds = {}
    for label, pat in BOND_TARGETS.items():
        r = next((r for r in rows if re.search(pat, _bond_name(r))), None)
        if not r:
            out["notes"].append(f"국고채 금리 {label} 항목 없음")
            continue
        y = _signed(r.get("bond_cntg_ert") or r.get("bond_mnrt_prpr"), "")
        chg = _signed(r.get("prdy_vrss") or r.get("bond_mnrt_prdy_vrss"), r.get("prdy_vrss_sign"))
        bonds[label] = {
            "name": _bond_name(r),
            "yield": None if y is None else f"{y:.3f}",
            "chg_pct_pt": None if chg is None else f"{chg:+.3f}",
            "chg_bp": None if chg is None else f"{chg * 100:+.1f}",
            "as_of": str(r.get("date_time") or r.get("stck_bsop_date") or "").strip(),
        }
    if bonds:
        out["bonds"] = bonds
        out["bonds_source"] = ("KIS comp-interest HHPST070200C0 DATA_GB=" + used
                               + (" (장외 최종호가·금투협 고시)" if used == "1" else " (장내 국고채 체결)"))
        out["units"]["bonds.yield"] = "%"
        out["units"]["bonds.chg_bp"] = "bp (전일대비 %p x 100)"

def kr_session_date(now):
    """수집한 종가가 속한 거래일 — 실행일이 아니라 세션일로 도장을 찍는다 (2026-09-29).

    발화 지연으로 자정을 넘겨 깨면 실행일은 이미 다음 날이지만 KIS 가 주는 값은 전날 종가다.
    9/28(월) 종가가 kr_close_20260929.json / base_date 2026-09-29 로 저장돼
    데일리·위클리의 휴장/결손 판정 룰(날짜 지정 스냅샷 404 = 휴장)이 거짓을 말한 사고 후 도입.
      - 15:40 KST 이전(마감 15:30 + 정산 여유)에 깨면 → 직전 영업일
      - 주말이면 → 직전 금요일
      - 평일 09:00~15:40 = 장중 → (True 반환) 저장 금지. 장중 시세를 종가로 덮어쓰는 사고 방지.
    휴장일 테이블은 없다 — base_date_source 에 그대로 적어 프리뷰가 staleness 를 교차 확인하게 둔다.
    KIS 현재가 응답에는 거래일 필드가 없어 계산으로 간다 (있으면 그쪽이 항상 옳다).
    """
    d = now.date()
    hm = now.hour * 60 + now.minute
    cutoff = 15 * 60 + 40
    in_session = now.weekday() < 5 and 9 * 60 <= hm < cutoff
    if hm < cutoff:
        d -= timedelta(days=1)
    while d.weekday() >= 5:
        d -= timedelta(days=1)
    return d, in_session

def main():
    now = datetime.now(KST)
    session_date, in_session = kr_session_date(now)
    if in_session:   # PROBE 라도 예외 없음 — 장중 시세가 전날 세션일 파일에 덮이는 사고 방지 (2026-09-30)
        print(f"[SKIP] {now:%Y-%m-%d %H:%M} KST 장중 — 장중 시세를 종가로 저장하지 않는다. 파일을 건드리지 않고 종료.")
        return
    tk = token()
    out = {"generated_at": now.isoformat(),
           "base_date": session_date.isoformat(),
           "base_date_source": "computed(session-date: 15:40 KST cutoff, weekend-adjusted, 휴장일 미반영)",
           "units": {"indices.value": "백만원", "top20.value": "원", "investor": "억원(백만원/100 반올림)"},
           "indices": {}, "value_top20": [], "investor": {}, "notes": []}

    for name, code in INDEX_CODES.items():
        try:
            d = kis_get(tk, "/uapi/domestic-stock/v1/quotations/inquire-index-price", TR_INDEX,
                        {"FID_COND_MRKT_DIV_CODE": "U", "FID_INPUT_ISCD": code})
            o = d.get("output", {})
            row = {"close": o.get("bstp_nmix_prpr"), "chg_pct": o.get("bstp_nmix_prdy_ctrt")}
            # OHLC/거래량 (2026-10-02): yahoo_dashboard 의 ^KS11/^KQ11 당일 지연 보충용
            row.update({"open": o.get("bstp_nmix_oprc"), "high": o.get("bstp_nmix_hgpr"),
                        "low": o.get("bstp_nmix_lwpr"), "volume": o.get("acml_vol")})
            if name in ("코스피", "코스닥"):
                row["value_krw_mn"] = o.get("acml_tr_pbmn")
                # 등락 종목수 (2026-10-07): 대시보드 ADR 당일 잠정치용 — KRX 확정치는 T+1 아침
                row["breadth"] = {"adv": o.get("ascn_issu_cnt"), "uplm": o.get("uplm_issu_cnt"),
                                  "unch": o.get("stnr_issu_cnt"), "dec": o.get("down_issu_cnt"),
                                  "lslm": o.get("lslm_issu_cnt")}
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
            except Exception as e:
                if PROBE:
                    print(f"PROBE {target} {a}/{b}: ERR {e}")
            time.sleep(0.6)
        if not picked:
            out["investor"][target] = None
            out["notes"].append(f"투자자별 {target} 미확보 (전 후보 zero)")

    fetch_bonds(tk, out)          # 국고채 3Y·10Y (2026-09-30) — 실패해도 위 항목 저장은 진행

    # ── 휴장일 중복 저장 방지 (2026-10-10) ──────────────────────────────────────
    # 10/9(한글날) 휴장일 밤에 깨서 KIS 가 돌려준 직전 거래일(10/8) 값을 kr_close_20261009.json 으로
    # 저장했다(휴장일 테이블이 없어 세션일 계산이 평일이면 무조건 그날로 찍는다). 데일리가 세션일 파일을
    # 「내용이 있으면 확정」으로 읽어 10/8 세션을 10/9 로 이중 보고할 뻔했다.
    # → 직전 저장분(latest)이 더 이른 세션일인데 지수 4종의 종가·등락률·거래대금이 전부 같으면
    #   「새 세션이 열리지 않았다」(휴장)로 보고 파일을 건드리지 않는다. 강제 저장은 FORCE=1.
    prev_path = "data/kr_close_latest.json"
    if os.path.exists(prev_path) and os.environ.get("FORCE", "0") != "1":
        try:
            with open(prev_path, encoding="utf-8") as f:
                prev = json.load(f)
            def _sig(o):
                return [(k, (v or {}).get("close"), (v or {}).get("chg_pct"), (v or {}).get("value_krw_mn"))
                        for k, v in sorted((o.get("indices") or {}).items())]
            if (prev.get("base_date") or "") < out["base_date"] and out["indices"] and _sig(prev) == _sig(out):
                print(f"[SKIP] 휴장 추정 — {out['base_date']} 지수 값이 직전 저장분({prev.get('base_date')})과 동일. "
                      "파일을 건드리지 않고 종료.")
                return
        except Exception as e:
            out["notes"].append(f"휴장 중복 검사 실패: {e}")

    os.makedirs("data", exist_ok=True)
    with open("data/kr_close_latest.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    with open(f"data/kr_close_{out['base_date'].replace('-', '')}.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    inv_ok = [k for k, v in out["investor"].items() if v]
    print(f"[OK] indices={len(out['indices'])} top20={len(out['value_top20'])} investor={inv_ok} "
          f"bonds={list((out.get('bonds') or {}).keys())} notes={out['notes']}")

if __name__ == "__main__":
    main()
