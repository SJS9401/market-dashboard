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

# ── 미국장 마감 가드 (2026-09-09 신설) ───────────────────────────────
# 깃허브 예약(cron)은 UTC 고정이라 미국 서머타임을 따라가지 않는다.
#   여름(3월 2째 일요일~11월 1째 일요일): 16:00 EDT = 20:00 UTC = 05:00 KST
#   겨울:                                16:00 EST = 21:00 UTC = 06:00 KST
# 같은 05:15 KST 슬롯이 여름엔 '마감 15분 후', 겨울엔 '마감 45분 전'이 된다.
# 겨울에 그대로 돌면 장중 시세를 종가인 척 덮어써서, 멈춘 것보다 나쁘다.
# → 예약은 넉넉히 깔고, 여기서 실제 뉴욕 시각을 보고 마감 전이면 그냥 나간다.
CLOSE_BUFFER_MIN = 10   # 16:10 ET 이후부터 진행 (체결 정산 여유)
OUT_PATH = "data/us_close_latest.json"

def _ny_now():
    try:
        from zoneinfo import ZoneInfo
        return datetime.now(ZoneInfo("America/New_York"))
    except Exception:
        # tzdata 부재 시 폴백 — 미국 DST 규칙 직접 계산
        u = datetime.now(timezone.utc)
        def nth_sun(y, m, n):
            d = datetime(y, m, 1, tzinfo=timezone.utc)
            while d.weekday() != 6:
                d += timedelta(days=1)
            return d + timedelta(weeks=n - 1)
        dst = nth_sun(u.year, 3, 2) + timedelta(hours=7) <= u < nth_sun(u.year, 11, 1) + timedelta(hours=6)
        return u - timedelta(hours=4 if dst else 5)

def base_date_of(ny):
    """직전 미국 거래일(주말만 고려, 휴장일 미반영)."""
    bd = ny.date()
    if ny.hour < 16:
        bd -= timedelta(days=1)
    while bd.weekday() >= 5:
        bd -= timedelta(days=1)
    return bd.isoformat()

def already_have(bd):
    """같은 거래일 데이터를 이미 받아놨으면 재수집·재커밋하지 않는다.
    슬롯을 4개 깔아도 커밋은 하루 1건만 나가게 하는 장치."""
    try:
        with open(OUT_PATH, encoding="utf-8") as f:
            prev = json.load(f)
        return prev.get("base_date") == bd and len(prev.get("rank_value") or []) >= 30
    except Exception:
        return False

def market_closed():
    ny = _ny_now()
    if ny.weekday() >= 5:                      # 뉴욕 기준 주말 = 직전 영업일 스냅샷, 진행
        return True, ny
    cutoff = ny.replace(hour=16, minute=CLOSE_BUFFER_MIN, second=0, microsecond=0)
    return ny >= cutoff, ny
# ────────────────────────────────────────────────────────────────────

def api_err(d, label, notes):
    """KIS 는 실패해도 HTTP 200 + rt_cd='1' 로 온다. 예외가 안 나므로 여기서 잡는다."""
    if not isinstance(d, dict):
        notes.append(label + " 응답 형식 이상: " + str(type(d)))
        return True
    rt = str(d.get("rt_cd", ""))
    if rt not in ("", "0"):
        notes.append(label + " rt_cd=" + rt + " msg=" + str(d.get("msg1", ""))[:120])
        return True
    return False

def token():
    """KIS 토큰 발급은 빈도 제한(EGW00133 계열)이 있어 단발 호출이면 잡 전체가 죽는다.
    2026-09-09 점검: 이 함수가 try 없이 호출돼 스케줄 실패 시 커밋이 0건이 되던 지점."""
    last = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(BASE + "/oauth2/tokenP",
                data=json.dumps({"grant_type": "client_credentials", "appkey": APPKEY, "appsecret": APPSECRET}).encode(),
                headers={"Content-Type": "application/json"}, method="POST")
            with urllib.request.urlopen(req, timeout=20) as r:
                body = json.loads(r.read())
            if body.get("access_token"):
                return body["access_token"]
            last = "no access_token: " + json.dumps(body, ensure_ascii=False)[:200]
        except Exception as e:
            last = repr(e)
        print("[WARN] token attempt " + str(attempt + 1) + " 실패: " + str(last))
        time.sleep(20 * (attempt + 1))
    raise RuntimeError("KIS 토큰 발급 3회 실패 — " + str(last))

def main():
    global TK
    closed, ny = market_closed()
    if not closed:
        print("[SKIP] 미국장 마감 전 — 뉴욕 " + ny.strftime("%Y-%m-%d %H:%M %Z")
              + " (마감 16:00 + 버퍼 " + str(CLOSE_BUFFER_MIN) + "분). 파일을 건드리지 않고 종료.")
        return
    BD = base_date_of(ny)
    if already_have(BD) and os.environ.get("FORCE", "0") != "1":
        print("[SKIP] " + BD + " 데이터 이미 확보됨 — 중복 수집·커밋 생략 (강제 실행은 FORCE=1)")
        return
    print("[GO] 뉴욕 " + ny.strftime("%Y-%m-%d %H:%M %Z") + " / 거래일 " + BD + " — 수집 시작")
    TK = token()
    out = {"generated_at": datetime.now(KST).isoformat(),
           "units": {"trading_amount": "USD(tamt 원시값 — probe 검증)", "volume": "주"},
           "rank_value": [], "stocks": {}, "new_highs": [], "notes": []}

    all_rank = {}
    for excd in ["NYS", "NAS", "AMS"]:
        try:
            d = http_get("/uapi/overseas-stock/v1/ranking/trade-pbmn", "HHDFS76320010",
                         {"EXCD": excd, "NDAY": "0", "VOL_RANG": "0", "AUTH": "", "KEYB": "", "PRC1": "", "PRC2": ""})
            if api_err(d, "rank " + excd, out["notes"]):
                rows = []
            else:
                rows = d.get("output2", []) or d.get("output1", []) or []
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

    # ⚠ 2026-09-09 점검: 9/4(거래일) 스냅샷인데 new_highs 0건 + notes 빈 배열이었다.
    #   = 예외 없이 output2 가 비어 온 것 → GUBN2 값 또는 응답 필드명 문제.
    #   KQI/F002 자가 발견과 같은 방식으로 후보를 순회하고, 어느 조합이 먹었는지 notes 에 남긴다.
    GUBN2_CANDIDATES = ["1", "0", "2", "3"]
    for excd in ["NYS", "NAS", "AMS"]:
        try:
            rows, used = [], None
            for g2 in GUBN2_CANDIDATES:
                d = http_get("/uapi/overseas-stock/v1/ranking/new-highlow", "HHDFS76300000",
                             {"EXCD": excd, "MINX": "0", "VOL_RANG": "0", "GUBN": "1", "GUBN2": g2, "KEYB": "", "AUTH": ""})
                if api_err(d, "new-high " + excd + " GUBN2=" + g2, out["notes"]):
                    time.sleep(0.4)
                    continue
                cand = d.get("output2", []) or d.get("output1", []) or []
                if PROBE:
                    print("NEWHIGH " + excd + " GUBN2=" + g2 + ": keys=" + str(list(d.keys())) + " rows=" + str(len(cand)))
                if cand:
                    rows, used = cand, g2
                    break
                time.sleep(0.4)
            if used is None:
                out["notes"].append("new-high " + excd + ": GUBN2 " + "/".join(GUBN2_CANDIDATES) + " 전부 0건")
            else:
                out["notes"].append("new-high " + excd + ": GUBN2=" + used + " 채택 (" + str(len(rows)) + "건)")
            for it in rows:
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

    # base_date — 노션 「미국장 마감 데이터 소스 규격」의 신선도 게이트가 요구하는 필드.
    # KR JSON 에는 있는데 US 에는 없어서 데일리가 generated_at + 대표 종목 등락률로 우회 판정해야 했다.
    # ⚠ 휴장일은 반영하지 못하는 '주말만 고려한 추정치'다. 그래서 source 를 함께 박아 둔다.
    out["base_date"] = BD
    out["base_date_source"] = "computed(weekday-only, 휴장일 미반영)"
    out["staleness_probe"] = [{"symbol": r["symbol"], "change_rate": r["change_rate"]} for r in ranked[:3]]
    out["base_date_note"] = "미국 직전 영업일 데이터 (휴장일엔 그 전 영업일 스냅샷 — 데일리는 base_date + staleness_probe 를 함께 확인)"

    os.makedirs("data", exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    ok_syms = sum(1 for v in out["stocks"].values() if v)
    print("[OK] rank=" + str(len(out['rank_value'])) + " stocks=" + str(ok_syms) + "/" + str(len(SYMBOLS)) + " new_highs=" + str(len(out['new_highs'])) + " notes=" + str(out['notes'][:5]))

if __name__ == "__main__":
    main()
