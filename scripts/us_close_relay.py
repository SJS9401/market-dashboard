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
MAX_WAIT_MIN = 300      # 잡 타임아웃(6h) 안에서 허용하는 최대 대기
WAITED_MIN = 0          # 실제 대기 분 (notes 기록용)
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

# ── 대기 루프 (2026-09-11 신설) ────────────────────────────────
# GitHub 예약 디스패치가 상시 1~4시간씩 밀린다(2026-09-10·11 실측). 언제 깨우는지를
# 통제할 수 없으므로, 아주 이른 슬롯에 예약해 두고 깨어난 시점이 마감 전이면
# 여기서 자고 일어나 수집한다. 지연이 0이든 2시간이든 도착 시각이 같아진다.
# ★ 부수 효과 — 서머타임 전환도 자동 흡수된다. 뉴욕 시계를 직접 보고 기다리므로
#   여름 마감 05:00 KST / 겨울 06:00 KST 어느 쪽이든 마감 직후에 수집한다.
def wait_for_close():
    global WAITED_MIN
    closed, ny = market_closed()
    if closed:
        return True, ny
    cutoff = ny.replace(hour=16, minute=CLOSE_BUFFER_MIN, second=0, microsecond=0)
    wait_s = (cutoff - ny).total_seconds()
    if wait_s > MAX_WAIT_MIN * 60:
        print("[SKIP] 마감까지 " + str(int(wait_s // 60)) + "분 — 최대 대기("
              + str(MAX_WAIT_MIN) + "분) 초과. 파일을 건드리지 않고 종료.")
        return False, ny
    print("[WAIT] 뉴욕 " + ny.strftime("%Y-%m-%d %H:%M %Z") + " — 마감까지 "
          + str(int(wait_s // 60)) + "분 대기 후 수집")
    while True:
        time.sleep(60)
        WAITED_MIN += 1
        closed, ny = market_closed()
        if closed:
            break
        if WAITED_MIN > MAX_WAIT_MIN:
            print("[SKIP] 대기 " + str(WAITED_MIN) + "분 초과 — 중단")
            return False, ny
    print("[GO-AFTER-WAIT] 뉴욕 " + ny.strftime("%Y-%m-%d %H:%M %Z")
          + " / 대기 " + str(WAITED_MIN) + "분")
    return True, ny
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
    closed, ny = wait_for_close()
    if not closed:
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
    if WAITED_MIN:
        out["notes"].append("마감 대기 " + str(WAITED_MIN) + "분 후 수집(예약 디스패치 조기 발화)")

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

    # ⚠ 2026-09-10 원인 확정 — 9/10 자동 슬롯 notes 전량이 "ERROR INPUT FIELD NOT FOUND [NDAY]" 였다.
    #   GUBN2 값 문제가 아니라, KIS 가 이 TR 에 NDAY 필수 입력을 추가했는데 우리가 안 보내고 있었다.
    #   (같은 파일의 trade-pbmn 은 이미 NDAY="0" 을 넘긴다. 공식 예제·문서에는 아직 NDAY 가 없다.)
    #   → NDAY x GUBN2 조합을 자가 순회하고(KQI/F002 방식), 먹은 조합은 캐시해 다음 거래소에 먼저 쓴다.
    #   실패 노트는 거래소당 1줄로 요약한다 — 조합 전수를 notes 에 쏟으면 데일리가 읽기 어렵다.
    NDAY_CANDIDATES = ["0", "1", "2", "3"]
    GUBN2_CANDIDATES = ["1", "0"]
    COMBOS = [(nd, g2) for nd in NDAY_CANDIDATES for g2 in GUBN2_CANDIDATES]
    found_combo = None
    for excd in ["NYS", "NAS", "AMS"]:
        try:
            rows, used, errs = [], None, []
            trial = ([found_combo] + [c for c in COMBOS if c != found_combo]) if found_combo else list(COMBOS)
            for nd, g2 in trial:
                d = http_get("/uapi/overseas-stock/v1/ranking/new-highlow", "HHDFS76300000",
                             {"EXCD": excd, "NDAY": nd, "MINX": "0", "VOL_RANG": "0",
                              "GUBN": "1", "GUBN2": g2, "KEYB": "", "AUTH": ""})
                if api_err(d, "new-high " + excd + " NDAY=" + nd + "/GUBN2=" + g2, errs):
                    time.sleep(0.4)
                    continue
                cand = d.get("output2", []) or d.get("output1", []) or []
                if PROBE:
                    print("NEWHIGH " + excd + " NDAY=" + nd + " GUBN2=" + g2 + ": keys=" + str(list(d.keys())) + " rows=" + str(len(cand)))
                if cand:
                    rows, used = cand, (nd, g2)
                    found_combo = used
                    break
                time.sleep(0.4)
            if used is None:
                out["notes"].append("new-high " + excd + ": " + str(len(trial)) + "개 조합 전부 실패 — "
                                    + (errs[0] if errs else "오류 없이 0건 반환"))
            else:
                out["notes"].append("new-high " + excd + ": NDAY=" + used[0] + "/GUBN2=" + used[1]
                                    + " 채택 (" + str(len(rows)) + "건)")
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
    # ⚠ 2026-09-11 실측: new-highlow 응답에는 tamt 가 없다(전부 null).
    #   구 코드는 tamt 로 정렬 후 상위 80건을 잘랐는데, 키가 전부 0이라 정렬이 무의미해지고
    #   API 응답 순서(NYS→NAS→AMS)가 그대로 남아 NYS 98건이 80칸을 다 먹고
    #   NAS·AMS 200건이 통째로 잘려나갔다. → 거래소별 40건 균등 컷으로 교체했었다.
    # ⚠⚠ 2026-09-12 재설계 — 40건 컷도 같은 병이었다.
    #   정렬 키가 없으니 "거래소별 40건"은 결국 API 응답 순서 앞 40개라는 임의 절단이고,
    #   거래소당 100건 중 60건(전체의 60%)을 아무 근거 없이 버린다.
    #   실제로 9/12 데일리는 이 120건을 거의 쓰지 못하고 인사이더트래킹 45종으로 ③-2를 판정했다.
    #   → 전수 보존하되 필드를 줄여 용량을 맞춘다.
    #     tamt = 항상 null 이므로 삭제 / price = ③-2 판정에 안 쓰이므로 삭제.
    #     symbol / name / change_rate / exchange / is_etf 만 남긴다 (항목당 약 85B, 300건 ≈ 25KB).
    #   ⚠ 거래소당 100건은 API 1페이지 상한이다(KEYB 페이징 미사용) — '전체'가 아니라 '1페이지 전수'.
    #   시총 필터는 이 API 가 시총을 안 주므로 불가 — $1B+ 필터가 있는 인사이더트래킹이
    #   ③-2 의 1순위이고 이 리스트는 그 리스트의 누락을 잡는 교차검증용이다.
    slim, by_ex = [], {}
    for it in out["new_highs"]:
        ex = it.get("exchange")
        slim.append({"symbol": it.get("symbol"), "name": it.get("name", ""),
                     "change_rate": it.get("change_rate"), "exchange": ex,
                     "is_etf": it.get("is_etf", False)})
        by_ex[ex] = by_ex.get(ex, 0) + 1
    out["new_highs"] = slim
    out["notes"].append("new-high 전수 보존 " + str(len(slim)) + "건 ("
                        + ", ".join(k + " " + str(v) for k, v in by_ex.items())
                        + ") — tamt 미제공으로 정렬·컷 불가, 거래소당 100건은 API 1페이지 상한")

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
    # ★ 2026-09-12 신설 — 날짜별 스냅샷도 함께 쓴다 (KR 릴레이는 처음부터 이 구조였다).
    #   latest 만 있으면 데일리가 그날 못 읽고 지나간 순간 그 회차 데이터는 영영 사라진다.
    #   실제로 2026-09-12 회차가 CDN 캐시 때문에 멀쩡한 파일을 스테일로 오판해 버렸는데,
    #   KR 은 날짜별 파일이 있어 위클리가 되찾을 수 있었고 US 는 그게 없어 불가능했다.
    #   워크플로가 data/us_close_*.json 을 add 하므로 별도 설정 불필요.
    #   용량 — 회차당 약 75KB, 거래일 기준 연 약 18MB. 리포 규모상 문제 없음.
    with open("data/us_close_" + BD.replace("-", "") + ".json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    ok_syms = sum(1 for v in out["stocks"].values() if v)
    print("[OK] rank=" + str(len(out['rank_value'])) + " stocks=" + str(ok_syms) + "/" + str(len(SYMBOLS)) + " new_highs=" + str(len(out['new_highs'])) + " notes=" + str(out['notes'][:5]))

if __name__ == "__main__":
    main()
