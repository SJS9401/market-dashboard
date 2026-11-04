"""
Leading Stocks (주도주) HTML 차트 생성기 v3
- 입력: ls_data_v3.json (키움 OHLC + 거래대금(억))
- 출력: Leading_stocks.html
- 스타일: BT 시장사이클 주봉차트.html 방식 (3단 스택 차트 + HTS 툴팁 + 크로스헤어 동기화)

뷰1 전체 히스토리: KOSPI(상) / 주도주(중) / 거래대금(하) 3단 스택, 주봉
뷰2 사이클 단위: 동일 3단 스택, 일봉/주봉 토글, 전체차트 보기
공통: 한국식 캔들(양봉=빨강 #E74C3C, 음봉=파랑 #3498DB),
      MA 5/10/20/60/120, HTS 툴팁(우상단 고정),
      크로스헤어 Y축폭 독립 동기화(scaleFix + dateValue 기반),
      드래그 줌, 휠 팬, 우측 경계 → 최근 데이터까지 드래그
      기본값: Linear + 일봉
"""

import json, os

# ===== 1. LOAD DATA =====
DATA_PATH = os.path.join(os.path.dirname(__file__), 'ls_data_v3.json')
if not os.path.exists(DATA_PATH):
    DATA_PATH = os.path.join(os.path.dirname(__file__), 'ls_new.json')

with open(DATA_PATH, encoding='utf-8') as f:
    raw = json.load(f)
# 보강 OHLC (ls_data_v3.json 에 없는 주도주 — 상장폐지 종목 등). 이미 있으면 덮어쓰지 않음
_extra_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "extra_stocks.json")
if os.path.exists(_extra_path):
    with open(_extra_path, encoding="utf-8") as _f:
        _extra = json.load(_f)
    for _k, _v in _extra.get("stocks", {}).items():
        if _k not in raw["stocks"]:
            raw["stocks"][_k] = _v
            raw.setdefault("meta", {})[_k] = _extra.get("meta", {}).get(_k, {})

# ===== 2. STOCK / CYCLE DEFINITIONS =====
LEADING_STOCKS = [
    # (stock_id, display_name, era_label, cycle_id, cycle_name, cycle_start, cycle_end, peak_start, peak_end)
    # era 리네이밍 (2026-04-19): 연도 → "연도 + 축약 내러티브 키워드"
    # 사이클명 변경: sideways_2011 / sideways_2023 를 "횡보 순환매장" 통일
    # 1986~1989 3저호황 (트로이카: 건설·증권·무역)
    ("hyundai_const", "현대건설",      "1988 서울올림픽",              "kr_troika_1986",     "1986~1989 3저호황",           "1986-01-01", "1989-12-31", "1987-01-01", "1989-03-01"),
    ("daishin_sec",   "대신증권",      "1989 코스피 첫 1,000 돌파",    "kr_troika_1986",     "1986~1989 3저호황",           "1986-01-01", "1989-12-31", "1988-01-01", "1989-04-01"),
    # 1990~1994 블루칩 (세부 섹터로 분할)
    ("kepco",         "한국전력",      "1994 공기업 민영화",           "kr_bluechip_1990",   "1990~1994 블루칩",            "1990-01-01", "1994-12-31", "1993-01-01", "1994-06-01"),
    ("posco",         "POSCO홀딩스",   "1994 포철 설비투자",           "kr_bluechip_1990",   "1990~1994 블루칩",            "1990-01-01", "1994-12-31", "1993-01-01", "1994-06-01"),
    ("hyundai_motor", "현대차",        "1994 자동차 수출 확대",        "kr_bluechip_1990",   "1990~1994 블루칩",            "1990-01-01", "1994-12-31", "1993-01-01", "1994-06-01"),
    ("spc_samlib",    "SPC삼립",       "1993 삼립호빵 내수",           "kr_bluechip_1990",   "1990~1994 블루칩",            "1990-01-01", "1994-12-31", "1993-01-01", "1994-12-31"),
    ("samsung_elec",  "삼성전자",      "1994 반도체 호황",             "kr_bluechip_1990",   "1990~1994 블루칩",            "1990-01-01", "1994-12-31", "1993-06-01", "1994-12-31"),
    # 1998~2000 IT강세장
    ("sk_telecom",    "SK텔레콤",      "1999 휴대폰 대중화",           "kr_it_1998",         "1998~2000 IT 버블 (통신·반도체)",          "1998-06-01", "2000-01-15", "1999-01-01", "2000-03-01"),
    ("samsung_elec",  "삼성전자",      "1999 반도체 회복·IT 버블",     "kr_it_1998",         "1998~2000 IT 버블 (통신·반도체)",          "1998-06-01", "2000-01-15", "1998-10-01", "2000-03-01"),
    ("daishin_sec",   "대신증권",      "1999 바이코리아 유동성",       "kr_it_1998",         "1998~2000 IT 버블 (통신·반도체)",          "1998-06-01", "2000-01-15", "1998-10-01", "1999-12-31"),
    ("hyundai_sec",   "현대증권",      "1999 바이코리아 펀드",         "kr_it_1998",         "1998~2000 IT 버블 (통신·반도체)",          "1998-06-01", "2000-01-15", "1998-10-01", "1999-12-31"),
    # 2001~2002 내수/카드버블
    ("coway",         "코웨이",        "2002 정수기 렌탈 개척",        "kr_card_2002",       "2001~2002 내수/카드버블 (렌탈)",     "2001-01-01", "2002-12-31", "2001-06-01", "2002-06-01"),
    # 2003~2007 중국 중후장대
    ("hyundai_elev",  "현대엘리베이터", "2004 중국 고층빌딩",           "kr_china_2003",      "2004~2007 중국 인프라 1 (조선·건설·철강)",     "2003-03-01", "2007-10-31", "2003-06-01", "2005-06-01"),
    ("hyundai_mipo",  "현대미포조선",   "2007 조선 슈퍼사이클",         "kr_china_2003",      "2004~2007 중국 인프라 1 (조선·건설·철강)",     "2003-03-01", "2007-10-31", "2005-01-01", "2007-10-01"),
    ("posco",         "POSCO홀딩스",   "2007 중국 철강 수요",          "kr_china_2003",      "2004~2007 중국 인프라 1 (조선·건설·철강)",     "2003-03-01", "2007-10-31", "2005-06-01", "2007-10-01"),
    # 2009~2011 차화정 (자동차·화학·정유)
    ("hyundai_motor", "현대차",        "2010 현대차 美 점유율 급등",   "kr_chahwajeong_2009","2009~2011 중국 인프라 2 (차화정)",            "2009-01-01", "2011-04-30", "2009-03-01", "2011-04-01"),
    ("kia",           "기아",          "2010 K5 턴어라운드",           "kr_chahwajeong_2009","2009~2011 중국 인프라 2 (차화정)",            "2009-01-01", "2011-04-30", "2009-03-01", "2011-04-01"),
    ("lg_chem",       "LG화학",        "2010 석유화학 호황",           "kr_chahwajeong_2009","2009~2011 중국 인프라 2 (차화정)",            "2009-01-01", "2011-04-30", "2009-03-01", "2011-04-01"),
    ("s_oil",         "S-Oil",         "2010 정제마진 확대",           "kr_chahwajeong_2009","2009~2011 중국 인프라 2 (차화정)",            "2009-01-01", "2011-04-30", "2009-03-01", "2011-04-01"),
    # 2011~2016 횡보 순환매장 (이름 변경, 삼성전자 2012~2013 스마트폰 신규 추가)
    ("samsung_elec",  "삼성전자",      "2012~2013 갤럭시S 히트",       "kr_smartphone_2012", "2012~2013 스마트폰 탄생",     "2011-08-01", "2013-12-31", "2012-01-01", "2013-05-31"),
    ("amorepacific",  "아모레퍼시픽",   "2014~2015 중국 따이공 K-뷰티", "kr_kbeauty_2015",    "2015~2016 중국 화장품·바이오 기술이전",     "2014-01-01", "2016-06-30", "2014-06-01", "2015-11-01"),
    ("hanmi_pharm",   "한미약품",      "2015 제약 사상 최대 기술수출", "kr_kbeauty_2015",    "2015~2016 중국 화장품·바이오 기술이전",     "2014-01-01", "2016-06-30", "2014-06-01", "2015-11-01"),
    # 2016~2018 반도체·바이오
    ("sk_hynix",      "SK하이닉스",    "2017 서버 D램 슈퍼사이클",     "kr_semi_2016",       "2017~2018 반도체 서버·바이오시밀러",     "2016-02-01", "2018-01-31", "2016-06-01", "2017-11-01"),
    ("celltrion",     "셀트리온",      "2017 바이오시밀러 미국 진출",  "kr_semi_2016",       "2017~2018 반도체 서버·바이오시밀러",     "2016-02-01", "2018-01-31", "2016-06-01", "2018-06-01"),
    # 2020~2021 코로나 강세장 (BBIG)
    ("seegene",       "씨젠",          "2020 코로나 진단키트",         "kr_covid_bull",      "2020~2021 진단키트·플랫폼·해운",     "2020-01-01", "2021-08-31", "2020-01-01", "2020-08-01"),
    ("hmm",           "HMM",           "2020 컨테이너 운임 폭등",      "kr_covid_bull",      "2020~2021 진단키트·플랫폼·해운",     "2020-01-01", "2021-08-31", "2020-06-01", "2021-06-01"),
    ("kakao",         "카카오",        "2021 자회사 IPO 붐",           "kr_covid_bull",      "2020~2021 진단키트·플랫폼·해운",     "2020-01-01", "2021-08-31", "2020-06-01", "2021-06-24"),
    ("sk_hynix",      "SK하이닉스",    "2021 반도체 대형주 랠리",      "kr_covid_bull",      "2020~2021 진단키트·플랫폼·해운",     "2020-01-01", "2021-08-31", "2020-09-01", "2021-03-31"),
    # 2023~2024 횡보 순환매장 (이름 변경)
    ("ecopro",        "에코프로",      "2023 美 IRA 수혜",             "kr_battery_2023",    "2023~2024 배터리·바이오 플랫폼",     "2022-10-01", "2025-03-31", "2023-01-01", "2023-07-01"),
    ("hanmi_semi",    "한미반도체",    "2023 엔비디아 HBM 본더",       "kr_battery_2023",    "2023~2024 배터리·바이오 플랫폼",     "2022-10-01", "2025-03-31", "2023-06-01", "2024-07-01"),
    ("alteogen",      "알테오젠",      "2024 SC 제형 플랫폼 기술이전", "kr_battery_2023",    "2023~2024 배터리·바이오 플랫폼",     "2022-10-01", "2025-03-31", "2024-01-01", "2025-01-01"),
    # 2025~ AI·조선·원전
    ("hanwha_ocean",  "한화오션",      "2025 미 해군 MRO",             "kr_ai_2025",         "2025~2026 조선·원전·반도체 / 방산·전력",          "2025-04-01", "2026-04-16", "2024-06-01", "2026-04-16"),
    ("doosan_enerbil","두산에너빌리티","2025 SMR 원전",                "kr_ai_2025",         "2025~2026 조선·원전·반도체 / 방산·전력",          "2025-04-01", "2026-04-16", "2024-06-01", "2026-04-16"),
    ("sk_hynix",      "SK하이닉스",    "2025 에이전트 AI",             "kr_ai_2025",         "2025~2026 조선·원전·반도체 / 방산·전력",          "2025-04-01", "2026-04-16", "2024-06-01", "2025-02-01"),
    ("samsung_elec",  "삼성전자",      "2025 에이전트 AI",             "kr_ai_2025",         "2025~2026 조선·원전·반도체 / 방산·전력",          "2025-04-01", "2026-04-16", "2025-10-01", "2026-04-16"),
]

# ===== AUTO-COMPUTE Longterm Zones (MA120 기반 중장기 박스, 2026-04-19 재구성) =====
# 기존 peak_zone(단기 스윙) 폐기. 새 규칙은 project_leading_stocks_box_restructure.md 참조.
#
# 시작점: [cycle_start, peak_high] 구간의 low argmin
# 종료점 (3-Step Cascade):
#   Step 1: peak_high 이후 close < MA60 첫 날 = ma60_break_idx
#   Step 2: [ma60_break_idx, +_LT_SWING_WIN] 구간 low argmin = swing_low_idx
#   Step 3: swing_low_idx 이후 close < low[swing_low_idx] 첫 날 (옵션 A)
#           + 2단계 휩쏘 필터:
#             1차 barrier = swing_low_price
#             1차 이탈 후 _LT_WHIPSAW_WIN 거래일 내 close ≥ swing_low_price 회귀 시 → 휩쏘 판정
#               → barrier를 whipsaw 구간 [이탈일, 회귀일] 의 low 최저값으로 교체, whipsaw_mode ON
#             2차 이탈 (close < whipsaw_low) 발생 시 → 즉시 종료 확정 (휩쏘 필터 미적용)
#
# Status:
#   진행중 (ongoing): Step 1 실패 (MA60 유지) → end = 데이터 최종일 (박스 우측 열림 표시)
#   조정중 (correction): Step 1~2 OK, Step 3 실패 (swing low 미이탈) → end = 데이터 최종일 (박스 우측 열림)
#   종료 (closed):   Step 3 충족 → end = 이탈일

LONGTERM_OVERRIDES = {
    # (stock_id, cycle_id): {"start": "YYYY-MM-DD" or None, "end": "YYYY-MM-DD" or None, "status": "..."}
    # 자동 산출 결과가 이상할 때만 override
}

_LT_SWING_WIN = 20          # MA60 이탈 후 swing low 탐색 거래일 (약 1개월)
_LT_WHIPSAW_WIN = 5         # 1차 이탈 휩쏘 필터: 이탈 후 회귀 판정 거래일
_LT_RECOVERY_WIN = 20       # 2차 이탈 후 3차 회귀 판정 거래일 (2026-04-20 추가)
_LT_RS_RECOVERY_WIN = 60    # 기술적 상대강도 재회귀 탐색 거래일 (2026-04-20 추가)
_LT_PREV_SL_WIN = 10        # peak_high 직전 swing low window (±5거래일 local min)
_LT_PREV_SL_WIN_IDX = 6     # 지수 prev swing low window (더 민감하게 = 최근 support)
                            # 비대칭 설계: 종목은 deep support(window=10), 지수는 recent support(window=6)
                            # 유저 원칙: 종목이 강한 저점 지키고, 지수가 최근 저점 깨면 → 기술적 상대강도 우위
_LT_PREV_SL_LOOKBACK = 150  # peak_high 직전 swing low 최대 lookback (약 7개월)
_LT_MA120_SLOPE_WIN = 20    # MA120 slope 체크 (validation only, 현재 미사용)


def _compute_prev_swing_low(rows, ph_idx, window=None, lookback=None):
    """peak_high 직전의 swing low 탐지.
    알고리즘: peak_high - half 시점부터 뒤로 lookback 거래일 범위를 스캔,
             각 포인트 i에 대해 low[i]가 [i-half, i+half] 구간의 최저값이면 swing low.
             peak_high에 가장 가까운(i가 가장 큰) swing low를 반환.
    설계 근거: SK하이닉스 2017/9/4, KOSPI 2017/9/28 같은 "직전 조정 바닥"을
             자동 탐지 (사용자 직관 일치, window=10).
    Returns: {"idx": int, "low": float, "date": "YYYY-MM-DD"} or None.
    """
    if window is None: window = _LT_PREV_SL_WIN
    if lookback is None: lookback = _LT_PREV_SL_LOOKBACK
    if ph_idx < window:
        return None
    lows = [r[3] for r in rows]
    half = window // 2
    start_i = ph_idx - half - 1
    end_i = max(half, ph_idx - lookback)
    for i in range(start_i, end_i - 1, -1):
        if i - half < 0 or i + half >= len(rows):
            continue
        if lows[i] == min(lows[i - half:i + half + 1]):
            d8 = rows[i][0]
            return {"idx": i, "low": lows[i], "date": f"{d8[:4]}-{d8[4:6]}-{d8[6:8]}"}
    return None


def _compute_longterm_zone(rows, cycle_start, cycle_end, peak_high_date=None, kospi_rows=None):
    """중장기 박스 계산. rows: [[YYYYMMDD,o,h,l,c,v], ...] ascending.
    Returns: {"start", "end", "status"} with dates as 'YYYY-MM-DD', or None on failure.
    peak_high_date: lifecycle에서 넘어온 peak_high (있으면 사용, 없으면 cycle 범위 내 close max fallback).
    kospi_rows: KOSPI OHLC (기술적 상대강도 재회귀 판정용). None이면 Step 5 skip.
    """
    if not rows:
        return None
    def rm(d): return d.replace("-", "")
    def fmt(d8): return f"{d8[:4]}-{d8[4:6]}-{d8[6:8]}"
    cs = rm(cycle_start); ce = rm(cycle_end)
    n = len(rows)
    closes = [r[4] for r in rows]
    lows = [r[3] for r in rows]

    # MA60 / MA120 (MA120은 현재 validation-only, 미사용)
    ma60 = [None] * n
    r60 = 0.0
    for i in range(n):
        r60 += closes[i]
        if i >= 60: r60 -= closes[i-60]
        if i >= 59: ma60[i] = r60 / 60.0

    # cycle_start 이후 첫 idx
    cs_idx = None
    for i, r in enumerate(rows):
        if r[0] >= cs:
            cs_idx = i; break
    if cs_idx is None:
        return None

    # cycle_end 이하 마지막 idx
    ce_idx = cs_idx
    for i in range(cs_idx, n):
        if rows[i][0] <= ce:
            ce_idx = i
        else:
            break

    # peak_high_idx 결정
    ph_idx = -1
    if peak_high_date:
        ph = rm(peak_high_date)
        for i in range(cs_idx, n):
            if rows[i][0] == ph:
                ph_idx = i; break
        if ph_idx < 0:
            for i in range(cs_idx, n):
                if rows[i][0] >= ph:
                    ph_idx = i; break
    if ph_idx < 0:
        # Fallback: [cs_idx, ce_idx] close 최대일
        ph_idx = cs_idx
        for i in range(cs_idx, ce_idx + 1):
            if closes[i] > closes[ph_idx]: ph_idx = i

    # 시작점 탐색 window 결정
    # 원칙: [cycle_start, peak_high]
    # 보정: 종목의 상승이 cycle 정의보다 먼저 시작된 경우 (예: 한화오션 2025 — lifecycle peak_high가
    #       cycle_start보다 이전) → peak_high 기준 250거래일(약 1년) lookback 허용
    search_start_idx = cs_idx
    if ph_idx <= cs_idx:
        search_start_idx = max(0, ph_idx - 250)
        if search_start_idx >= ph_idx:
            return None

    # 시작점: [search_start_idx, ph_idx-1] low argmin
    start_idx = search_start_idx
    start_low = lows[search_start_idx]
    for i in range(search_start_idx, ph_idx):
        if lows[i] < start_low:
            start_low = lows[i]; start_idx = i

    # Step 1: peak_high 이후 close < MA60 첫 날
    ma60_break_idx = None
    for i in range(ph_idx + 1, n):
        if ma60[i] is None: continue
        if closes[i] < ma60[i]:
            ma60_break_idx = i; break

    if ma60_break_idx is None:
        return {
            "start": fmt(rows[start_idx][0]),
            "end": fmt(rows[n - 1][0]),
            "status": "진행중",
            "peak_high_close": closes[ph_idx],
            "swing_low_close": None,
        }

    # Step 2: swing low 탐색 [ma60_break_idx, +_LT_SWING_WIN]
    swing_end = min(ma60_break_idx + _LT_SWING_WIN, n - 1)
    swing_low_idx = ma60_break_idx
    swing_low_price = lows[ma60_break_idx]
    for i in range(ma60_break_idx, swing_end + 1):
        if lows[i] < swing_low_price:
            swing_low_price = lows[i]; swing_low_idx = i

    # Step 3: swing low 이탈 + 2단계 휩쏘 필터
    # 1차 barrier = swing_low_price
    # 1차 이탈 후 5일 내 close ≥ swing_low_price 회귀 시 → 휩쏘 판정, barrier를 whipsaw_low로 교체
    # 2차 이탈 (close < whipsaw_low) → 종료 확정 (휩쏘 필터 미적용)
    barrier = swing_low_price
    whipsaw_mode = False
    i = swing_low_idx + 1
    end_idx = None
    while i < n:
        if closes[i] < barrier:
            if whipsaw_mode:
                # 2차 이탈 = 휩쏘 구간 저가 이탈 → 종료 확정
                end_idx = i; break
            # 1차 이탈. 휩쏘 체크
            whipsaw_end = min(i + _LT_WHIPSAW_WIN, n - 1)
            recover_j = None
            for j in range(i + 1, whipsaw_end + 1):
                if closes[j] >= swing_low_price:
                    recover_j = j; break
            if recover_j is not None:
                # 휩쏘 판정. 휩쏘 구간 [i, recover_j] 의 low 최저값을 새 barrier로
                whipsaw_low_price = min(lows[i:recover_j + 1])
                barrier = whipsaw_low_price
                whipsaw_mode = True
                i = recover_j + 1
                continue
            else:
                end_idx = i; break
        i += 1

    if end_idx is None:
        return {
            "start": fmt(rows[start_idx][0]),
            "end": fmt(rows[n - 1][0]),
            "status": "조정중",
            "peak_high_close": closes[ph_idx],
            "swing_low_close": closes[swing_low_idx],
        }

    # Step 4: 3차 회귀 판정 (2026-04-20 추가)
    # 2차 이탈 종료 후 _LT_RECOVERY_WIN 거래일 내 close ≥ swing_low_price (원래 1차 barrier)
    # 회복 시 → 박스 재연장 (2차 이탈 무효화).
    # 재연장 이후 close < swing_low_price 재이탈 시 → 최종 종료 (필터 없음).
    recovery_end = min(end_idx + _LT_RECOVERY_WIN, n - 1)
    recovery_j = None
    for j in range(end_idx + 1, recovery_end + 1):
        if closes[j] >= swing_low_price:
            recovery_j = j; break

    if recovery_j is None:
        final_end_idx = end_idx  # Step 4 실패 → 2차 이탈 종료
        recovered_flag = False
    else:
        # 3차 회귀 발생 → 재연장. 이후 재이탈 (close < swing_low_price) 시 최종 종료
        final_end_idx = None
        for i in range(recovery_j + 1, n):
            if closes[i] < swing_low_price:
                final_end_idx = i; break
        recovered_flag = True

        if final_end_idx is None:
            # 재연장 후 아직 안 깸 = 박스 우측 열림
            return {
                "start": fmt(rows[start_idx][0]),
                "end": fmt(rows[n - 1][0]),
                "status": "재연장",
                "peak_high_close": closes[ph_idx],
                "swing_low_close": closes[swing_low_idx],
            }

    # Step 5: 기술적 상대강도 재회귀 (2026-04-20 추가)
    # 2차 이탈 또는 3차 회귀 후 재이탈로 종료된 경우, 지수-종목 간 기술적 상대강도 체크.
    # 조건 (AND):
    #   (a) 종료일(final_end_idx) 후 _LT_RS_RECOVERY_WIN 거래일 내
    #   (b) KOSPI low < KOSPI prev_swing_low (지수 이전 조정 저점 붕괴)
    #   (c) 종목 low > 종목 prev_swing_low (종목 이전 조정 저점 유지)
    #   (d) 종목 close ≥ swing_low_price (현재 사이클 barrier) 회복
    # 위 모두 만족 시 → 박스를 회귀일(d) 이후로 재연장, status = "재연장-RS"
    rs_extended = False
    rs_recovery_date = None
    if kospi_rows:
        stock_psl = _compute_prev_swing_low(rows, ph_idx)
        # KOSPI의 peak_high에 해당하는 idx 탐색 (종목 ph_date와 동일 or 이후 첫 날짜)
        ph_d8 = rows[ph_idx][0]
        kospi_ph_idx = None
        for ki, kr in enumerate(kospi_rows):
            if kr[0] >= ph_d8:
                kospi_ph_idx = ki; break
        # 비대칭 window: 지수는 더 민감한(작은) window로 최근 support까지 포착
        kospi_psl = _compute_prev_swing_low(kospi_rows, kospi_ph_idx, window=_LT_PREV_SL_WIN_IDX) if kospi_ph_idx else None

        if stock_psl and kospi_psl:
            # 종료일 이후 _LT_RS_RECOVERY_WIN 거래일 내 탐색
            rs_end = min(final_end_idx + _LT_RS_RECOVERY_WIN, n - 1)
            # 같은 구간 KOSPI idx 매핑
            fe_d8 = rows[final_end_idx][0]
            re_d8 = rows[rs_end][0]
            k_fe_idx = next((ki for ki, kr in enumerate(kospi_rows) if kr[0] >= fe_d8), None)
            k_re_idx = next((ki for ki, kr in enumerate(kospi_rows) if kr[0] > re_d8), len(kospi_rows)) - 1
            if k_fe_idx is not None and k_re_idx >= k_fe_idx:
                kospi_min_low = min(kr[3] for kr in kospi_rows[k_fe_idx:k_re_idx + 1])
                stock_min_low = min(r[3] for r in rows[final_end_idx:rs_end + 1])
                cond_b = kospi_min_low < kospi_psl["low"]
                cond_c = stock_min_low > stock_psl["low"]
                if cond_b and cond_c:
                    # 종목 close ≥ swing_low_price 회복일 탐색
                    for j in range(final_end_idx + 1, rs_end + 1):
                        if closes[j] >= swing_low_price:
                            # KOSPI 저점이 이 시점 이전에 형성됐는지 확인 (반등 동조)
                            k_j_idx = next((ki for ki, kr in enumerate(kospi_rows) if kr[0] >= rows[j][0]), None)
                            if k_j_idx is not None:
                                k_low_before_j = min(kr[3] for kr in kospi_rows[k_fe_idx:k_j_idx + 1])
                                if k_low_before_j < kospi_psl["low"]:
                                    rs_extended = True
                                    rs_recovery_date = rows[j][0]
                                    break

    if rs_extended:
        # 기술적 상대강도 재회귀 성공 → 박스 데이터 끝까지 재연장 (진짜 이탈 감지 전까지)
        # 회귀일 이후 새 이탈 탐색: close < swing_low_price
        rs_j = next(i for i, r in enumerate(rows) if r[0] == rs_recovery_date)
        rs_final_end = None
        for i in range(rs_j + 1, n):
            if closes[i] < swing_low_price:
                rs_final_end = i; break
        if rs_final_end is None:
            return {
                "start": fmt(rows[start_idx][0]),
                "end": fmt(rows[n - 1][0]),
                "status": "재연장-RS",
                "peak_high_close": closes[ph_idx],
                "swing_low_close": closes[swing_low_idx],
                "rs_recovery": rs_recovery_date[:4] + "-" + rs_recovery_date[4:6] + "-" + rs_recovery_date[6:8],
            }
        return {
            "start": fmt(rows[start_idx][0]),
            "end": fmt(rows[rs_final_end][0]),
            "status": "종료",
            "peak_high_close": closes[ph_idx],
            "swing_low_close": closes[swing_low_idx],
            "recovered": True,
            "rs_recovery": rs_recovery_date[:4] + "-" + rs_recovery_date[4:6] + "-" + rs_recovery_date[6:8],
        }

    return {
        "start": fmt(rows[start_idx][0]),
        "end": fmt(rows[final_end_idx][0]),
        "status": "종료",
        "peak_high_close": closes[ph_idx],
        "swing_low_close": closes[swing_low_idx],
        "recovered": recovered_flag,
    }


# ===== SIDEWAYS DETECTION (2026-04-20) =====
# 목적: 이전 상승장의 매물대 상단(peak_high) 대비 현재 사이클이 횡보장인지 판정.
# 프레임워크 (사용자 확정, 2026-04-19 세션):
#   - 매물대 상단 = prev cycle peak_high close (이전 상승장의 고점)
#   - 현재 사이클이 매물대 상단을 돌파 X + 반등 강도 부족(= 내부에 머묾) → 횡보장
#
# 2 조건 (AND):
#   A. 매물대 상단 미돌파: cycle_max_close < prev_peak_close × 1.15
#   B. 반등 강도 부족: bounce% < 40% OR 50% 되돌림 실패
#      - bounce% = (cycle_min 이후 cycle_max - cycle_min) / cycle_min × 100
#      - 50% 되돌림 = (prev_peak_close + cycle_min_close) / 2  # prev_peak ↔ cycle 저점 중간
#      - 50% 되돌림 실패 = cycle의 bounce_high < 50% 되돌림 지점
#
# 설계 결정: 기존 3조건 프레임워크에서 "매물대 하단 미이탈" 조건 제거.
#   이유: prev_swing_low_close는 3-Step Cascade의 1차 swing low이며, 실제 bear market 바닥을
#        담지 못함 (예: 1997 IMF 바닥 280 ≠ kr_bluechip_1990 의 swing_low 1026). 따라서
#        prev_swing_low 기준 이탈 판정이 불가능. 대안으로 50% 되돌림 계산에서도 prev_swing_low
#        대신 cycle_min_close 를 사용.
#
# 검증 케이스:
#   - 2011-2016 (sideways): cond_A ✓, cond_B (bounce 31.5% < 40%) ✓ → sideways
#   - 2023-2024 (sideways): cond_A ✓, cond_B (bounce 33.7% < 40%) ✓ → sideways
#   - 1990-1994 (uptrend):  cond_A ✓, cond_B (bounce 148%) ✗ → uptrend
#   - 1998-2000 (uptrend):  cond_A ✓, cond_B (bounce 278%) ✗ → uptrend
#   - 2001-2002 (uptrend):  cond_A ✓, cond_B (bounce 100%) ✗ → uptrend
#   - 2003-2007 (uptrend):  cond_A ✗ (+119% 돌파) → uptrend
#   - 2009-2011 (uptrend):  cond_A ✓, cond_B (bounce 118%) ✗ → uptrend
#   - 2016-2018 (uptrend):  cond_A ✗ → uptrend
#   - 2020-2021 (uptrend):  cond_A ✗ → uptrend
#   - 2025-    (uptrend):  cond_A ✗ → uptrend

_SW_BREAKOUT_TH = 1.15    # 매물대 상단 돌파 기준 (×prev_peak)
_SW_BOUNCE_TH = 40.0      # 반등 강도 기준 (%)


def _compute_sideways_detection(rows, cycle_start, cycle_end, prev_peak_close, prev_swing_low_close=None):
    """현재 사이클이 횡보장인지 판정.
    Returns: {"is_sideways": bool, "diagnostics": {...}} or None on failure.

    2 조건 (AND): cond_A (매물대 상단 미돌파) + cond_B (반등 강도 부족)
    prev_swing_low_close 는 diagnostics 기록용으로만 사용 (판정엔 영향 없음).
    """
    if not rows or prev_peak_close is None or prev_peak_close <= 0:
        return None

    def rm(d): return d.replace("-", "")
    cs, ce = rm(cycle_start), rm(cycle_end)
    n = len(rows)

    cs_idx, ce_idx = -1, -1
    for i, r in enumerate(rows):
        if cs_idx < 0 and r[0] >= cs:
            cs_idx = i
        if r[0] <= ce:
            ce_idx = i
        elif cs_idx >= 0:
            break
    if cs_idx < 0 or ce_idx < cs_idx:
        return None

    # cycle close 통계
    seg = rows[cs_idx:ce_idx + 1]
    closes = [r[4] for r in seg]
    if not closes:
        return None
    cycle_max_close = max(closes)
    cycle_min_close = min(closes)

    # bounce: cycle_min 이후 cycle_max (bounce_high)
    min_rel = 0
    for i, c in enumerate(closes):
        if c < closes[min_rel]:
            min_rel = i
    bounce_low = closes[min_rel]
    bounce_high = bounce_low
    for i in range(min_rel, len(closes)):
        if closes[i] > bounce_high:
            bounce_high = closes[i]
    bounce_pct = (bounce_high - bounce_low) / bounce_low * 100.0 if bounce_low > 0 else 0.0

    # 50% 되돌림 (prev_peak ↔ cycle 저점 중간)
    midpoint = (prev_peak_close + cycle_min_close) / 2.0
    retrace_failed = bounce_high < midpoint

    # 2 조건 (AND)
    cond_a = cycle_max_close < prev_peak_close * _SW_BREAKOUT_TH
    cond_b = (bounce_pct < _SW_BOUNCE_TH) or retrace_failed

    is_sw = cond_a and cond_b

    return {
        "is_sideways": is_sw,
        "diagnostics": {
            "prev_peak_close": prev_peak_close,
            "prev_swing_low_close": prev_swing_low_close,
            "cycle_max_close": cycle_max_close,
            "cycle_min_close": cycle_min_close,
            "bounce_low": bounce_low,
            "bounce_high": bounce_high,
            "bounce_pct": bounce_pct,
            "midpoint": midpoint,
            "retrace_failed": retrace_failed,
            "cond_A_nobreakout": cond_a,
            "cond_B_weakBounce": cond_b,
        }
    }


# ===== AUTO-COMPUTE Lifecycle Zones (관성~F~낙주~수렴~전고점 트라이, 2026-04-19) =====
# Rule (see .auto-memory/project_lifecycle_detection_spec.md):
#   peak_high : window max close 의 85% 이상 && 다음 3거래일 내 -7%+ 낙폭 && local max (k=1)
#               → 조건 만족하는 FIRST 캔들
#   F         : [peak_high - 10거래일, peak_high] 구간에서 A(volume) max == B(pct_close) max 동시
#               → A=B primary, 아니면 B-preferred fallback
#   inertia   : F 기준 역 20거래일 (관성 시작)
#   peak_try  : [peak_high + 3, peak_high + 30] 구간에서
#               상위권(Δc OR Δh ≥ inertia avg, volume ≥ inertia avg) 캔들 중 high 최대값
#
# Lifecycle window 오버라이드: 특정 (stock_id, cycle_id)에 대해 좁은 search window 사용
# (LEADING_STOCKS의 manual_peak가 너무 넓을 때)
LIFECYCLE_OVERRIDES = {
    # (stock_id, cycle_id): (window_start, window_end)
    ("hanwha_ocean",   "kr_ai_2025"): ("2024-12-09", "2025-04-06"),
    ("doosan_enerbil", "kr_ai_2025"): ("2025-04-08", "2025-08-18"),
    ("sk_hynix",       "kr_ai_2025"): ("2025-08-21", "2025-11-21"),
    ("samsung_elec",   "kr_ai_2025"): ("2025-12-16", "2026-03-31"),
}

# Params (튜닝: 4개 케이스 검증 완료)
_LC_INERTIA_DAYS = 20
_LC_F_LOOKBACK = 10
_LC_NAKJU_DROP_TH = -7.0
_LC_NAKJU_WIN = 3
_LC_PEAK_CLOSE_RATIO = 0.85
_LC_PT_MIN_GAP = 3
_LC_PT_MAX_GAP = 30


def _compute_lifecycle_zone(rows, w_start, w_end):
    """rows: [[YYYYMMDD,o,h,l,c,v], ...] ascending.
    Returns dict with markers as 'YYYY-MM-DD' strings, or None if detection fails.
    """
    if not rows or not w_start or not w_end:
        return None
    def rm(d): return d.replace("-", "")
    def fmt(d8): return f"{d8[:4]}-{d8[4:6]}-{d8[6:8]}"
    ws, we = rm(w_start), rm(w_end)
    n = len(rows)
    # window bounds
    i_start, i_end = -1, -1
    for i, r in enumerate(rows):
        if i_start < 0 and r[0] >= ws:
            i_start = i
        if r[0] <= we:
            i_end = i
        else:
            break
    if i_start < 0 or i_end < 0 or i_start >= i_end:
        return None

    closes = [r[4] for r in rows]
    highs = [r[2] for r in rows]
    vols = [r[5] for r in rows]
    # pct_close, pct_high (enrich)
    pct_c = [0.0] * n
    pct_h = [0.0] * n
    for i in range(1, n):
        pc = closes[i - 1]
        if pc > 0:
            pct_c[i] = (closes[i] - pc) / pc * 100.0
            pct_h[i] = (highs[i] - pc) / pc * 100.0

    # 1) peak_high: FIRST day satisfying:
    #    - close >= window_max_close × 0.85
    #    - local max (k=1)
    #    - next 3 days close drops by >= 7%
    win_max_close = max(closes[i_start:i_end + 1])
    thresh_close = win_max_close * _LC_PEAK_CLOSE_RATIO
    ph_idx = -1
    for i in range(i_start, min(i_end + 1, n - 1)):
        if closes[i] < thresh_close:
            continue
        if i > 0 and closes[i - 1] >= closes[i]:
            continue
        if i + 1 < n and closes[i + 1] >= closes[i]:
            continue
        end = min(n, i + 1 + _LC_NAKJU_WIN)
        if end <= i + 1:
            continue
        min_c = min(closes[i + 1:end])
        drop = (min_c - closes[i]) / closes[i] * 100.0
        if drop <= _LC_NAKJU_DROP_TH:
            ph_idx = i
            break
    if ph_idx < 0:
        return None

    # 2) F: [ph - F_LOOKBACK, ph] 에서 A=B (primary) or B-preferred fallback
    fs = max(0, ph_idx - _LC_F_LOOKBACK)
    fe = ph_idx
    a_idx, b_idx = fs, fs
    for i in range(fs, fe + 1):
        if vols[i] > vols[a_idx]:
            a_idx = i
        if pct_c[i] > pct_c[b_idx]:
            b_idx = i
    f_idx = a_idx if a_idx == b_idx else b_idx

    # 3) inertia: [F - 20, F]
    in_s = max(0, f_idx - _LC_INERTIA_DAYS + 1)
    in_e = f_idx
    in_win = rows[in_s:in_e + 1]
    if not in_win:
        return None
    avg_pct_c = sum(pct_c[in_s:in_e + 1]) / (in_e - in_s + 1)
    avg_pct_h = sum(pct_h[in_s:in_e + 1]) / (in_e - in_s + 1)
    avg_vol = sum(vols[in_s:in_e + 1]) / (in_e - in_s + 1)

    # 4) peak_try: [ph + 3, ph + 30] 상위권 중 high 최대
    s = ph_idx + _LC_PT_MIN_GAP
    e = min(n, ph_idx + _LC_PT_MAX_GAP + 1, i_end + 1)
    pt_idx = -1
    pt_high = -1
    for i in range(s, e):
        pct_ok = (pct_c[i] >= avg_pct_c) or (pct_h[i] >= avg_pct_h)
        vol_ok = vols[i] >= avg_vol
        if pct_ok and vol_ok:
            if highs[i] > pt_high:
                pt_high = highs[i]
                pt_idx = i

    return {
        "inertia_start": fmt(rows[in_s][0]),
        "F": fmt(rows[f_idx][0]),
        "peak_high": fmt(rows[ph_idx][0]),
        "peak_try": fmt(rows[pt_idx][0]) if pt_idx >= 0 else None,
        # 박스 영역
        "box_start": fmt(rows[in_s][0]),
        "box_end": fmt(rows[pt_idx][0]) if pt_idx >= 0 else fmt(rows[ph_idx][0]),
    }


# Apply lifecycle detection for configured overrides
_computed_lifecycles = {}  # (stock_id, cycle_id) -> lifecycle dict or None
for _s in LEADING_STOCKS:
    _sid, _cid = _s[0], _s[3]
    _override = LIFECYCLE_OVERRIDES.get((_sid, _cid))
    if _override:
        _ws, _we = _override
        _rows = raw["stocks"].get(_sid, [])
        _lc = _compute_lifecycle_zone(_rows, _ws, _we)
        _computed_lifecycles[(_sid, _cid)] = _lc
    else:
        _computed_lifecycles[(_sid, _cid)] = None

# Apply longterm zone detection (uses lifecycle's peak_high if available)
# KOSPI rows preloaded here to support Step 5 (기술적 상대강도 재회귀) in _compute_longterm_zone
_kospi_rows_preload = raw["stocks"].get("kospi", [])
_computed_longterms = {}  # (stock_id, cycle_id) -> longterm dict or None
for _s in LEADING_STOCKS:
    _sid, _cid, _cs, _ce = _s[0], _s[3], _s[5], _s[6]
    _override = LONGTERM_OVERRIDES.get((_sid, _cid))
    if _override:
        _computed_longterms[(_sid, _cid)] = _override
        continue
    _rows = raw["stocks"].get(_sid, [])
    _lc = _computed_lifecycles.get((_sid, _cid))
    _ph = _lc.get("peak_high") if _lc else None
    _lt = _compute_longterm_zone(_rows, _cs, _ce, _ph, _kospi_rows_preload)
    _computed_longterms[(_sid, _cid)] = _lt

# ===== AUTO-COMPUTE Index Cycle Bounds (KOSPI, 2026-04-19, sideways v2 2026-04-20) =====
# 지수 사이클 박스의 start/end를 KOSPI에 _compute_longterm_zone + sideways detection 적용해 자동 탐지.
# Pass 1: 각 cycle에 대해 _compute_longterm_zone 실행 → peak_high_close / swing_low_close 추출
# Pass 2: 이전 uptrend cycle의 매물대 (prev_peak_close, prev_swing_low_close) 기반
#         _compute_sideways_detection → 현재 cycle sideways 여부 판정
# Pass 3: sideways로 판정된 cycle은 전체 manual 범위로 박스 확장 (종료=cycle_end)
#         그 외는 Pass 1의 3-Step Cascade 결과 사용
# 복원 백업: .auto-memory/project_index_cycle_manual_backup.md
INDEX_CYCLE_OVERRIDES = {
    # cycle_id: {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD", "status": "..."}
    # 자동 산출 결과가 이상할 때만 등록. 횡보장은 sideways detection이 자동 처리함.
}

_kospi_rows = raw["stocks"].get("kospi", [])

# Pass 0: LEADING_STOCKS에서 cycle_id 순서 + manual (cs, ce) 수집
_cycle_order_for_index = []
_cycle_manual = {}
_seen_cid_ord = set()
for _s in LEADING_STOCKS:
    _cid, _cs, _ce = _s[3], _s[5], _s[6]
    if _cid in _seen_cid_ord:
        continue
    _seen_cid_ord.add(_cid)
    _cycle_order_for_index.append(_cid)
    _cycle_manual[_cid] = (_cs, _ce)

# Pass 1: 각 cycle에 대해 _compute_longterm_zone 실행
_cycle_longterm_raw = {}  # cycle_id -> longterm_zone result dict (peak_high_close, swing_low_close 포함)
for _cid in _cycle_order_for_index:
    _cs, _ce = _cycle_manual[_cid]
    _cycle_longterm_raw[_cid] = _compute_longterm_zone(_kospi_rows, _cs, _ce, None)

# Pass 2: sideways detection (순차 진행, prev cycle 의 매물대 기준)
_sideways_detected = {}   # cycle_id -> bool
_sideways_diag = {}       # cycle_id -> diagnostics dict
_prev_peak_close = None
_prev_swing_low_close = None
for _cid in _cycle_order_for_index:
    _cs, _ce = _cycle_manual[_cid]
    _is_sw = False
    _sw_res = None
    if _prev_peak_close is not None and _prev_swing_low_close is not None:
        _sw_res = _compute_sideways_detection(
            _kospi_rows, _cs, _ce, _prev_peak_close, _prev_swing_low_close
        )
        if _sw_res:
            _is_sw = bool(_sw_res.get("is_sideways"))
    _sideways_detected[_cid] = _is_sw
    if _sw_res:
        _sideways_diag[_cid] = _sw_res.get("diagnostics")

    # 매물대 기준점 갱신: sideways이면 이전 값 유지 (횡보 중엔 기준 리셋하지 않음)
    #                    uptrend/downtrend이면 현재 cycle 값으로 업데이트
    _lt = _cycle_longterm_raw.get(_cid)
    if _lt and not _is_sw:
        _new_peak = _lt.get("peak_high_close")
        _new_swing = _lt.get("swing_low_close")
        if _new_peak is not None:
            _prev_peak_close = _new_peak
        if _new_swing is not None:
            _prev_swing_low_close = _new_swing

# Pass 3: 최종 INDEX_CYCLE 조립
_computed_index_cycles = {}  # cycle_id -> {start, end, status} or None
for _cid in _cycle_order_for_index:
    _override = INDEX_CYCLE_OVERRIDES.get(_cid)
    if _override:
        _computed_index_cycles[_cid] = _override
        continue
    _cs, _ce = _cycle_manual[_cid]
    if _sideways_detected.get(_cid):
        # 횡보장: 전체 manual cycle 범위 사용 (횡보 밴드 전체 표시)
        _computed_index_cycles[_cid] = {
            "start": _cs,
            "end": _ce,
            "status": "횡보",
        }
    else:
        _computed_index_cycles[_cid] = _cycle_longterm_raw.get(_cid)


# ===== Per-index cycle zones (KOSPI / KOSDAQ / S&P500 / NASDAQ) =====
# 각 지수마다 _compute_longterm_zone (3-Step Cascade + 2단계 휩쏘) 적용해
# 사이클 박스 계산. KOSPI 는 위에서 sideways detection까지 적용된 결과 재사용.
_per_index_zones = {}  # cycle_id -> { idx_id: {start,end,status} }
_idx_rows_map = {
    "kospi":  raw["stocks"].get("kospi",  []),
    "kosdaq": raw["stocks"].get("kosdaq", []),
    "sp500":  raw["stocks"].get("sp500",  []),
    "nasdaq": raw["stocks"].get("nasdaq", []),
}
for _cid in _cycle_order_for_index:
    _cs, _ce = _cycle_manual[_cid]
    _zone_per_idx = {}
    # KOSPI: 기존 sideways/longterm 결과 재사용
    _kz = _computed_index_cycles.get(_cid)
    if _kz:
        _zone_per_idx["kospi"] = {
            "start": _kz.get("start"),
            "end": _kz.get("end"),
            "status": _kz.get("status"),
        }
    # 나머지 3 지수: longterm zone 만 (sideways detection 미적용)
    for _idx_id in ("kosdaq", "sp500", "nasdaq"):
        _rows = _idx_rows_map[_idx_id]
        if not _rows:
            continue
        _lt = _compute_longterm_zone(_rows, _cs, _ce, None)
        if _lt and _lt.get("start") and _lt.get("end"):
            _zone_per_idx[_idx_id] = {
                "start": _lt.get("start"),
                "end": _lt.get("end"),
                "status": _lt.get("status"),
            }
    if _zone_per_idx:
        _per_index_zones[_cid] = _zone_per_idx

# ===== SECTOR CATEGORY (2026-11-03, BT 확정) =====
# 인프라 = B2B + 설비투자 필요 / 기술 = B2B + 설비 불필요(기술이전·플랫폼) / 소비 = B2C / 참고 = 1998 이전
SECTOR_CATEGORY = {
    ("hyundai_const","kr_troika_1986"):"참고", ("daishin_sec","kr_troika_1986"):"참고",
    ("kepco","kr_bluechip_1990"):"참고", ("posco","kr_bluechip_1990"):"참고",
    ("hyundai_motor","kr_bluechip_1990"):"참고", ("spc_samlib","kr_bluechip_1990"):"참고",
    ("sk_telecom","kr_it_1998"):"인프라", ("samsung_elec","kr_it_1998"):"인프라", ("daishin_sec","kr_it_1998"):"참고", ("hyundai_sec","kr_it_1998"):"참고", ("samsung_elec","kr_bluechip_1990"):"참고",
    ("coway","kr_card_2002"):"소비",
    ("hyundai_elev","kr_china_2003"):"인프라", ("hyundai_mipo","kr_china_2003"):"인프라", ("posco","kr_china_2003"):"인프라",
    ("hyundai_motor","kr_chahwajeong_2009"):"인프라", ("kia","kr_chahwajeong_2009"):"인프라",
    ("lg_chem","kr_chahwajeong_2009"):"인프라", ("s_oil","kr_chahwajeong_2009"):"인프라",
    ("samsung_elec","kr_smartphone_2012"):"소비",
    ("amorepacific","kr_kbeauty_2015"):"소비", ("hanmi_pharm","kr_kbeauty_2015"):"기술",
    ("sk_hynix","kr_semi_2016"):"인프라", ("celltrion","kr_semi_2016"):"인프라",
    ("seegene","kr_covid_bull"):"인프라", ("hmm","kr_covid_bull"):"인프라", ("kakao","kr_covid_bull"):"소비", ("sk_hynix","kr_covid_bull"):"인프라",
    ("ecopro","kr_battery_2023"):"인프라", ("hanmi_semi","kr_battery_2023"):"인프라", ("alteogen","kr_battery_2023"):"기술",
    ("hanwha_ocean","kr_ai_2025"):"인프라", ("doosan_enerbil","kr_ai_2025"):"인프라",
    ("sk_hynix","kr_ai_2025"):"인프라", ("samsung_elec","kr_ai_2025"):"인프라",
}
_SECTOR_ORDER = ["인프라", "기술", "소비", "참고"]
# 섹터 박스 종료일 보정 (종목 자체 중장기 박스는 그대로, 섹터 박스 기여분만 자름) — BT 지시 2026-11-03
#   알테오젠: 2025년부터 코스피가 코스닥을 아웃퍼폼하는 시장 → 2024년 말로 종료
#   기아: 차화정 동반 붕괴(2011-08) 시점에 맞춤 (현대차 8/3, LG화학 8/4, S-Oil 8/10)
SECTOR_END_OVERRIDES = {
    ("alteogen", "kr_battery_2023"): "2024-12-31",
    ("kia", "kr_chahwajeong_2009"): "2011-08-10",
}
# 사이클·분류별 섹터 박스 = 해당 분류 주도주 중장기 박스의 합집합 (가장 이른 시작 ~ 가장 늦은 종료)
_sector_zones = {}   # cycle_id -> [ {cat, start, end, status, stocks}, ... ]
_sector_union = {}   # cycle_id -> {start, end, status}
for _s in LEADING_STOCKS:
    _sid, _cid = _s[0], _s[3]
    _lt = _computed_longterms.get((_sid, _cid))
    if not _lt or not _lt.get("start") or not _lt.get("end"):
        continue
    _cat = SECTOR_CATEGORY.get((_sid, _cid), "참고")
    _lst = _sector_zones.setdefault(_cid, [])
    _z = next((z for z in _lst if z["cat"] == _cat), None)
    _closed = _lt.get("status") == "종료"
    _lt_end = _lt["end"]
    if (_sid, _cid) in SECTOR_END_OVERRIDES:
        _lt_end = min(_lt_end, SECTOR_END_OVERRIDES[(_sid, _cid)]); _closed = True
    if _z is None:
        _lst.append({"cat": _cat, "start": _lt["start"], "end": _lt_end,
                     "status": "종료" if _closed else "진행중", "stocks": [_s[1]]})
    else:
        _z["start"] = min(_z["start"], _lt["start"]); _z["end"] = max(_z["end"], _lt_end)
        if not _closed: _z["status"] = "진행중"
        if _s[1] not in _z["stocks"]: _z["stocks"].append(_s[1])
for _cid, _lst in _sector_zones.items():
    _lst.sort(key=lambda z: _SECTOR_ORDER.index(z["cat"]))
    _sector_union[_cid] = {
        "start": min(z["start"] for z in _lst), "end": max(z["end"] for z in _lst),
        "status": "종료" if all(z["status"] == "종료" for z in _lst) else "진행중",
    }

# Build cycle groups for View 2
cycle_order = []
seen_cycles = set()
for s in LEADING_STOCKS:
    cid = s[3]
    if cid not in seen_cycles:
        seen_cycles.add(cid)
        _idx = _sector_union.get(cid) or _computed_index_cycles.get(cid)
        if _idx:
            _cstart, _cend, _cstatus = _idx["start"], _idx["end"], _idx.get("status")
        else:
            _cstart, _cend, _cstatus = s[5], s[6], None
        cycle_order.append({
            "id": cid, "name": s[4],
            "start": _cstart, "end": _cend,
            "status": _cstatus,
            "manualStart": s[5], "manualEnd": s[6],  # 백업용 (복원 가능)
            "indexZones": _per_index_zones.get(cid, {}),  # idx_id -> {start,end,status} (구 지수 박스, 미사용)
            "sectorZones": _sector_zones.get(cid, []),    # 주도 섹터 박스 (2026-11-03)
            "stocks": []
        })
    _lt = _computed_longterms.get((s[0], cid))
    _lc = _computed_lifecycles.get((s[0], cid))
    _entry = {"id": s[0], "name": s[1], "era": s[2]}
    if _lt:
        _entry["longterm"] = _lt  # {start, end, status}
    if _lc:
        _entry["lifecycle"] = _lc  # {inertia_start, F, peak_high, peak_try, box_start, box_end}
    for c in cycle_order:
        if c["id"] == cid:
            c["stocks"].append(_entry)
            break

# Unique stocks for View 1 (with longterm zones for highlight)
unique_stocks = []
seen_stock_ids = set()
stock_zones = []  # For View 1 highlights
all_stock_entries = []  # v1 상단 탭: LEADING_STOCKS 1엔트리 = 버튼 1개 (중복 stock도 별도)

for s in LEADING_STOCKS:
    key = s[0]
    if key not in seen_stock_ids:
        seen_stock_ids.add(key)
        unique_stocks.append({"id": s[0], "name": s[1], "era": s[2]})
    _lt = _computed_longterms.get((s[0], s[3]))
    _lc = _computed_lifecycles.get((s[0], s[3]))
    # 라벨 포맷: "연도 종목명(키워드)"  e.g. "1988 현대건설(올림픽)"
    _era = s[2]
    _sp = _era.find(" ")
    if _sp < 0:
        _label = _era + " " + s[1]
    else:
        _label = _era[:_sp] + " " + s[1] + "(" + _era[_sp+1:] + ")"
    _z = {
        "stockId": s[0],
        "cycleId": s[3],
        "label": _label,
    }
    if _lt:
        _z["longterm"] = _lt
    if _lc:
        _z["lifecycle"] = _lc
    stock_zones.append(_z)
    all_stock_entries.append({
        "id": s[0],
        "name": s[1],
        "era": s[2],
        "cycleId": s[3],
        "label": _label,
    })

STOCK_COLORS = [
    "#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7",
    "#DDA0DD", "#98D8C8", "#F7DC6F", "#BB8FCE", "#85C1E9",
    "#F1948A", "#82E0AA", "#F8C471", "#AED6F1", "#D7BDE2",
    "#A3E4D7", "#FAD7A0", "#E59866", "#F5B7B1", "#ABEBC6",
    "#AED6F1", "#F9E79F", "#D5DBDB", "#FADBD8", "#D1F2EB",
    "#FCF3CF", "#EBDEF0", "#D6EAF8"
]

# ===== 3. PREPARE DATA =====
stocks_data = {}
for uid in seen_stock_ids:
    if uid in raw["stocks"]:
        stocks_data[uid] = raw["stocks"][uid]

kospi_data = raw["stocks"].get("kospi", [])
kosdaq_data = raw["stocks"].get("kosdaq", [])
sp500_data = raw["stocks"].get("sp500", [])
nasdaq_data = raw["stocks"].get("nasdaq", [])
meta = raw["meta"]

# ===== 미국 시장 사이클 (Market_cycle.html 에서 추출) =====
# extract_market_cycles.py 로 미리 추출. 미국 지수 박스에 사용.
import os as _os
_mc_path = _os.path.join(_os.path.dirname(__file__), "market_cycles.json")
us_market_cycles = []
if _os.path.exists(_mc_path):
    with open(_mc_path, encoding="utf-8") as _f:
        _mc = json.load(_f)
    for _c in _mc.get("cycles", []):
        _idx = set(_c.get("indices", []) or [])
        if _idx & {"SP500", "NASDAQ"}:
            # 박스에 필요한 필드만
            us_market_cycles.append({
                "id":       _c.get("id"),
                "name":     _c.get("name"),
                "start":    _c.get("start"),
                "end":      _c.get("end"),
                "category": _c.get("category"),  # bull / bear
                "subtype":  _c.get("subtype"),
            })
    print(f"[*] US market cycles: {len(us_market_cycles)} 개")
else:
    print(f"[WARN] {_mc_path} 없음 — 미국 사이클 박스 비활성")

# ===== 4. GENERATE HTML =====
# ===== 산업 사이클 (유형별 / 시계열별 탭, 2026-11-03 BT 확정) =====
# type: 재가동형(과거 공급이 줄었다가 다시 도는 산업) / 개척형(처음부터 공급이 없던 산업)
# term: 장기(14~30년) / 중기(4~8년) / 단기(2~5년) / 1회
# cycles: (시작 YYYY-MM, 끝 YYYY-MM 또는 None=진행중, 메모). 시작 = 60·120일선 정배열 진입,
#         산업 가격지표 우선(없으면 영업이익, 바이오만 주가). 근거는 대화 기록·메모리 korea-leadership-cycles 참조
SECTOR_CYCLES_SPEC = [
    {"sector": "건설", "sid": "hyundai_const", "name": "현대건설", "type": "재가동형", "term": "장기", "from": "19850101",
     "cycles": [("1986-01", "1991-12", "3저·주택 200만 호"), ("2004-09", "2008-01", "해외 플랜트·주택"), ("2025-02", None, "원전 시공·주택 공급")],
     "note": "1975~1982 중동 건설 붐은 주가 데이터 없음. 현대엘리베이터 포함(2004 중국 엘리베이터 수요, 대북은 별도 이슈)"},
    {"sector": "조선", "sid": "hd_ksoe", "name": "HD한국조선해양", "type": "재가동형", "term": "장기", "from": "19990101",
     "cycles": [("2004-10", "2011-07", "중국 인프라"), ("2024-02", None, "친환경 선박 교체·MASGA")], "note": "2010년대 도크 축소 후 재가동"},
    {"sector": "해운", "sid": "hmm", "name": "HMM", "type": "재가동형", "term": "장기", "from": "19990101",
     "cycles": [("2002-05", "2008-09", "중국 인프라"), ("2021-02", "2022-12", "공급망 병목")], "note": "기준: 미국 원양화물 PPI. 2016 한진해운 파산"},
    {"sector": "전력", "sid": "ls_electric", "name": "LS ELECTRIC", "type": "재가동형", "term": "장기", "from": "20000101",
     "cycles": [("2004-05", "2008-10", "송전 투자 재개"), ("2020-08", None, "교체·재생에너지·AI")], "note": "기준: 미국 변압기 PPI. 1970년대 전력망 구축기 이후 세 번째"},
    {"sector": "원전", "sid": "doosan_enerbil", "name": "두산에너빌리티", "type": "재가동형", "term": "장기", "from": "20000101",
     "cycles": [("2001-03", "2008-02", "원전 르네상스 (한국 미참여)"), ("2009-12", "2012-12", "UAE 수주 (투자 메리트 낮음)"),
                ("2024-11", "2026-07", "SMR·AI 전력")],
     "note": "2001~07 두산중공업 상승은 중국 인프라·담수 플랜트 몫. 2009~12는 한전기술 이익 업사이클(실적 O, 섹터 쏠림 X). 우라늄 가격은 2021년부터 선행. 한국 원전주 기준 첫 본격 사이클은 2024-11~ SMR"},
    {"sector": "방산", "sid": "hanwha_aero", "name": "한화에어로스페이스", "type": "재가동형", "term": "장기", "from": "19900101",
     "cycles": [("2001-09", "2010-12", "9·11 (한국 미참여)"), ("2022-02", None, "글로벌 재무장")], "note": "글로벌 1980년대/2001/2022, 한국 실적은 2023~ 첫 사이클. 2015년 이전은 삼성테크윈"},
    {"sector": "자동차", "sid": "hyundai_motor", "name": "현대차", "type": "재가동형", "term": "장기", "from": "19850101",
     "cycles": [("1986-01", "1988-12", "3저 호황·수출 호조"), ("2009-03", "2011-08", "금융위기 후 점유율 확대"), ("2020-07", "2021-05", "보복소비·전기차")], "note": "2003년은 멀티플만, 2025년은 로봇 테마라 제외"},
    {"sector": "철강", "sid": "posco", "name": "POSCO홀딩스", "type": "재가동형", "term": "중기", "from": "19900101",
     "cycles": [("2003-10", "2008-10", "중국 인프라"), ("2009-09", "2010-08", "중국 부양책"), ("2016-05", "2018-12", "중국 공급개혁"), ("2020-11", "2022-01", "원자재 랠리"), ("2026-01", None, "강판 가격 반등")],
     "note": "기준: 미국 강판 PPI. 한국 기업은 중국에 밀려 주가 반응이 약함"},
    {"sector": "화학", "sid": "lotte_chem", "name": "롯데케미칼", "type": "재가동형", "term": "중기", "from": "19900101",
     "cycles": [("2004-05", "2008-09", "중국 인프라"), ("2009-06", "2010-04", "중국 부양책"), ("2012-09", "2017-04", "에틸렌 스프레드 최대"), ("2020-05", "2021-05", "코로나 후 수요 회복")],
     "note": "기준: 2009년 이후 에틸렌 스프레드(KB증권), 이전은 미국 석유화학 PPI"},
    {"sector": "정유", "sid": "s_oil", "name": "S-Oil", "type": "재가동형", "term": "중기", "from": "19900101",
     "cycles": [("2004-01", "2008-11", "중국 인프라·고유가"), ("2012-02", "2018-09", "저유가·정제마진 강세"), ("2019-04", "2022-12", "IMO2020·러우 전쟁"), ("2025-01", None, "정제설비 폐쇄")], "note": "기준: 정제마진 (휘발유·경유 − 브렌트)"},
    {"sector": "반도체", "sid": "sk_hynix", "name": "SK하이닉스", "type": "재가동형", "term": "단기", "from": "19970101",
     "cycles": [("2005-02", "2007-10", "PC·낸드"), ("2009-04", "2011-07", "PC 교체"), ("2012-10", "2013-08", "스마트폰"), ("2016-07", "2018-02", "서버"), ("2020-11", "2021-06", "비대면"), ("2025-06", "2026-09", "AI")],
     "note": "2023~2024 HBM은 하이닉스 단독이라 제외"},
    {"sector": "배터리", "sid": "samsung_sdi", "name": "삼성SDI", "type": "재가동형", "term": "단기", "from": "20100101",
     "cycles": [("2017-02", "2018-04", "태동기"), ("2020-02", "2022-01", "전기차 침투율 급증"), ("2022-06", "2023-10", "미국 IRA")], "note": "2023년 이후 공급 과잉으로 재가동형. 2025~2026은 지수 대비 약해 제외"},
    {"sector": "바이오", "sid": "celltrion", "name": "셀트리온", "type": "개척형", "term": "단기", "from": "20050101",
     "cycles": [("2011-08", "2014-05", "바이오시밀러"), ("2014-09", "2015-10", "기술이전"), ("2017-04", "2018-06", "시밀러·신약"), ("2019-12", "2021-03", "진단·CMO"), ("2023-02", "2025-01", "플랫폼(알테오젠)"), ("2026-01", "2026-04", "경구 비만약 기대(삼천당, 데이터 실패)")],
     "note": "매번 세부 분야 교체. 주가 기준 예외(바이오만)"},
    {"sector": "통신", "sid": "telecom_chain", "name": "SK텔레콤 → 통신장비", "type": "재가동형", "term": "중기", "from": "19900101",
     "cycles": [("1998-12", "2000-03", "휴대폰 보급"), ("2005-01", "2007-10", "3G·와이브로"), ("2012-01", "2013-10", "LTE"),
                ("2017-03", "2019-12", "5G"), ("2025-07", "2026-07", "AI 광통신")],
     "note": "2004년까지 SK텔레콤, 2005년~ 통신장비 8종 동일가중(케이엠더블유·쏠리드·에이스테크·다산네트웍스·대한광통신·성호전자·LIG아큐버·RFHIC). 업사이클은 장비사 영업이익 기준"},
    {"sector": "플랫폼", "sid": "kakao", "name": "카카오", "type": "개척형", "term": "1회", "from": "20100101",
     "cycles": [("2020-03", "2021-07", "플랫폼·비대면")], "note": ""},
    {"sector": "증권", "sid": "daishin_sec", "name": "대신증권", "type": "재가동형", "term": "중기", "from": "19900101",
     "cycles": [("1998-10", "1999-09", "바이코리아 유동성"), ("2004-11", "2007-10", "펀드 붐"), ("2020-06", "2021-04", "동학개미"),
                ("2025-03", "2026-07", "비상장 지분 리레이팅")],
     "note": "상승장마다 증시 호황으로 사이클. 2025~26은 스페이스X·앤트로픽 등 비상장 지분가치로 글로벌 IB형 리레이팅"},
    {"sector": "뷰티", "sid": "amorepacific", "name": "아모레퍼시픽", "type": "개척형", "term": "단기", "from": "20060101",
     "cycles": [("2013-12", "2015-09", "중국 화장품"), ("2022-11", "2024-02", "에스테틱 장비"), ("2024-05", "2026-08", "리쥬란·K-뷰티 디바이스")],
     "note": "화장품 → 에스테틱(클래시스·파마리서치·비올) → 에이피알. 바이오처럼 매번 세부 분야 교체. 주가 기준"},
    {"sector": "개별주", "sid": "coway", "name": "코웨이", "type": "개척형", "term": "1회", "from": "19980101",
     "cycles": [("1998-10", "1999-10", "정수기 렌탈 도입")], "note": "렌탈 섹터 사이클은 없었음 — 완전 개별주. IMF 이후 좋은 정수기+구독(렌탈) BM 개척. 이후 상승(2004~06, 2012~14 MBK 인수·이익률 개선, 2023~25)은 회사 개별 이벤트라 제외"},
    {"sector": "음식료", "sid": "spc_samlib", "name": "SPC삼립", "type": "재가동형", "term": "중기", "from": "19900101",
     "cycles": [("1992-11", "1993-10", "삼립호빵 (개척형 성격)"), ("2001-02", "2002-12", "커피믹스 대중화 (개척형 성격)"),
                ("2005-01", "2008-03", "해외 성장·판가 인상·환율 하락"), ("2010-11", "2016-01", "중국 수출·HMR·스프레드 확대"),
                ("2024-04", "2025-12", "K-푸드 수출 (불닭, 개척형 성격)")],
     "note": "이익 = Q×P−C 스프레드 사이클(판가 인상 3~4년 주기: 02~04/07~09/11~12/16~17/20~21/25~). 2차는 오리온 대장·식자재 유통·간편식 동반. 3차는 삼양식품 불닭이 만든 수출이라 개척형 성격. 1993 삼립호빵·2001 동서 커피믹스는 개별 제품이 만든 개척형 구간. 스프레드(식품 CPI ÷ 원화 곡물원가, 6개월 후행) 상승 구간: 1999-07~2001-06, 2014-01~2017-05, 2024-03~. 출처: 유안타증권"},
    {"sector": "디스플레이", "sid": "lgd", "name": "LG디스플레이", "type": "재가동형", "term": "단기", "from": "19900101",
     "cycles": [("2003-10", "2004-07", "LCD 증설"), ("2007-03", "2008-02", "LCD 패널 호황"), ("2010-02", "2011-10", "AMOLED 1차 투자"),
                ("2015-12", "2017-12", "플렉서블 OLED 투자"), ("2020-08", "2021-11", "코로나 TV·IT 수요")],
     "note": "패널 가격·증설 사이클. 2014년 6월 이전 삼성SDI(디스플레이 본업) 포함, AP시스템은 2017 분할 전후 코드 연결. 판정 지표(패널 가격) 미수집 — 주가 기준"},
    {"sector": "전자부품", "sid": "semco", "name": "삼성전기", "type": "재가동형", "term": "중기", "from": "19900101",
     "cycles": [("1998-12", "2000-05", "IT 버블"), ("2009-02", "2010-09", "스마트폰·LED"), ("2017-02", "2018-02", "MLCC 슈퍼사이클"),
                ("2021-01", "2022-08", "기판 대면적화(FC-BGA)"), ("2025-08", None, "AI 기판·MLCC")],
     "note": "MLCC·카메라모듈·기판. 2021~22 FC-BGA 대면적화: 대덕전자 +130%·심텍 +128%·이수페타시스 +127%. 2025~26 삼성전기 +1,480%·LG이노텍 +770%·이수페타시스. 대덕전자·심텍은 분할 전후 코드 연결. 주가 기준"},
    {"sector": "엔터", "sid": "sm_ent", "name": "에스엠", "type": "개척형", "term": "단기", "from": "20000101",
     "cycles": [("2005-02", "2005-10", "한류 1기"), ("2009-12", "2011-02", "K-팝 일본 진출"), ("2017-04", "2019-01", "K-팝 글로벌(트와이스·BTS)"),
                ("2021-04", "2023-10", "팬덤 플랫폼·앨범 판매"), ("2024-12", "2025-11", "한한령 해제 기대")],
     "note": "엔터·미디어. 매번 드라이버 교체. CJ ENM은 2018-07 합병 전 CJ E&M 코드 연결. 주가 기준"},
    {"sector": "게임", "sid": "ncsoft", "name": "엔씨소프트", "type": "개척형", "term": "단기", "from": "20000101",
     "cycles": [("2001-11", "2002-06", "리니지 온라인"), ("2009-01", "2009-09", "아이온"), ("2011-05", "2013-01", "모바일 게임 1기"),
                ("2014-02", "2015-01", "서머너즈워"), ("2017-02", "2018-02", "리니지M"), ("2020-02", "2022-02", "비대면·P2E")],
     "note": "히트작 하나가 사이클을 만드는 개척형. 2021 위메이드 P2E +730%. 엔씨소프트는 플랫폼에서 게임으로 이동. 주가 기준"},
]
_sector_seed = {}
_seed_path = os.path.join(os.path.dirname(__file__), "sector_weekly_seed.json")
if os.path.exists(_seed_path):
    with open(_seed_path, encoding="utf-8") as _f:
        _sector_seed = json.load(_f)
def _to_weekly(rows):
    import datetime as _dt
    out = {}
    for r in rows:
        d = r[0]; c = r[4]
        if not c or c <= 0: continue
        k = _dt.date(int(d[:4]), int(d[4:6]), int(d[6:8])).isocalendar()[:2]
        out[k] = [d, round(float(c), 2)]
    return list(out.values())
sector_cycles = []
for _sp in SECTOR_CYCLES_SPEC:
    _rows = raw["stocks"].get(_sp["sid"])
    _w = _to_weekly(_rows) if _rows else _sector_seed.get(_sp["sid"], [])
    _w = [x for x in _w if x[0] >= _sp.get("from", "19000101")]
    _e = {k: v for k, v in _sp.items() if k != "cycles"}
    _e["cycles"] = [{"start": a, "end": b, "label": c} for a, b, c in _sp["cycles"]]
    _e["series"] = _w
    sector_cycles.append(_e)

# ===== 섹터 시총 합산 (2026-11-03) — 좌축: 섹터 시총 합산(억원), 우축: 코스피+코스닥 대비 비중(%) =====
# (code, sector, from YYYYMMDD, to YYYYMMDD) — 해당 섹터 사업이 본업인 기간만 합산
SECTOR_MEMBERS = [
 ("000720","건설","0","9"),("017800","건설","0","9"),("006360","건설","0","9"),("047040","건설","0","9"),("000210","건설","0","20210430"),("375500","건설","20210501","9"),
 ("009540","조선","0","9"),("329180","조선","0","9"),("010140","조선","0","9"),("042660","조선","0","9"),("010620","조선","0","9"),
 ("011200","해운","0","9"),("028670","해운","0","9"),
 ("010120","전력","0","9"),("267260","전력","0","9"),("298040","전력","0","9"),("103590","전력","0","9"),
 ("034020","원전","0","9"),("052690","원전","0","9"),("051600","원전","0","9"),("015760","원전","20091201","9"),
 ("012450","방산","0","9"),("079550","방산","0","9"),("047810","방산","0","9"),("064350","방산","0","9"),("103140","방산","0","9"),
 ("005380","자동차","0","9"),("000270","자동차","0","9"),("012330","자동차","0","9"),
 ("005490","철강","0","9"),("004020","철강","0","9"),
 ("051910","화학","0","20191231"),("051910","배터리","20200101","20220126"),("051910","화학","20220127","9"),
 ("011170","화학","0","9"),("011780","화학","0","9"),("009830","화학","0","9"),
 ("010950","정유","0","9"),("096770","정유","0","20191231"),("096770","배터리","20200101","9"),
 ("005930","반도체","0","9"),("000660","반도체","0","9"),
 ("373220","배터리","0","9"),("006400","배터리","20140701","9"),("086520","배터리","0","9"),("247540","배터리","0","9"),
 ("066970","배터리","20120101","9"),("003670","배터리","20190401","9"),
 ("068270","바이오","0","9"),("091990","바이오","0","9"),("207940","바이오","0","9"),("128940","바이오","0","9"),
 ("008930","바이오","0","9"),("000100","바이오","0","9"),("096530","바이오","0","9"),("196170","바이오","0","9"),("215600","바이오","0","9"),("000250","바이오","0","9"),
 ("017670","통신","0","9"),("030200","통신","0","9"),("032640","통신","0","9"),
 ("032500","통신","0","9"),("050890","통신","0","9"),("088800","통신","0","9"),("039560","통신","0","9"),
 ("010170","통신","0","9"),("043260","통신","0","9"),("073490","통신","0","9"),("218410","통신","0","9"),
 ("035420","플랫폼","0","9"),("035720","플랫폼","0","9"),
 ("006800","증권","0","9"),("071050","증권","0","9"),("016360","증권","0","9"),("005940","증권","0","9"),("039490","증권","0","9"),("003540","증권","0","9"),
 ("097950","음식료","0","9"),("001800","음식료","0","20170630"),("271560","음식료","20170701","9"),("004370","음식료","0","9"),
 ("007310","음식료","0","9"),("003230","음식료","0","9"),("049770","음식료","0","9"),("005610","음식료","0","9"),("051500","음식료","0","9"),
 ("031440","음식료","0","9"),("026960","음식료","0","9"),("005300","음식료","0","9"),("004990","음식료","0","20171031"),("280360","음식료","20171101","9"),
 ("001680","음식료","0","9"),("005180","음식료","0","9"),
 ("090430","뷰티","0","9"),("051900","뷰티","0","9"),("192820","뷰티","0","9"),("161890","뷰티","0","9"),("214150","뷰티","0","9"),
 ("214450","뷰티","0","9"),("335890","뷰티","0","9"),("278470","뷰티","0","9"),("145020","뷰티","0","9"),
 ("001440","전력","0","9"),("000500","전력","0","9"),("006260","전력","0","9"),("062040","전력","0","9"),("033100","전력","0","9"),("006730","전력","0","9"),
 ("443060","조선","0","9"),("082740","조선","0","9"),("023160","조선","0","9"),("014620","조선","0","9"),
 ("000240","자동차","0","20120930"),("161390","자동차","20121001","9"),("018880","자동차","0","9"),("005850","자동차","0","9"),("007340","자동차","0","9"),
 ("028050","건설","0","9"),("002380","건설","0","9"),("038500","건설","0","9"),
 ("028300","바이오","0","9"),("141080","바이오","0","9"),("298380","바이오","0","9"),("326030","바이오","0","9"),("087010","바이오","0","9"),("328130","바이오","0","9"),
 ("241710","뷰티","0","9"),("257720","뷰티","0","9"),("251970","뷰티","0","9"),
 ("034220","디스플레이","0","9"),("006400","디스플레이","0","20140630"),("054620","디스플레이","0","20170331"),("265520","디스플레이","20170401","9"),
 ("213420","디스플레이","0","9"),("171090","디스플레이","0","9"),("161580","디스플레이","0","9"),
 ("009150","전자부품","0","9"),("011070","전자부품","0","9"),("007660","전자부품","0","9"),("008060","전자부품","0","20200430"),("353200","전자부품","20200501","9"),
 ("036710","전자부품","0","20150731"),("222800","전자부품","20150801","9"),
 ("352820","엔터","0","9"),("035900","엔터","0","9"),("041510","엔터","0","9"),("122870","엔터","0","9"),("130960","엔터","0","20180630"),("035760","엔터","20180701","9"),("253450","엔터","0","9"),
 ("036570","게임","0","9"),("251270","게임","0","9"),("259960","게임","0","9"),("263750","게임","0","9"),("293490","게임","0","9"),("112040","게임","0","9"),("078340","게임","0","9"),("225570","게임","0","9"),("069080","게임","0","9"),
]
def _load_mcap():
    import gzip as _gz, datetime as _dt
    snap, names = {}, {}
    base = os.path.dirname(os.path.abspath(__file__))
    for fn, combined in (("kr_mcap_pre2010.json.gz", True), ("kr_mcap_history.json.gz", False)):
        fp = os.path.join(base, "data", fn)
        if not os.path.exists(fp):
            continue
        try:
            h = json.loads(_gz.decompress(open(fp, "rb").read()).decode("utf-8"))
        except Exception as _ex:
            print(f"[WARN] {fn} 로드 실패: {_ex}"); continue
        names.update(h.get("codes", {}))
        for d, t, caps in zip(h["dates"], h["tot"], h["days"]):
            snap[d] = (t if combined else t[0] + t[1], caps)
    last = {}
    for d in sorted(snap):
        last[_dt.date(int(d[:4]), int(d[4:6]), int(d[6:8])).isocalendar()[:2]] = d
    return snap, sorted(last.values()), names
try:
    _snap, _wdays, _mnames = _load_mcap()
except Exception as _ex:
    print(f"[WARN] 섹터 시총 로드 실패: {_ex}"); _snap, _wdays, _mnames = {}, [], {}
_sec_mcap = {}
for _d in _wdays:
    _tot, _caps = _snap[_d]
    _acc = {}
    for _c, _sec, _a, _b in SECTOR_MEMBERS:
        if _a <= _d <= _b and _c in _caps:
            _acc[_sec] = _acc.get(_sec, 0) + _caps[_c]
    for _sec, _v in _acc.items():
        _sec_mcap.setdefault(_sec, []).append([_d, _v, round(_v / _tot * 100, 2) if _tot else None])
for _e in sector_cycles:
    _e["mcap"] = _sec_mcap.get(_e["sector"], [])
    _e["members"] = sorted({_mnames.get(_c, _c) for _c, _sec, _a, _b in SECTOR_MEMBERS if _sec == _e["sector"]})
print(f"[*] 섹터 시총: {len(_wdays)}주, 섹터 {len(_sec_mcap)}개")

# ===== 매매 구간 (BT 직접 정리, 2026-11-04) — 현재 로직으로 매매했을 구간 =====
TRADE_ZONES_SPEC = [
    {"stockId": "hyundai_const", "cycleId": "kr_troika_1986", "start": "1987-07-06", "end": "1987-08-24"},
    {"stockId": "hyundai_const", "cycleId": "kr_troika_1986", "start": "1988-07-21", "end": "1988-08-29"},
    {"stockId": "hyundai_const", "cycleId": "kr_troika_1986", "start": "1988-12-01", "end": "1989-01-16"},
    {"stockId": "kepco", "cycleId": "kr_bluechip_1990", "start": "1992-10-21", "end": "1992-12-01"},
    {"stockId": "posco", "cycleId": "kr_bluechip_1990", "start": "1993-11-03", "end": "1993-11-20"},
    {"stockId": "posco", "cycleId": "kr_bluechip_1990", "start": "1993-11-30", "end": "1994-02-05"},
    {"stockId": "samsung_elec", "cycleId": "kr_bluechip_1990", "start": "1994-04-28", "end": "1994-05-31"},
    {"stockId": "samsung_elec", "cycleId": "kr_bluechip_1990", "start": "1994-08-11", "end": "1994-09-28"},
    {"stockId": "daishin_sec", "cycleId": "kr_it_1998", "start": "1998-10-29", "end": "1998-12-22"},
    {"stockId": "hyundai_sec", "cycleId": "kr_it_1998", "start": "1999-03-25", "end": "1999-05-12"},
    {"stockId": "samsung_elec", "cycleId": "kr_it_1998", "start": "1999-06-10", "end": "1999-09-27"},
    {"stockId": "sk_telecom", "cycleId": "kr_it_1998", "start": "1999-11-09", "end": "2000-01-11"},
    {"stockId": "coway", "cycleId": "kr_card_2002", "start": "2002-01-25", "end": "2002-04-15"},
    {"stockId": "hyundai_elev", "cycleId": "kr_china_2003", "start": "2003-10-22", "end": "2003-11-14"},
    {"stockId": "posco", "cycleId": "kr_china_2003", "start": "2006-11-21", "end": "2007-07-26"},
    {"stockId": "posco", "cycleId": "kr_china_2003", "start": "2007-09-14", "end": "2007-10-12"},
    {"stockId": "lg_chem", "cycleId": "kr_chahwajeong_2009", "start": "2009-07-30", "end": "2009-10-12"},
    {"stockId": "kia", "cycleId": "kr_chahwajeong_2009", "start": "2010-03-17", "end": "2010-05-24"},
    {"stockId": "kia", "cycleId": "kr_chahwajeong_2009", "start": "2010-09-06", "end": "2010-11-25"},
    {"stockId": "kia", "cycleId": "kr_chahwajeong_2009", "start": "2011-03-29", "end": "2011-05-02"},
    {"stockId": "samsung_elec", "cycleId": "kr_smartphone_2012", "start": "2012-01-19", "end": "2012-04-12"},
    {"stockId": "amorepacific", "cycleId": "kr_kbeauty_2015", "start": "2015-03-11", "end": "2015-06-01"},
    {"stockId": "hanmi_pharm", "cycleId": "kr_kbeauty_2015", "start": "2015-11-03", "end": "2015-11-27"},
    {"stockId": "sk_hynix", "cycleId": "kr_semi_2016", "start": "2017-04-20", "end": "2017-07-27"},
    {"stockId": "sk_hynix", "cycleId": "kr_semi_2016", "start": "2017-09-06", "end": "2017-10-17"},
    {"stockId": "celltrion", "cycleId": "kr_semi_2016", "start": "2017-12-27", "end": "2018-02-01"},
    {"stockId": "seegene", "cycleId": "kr_covid_bull", "start": "2020-07-03", "end": "2020-08-19"},
    {"stockId": "sk_hynix", "cycleId": "kr_covid_bull", "start": "2020-12-01", "end": "2021-01-14"},
    {"stockId": "kakao", "cycleId": "kr_covid_bull", "start": "2021-04-06", "end": "2021-07-04"},
    {"stockId": "hmm", "cycleId": "kr_covid_bull", "start": "2021-04-26", "end": "2021-06-02"},
    {"stockId": "ecopro", "cycleId": "kr_battery_2023", "start": "2023-02-23", "end": "2023-05-03"},
    {"stockId": "ecopro", "cycleId": "kr_battery_2023", "start": "2023-06-30", "end": "2023-08-04"},
    {"stockId": "alteogen", "cycleId": "kr_battery_2023", "start": "2024-02-22", "end": "2024-03-29"},
    {"stockId": "alteogen", "cycleId": "kr_battery_2023", "start": "2024-06-03", "end": "2024-06-17"},
    {"stockId": "hanwha_ocean", "cycleId": "kr_ai_2025", "start": "2025-01-07", "end": "2025-03-10"},
    {"stockId": "doosan_enerbil", "cycleId": "kr_ai_2025", "start": "2025-05-14", "end": "2025-07-01"},
    {"stockId": "sk_hynix", "cycleId": "kr_ai_2025", "start": "2025-09-09", "end": "2025-11-18"},
    {"stockId": "samsung_elec", "cycleId": "kr_ai_2025", "start": "2025-12-17", "end": "2026-03-20"},
    {"stockId": "sk_hynix", "cycleId": "kr_ai_2025", "start": "2026-04-10", "end": "2026-07-01"},
]

html = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>주도주 사이클</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns@3.0.0/dist/chartjs-adapter-date-fns.bundle.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-annotation@3.0.1/dist/chartjs-plugin-annotation.min.js"></script>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; background: #0d1117; color: #e6edf3; }
.header { padding: 16px 28px; background: #161b22; border-bottom: 2px solid #F39C12; }
.header h1 { font-size: 20px; color: #fff; margin-bottom: 2px; }
.header p { font-size: 11px; color: #484f58; }

/* 페이지 간 네비게이션 (마켓 대시보드 ↔ 시장 사이클 ↔ 주도주 사이클) */
.global-nav { display: flex; gap: 0; background: #010409; border-bottom: 1px solid #21262d; padding: 0 24px; }
.global-nav a { display: inline-block; padding: 8px 18px; font-size: 13px; font-weight: 600; color: #8b949e; text-decoration: none; border-bottom: 2px solid transparent; transition: all 0.15s; }
.global-nav a:hover { color: #f0f6fc; }
.global-nav a.active { color: #f0f6fc; border-bottom-color: #1f6feb; }

.tab-bar { display: flex; gap: 0; background: #161b22; border-bottom: 1px solid #30363d; padding: 0 28px; }
.tab-btn { padding: 10px 20px; font-size: 13px; font-weight: 600; color: #8b949e; cursor: pointer; border: none; background: none; border-bottom: 2px solid transparent; transition: all 0.15s; }
.tab-btn:hover { color: #e6edf3; }
.tab-btn.active { color: #F39C12; border-bottom-color: #F39C12; }

.nav-section { padding: 10px 28px; background: #0d1117; }
.nav-row { display: flex; align-items: center; gap: 6px; padding: 3px 0; flex-wrap: wrap; }
.stock-btn { padding: 4px 11px; border: 1px solid #30363d; border-radius: 14px; background: transparent; color: #8b949e; font-size: 11px; cursor: pointer; transition: all 0.15s; white-space: nowrap; }
.stock-btn:hover { border-color: #F39C12; color: #e6edf3; }
.stock-btn.on { border-color: #FF6B6B; color: #fff; background: #FF6B6B; }
.cycle-btn { padding: 4px 11px; border: 1px solid #30363d; border-radius: 14px; background: transparent; color: #8b949e; font-size: 11px; cursor: pointer; transition: all 0.15s; white-space: nowrap; }
.cycle-btn:hover { border-color: #58a6ff; color: #e6edf3; }
.cycle-btn.active { background: #1f6feb; border-color: #1f6feb; color: #fff; }
.v2all-panel { margin-top: 8px; border: 1px solid #30363d; border-radius: 6px; background: #0d1117; overflow: hidden; }
.v2all-label { display: inline-block; padding: 4px 12px; font-size: 13px; font-weight: 700; color: #0d1117; background: var(--lc); border-bottom-right-radius: 6px; letter-spacing: 0.2px; }
.v2all-cv { position: relative; padding: 2px 6px 4px; }
.v2all-sel { position: absolute; top: 0; bottom: 0; background: rgba(88,166,255,0.18); border: 1px solid #58a6ff; pointer-events: none; display: none; }
.v2all-stats { margin: 6px 0 2px; font-size: 12px; color: #e6edf3; background: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 6px 10px; line-height: 1.6; }
.v2all-stats b { color: #e3b341; }

.ctrl-row { display: flex; gap: 6px; align-items: center; padding: 6px 28px; flex-wrap: wrap; }
.ctrl-label { font-size: 11px; color: #484f58; margin-right: 2px; }
.ctrl-btn { padding: 3px 10px; border-radius: 4px; font-size: 11px; cursor: pointer; border: 1px solid #30363d; background: transparent; color: #8b949e; transition: all 0.15s; }
.ctrl-btn.active { background: #1f6feb; border-color: #1f6feb; color: #fff; }
.expand-btn { padding: 3px 10px; border-radius: 4px; font-size: 11px; cursor: pointer; border: 1px solid #F39C12; background: transparent; color: #F39C12; transition: all 0.15s; margin-left: 12px; }
.expand-btn.active { background: #F39C12; color: #000; }

.main { padding: 10px 28px 24px; position: relative; }
.chart-info { display: flex; align-items: center; gap: 10px; margin-bottom: 4px; }
.chart-title { font-size: 16px; font-weight: 700; color: #e6edf3; }
.chart-badge { padding: 3px 10px; border-radius: 10px; font-size: 11px; font-weight: 600; }
.chart-meta { font-size: 11px; color: #484f58; margin-bottom: 8px; }

/* 4단 스택 차트 박스 — 키움 HTS 회색 테마 */
.stack-wrap { background: #C0C0C0; border-radius: 8px; border: 1px solid #707070; padding: 10px 12px 14px; position: relative; }
.panel { display: flex; flex-direction: column; position: relative; }
.panel-us { height: 220px; }
.panel-price { height: 220px; }
.panel-stock { height: 320px; }
.panel-volume { height: 120px; }
/* 미국 지수 / 한국 지수 / 종목 영역 진입 시 강한 가로 구분선 (거래대금은 제외) */
.panel-price { border-top: 2px solid #707070; padding-top: 4px; margin-top: 4px; }
.panel-stock { border-top: 2px solid #707070; padding-top: 4px; margin-top: 4px; }
/* 패널 헤더: 라벨 + 토글 (캔버스 위 별도 행, absolute 아님) */
.panel-header { display: flex; align-items: center; gap: 10px; height: 22px; flex: 0 0 auto; padding: 0 0 2px 70px; }
.panel-label { font-size: 11px; font-weight: 700; color: #1c2128; }
.panel-canvas-wrap { flex: 1 1 auto; position: relative; min-height: 0; }

/* 토글 버튼 행 (패널 라벨 바로 옆) */
.panel-toggle-row { display: flex; gap: 6px; }
.toggle-btn { padding: 3px 10px; border-radius: 4px; font-size: 10px; cursor: pointer; border: 1px solid #707070; background: #E8E8E8; color: #1c2128; transition: all 0.15s; white-space: nowrap; }
.toggle-btn:hover { border-color: #1f6feb; color: #1f6feb; }
.toggle-btn.active { background: #1f6feb; border-color: #1f6feb; color: #fff; }

/* HTS 스타일 툴팁 (흰 배경 + 키움 톤) */
.hts-tooltip { position: absolute; top: 14px; left: 16px; background: rgba(255, 255, 255, 0.97); border: 1px solid #707070; border-radius: 6px; padding: 9px 13px; font-size: 13px; color: #1c2128; z-index: 20; pointer-events: none; min-width: 240px; line-height: 1.7; box-shadow: 0 2px 8px rgba(0,0,0,0.15); }
.hts-date { font-weight: 700; color: #1c2128; margin-bottom: 5px; font-size: 14px; border-bottom: 1px solid #B0B0B0; padding-bottom: 4px; }
.hts-section { margin-top: 5px; }
.hts-section-title { font-weight: 700; font-size: 13px; margin-bottom: 3px; }
.hts-row { display: flex; justify-content: space-between; gap: 14px; font-family: 'Menlo', monospace; font-size: 12px; }
.hts-row .k { color: #1c2128; }
.hts-row .v { color: #1c2128; }
.hts-up { color: #C9302C; }
.hts-down { color: #1565C0; }

/* 줌/드래그 */
.drag-overlay { position: absolute; top: 0; bottom: 0; background: rgba(31,111,235,0.12); border-left: 1px solid rgba(31,111,235,0.4); border-right: 1px solid rgba(31,111,235,0.4); pointer-events: none; z-index: 10; display: none; }
.zoom-controls { display: flex; align-items: center; justify-content: center; gap: 10px; margin-top: 6px; }
.zoom-reset-btn { padding: 4px 12px; border-radius: 4px; font-size: 11px; cursor: pointer; border: 1px solid #1f6feb; background: #1f6feb22; color: #58a6ff; transition: all 0.15s; }
.zoom-reset-btn:hover { background: #1f6feb44; }
.zoom-hint { font-size: 11px; color: #484f58; }
/* X축 스크롤바 */
.xscroll-wrap { margin: 6px 50px 0 70px; position: relative; height: 18px; display: none; }
.xscroll-wrap.active { display: block; }
.xscroll-track { position: absolute; top: 7px; left: 0; right: 0; height: 4px; background: #21262d; border-radius: 2px; }
.xscroll-thumb { position: absolute; top: 2px; height: 14px; background: #30363d; border: 1px solid #484f58; border-radius: 3px; cursor: grab; transition: background 0.1s; }
.xscroll-thumb:hover { background: #484f58; }
.xscroll-thumb.dragging { cursor: grabbing; background: #58a6ff; border-color: #58a6ff; }

.legend-row { display: flex; gap: 14px; justify-content: center; margin-top: 6px; flex-wrap: wrap; }
.legend-item { display: flex; align-items: center; gap: 5px; font-size: 11px; color: #8b949e; }
.legend-dot { width: 10px; height: 10px; border-radius: 50%; }
.legend-line { width: 14px; height: 2px; border-radius: 1px; }

.view-panel { display: none; }
.view-panel.active { display: block; }

/* ===== 산업 사이클 매트릭스 (SECTOR_VIEW_V1) ===== */
.sec-intro { padding: 12px 28px 0; font-size: 12px; color: #8b949e; line-height: 1.6; }
.sec-matrix { display: grid; gap: 16px; padding: 12px 28px 28px; align-items: start; }
.sec-col h3 { font-size: 14px; margin: 0 0 8px; padding-bottom: 6px; border-bottom: 1px solid #30363d; }
.sec-col h3 .sub { font-size: 11px; color: #8b949e; font-weight: 400; margin-left: 8px; }
.sec-sub2 { display: grid; grid-template-columns: 1fr 1fr; gap: 0 12px; }
.sec-group { grid-column: 1 / -1; font-size: 11.5px; color: #c9d1d9; font-weight: 600; margin: 4px 0 6px; }
.sec-card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 8px 10px 6px; margin-bottom: 10px; }
.sec-head { display: flex; align-items: baseline; gap: 6px; flex-wrap: wrap; }
.sec-name { font-size: 13px; font-weight: 700; color: #e6edf3; }
.sec-stock { font-size: 11px; color: #8b949e; }
.sec-tag { font-size: 10px; padding: 0 6px; border-radius: 8px; border: 1px solid; }
.sec-gap { font-size: 11px; color: #c9d1d9; margin: 3px 0 4px; }
.sec-canvas { position: relative; height: 140px; }
.sec-canvas.big { height: 300px; }
#sec-type .sec-col + .sec-col { margin-top: 10px; }
#sec-type .sec-group { font-size: 13px; margin: 10px 0 8px; }
#sec-term .sec-card, #sec-type .sec-card { cursor: zoom-in; }
#sec-term .sec-card:hover, #sec-type .sec-card:hover { border-color: #58a6ff88; }
#sec-modal { display: none; position: fixed; inset: 0; background: rgba(1,4,9,0.78); z-index: 1000; padding: 3vh 1.5vw; }
#sec-modal.open { display: flex; align-items: center; }
.sec-modal-box { background: #0d1117; border: 1px solid #30363d; border-radius: 10px; width: 100%; height: min(830px, 94vh); padding: 12px 16px; display: flex; flex-direction: column; }
.sec-modal-top { display: flex; justify-content: space-between; align-items: flex-start; gap: 10px; }
.sec-modal-x { background: #21262d; color: #c9d1d9; border: 1px solid #30363d; border-radius: 6px; padding: 4px 12px; cursor: pointer; font-size: 12px; }
.sec-modal-x:hover { color: #fff; border-color: #58a6ff; }
.sec-modal-canvas { position: relative; flex: 1; min-height: 0; margin-top: 6px; }
.sec-note { font-size: 10.5px; color: #6e7681; margin-top: 3px; line-height: 1.45; }
.sec-empty { font-size: 11px; color: #6e7681; padding: 50px 0; text-align: center; }
@media (max-width: 1100px) { .sec-sub2 { grid-template-columns: 1fr; } }
</style>
</head>
<body>

<div class="global-nav">
  <a href="dashboard.html">마켓 대시보드</a>
  <a href="Market_cycle.html">시장 사이클</a>
  <a href="Leading_stocks.html" class="active">주도주 사이클</a>
  <a href="Industry_semiconductor.html">반도체</a>
</div>

<div class="header">
  <h1>주도주 사이클</h1>
  <p>KOSPI + 시대별 주도주 | 3단 스택 (지수/종목/거래대금) | 한국식 캔들 | MA 5·10·20·60·120 | HTS 툴팁 | 드래그 줌 · 휠 1캔들 팬 · X축 스크롤바</p>
</div>

<div class="tab-bar">
  <button class="tab-btn active" onclick="switchView(event,'v2')">주도주</button>
  <button class="tab-btn" onclick="switchView(event,'vtype')">유형별</button>
  <button class="tab-btn" onclick="switchView(event,'vterm')">시계열별</button>
</div>

<!-- SECTOR_VIEW_V1: 산업 사이클 매트릭스 (2026-11-03) -->
<div class="view-panel" id="view-vtype">
  <div class="sec-intro">산업 사이클이 어느 정도 주기로 도는지 가늠하기 위한 화면. 대표종목 주봉(로그) 위에 업사이클 구간을 음영으로 표시. 업사이클 시작 = 60·120일선 정배열 진입, 산업 가격지표 우선(없으면 영업이익, 바이오만 주가). 점선 = 진행 중. 카드를 누르면 크게 열려.</div>
  <div class="sec-matrix" id="sec-type"></div>
</div>
<div class="view-panel" id="view-vterm">
  <div class="sec-intro">같은 산업 사이클을 주기 길이별로 배치. 장기 14~30년 · 중기 4~8년 · 단기 2~5년 · 1회. 카드 색 태그 = 재가동형(파랑) / 개척형(초록). 카드를 누르면 화면 폭 전체로 크게 열리고, 닫기·바깥 클릭·Esc로 닫혀.</div>
  <div class="sec-matrix" id="sec-term"></div>
</div>

<!-- VIEW 1 -->
<div class="view-panel" id="view-v1">
  <div class="nav-section"><div class="nav-row" id="v1-stock-btns"></div></div>
  <div class="ctrl-row">
    <span class="ctrl-label">스케일:</span>
    <button class="ctrl-btn active" id="v1-linear" onclick="setV1Scale('linear')">Linear</button>
    <button class="ctrl-btn" id="v1-log" onclick="setV1Scale('log')">Log</button>
  </div>
  <div class="main">
    <div class="chart-info">
      <span class="chart-title" id="v1-title">KOSPI 전체 + 주도주를 선택하세요</span>
      <span class="chart-badge" style="background:#27AE6022;color:#27AE60;border:1px solid #27AE6044;">주봉</span>
    </div>
    <div class="chart-meta" id="v1-meta"></div>
    <div class="stack-wrap">
      <div class="hts-tooltip" id="v1-tooltip" style="display:none;"></div>
      <div class="panel panel-us">
        <div class="panel-header">
          <span class="panel-label">미국 지수</span>
          <div class="panel-toggle-row">
            <button class="toggle-btn active" id="v1-us-nasdaq" onclick="toggleUSIndex('v1','nasdaq')">NASDAQ</button>
            <button class="toggle-btn" id="v1-us-sp500" onclick="toggleUSIndex('v1','sp500')">S&P500</button>
          </div>
        </div>
        <div class="panel-canvas-wrap">
          <canvas id="v1-us-price"></canvas>
          <div class="drag-overlay" id="drag-overlay-v1-us-price"></div>
        </div>
      </div>
      <div class="panel panel-price">
        <div class="panel-header">
          <span class="panel-label">한국 지수</span>
          <div class="panel-toggle-row">
            <button class="toggle-btn active" id="v1-kr-kospi" onclick="toggleKRIndex('v1','kospi')">KOSPI</button>
            <button class="toggle-btn" id="v1-kr-kosdaq" onclick="toggleKRIndex('v1','kosdaq')">KOSDAQ</button>
          </div>
        </div>
        <div class="panel-canvas-wrap">
          <canvas id="v1-price"></canvas>
          <div class="drag-overlay" id="drag-overlay-v1-price"></div>
        </div>
      </div>
      <div class="panel panel-stock">
        <div class="panel-header">
          <span class="panel-label" id="v1-stock-label">주도주</span>
        </div>
        <div class="panel-canvas-wrap">
          <canvas id="v1-stock"></canvas>
          <div class="drag-overlay" id="drag-overlay-v1-stock"></div>
        </div>
      </div>
      <div class="panel panel-volume">
        <div class="panel-header">
          <span class="panel-label">거래대금 (억원)</span>
        </div>
        <div class="panel-canvas-wrap">
          <canvas id="v1-volume"></canvas>
          <div class="drag-overlay" id="drag-overlay-v1-volume"></div>
        </div>
      </div>
    </div>
    <div class="legend-row" id="v1-legend"></div>
    <div class="xscroll-wrap" id="v1-xscroll">
      <div class="xscroll-track"></div>
      <div class="xscroll-thumb" id="v1-xscroll-thumb"></div>
    </div>
    <div class="zoom-controls" id="v1-zoom" style="display:none;">
      <button class="zoom-reset-btn" onclick="resetZoom('v1')">줌 리셋</button>
      <span class="zoom-hint" id="v1-zoom-hint"></span>
    </div>
  </div>
</div>

<!-- VIEW 2 -->
<div class="view-panel active" id="view-v2">
  <div class="nav-section"><div class="nav-row" id="v2-cycle-btns"></div></div>
  <div class="nav-section" style="padding-top:0;"><div class="nav-row" id="v2-stock-btns"></div></div>
  <div class="ctrl-row">
    <span class="ctrl-label">스케일:</span>
    <button class="ctrl-btn active" id="v2-linear" onclick="setV2Scale('linear')">Linear</button>
    <button class="ctrl-btn" id="v2-log" onclick="setV2Scale('log')">Log</button>
    <span class="ctrl-label" style="margin-left:12px;">주기:</span>
    <button class="ctrl-btn active" id="v2-daily" onclick="setV2Interval('daily')">일봉</button>
    <button class="ctrl-btn" id="v2-weekly" onclick="setV2Interval('weekly')">주봉</button>
    <button class="expand-btn" id="v2-expand" onclick="toggleExpand()">전체차트 보기</button>
  </div>
  <div class="main" id="v2-all" style="display:none;">
    <div class="chart-info"><span class="chart-title">전체 사이클 — 주도주 모멘텀 구간 연결</span>
      <button class="ctrl-btn active" id="v2all-t-up" onclick="_allToggle('up')" style="margin-left:14px;">상승 구간</button><button class="ctrl-btn active" id="v2all-t-tr" onclick="_allToggle('tr')" style="margin-left:4px;">매매 구간</button><button class="zoom-reset-btn" onclick="_allResetZoom()" style="margin-left:12px;">줌 리셋</button></div>
    <div class="chart-meta">지수는 전체 기간, 주도주는 박스(모멘텀) 구간만 표시 · 각 구간 시작 = 100 (로그) · 드래그 = 확대, 휠 = 확대/축소, 더블클릭 = 리셋</div>
    <div class="v2all-stats" id="v2all-stats"></div>
    <div class="v2all-panel"><div class="v2all-label" style="--lc:#58a6ff">NASDAQ</div><div class="v2all-cv" style="height:160px;"><canvas id="v2all-nasdaq"></canvas></div></div>
    <div class="v2all-panel"><div class="v2all-label" style="--lc:#f0883e">KOSPI</div><div class="v2all-cv" style="height:160px;"><canvas id="v2all-kospi"></canvas></div></div>
    <div class="v2all-panel"><div class="v2all-label" style="--lc:#a371f7">KOSDAQ</div><div class="v2all-cv" style="height:160px;"><canvas id="v2all-kosdaq"></canvas></div></div>
    <div class="v2all-panel"><div class="v2all-label" style="--lc:#3fb950">주도주 · 모멘텀 구간 (시작=100)</div><div class="v2all-cv" style="height:340px;"><canvas id="v2all-stock"></canvas></div></div>
    <div class="v2all-panel"><div class="v2all-label" style="--lc:#e3b341">매매 가능 구간 · 대기 기간</div><span style="margin-left:10px;font-size:11px;color:#8b949e;">위: 상승 구간(파랑) · 아래: 매매 구간(초록) · 사이 = 대기 기간</span><div class="v2all-cv" style="height:96px;"><canvas id="v2all-win"></canvas></div></div>
  </div>
  <div class="main" id="v2-main">
    <div class="chart-info">
      <span class="chart-title" id="v2-title">사이클을 선택하세요</span>
    </div>
    <div class="chart-meta" id="v2-meta"></div>
    <div class="stack-wrap">
      <div class="hts-tooltip" id="v2-tooltip" style="display:none;"></div>
      <div class="panel panel-us">
        <div class="panel-header">
          <span class="panel-label">미국 지수</span>
          <div class="panel-toggle-row">
            <button class="toggle-btn active" id="v2-us-nasdaq" onclick="toggleUSIndex('v2','nasdaq')">NASDAQ</button>
            <button class="toggle-btn" id="v2-us-sp500" onclick="toggleUSIndex('v2','sp500')">S&P500</button>
          </div>
        </div>
        <div class="panel-canvas-wrap">
          <canvas id="v2-us-price"></canvas>
          <div class="drag-overlay" id="drag-overlay-v2-us-price"></div>
        </div>
      </div>
      <div class="panel panel-price">
        <div class="panel-header">
          <span class="panel-label">한국 지수</span>
          <div class="panel-toggle-row">
            <button class="toggle-btn active" id="v2-kr-kospi" onclick="toggleKRIndex('v2','kospi')">KOSPI</button>
            <button class="toggle-btn" id="v2-kr-kosdaq" onclick="toggleKRIndex('v2','kosdaq')">KOSDAQ</button>
          </div>
        </div>
        <div class="panel-canvas-wrap">
          <canvas id="v2-price"></canvas>
          <div class="drag-overlay" id="drag-overlay-v2-price"></div>
        </div>
      </div>
      <div class="panel panel-stock">
        <div class="panel-header">
          <span class="panel-label" id="v2-stock-label">주도주</span>
        </div>
        <div class="panel-canvas-wrap">
          <canvas id="v2-stock"></canvas>
          <div class="drag-overlay" id="drag-overlay-v2-stock"></div>
        </div>
      </div>
      <div class="panel panel-volume">
        <div class="panel-header">
          <span class="panel-label">거래대금 (억원)</span>
        </div>
        <div class="panel-canvas-wrap">
          <canvas id="v2-volume"></canvas>
          <div class="drag-overlay" id="drag-overlay-v2-volume"></div>
        </div>
      </div>
    </div>
    <div class="legend-row" id="v2-legend"></div>
    <div class="xscroll-wrap" id="v2-xscroll">
      <div class="xscroll-track"></div>
      <div class="xscroll-thumb" id="v2-xscroll-thumb"></div>
    </div>
    <div class="zoom-controls" id="v2-zoom" style="display:none;">
      <button class="zoom-reset-btn" onclick="resetZoom('v2')">줌 리셋</button>
      <span class="zoom-hint" id="v2-zoom-hint"></span>
    </div>
  </div>
</div>

<script>
// ===== DATA =====
const KOSPI_RAW = """ + json.dumps(kospi_data) + """;
const KOSDAQ_RAW = """ + json.dumps(kosdaq_data) + """;
const SP500_RAW = """ + json.dumps(sp500_data) + """;
const NASDAQ_RAW = """ + json.dumps(nasdaq_data) + """;
const STOCKS_RAW = """ + json.dumps(stocks_data) + """;
const META = """ + json.dumps(meta) + """;
const UNIQUE_STOCKS = """ + json.dumps(unique_stocks) + """;
const ALL_STOCK_ENTRIES = """ + json.dumps(all_stock_entries) + """;
const CYCLES = """ + json.dumps(cycle_order) + """;
const STOCK_COLORS = """ + json.dumps(STOCK_COLORS) + """;
const STOCK_ZONES = """ + json.dumps(stock_zones) + """;
const US_MARKET_CYCLES = """ + json.dumps(us_market_cycles) + """;
const SECTOR_CYCLES = """ + json.dumps(sector_cycles, ensure_ascii=False, separators=(",", ":")) + """;
const TRADE_ZONES = """ + json.dumps(TRADE_ZONES_SPEC, ensure_ascii=False, separators=(",", ":")) + """;

const stockColorMap = {};
UNIQUE_STOCKS.forEach((s, i) => { stockColorMap[s.id] = STOCK_COLORS[i % STOCK_COLORS.length]; });

// ===== 토글 상태 =====
const toggleStates = {
  v1: { us_nasdaq: true, us_sp500: false, kr_kospi: true, kr_kosdaq: false },
  v2: { us_nasdaq: true, us_sp500: false, kr_kospi: true, kr_kosdaq: false },
};

// 라벨 포맷: "연도 종목명(키워드)" — 차트 타이틀과 동일
function formatStockLabel(s) {
  const era = s.era || '';
  const name = s.name || '';
  const sp = era.indexOf(' ');
  if (sp < 0) return era + ' ' + name;
  return era.substring(0, sp) + ' ' + name + '(' + era.substring(sp + 1) + ')';
}

// 한국식 캔들 컬러
const CANDLE_UP = '#DC0000';   // 양봉 = 진한 빨강 (회색 배경 대비 강화)
const CANDLE_DN = '#003CC8';   // 음봉 = 진한 파랑
const VOL_UP = 'rgba(220, 0, 0, 0.7)';
const VOL_DN = 'rgba(0, 60, 200, 0.7)';

// MA 컬러
// 이평선 색상 (2026-05-15 swap — BT 선호: MA60 보라 / MA120 초록)
//   MA5  검정 (0,0,0) / MA10 파랑 (0,0,255) / MA20 노랑 (255,255,0)
//   MA60 보라 (153,0,204) / MA120 초록 (0,128,0)
const MA_COLORS = { ma5: '#000000', ma10: '#0000FF', ma20: '#FFFF00', ma60: '#9900CC', ma120: '#008000' };

// ===== HELPERS =====
function parseDate(d) {
  return new Date(+d.slice(0,4), +d.slice(4,6)-1, +d.slice(6,8));
}
// 라벨 포맷: "연도 종목명(키워드)"
function fmtStockLabel(era, name) {
  if (!era) return name || '';
  const i = era.indexOf(' ');
  if (i < 0) return era + ' ' + name;
  return era.substring(0, i) + ' ' + name + '(' + era.substring(i + 1) + ')';
}
function toDaily(raw) {
  return raw.map(r => ({ x: parseDate(r[0]).getTime(), y: r[4], o: r[1], h: r[2], l: r[3], c: r[4], v: r[5] || 0 }));
}
function toWeekly(raw) {
  if (!raw || !raw.length) return [];
  const weeks = [];
  let week = null;
  for (const r of raw) {
    const d = parseDate(r[0]);
    const mon = new Date(d);
    mon.setDate(mon.getDate() - ((mon.getDay() + 6) % 7));
    const monKey = mon.toISOString().slice(0,10);
    if (!week || week.key !== monKey) {
      if (week) weeks.push(week);
      week = { key: monKey, x: mon.getTime(), y: r[4], o: r[1], h: r[2], l: r[3], c: r[4], v: r[5] || 0 };
    } else {
      week.h = Math.max(week.h, r[2]);
      week.l = Math.min(week.l, r[3]);
      week.c = r[4];
      week.y = r[4];
      week.v += (r[5] || 0);
    }
  }
  if (week) weeks.push(week);
  return weeks;
}
function computeMA(data, period) {
  const out = [];
  let sum = 0;
  for (let i = 0; i < data.length; i++) {
    sum += data[i].c;
    if (i >= period) sum -= data[i - period].c;
    if (i >= period - 1) out.push({ x: data[i].x, y: sum / period });
    else out.push({ x: data[i].x, y: null });
  }
  return out;
}
function filterByDate(data, start, end) {
  const s = start ? new Date(start).getTime() : 0;
  const e = end ? new Date(end).getTime() : Infinity;
  return data.filter(r => { const t = parseDate(r[0]).getTime(); return t >= s && t <= e; });
}
function fmt(n, dec) {
  if (n == null || isNaN(n)) return '-';
  if (dec === 0) return Math.round(n).toLocaleString();
  return n.toLocaleString(undefined, { maximumFractionDigits: dec || 0 });
}
function findRowAtTime(arr, t) {
  // Binary search for closest row at time t (on/before)
  if (!arr.length) return null;
  let lo = 0, hi = arr.length - 1;
  while (lo < hi) {
    const mid = (lo + hi + 1) >> 1;
    if (arr[mid].x <= t) lo = mid;
    else hi = mid - 1;
  }
  return arr[lo];
}
function _dayKey(t) {
  const d = new Date(t);
  return d.getFullYear() * 10000 + (d.getMonth()+1) * 100 + d.getDate();
}
function findRowAtTimeExact(arr, t) {
  // 정확한 같은 날짜의 row 만 반환. 없으면 null. (휴장일/공휴일 처리용)
  if (!arr || !arr.length) return null;
  const tKey = _dayKey(t);
  let lo = 0, hi = arr.length - 1;
  while (lo <= hi) {
    const mid = (lo + hi) >> 1;
    const mKey = _dayKey(arr[mid].x);
    if (mKey === tKey) return arr[mid];
    if (mKey < tKey) lo = mid + 1;
    else hi = mid - 1;
  }
  return null;
}
function _fmtDateDow(t) {
  // 외부 괄호 포함 — top label 용 ("2026-04-30 (목)")
  const d = new Date(t);
  const dow = ['일','월','화','수','목','금','토'][d.getDay()];
  return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0')+' ('+dow+')';
}
function _fmtDateDowPlain(t) {
  // 외부 괄호 없이 — 섹션 제목의 (날짜 요일) 안쪽에 들어갈 때 중복 괄호 방지
  const d = new Date(t);
  const dow = ['일','월','화','수','목','금','토'][d.getDay()];
  return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0')+' '+dow;
}
// 토글된(visible) 캔들 dataset 정보 추출 — 휴장 섹션 렌더링용
function _visibleCandleInfo(chart) {
  const out = [];
  if (!chart) return out;
  for (let i = 0; i < chart.data.datasets.length; i++) {
    const ds = chart.data.datasets[i];
    if (!ds._candle) continue;
    if (!chart.isDatasetVisible(i)) continue;
    out.push({ ds, label: ds.label, indexId: ds._indexId });
  }
  return out;
}

// ===== Y-AXIS WIDTH FIX (크로스헤어 Y축폭 일치용) =====
// 고정 너비로 강제 → 차트마다 y-axis 라벨 폭이 달라도 chartArea.left 가 동일해져
// 같은 시점(time) 이 같은 캔버스 픽셀 위치에 그려짐 (크로스헤어 정렬 보장)
const _FIXED_Y_AXIS_W = 82;
const scaleFixPlugin = {
  id: 'scaleFix',
  beforeLayout(chart) {
    for (const key of Object.keys(chart.options.scales)) {
      if (key.startsWith('y')) {
        const ax = chart.options.scales[key];
        ax.afterFit = function(axis) {
          axis.width = _FIXED_Y_AXIS_W;
        };
      }
    }
  }
};
Chart.register(scaleFixPlugin);

// ===== CROSSHAIR PLUGIN (dateValue 기반 교차 동기화) =====
const crosshairState = { x: null, y: null, sourceChart: null, activeView: null };
const crosshairPlugin = {
  id: 'crosshair',
  afterEvent(chart, args) {
    if (!chart.$view) return;
    const evt = args.event;
    if (evt.type === 'mousemove') {
      const area = chart.chartArea;
      if (evt.x >= area.left && evt.x <= area.right && evt.y >= area.top && evt.y <= area.bottom) {
        crosshairState.x = evt.x;
        crosshairState.y = evt.y;
        crosshairState.sourceChart = chart;
        crosshairState.activeView = chart.$view;
        updateHTSTooltip(chart.$view, evt.x, evt, chart);
        getChartsForView(chart.$view).forEach(ch => { if (ch && ch !== chart) ch.draw(); });
      }
    } else if (evt.type === 'mouseout') {
      crosshairState.x = null; crosshairState.y = null; crosshairState.sourceChart = null;
      const view = chart.$view;
      hideHTSTooltip(view);
      getChartsForView(view).forEach(ch => { if (ch) ch.draw(); });
    }
  },
  afterDraw(chart) {
    if (crosshairState.x == null || !chart.$view) return;
    if (crosshairState.activeView !== chart.$view) return;
    const ctx = chart.ctx;
    const area = chart.chartArea;
    let xPx = crosshairState.x;
    const _srcChart = crosshairState.sourceChart;
    if (_srcChart && _srcChart !== chart) {
      const xScale = _srcChart.scales.x;
      const val = xScale.getValueForPixel(crosshairState.x);
      xPx = chart.scales.x.getPixelForValue(val);
    }
    if (xPx < area.left || xPx > area.right) return;

    // 호버 시점의 timestamp (모든 패널 공유 — 황금점 exact-match 용)
    let xValMark = null;
    if (_srcChart) {
      xValMark = _srcChart.scales.x.getValueForPixel(crosshairState.x);
    }

    ctx.save();
    // 실선 + 다크 마젠타 (회색 배경 + 캔들 빨/파와 충돌 X)
    ctx.beginPath();
    ctx.setLineDash([]);
    ctx.lineWidth = 1;
    ctx.strokeStyle = 'rgba(194, 24, 91, 0.9)';
    ctx.moveTo(xPx, area.top);
    ctx.lineTo(xPx, area.bottom);
    ctx.stroke();
    // === 같은 날짜 캔들 위에 굵은 점 (시계열 정렬 확인용) — exact match 만 ===
    if (xValMark != null) {
      ctx.setLineDash([]);
      // candle datasets — close 위에 마커
      chart.data.datasets.forEach((ds, i) => {
        if (!ds._candle) return;
        if (!chart.isDatasetVisible(i)) return;
        const row = findRowAtTimeExact(ds.data, xValMark);
        if (!row || row.c == null) return;
        const xS = chart.scales.x; const yS = chart.scales[ds.yAxisID || 'y'];
        const rxPx = xS.getPixelForValue(row.x);
        const ryPx = yS.getPixelForValue(row.c);
        if (rxPx < area.left || rxPx > area.right) return;
        if (ryPx < area.top || ryPx > area.bottom) return;
        ctx.beginPath();
        ctx.fillStyle = '#FFD700';
        ctx.strokeStyle = '#0d1117';
        ctx.lineWidth = 1.5;
        ctx.arc(rxPx, ryPx, 4, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();
      });
      // volume dataset — 막대 끝에 마커
      chart.data.datasets.forEach((ds, i) => {
        if (!ds._volume) return;
        if (!chart.isDatasetVisible(i)) return;
        const row = findRowAtTimeExact(ds.data, xValMark);
        if (!row || row.v == null) return;
        const xS = chart.scales.x; const yS = chart.scales[ds.yAxisID || 'y'];
        const rxPx = xS.getPixelForValue(row.x);
        const ryPx = yS.getPixelForValue(row.v);
        if (rxPx < area.left || rxPx > area.right) return;
        if (ryPx < area.top || ryPx > area.bottom) return;
        ctx.beginPath();
        ctx.fillStyle = '#FFD700';
        ctx.strokeStyle = '#0d1117';
        ctx.lineWidth = 1.5;
        ctx.arc(rxPx, ryPx, 4, 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();
      });
    }
    // horizontal solid only on hovered chart
    if (_srcChart === chart && crosshairState.y >= area.top && crosshairState.y <= area.bottom) {
      ctx.beginPath();
      ctx.setLineDash([]);
      ctx.lineWidth = 1;
      ctx.strokeStyle = 'rgba(194, 24, 91, 0.7)';
      ctx.moveTo(area.left, crosshairState.y);
      ctx.lineTo(area.right, crosshairState.y);
      ctx.stroke();
    }
    // date label at bottom of volume chart only (since volume is last)
    // 차트 area 안쪽 하단에 그려서 캔버스/패널 경계로 잘리지 않도록
    if (chart.$role === 'volume') {
      const xScale = chart.scales.x;
      const dateVal = xScale.getValueForPixel(xPx);
      if (dateVal) {
        const dt = new Date(dateVal);
        const label = dt.getFullYear()+'-'+String(dt.getMonth()+1).padStart(2,'0')+'-'+String(dt.getDate()).padStart(2,'0');
        ctx.setLineDash([]);
        ctx.font = '10px -apple-system, sans-serif';
        const tw = ctx.measureText(label).width;
        const lx = Math.max(area.left, Math.min(xPx - tw/2 - 4, area.right - tw - 8));
        const lblH = 16;
        const lblY = area.bottom - lblH - 1;  // chart area 안쪽 하단
        ctx.fillStyle = 'rgba(48, 54, 61, 0.95)';
        ctx.fillRect(lx, lblY, tw + 8, lblH);
        ctx.fillStyle = '#e6edf3';
        ctx.fillText(label, lx + 4, lblY + 11);
      }
    }
    ctx.restore();
  }
};
Chart.register(crosshairPlugin);

// ===== CANDLESTICK PLUGIN =====
const candlestickPlugin = {
  id: 'candlestick',
  afterDatasetDraw(chart, args) {
    const ds = chart.data.datasets[args.index];
    if (!ds._candle) return;
    if (!chart.isDatasetVisible(args.index)) return;
    const ctx = chart.ctx;
    const xScale = chart.scales.x;
    const yScale = chart.scales[ds.yAxisID || 'y'];
    const data = ds.data;
    if (!data || !data.length) return;

    const area = chart.chartArea;
    let visCount = 0;
    for (const d of data) {
      const px = xScale.getPixelForValue(d.x);
      if (px >= area.left && px <= area.right) visCount++;
    }
    const barWidth = Math.max(1.2, Math.min(10, (area.right - area.left) / Math.max(visCount, 1) * 0.62));
    ctx.save();
    for (const d of data) {
      if (d.o == null || d.c == null) continue;
      const xPx = xScale.getPixelForValue(d.x);
      if (xPx < area.left - barWidth || xPx > area.right + barWidth) continue;
      const oY = yScale.getPixelForValue(d.o);
      const cY = yScale.getPixelForValue(d.c);
      const hY = yScale.getPixelForValue(d.h);
      const lY = yScale.getPixelForValue(d.l);
      const isUp = d.c >= d.o;
      const color = isUp ? (ds._candleUp || CANDLE_UP) : (ds._candleDown || CANDLE_DN);
      ctx.beginPath();
      ctx.strokeStyle = color;
      ctx.lineWidth = 1;
      ctx.moveTo(xPx, hY);
      ctx.lineTo(xPx, lY);
      ctx.stroke();
      const top = Math.min(oY, cY);
      const bodyH = Math.max(1, Math.abs(oY - cY));
      ctx.fillStyle = color;
      ctx.fillRect(xPx - barWidth/2, top, barWidth, bodyH);
    }
    ctx.restore();
  }
};
Chart.register(candlestickPlugin);

// ===== VOLUME BAR PLUGIN =====
const volumeBarPlugin = {
  id: 'volumeBar',
  afterDatasetDraw(chart, args) {
    const ds = chart.data.datasets[args.index];
    if (!ds._volume) return;
    const ctx = chart.ctx;
    const xScale = chart.scales.x;
    const yScale = chart.scales[ds.yAxisID || 'y'];
    const data = ds.data;
    if (!data || !data.length) return;
    const area = chart.chartArea;
    let visCount = 0;
    for (const d of data) {
      const px = xScale.getPixelForValue(d.x);
      if (px >= area.left && px <= area.right) visCount++;
    }
    const barWidth = Math.max(1.2, Math.min(10, (area.right - area.left) / Math.max(visCount, 1) * 0.62));
    const zeroY = yScale.getPixelForValue(0);
    ctx.save();
    for (const d of data) {
      if (d.y == null || d.v == null) continue;
      const xPx = xScale.getPixelForValue(d.x);
      if (xPx < area.left - barWidth || xPx > area.right + barWidth) continue;
      const yPx = yScale.getPixelForValue(d.v);
      const h = Math.max(1, Math.abs(zeroY - yPx));
      ctx.fillStyle = d.up ? VOL_UP : VOL_DN;
      ctx.fillRect(xPx - barWidth/2, Math.min(zeroY, yPx), barWidth, h);
    }
    ctx.restore();
  }
};
Chart.register(volumeBarPlugin);

// ===== HTS TOOLTIP =====
// 헬퍼: 호버 위치가 실제 캔들 "위"인지 판정 (빈 공간이면 false)
// row.x 와 xVal 을 source chart 의 x-scale 에서 픽셀로 환산한 뒤,
// 두 픽셀 간 거리가 반 bar 이내인 경우에만 "캔들 위" 로 판정
// hoverY 가 주어지면 세로 방향도 체크 (캔들의 고가~저가 범위 안에 있어야 함).
function _isOnCandle(chart, row, xVal, hoverY) {
  if (!chart || !row) return false;
  const xScale = chart.scales.x;
  const rowPx = xScale.getPixelForValue(row.x);
  const hoverPx = xScale.getPixelForValue(xVal);
  // bar width 추정 (인접 캔들 간격)
  const arr = chart.data.datasets.find(d => d._candle || d._volume);
  let barW = 6;
  if (arr && arr.data && arr.data.length) {
    const idx = arr.data.indexOf(row);
    if (idx >= 0) {
      if (idx + 1 < arr.data.length) {
        barW = Math.abs(xScale.getPixelForValue(arr.data[idx + 1].x) - rowPx);
      } else if (idx > 0) {
        barW = Math.abs(rowPx - xScale.getPixelForValue(arr.data[idx - 1].x));
      }
    }
  }
  if (Math.abs(hoverPx - rowPx) > Math.max(barW * 0.6, 3)) return false;
  // 세로 방향 체크 (hoverY 주어졌을 때만)
  if (hoverY != null) {
    const yScale = chart.scales.y;
    if (!yScale) return false;
    const pad = 2;  // 픽셀 여유
    if (row.h != null && row.l != null) {
      // 캔들: 고가~저가 픽셀 범위 (y축은 반전 — 고가가 더 작은 픽셀값)
      const hPx = yScale.getPixelForValue(row.h);
      const lPx = yScale.getPixelForValue(row.l);
      const top = Math.min(hPx, lPx) - pad;
      const bot = Math.max(hPx, lPx) + pad;
      if (hoverY < top || hoverY > bot) return false;
    } else if (row.v != null) {
      // 거래대금 바: 0 ~ v 픽셀 범위
      const zeroPx = yScale.getPixelForValue(0);
      const vPx = yScale.getPixelForValue(row.v);
      const top = Math.min(zeroPx, vPx) - pad;
      const bot = Math.max(zeroPx, vPx) + pad;
      if (hoverY < top || hoverY > bot) return false;
    }
  }
  return true;
}

function updateHTSTooltip(view, px, evt, sourceChart) {
  const box = document.getElementById(view + '-tooltip');
  if (!box) return;
  const charts = getChartsForView(view);
  if (!charts.length) return;
  const src = crosshairState.sourceChart || charts[0];
  const xVal = src.scales.x.getValueForPixel(px);
  if (xVal == null) { box.style.display = 'none'; return; }

  const usIndexChart = charts.find(c => c.$role === 'us-price');
  const priceChart = charts.find(c => c.$role === 'price');
  const stockChart = charts.find(c => c.$role === 'stock');
  const volChart = charts.find(c => c.$role === 'volume');

  // 1차 판정: 호버 위치가 "어느 차트의 캔들" 위에 있는지 검사.
  // 보이는(hidden=false) candle dataset 을 찾아 그 시점의 row 반환.
  // === EXACT-MATCH 만 채택: 휴장일 패널은 자연스럽게 null → 섹션 누락 ===
  function nearestVisibleCandle(chart) {
    if (!chart) return null;
    for (let i = 0; i < chart.data.datasets.length; i++) {
      const ds = chart.data.datasets[i];
      if (!ds._candle) continue;
      if (!chart.isDatasetVisible(i)) continue;
      const r = findRowAtTimeExact(ds.data, xVal);
      if (r) return { ds, row: r, dsIndex: i };
    }
    return null;
  }
  const usHit = nearestVisibleCandle(usIndexChart);
  const krHit = nearestVisibleCandle(priceChart);
  const stockHit = nearestVisibleCandle(stockChart);

  // source chart 기준으로 캔들 위 판정 (우선)
  // hoverY 를 넘겨 x 뿐만 아니라 세로 방향(캔들 실제 범위)도 체크
  // 지수 패널은 visible candle 가 여러 개일 수 있으므로 ANY-hit 채택
  const hoverY = crosshairState.y;
  let hoveredOnCandle = false;
  function anyHitOnCandle(chart, hit) {
    return !!(hit && _isOnCandle(chart, hit.row, xVal, hoverY));
  }
  function anyVisibleOnCandle(chart) {
    if (!chart) return false;
    for (let i = 0; i < chart.data.datasets.length; i++) {
      const ds = chart.data.datasets[i];
      if (!ds._candle) continue;
      if (!chart.isDatasetVisible(i)) continue;
      const r = findRowAtTimeExact(ds.data, xVal);
      if (r && _isOnCandle(chart, r, xVal, hoverY)) return true;
    }
    return false;
  }
  if (src.$role === 'us-price') {
    hoveredOnCandle = anyVisibleOnCandle(src);
  } else if (src.$role === 'price') {
    hoveredOnCandle = anyVisibleOnCandle(src);
  } else if (src.$role === 'stock' && stockHit) {
    hoveredOnCandle = anyHitOnCandle(src, stockHit);
  } else if (src.$role === 'volume') {
    const vds = volChart ? volChart.data.datasets.find(d => d._volume) : null;
    const vrow = vds ? findRowAtTimeExact(vds.data, xVal) : null;
    hoveredOnCandle = !!(vrow && _isOnCandle(src, vrow, xVal, hoverY));
  }
  if (!hoveredOnCandle) {
    box.style.display = 'none';
    return;
  }

  const dateLabel = _fmtDateDow(xVal);

  let html = '<div class="hts-date">' + dateLabel + '</div>';

  function renderSection(title, chart, color, hit) {
    if (!chart || !hit || !hit.row) return '';
    const cds = hit.ds;
    if (!cds || !cds.data.length) return '';
    const row = hit.row;
    // 해당 차트에서도 캔들 위 판정 — 아니면 이 섹션은 비움
    if (!_isOnCandle(chart, row, xVal)) return '';
    const idx = cds.data.indexOf(row);
    const prev = idx > 0 ? cds.data[idx - 1] : null;
    const prevC = prev ? prev.c : null;
    function pctOf(val) {
      if (prevC == null || !prevC) return null;
      return (val - prevC) / prevC * 100;
    }
    function pctSpan(pct) {
      if (pct == null) return '';
      const up = pct >= 0;
      const cls = up ? 'hts-up' : 'hts-down';
      const sign = up ? '+' : '';
      return ' <span class="' + cls + '" style="font-size:11px;">(' + sign + fmt(pct, 2) + '%)</span>';
    }
    const oP = pctOf(row.o), hP = pctOf(row.h), lP = pctOf(row.l), cP = pctOf(row.c);
    const cCls = (cP != null && cP >= 0) ? 'hts-up' : 'hts-down';
    // 섹션 실제 데이터 날짜 (xVal 과 다를 수 있음 — 정합성 검증용)
    const _rowDateLbl = _fmtDateDowPlain(row.x);
    let s = '<div class="hts-section">';
    s += '<div class="hts-section-title" style="color:' + (color || '#8b949e') + ';">' + title + ' <span style="color:#8b949e;font-size:11px;font-weight:normal;">(' + _rowDateLbl + ')</span></div>';
    s += '<div class="hts-row"><span class="k">시가</span><span class="v">' + fmt(row.o) + pctSpan(oP) + '</span></div>';
    s += '<div class="hts-row"><span class="k">고가</span><span class="v">' + fmt(row.h) + pctSpan(hP) + '</span></div>';
    s += '<div class="hts-row"><span class="k">저가</span><span class="v">' + fmt(row.l) + pctSpan(lP) + '</span></div>';
    s += '<div class="hts-row"><span class="k">종가</span><span class="v ' + cCls + '">' + fmt(row.c) + pctSpan(cP) + '</span></div>';
    // MA values with 이격도 (당일종가 기준)
    // 정책: (1) 토글 OFF (hidden) dataset 절대 표시 안 함
    //        (2) 같은 _indexId 의 MA 만 매칭 (지수 패널 멀티 시리즈 분리)
    chart.data.datasets.forEach((ds, i) => {
      if (!ds._isMa) return;
      if (!chart.isDatasetVisible(i)) return;
      if (cds._indexId && ds._indexId && cds._indexId !== ds._indexId) return;
      const mp = findRowAtTimeExact(ds.data, row.x);
      if (mp && mp.y != null) {
        const disparity = ((row.c - mp.y) / mp.y) * 100;
        const dUp = disparity >= 0;
        const dCls = dUp ? 'hts-up' : 'hts-down';
        const dSign = dUp ? '+' : '';
        // MA 라벨은 일반 색 (큰 카테고리만 색을 유지). 등락 % 만 빨/파.
        s += '<div class="hts-row"><span class="k">' + ds.label + '</span><span class="v">' + fmt(mp.y) + ' <span class="' + dCls + '" style="font-size:11px;">(' + dSign + fmt(disparity, 2) + '%)</span></span></div>';
      }
    });
    s += '</div>';
    return s;
  }

  // 모든 visible candle 수집 (지수 패널은 NASDAQ+S&P500 또는 KOSPI+KOSDAQ 동시 표시 가능)
  // === EXACT-MATCH: 정확히 같은 날짜의 캔들만 — 휴장일은 빈 배열 반환 ===
  function allVisibleHits(chart) {
    if (!chart) return [];
    const out = [];
    for (let i = 0; i < chart.data.datasets.length; i++) {
      const ds = chart.data.datasets[i];
      if (!ds._candle) continue;
      if (!chart.isDatasetVisible(i)) continue;
      const r = findRowAtTimeExact(ds.data, xVal);
      if (r) out.push({ ds, row: r, dsIndex: i });
    }
    return out;
  }
  const usHits = allVisibleHits(usIndexChart);
  const krHits = allVisibleHits(priceChart);

  // 휴장 섹션 — 제목 + (날짜 요일) - 휴장 표시만
  function renderClosedSection(title, color) {
    return '<div class="hts-section">'
      + '<div class="hts-section-title" style="color:' + (color || '#8b949e') + ';">'
      + title + ' <span style="color:#8b949e;font-size:11px;font-weight:normal;">'
      + '(' + _fmtDateDowPlain(xVal) + ') - 휴장</span></div>'
      + '</div>';
  }

  // US 지수 섹션 (NASDAQ / S&P500 토글된 항목만)
  const _usColors = { nasdaq: '#FF6B6B', sp500: '#4ECDC4' };
  let usSection = '';
  if (usHits.length > 0) {
    usHits.forEach(h => {
      const lbl = h.ds.label;
      const color = _usColors[h.ds._indexId] || '#8b949e';
      usSection += renderSection(lbl, usIndexChart, color, h);
    });
  } else {
    // 미장 휴장 — visible candle dataset 라벨로 휴장 섹션 생성
    _visibleCandleInfo(usIndexChart).forEach(info => {
      const color = _usColors[info.indexId] || '#8b949e';
      usSection += renderClosedSection(info.label, color);
    });
  }
  // KR 지수 섹션 (KOSPI / KOSDAQ)
  const _krColors = { kospi: '#F39C12', kosdaq: '#4ECDC4' };
  let krSection = '';
  if (krHits.length > 0) {
    krHits.forEach(h => {
      const lbl = h.ds.label;
      const color = _krColors[h.ds._indexId] || '#8b949e';
      krSection += renderSection(lbl, priceChart, color, h);
    });
  } else {
    _visibleCandleInfo(priceChart).forEach(info => {
      const color = _krColors[info.indexId] || '#8b949e';
      krSection += renderClosedSection(info.label, color);
    });
  }
  // 종목 섹션
  let stockSection = '';
  if (stockHit) {
    stockSection = renderSection(stockChart && stockChart.$stockName ? stockChart.$stockName : '주도주', stockChart, stockChart && stockChart.$stockColor || '#58a6ff', stockHit);
  } else if (stockChart) {
    // 종목 휴장 — 종목명+휴장 표시
    const stockColor = stockChart.$stockColor || '#58a6ff';
    const stockName = stockChart.$stockName || '주도주';
    stockSection = renderClosedSection(stockName, stockColor);
  }
  html += usSection + krSection + stockSection;

  // 거래대금 — volume 섹션은 stock 캔들과 동일한 시점이므로 stock 이 캔들 위일 때만 표시
  if (volChart && stockSection) {
    const vds = volChart.data.datasets.find(d => d._volume);
    if (vds) {
      const row = findRowAtTimeExact(vds.data, xVal);
      if (row && row.v != null) {
        html += '<div class="hts-section"><div class="hts-row"><span class="k">거래대금</span><span class="v">' + fmt(row.v, 0) + ' 억</span></div></div>';
      }
    }
  }

  // 결과: 어떤 섹션도 렌더되지 않으면 숨김 (edge case 방어)
  if (!usSection && !krSection && !stockSection) {
    box.style.display = 'none';
    return;
  }

  box.innerHTML = html;
  box.style.display = 'block';

  // === HTS-style positioning: follow cursor, flip when near right edge ===
  if (evt && evt.native && sourceChart) {
    const container = box.parentElement; // .stack-wrap
    if (container) {
      const cRect = container.getBoundingClientRect();
      const mx = evt.native.clientX - cRect.left;
      const my = evt.native.clientY - cRect.top;
      const bw = box.offsetWidth || 240;
      const bh = box.offsetHeight || 200;
      const pad = 16;
      // Flip horizontally when cursor is on right half of container
      let left = (mx < cRect.width / 2) ? (mx + pad) : (mx - bw - pad);
      // Clamp within container
      left = Math.max(4, Math.min(cRect.width - bw - 4, left));
      let top = my + pad;
      // If tooltip would overflow bottom, show above cursor
      if (top + bh > cRect.height - 4) top = Math.max(4, my - bh - pad);
      box.style.left = left + 'px';
      box.style.top = top + 'px';
      box.style.right = 'auto';
    }
  }
}
function hideHTSTooltip(view) {
  const box = document.getElementById(view + '-tooltip');
  if (box) box.style.display = 'none';
}

// ===== CHART REGISTRY =====
const chartRegistry = { v1: [], v2: [] };
function getChartsForView(view) { return chartRegistry[view] || []; }
function destroyView(view) {
  chartRegistry[view].forEach(c => { try { c.destroy(); } catch(e){} });
  chartRegistry[view] = [];
}

// ===== DRAG-ZOOM & WHEEL-PAN =====
const zoomStates = { v1: {zoomed:false}, v2: {zoomed:false} };
let dragState = { active: false, startX: null, startPx: null, chart: null, view: null };

function getOverlayForChart(chart) {
  if (!chart.$view || !chart.$role) return null;
  return document.getElementById('drag-overlay-' + chart.$view + '-' + chart.$role);
}
function hideAllOverlays(view) {
  ['us-price','price','stock','volume'].forEach(r => {
    const el = document.getElementById('drag-overlay-' + view + '-' + r);
    if (el) el.style.display = 'none';
  });
}

function applyZoomRange(view, minVal, maxVal) {
  const st = zoomStates[view];
  st.zoomed = true;
  st.curMin = minVal;
  st.curMax = maxVal;
  const isoMin = new Date(minVal).toISOString();
  const isoMax = new Date(maxVal).toISOString();
  getChartsForView(view).forEach(ch => {
    ch.options.scales.x.min = isoMin;
    ch.options.scales.x.max = isoMax;
    ch.update('none');
  });
  document.getElementById(view + '-zoom').style.display = 'flex';
  const d1 = new Date(minVal), d2 = new Date(maxVal);
  const f = d => d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0');
  document.getElementById(view + '-zoom-hint').textContent = f(d1) + ' ~ ' + f(d2);
  updateScrollbar(view);
}

// ===== X축 스크롤바 =====
function getFullDataRange(view) {
  const charts = getChartsForView(view);
  for (const ch of charts) {
    const cds = ch.data.datasets.find(d => d._candle || d._volume);
    if (cds && cds.data.length) {
      return { min: cds.data[0].x, max: cds.data[cds.data.length-1].x, data: cds.data };
    }
  }
  return null;
}
function getAvgCandleSpacing(view) {
  const r = getFullDataRange(view);
  if (!r || r.data.length < 2) return 86400000; // 1 day fallback
  const data = r.data;
  const sample = Math.min(data.length - 1, 60);
  let total = 0;
  for (let i = data.length - sample; i < data.length; i++) {
    total += data[i].x - data[i-1].x;
  }
  return total / sample;
}
function updateScrollbar(view) {
  const wrap = document.getElementById(view + '-xscroll');
  const thumb = document.getElementById(view + '-xscroll-thumb');
  if (!wrap || !thumb) return;
  const st = zoomStates[view];
  if (!st.zoomed) { wrap.classList.remove('active'); return; }
  const r = getFullDataRange(view);
  if (!r) { wrap.classList.remove('active'); return; }
  const fullRange = r.max - r.min;
  if (fullRange <= 0) { wrap.classList.remove('active'); return; }
  const viewRange = st.curMax - st.curMin;
  const leftPct = Math.max(0, Math.min(100, ((st.curMin - r.min) / fullRange) * 100));
  const widthPct = Math.max(3, Math.min(100, (viewRange / fullRange) * 100));
  wrap.classList.add('active');
  thumb.style.left = leftPct + '%';
  thumb.style.width = widthPct + '%';
}
function attachScrollbar(view) {
  const wrap = document.getElementById(view + '-xscroll');
  const thumb = document.getElementById(view + '-xscroll-thumb');
  if (!wrap || !thumb) return;
  let drag = null;
  const onDown = e => {
    const r = getFullDataRange(view);
    if (!r) return;
    const st = zoomStates[view];
    if (!st.zoomed) return;
    const wrapRect = wrap.getBoundingClientRect();
    const thumbRect = thumb.getBoundingClientRect();
    drag = {
      offsetX: e.clientX - thumbRect.left,
      wrapLeft: wrapRect.left,
      wrapWidth: wrapRect.width,
      fullMin: r.min, fullMax: r.max,
      viewRange: st.curMax - st.curMin,
    };
    thumb.classList.add('dragging');
    e.preventDefault();
  };
  const onMove = e => {
    if (!drag) return;
    const px = e.clientX - drag.wrapLeft - drag.offsetX;
    const thumbWidthPx = drag.wrapWidth * (drag.viewRange / (drag.fullMax - drag.fullMin));
    const maxLeft = drag.wrapWidth - thumbWidthPx;
    const clamped = Math.max(0, Math.min(maxLeft, px));
    const pct = clamped / drag.wrapWidth;
    const newMin = drag.fullMin + pct * (drag.fullMax - drag.fullMin);
    const newMax = newMin + drag.viewRange;
    applyZoomRange(view, newMin, newMax);
  };
  const onUp = () => {
    if (drag) { thumb.classList.remove('dragging'); drag = null; }
  };
  thumb.addEventListener('mousedown', onDown);
  document.addEventListener('mousemove', onMove);
  document.addEventListener('mouseup', onUp);
  // Click on track to jump
  wrap.addEventListener('mousedown', e => {
    if (e.target === thumb) return;
    const r = getFullDataRange(view);
    if (!r) return;
    const st = zoomStates[view];
    if (!st.zoomed) return;
    const wrapRect = wrap.getBoundingClientRect();
    const viewRange = st.curMax - st.curMin;
    const thumbWidthPx = wrapRect.width * (viewRange / (r.max - r.min));
    const clickPx = e.clientX - wrapRect.left - thumbWidthPx / 2;
    const maxLeft = wrapRect.width - thumbWidthPx;
    const clamped = Math.max(0, Math.min(maxLeft, clickPx));
    const pct = clamped / wrapRect.width;
    const newMin = r.min + pct * (r.max - r.min);
    const newMax = newMin + viewRange;
    applyZoomRange(view, newMin, newMax);
  });
}
// 초기화 (DOM 로드 후 한 번만)
window.addEventListener('DOMContentLoaded', () => {
  attachScrollbar('v1');
  attachScrollbar('v2');
});
function resetZoom(view) {
  const st = zoomStates[view];
  st.zoomed = false;
  getChartsForView(view).forEach(ch => {
    if (st.origMin != null) {
      ch.options.scales.x.min = st.origMin;
      ch.options.scales.x.max = st.origMax;
    } else {
      delete ch.options.scales.x.min;
      delete ch.options.scales.x.max;
    }
    ch.update('none');
  });
  document.getElementById(view + '-zoom').style.display = 'none';
  const wrap = document.getElementById(view + '-xscroll');
  if (wrap) wrap.classList.remove('active');
}

function attachZoomEvents(canvas, getChart, view) {
  canvas.addEventListener('mousedown', e => {
    const chart = getChart();
    if (!chart) return;
    const area = chart.chartArea;
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    if (x < area.left || x > area.right || y < area.top || y > area.bottom) return;
    dragState = { active: true, startPx: x, startX: chart.scales.x.getValueForPixel(x), chart, view };
    e.preventDefault();
  });

  canvas.addEventListener('mousemove', e => {
    if (!dragState.active || dragState.view !== view) return;
    const chart = getChart();
    if (!chart) return;
    const area = chart.chartArea;
    const rect = canvas.getBoundingClientRect();
    const x = Math.max(area.left, Math.min(e.clientX - rect.left, area.right));
    const left = Math.min(dragState.startPx, x);
    const width = Math.abs(x - dragState.startPx);
    // Show overlay on all charts for this view
    getChartsForView(view).forEach(ch => {
      const ov = getOverlayForChart(ch);
      if (!ov) return;
      const srcArea = dragState.chart.chartArea;
      const ratio1 = (left - srcArea.left) / (srcArea.right - srcArea.left);
      const ratio2 = (left + width - srcArea.left) / (srcArea.right - srcArea.left);
      const ca = ch.chartArea;
      const cL = ca.left + ratio1 * (ca.right - ca.left);
      const cR = ca.left + ratio2 * (ca.right - ca.left);
      ov.style.display = 'block';
      ov.style.left = cL + 'px';
      ov.style.width = (cR - cL) + 'px';
    });
  });

  canvas.addEventListener('wheel', e => {
    const st = zoomStates[view];
    if (!st.zoomed) return;
    e.preventDefault();
    // 휠 1틱 = 캔들 1개 이동 (deltaY 음수 = 우측으로, 양수 = 좌측으로)
    const spacing = getAvgCandleSpacing(view);
    const pan = spacing;  // 1 candle
    const r = getFullDataRange(view);
    let newMin, newMax;
    if (e.deltaY < 0) { newMin = st.curMin + pan; newMax = st.curMax + pan; }
    else { newMin = st.curMin - pan; newMax = st.curMax - pan; }
    // Clamp to data bounds
    if (r) {
      const vr = newMax - newMin;
      if (newMin < r.min) { newMin = r.min; newMax = newMin + vr; }
      if (newMax > r.max) { newMax = r.max; newMin = newMax - vr; }
    }
    applyZoomRange(view, newMin, newMax);
  }, { passive: false });
}

// Document-level mouseup
document.addEventListener('mouseup', e => {
  if (!dragState.active) return;
  const chart = dragState.chart;
  const view = dragState.view;
  if (!chart || !view) { dragState.active = false; return; }
  const canvas = chart.canvas;
  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const area = chart.chartArea;
  hideAllOverlays(view);
  const dx = x - dragState.startPx;
  dragState.active = false;

  if (dx > 5 || x > area.right) {
    // Right drag (or exit right edge) → zoom in. Clamp to data max.
    let endVal;
    if (x >= area.right) {
      // Pan to most recent data
      const cds = chart.data.datasets.find(d => d._candle || d._volume);
      if (cds && cds.data.length) endVal = cds.data[cds.data.length - 1].x;
      else endVal = chart.scales.x.getValueForPixel(area.right);
    } else {
      endVal = chart.scales.x.getValueForPixel(Math.min(x, area.right));
    }
    const minVal = Math.min(dragState.startX, endVal);
    const maxVal = Math.max(dragState.startX, endVal);
    const st = zoomStates[view];
    if (!st.zoomed) {
      st.origMin = chart.options.scales.x.min || null;
      st.origMax = chart.options.scales.x.max || null;
    }
    applyZoomRange(view, minVal, maxVal);
  } else if (dx < -5) {
    if (zoomStates[view].zoomed) resetZoom(view);
  }
});

// ===== CHART BUILDERS =====
function makePriceChart(canvasId, ohlcData, title, color, extraAnn, scaleType, view, role) {
  const datasets = [];
  datasets.push({
    label: title, data: ohlcData,
    borderColor: color + '00', backgroundColor: color + '00',
    pointRadius: 0, yAxisID: 'y', order: 10,
    _candle: true, _candleUp: CANDLE_UP, _candleDown: CANDLE_DN,
  });
  // MA 5/10/20/60/120
  [5, 10, 20, 60, 120].forEach(p => {
    const ma = computeMA(ohlcData, p);
    datasets.push({
      label: 'MA' + p, data: ma,
      borderColor: MA_COLORS['ma' + p], backgroundColor: 'transparent',
      borderWidth: 1.2, pointRadius: 0, fill: false, yAxisID: 'y', order: 20,
      tension: 0, _isMa: true,
      spanGaps: true,
    });
  });

  const annotations = extraAnn || {};
  const ctx = document.getElementById(canvasId).getContext('2d');
  const ch = new Chart(ctx, {
    type: 'line',
    data: { datasets },
    options: {
      responsive: true, maintainAspectRatio: false,
      animation: false,
      interaction: { mode: 'nearest', intersect: false },
      plugins: {
        legend: { display: false },
        annotation: { annotations },
        tooltip: { enabled: false }
      },
      scales: {
        x: {
          type: 'timeseries',
          time: { unit: 'year', displayFormats: { year: 'yyyy', month: 'yyyy-MM', day: 'yyyy-MM-dd' } },
          grid: { color: '#9A9A9A' },
          ticks: { color: '#1c2128', font: { size: 10 }, maxTicksLimit: 14, autoSkip: true,
            // 줌 윈도우 시간 범위 기준 분기 (4년):
            //   - 4년 이상: 연도 변경 tick 만 yyyy, 같은 연도 중복은 빈 라벨
            //   - 4년 미만: 매 tick에 라벨. 1월(또는 첫 tick)은 yyyy, 그 외는 'M월'
            // autoSkip:false 로 chart.js 자동 hide 방지 — 빈 라벨도 자리만 차지하고 그 외는 모두 표시.
            callback: function(value, index, ticks) {
              if (!ticks || !ticks.length) return '';
              const winYears = (ticks[ticks.length - 1].value - ticks[0].value) / (365.25 * 86400000);
              const d = new Date(value);
              const yr = d.getFullYear();
              const mo = d.getMonth() + 1;
              if (winYears >= 4) return yr;
              if (mo === 1 || index === 0) return yr;
              return mo + '월';
            }
          },
          display: false
        },
        y: {
          type: scaleType === 'log' ? 'logarithmic' : 'linear',
          position: 'left',
          grid: { color: '#9A9A9A' },
          ticks: { color: '#1c2128', font: { size: 10 }, callback: v => v.toLocaleString() }
        }
      }
    }
  });
  ch.$view = view; ch.$role = role; ch.$stockName = title; ch.$stockColor = color;
  return ch;
}

function makeIndexChart(canvasId, data1, data2, scaleType, view, role, annotations) {
  // 한국식 캔들 차트 (양봉=빨강 / 음봉=파랑) — 종목 패널과 동일 스타일
  // data1, data2 는 항상 전달 (full OHLC). 표시 여부는 hidden 으로 토글.
  // MA 5/10/20/60/120 동봉. 사이클 박스는 annotations 로 전달.
  const isUS = role === 'us-price';
  const id1 = isUS ? 'nasdaq' : 'kospi';
  const id2 = isUS ? 'sp500'  : 'kosdaq';
  const lbl1 = isUS ? 'NASDAQ' : 'KOSPI';
  const lbl2 = isUS ? 'S&P500' : 'KOSDAQ';
  const k1 = (isUS ? 'us_' : 'kr_') + id1;
  const k2 = (isUS ? 'us_' : 'kr_') + id2;
  const hidden1 = !toggleStates[view][k1];
  const hidden2 = !toggleStates[view][k2];

  const datasets = [
    {
      label: lbl1, data: data1 || [],
      borderColor: 'transparent', backgroundColor: 'transparent',
      pointRadius: 0, yAxisID: 'y', order: 10,
      _candle: true, _candleUp: CANDLE_UP, _candleDown: CANDLE_DN,
      _indexId: id1,
      hidden: hidden1,
    },
  ];
  // MA for dataset 1
  [5, 10, 20, 60, 120].forEach(p => {
    const ma = (data1 && data1.length) ? computeMA(data1, p) : [];
    datasets.push({
      label: 'MA' + p, data: ma,
      borderColor: MA_COLORS['ma' + p], backgroundColor: 'transparent',
      borderWidth: 1.0, pointRadius: 0, fill: false, yAxisID: 'y', order: 20,
      tension: 0, _isMa: true, _indexId: id1, spanGaps: true,
      hidden: hidden1,
    });
  });
  datasets.push({
    label: lbl2, data: data2 || [],
    borderColor: 'transparent', backgroundColor: 'transparent',
    pointRadius: 0, yAxisID: 'y', order: 10,
    _candle: true, _candleUp: CANDLE_UP, _candleDown: CANDLE_DN,
    _indexId: id2,
    hidden: hidden2,
  });
  // MA for dataset 2
  [5, 10, 20, 60, 120].forEach(p => {
    const ma = (data2 && data2.length) ? computeMA(data2, p) : [];
    datasets.push({
      label: 'MA' + p, data: ma,
      borderColor: MA_COLORS['ma' + p], backgroundColor: 'transparent',
      borderWidth: 1.0, pointRadius: 0, fill: false, yAxisID: 'y', order: 20,
      tension: 0, _isMa: true, _indexId: id2, spanGaps: true,
      hidden: hidden2,
    });
  });

  const ctx = document.getElementById(canvasId).getContext('2d');
  const ch = new Chart(ctx, {
    type: 'line',
    data: { datasets },
    options: {
      responsive: true, maintainAspectRatio: false,
      animation: false,
      interaction: { mode: 'nearest', intersect: false },
      plugins: {
        legend: { display: false },
        annotation: { annotations: annotations || {} },
        tooltip: { enabled: false }
      },
      scales: {
        x: {
          type: 'timeseries',
          time: { unit: 'year', displayFormats: { year: 'yyyy', month: 'yyyy-MM', day: 'yyyy-MM-dd' } },
          grid: { color: '#9A9A9A' },
          ticks: { color: '#1c2128', font: { size: 10 }, maxTicksLimit: 14, autoSkip: true,
            // 줌 윈도우 시간 범위 기준 분기 (4년):
            //   - 4년 이상: 연도 변경 tick 만 yyyy, 같은 연도 중복은 빈 라벨
            //   - 4년 미만: 매 tick에 라벨. 1월(또는 첫 tick)은 yyyy, 그 외는 'M월'
            // autoSkip:false 로 chart.js 자동 hide 방지 — 빈 라벨도 자리만 차지하고 그 외는 모두 표시.
            callback: function(value, index, ticks) {
              if (!ticks || !ticks.length) return '';
              const winYears = (ticks[ticks.length - 1].value - ticks[0].value) / (365.25 * 86400000);
              const d = new Date(value);
              const yr = d.getFullYear();
              const mo = d.getMonth() + 1;
              if (winYears >= 4) return yr;
              if (mo === 1 || index === 0) return yr;
              return mo + '월';
            }
          },
          display: false
        },
        y: {
          type: scaleType === 'log' ? 'logarithmic' : 'linear',
          position: 'left',
          grid: { color: '#9A9A9A' },
          ticks: { color: '#1c2128', font: { size: 10 }, callback: v => v.toLocaleString() }
        }
      }
    }
  });
  ch.$view = view; ch.$role = role;
  return ch;
}

// ===== INDEX ANNOTATION BUILDERS =====
// 토글 OFF 시 같이 숨기 위해 display 콜백 사용 (toggleStates 평가).
function _idxToggleKey(idxId) {
  if (idxId === 'nasdaq' || idxId === 'sp500') return 'us_' + idxId;
  return 'kr_' + idxId;
}

// 미국 사이클 = bull/bear 에 따라 색상 구분
//   bull: 인디고 (강세장)
//   bear: 진한 빨강 톤 (약세장 — 회색 배경 대비 강한 대비)
function _usCycleColor(category) {
  if (category === 'bear') {
    return { bg: 'rgba(176, 0, 32, 0.07)', border: 'rgba(176, 0, 32, 0.75)', text: '#B00020' };
  }
  // bull / 그 외
  return { bg: 'rgba(40, 53, 147, 0.07)', border: 'rgba(40, 53, 147, 0.75)', text: '#283593' };
}

// V1 전체 히스토리: 모든 사이클의 박스를 누적 표시 (지수별)
//   - 미국 지수 (nasdaq/sp500): US_MARKET_CYCLES (Market_cycle 정의 기반)
//   - 한국 지수 (kospi/kosdaq):  CYCLES.indexZones (LEADING_STOCKS 기반)
function buildAllCyclesIndexAnn(idxId, view) {
  const ann = {};
  const k = _idxToggleKey(idxId);
  const isUS = (idxId === 'nasdaq' || idxId === 'sp500');
  if (isUS) {
    // 주도주 사이클 차트는 상승장 위주 — 약세장(bear) 박스는 제외
    US_MARKET_CYCLES.forEach((c, i) => {
      if (!c.start || !c.end) return;
      if (c.category === 'bear') return;
      const col = _usCycleColor(c.category);
      ann['us_' + i] = {
        type: 'box',
        xMin: new Date(c.start).getTime(),
        xMax: new Date(c.end).getTime(),
        backgroundColor: col.bg,
        borderColor: col.border,
        borderWidth: 1,
        // 개별 사이클 탭과 동일하게 박스마다 사이클 이름 표시
        label: { display: true, content: c.name, position: 'start', color: col.text, font: { size: 9, weight: 'bold' } },
        // US 박스는 NASDAQ 또는 S&P500 둘 중 하나라도 ON 이면 표시
        display: () => !!(toggleStates[view].us_nasdaq || toggleStates[view].us_sp500),
      };
    });
  } else {
    // 한국: 주도 섹터 박스 (지수와 무관) — kospi 호출에서 한 번만 생성
    if (idxId !== 'kospi') return ann;
    CYCLES.forEach((c, i) => Object.assign(ann, _sectorBoxes(c, i, view, 9)));
  }
  return ann;
}

// ===== 주도 섹터 박스 (2026-11-03) =====
// 사이클·분류별 박스 = 해당 분류 주도주 중장기 박스의 합집합 (create_leading_stocks.py SECTOR_CATEGORY)
//   인프라 = B2B + 설비투자 필요 / 기술 = B2B + 설비 불필요 / 소비 = B2C / 참고 = 1998 이전
const SECTOR_BOX_COLORS = {
  '인프라': { bg: 'rgba(40, 53, 147, 0.08)', border: 'rgba(40, 53, 147, 0.75)', text: '#283593' },
  '기술':   { bg: 'rgba(191, 96, 0, 0.10)',  border: 'rgba(191, 96, 0, 0.80)',  text: '#A35200' },
  '소비':   { bg: 'rgba(46, 125, 50, 0.10)', border: 'rgba(46, 125, 50, 0.80)', text: '#2E7D32' },
  '참고':   { bg: 'rgba(97, 97, 97, 0.06)',  border: 'rgba(97, 97, 97, 0.55)',  text: '#616161' },
};
function _sectorBoxes(c, i, view, fontSize) {
  const out = {};
  (c.sectorZones || []).forEach((z, j) => {
    if (!z.start || !z.end) return;
    const col = SECTOR_BOX_COLORS[z.cat] || SECTOR_BOX_COLORS['참고'];
    const closed = z.status === '종료';
    const txt = (j === 0 ? c.name + ' · ' : '') + z.cat + (closed ? '' : ' [' + z.status + ']');
    out['sec_' + i + '_' + j] = {
      type: 'box',
      xMin: new Date(z.start).getTime(),
      xMax: new Date(z.end).getTime(),
      backgroundColor: col.bg,
      borderColor: col.border,
      borderWidth: 1,
      borderDash: closed ? undefined : [4, 4],
      label: { display: true, content: txt, position: 'start', yAdjust: j * (fontSize + 5), color: col.text, font: { size: fontSize, weight: 'bold' } },
      display: () => !!(toggleStates[view].kr_kospi || toggleStates[view].kr_kosdaq),
    };
  });
  return out;
}

// V2 사이클 단위: 현재 사이클의 박스 (지수별)
//   - 한국 지수: 선택된 KR 사이클 박스 1개 (현재 로직)
//   - 미국 지수: cycle 의 시간 윈도우와 겹치는 US 사이클들 모두 (각각 미국 사이클명 라벨)
function buildCycleIndexAnn(cycle, idxId, view) {
  const k = _idxToggleKey(idxId);
  const isUS = (idxId === 'nasdaq' || idxId === 'sp500');

  if (isUS) {
    // cycle ±2년 범위와 overlap 되는 US 사이클들
    const winStart = (cycle && cycle.manualStart) ? new Date(cycle.manualStart) : (cycle && cycle.start ? new Date(cycle.start) : null);
    const winEnd   = (cycle && cycle.manualEnd)   ? new Date(cycle.manualEnd)   : (cycle && cycle.end   ? new Date(cycle.end)   : null);
    if (!winStart || !winEnd) return {};
    const ws = new Date(winStart); ws.setFullYear(ws.getFullYear() - 2);
    const we = new Date(winEnd);   we.setFullYear(we.getFullYear() + 2);
    const wsMs = ws.getTime(), weMs = we.getTime();
    const ann = {};
    US_MARKET_CYCLES.forEach((c, i) => {
      if (!c.start || !c.end) return;
      // 주도주 사이클 차트는 상승장 위주 — 약세장(bear) 박스는 제외
      if (c.category === 'bear') return;
      const cs = new Date(c.start).getTime();
      const ce = new Date(c.end).getTime();
      if (ce < wsMs || cs > weMs) return;  // overlap 없음
      const col = _usCycleColor(c.category);
      ann['us_' + i] = {
        type: 'box',
        xMin: cs, xMax: ce,
        backgroundColor: col.bg,
        borderColor: col.border,
        borderWidth: 1,
        label: { display: true, content: c.name, position: 'start', color: col.text, font: { size: 10, weight: 'bold' } },
        display: () => !!(toggleStates[view].us_nasdaq || toggleStates[view].us_sp500),
      };
    });
    return ann;
  }

  // KR 패널 — 주도 섹터 박스 (2026-11-03). kospi 호출에서만 생성
  if (idxId !== 'kospi' || !cycle) return {};
  return _sectorBoxes(cycle, 0, view, 10);
}

function makeVolumeChart(canvasId, ohlcData, view) {
  // Volume data with 'up' flag based on close vs open
  const data = ohlcData.map((d, i) => {
    const prev = i > 0 ? ohlcData[i-1] : null;
    const up = prev ? (d.c >= prev.c) : (d.c >= d.o);
    return { x: d.x, y: d.v, v: d.v, up };
  });
  const ctx = document.getElementById(canvasId).getContext('2d');
  const ch = new Chart(ctx, {
    type: 'line',
    data: { datasets: [{
      label: '거래대금', data, pointRadius: 0,
      borderColor: 'transparent', backgroundColor: 'transparent',
      yAxisID: 'y', _volume: true
    }]},
    options: {
      responsive: true, maintainAspectRatio: false,
      animation: false,
      interaction: { mode: 'nearest', intersect: false },
      plugins: { legend: { display: false }, tooltip: { enabled: false } },
      scales: {
        x: {
          type: 'timeseries',
          time: { unit: 'year', displayFormats: { year: 'yyyy', month: 'yyyy-MM', day: 'yyyy-MM-dd' } },
          grid: { color: '#9A9A9A' },
          ticks: { color: '#1c2128', font: { size: 10 }, maxTicksLimit: 14, autoSkip: true,
            callback: function(value, index, ticks) {
              if (!ticks || !ticks.length) return '';
              const winYears = (ticks[ticks.length - 1].value - ticks[0].value) / (365.25 * 86400000);
              const d = new Date(value);
              const yr = d.getFullYear();
              const mo = d.getMonth() + 1;
              if (winYears >= 4) return yr;
              if (mo === 1 || index === 0) return yr;
              return mo + '월';
            }
          }
        },
        y: {
          type: 'linear', position: 'left', beginAtZero: true,
          grid: { color: '#9A9A9A' },
          ticks: { color: '#1c2128', font: { size: 10 }, callback: v => v.toLocaleString() }
        }
      }
    }
  });
  ch.$view = view; ch.$role = 'volume';
  return ch;
}

// ===== VIEW 1 =====
let v1Scale = 'linear';
let v1CurrentStock = null;  // single-select

function initV1() {
  const container = document.getElementById('v1-stock-btns');
  ALL_STOCK_ENTRIES.forEach(s => {
    const color = stockColorMap[s.id];
    const btn = document.createElement('button');
    btn.className = 'stock-btn';
    btn.style.setProperty('--sc', color);
    btn.textContent = formatStockLabel(s);
    btn.dataset.stockId = s.id;
    btn.dataset.cycleId = s.cycleId;
    btn.onclick = () => {
      document.querySelectorAll('#v1-stock-btns .stock-btn').forEach(b => b.classList.remove('on'));
      btn.classList.add('on');
      v1CurrentStock = s;
      renderV1();
    };
    container.appendChild(btn);
  });
}

function setV1Scale(scale) {
  v1Scale = scale;
  document.getElementById('v1-linear').classList.toggle('active', scale === 'linear');
  document.getElementById('v1-log').classList.toggle('active', scale === 'log');
  if (v1CurrentStock) renderV1();
}

function renderV1() {
  destroyView('v1');
  zoomStates.v1 = { zoomed: false };
  document.getElementById('v1-zoom').style.display = 'none';

  if (!v1CurrentStock) {
    document.getElementById('v1-legend').innerHTML = '<div class="legend-item" style="color:#8b949e;">종목을 선택하면 3단 차트가 표시됩니다</div>';
    return;
  }

  const stock = v1CurrentStock;
  const color = stockColorMap[stock.id];
  const stockMeta = META[stock.id];
  const stockRaw = STOCKS_RAW[stock.id] || [];
  const kospiWeekly = toWeekly(KOSPI_RAW);
  const stockWeekly = toWeekly(stockRaw);

  document.getElementById('v1-title').textContent = fmtStockLabel(stock.era, stock.name) + ' × KOSPI 전체';
  document.getElementById('v1-meta').textContent =
    'KOSPI ' + (kospiWeekly.length ? (new Date(kospiWeekly[0].x).toISOString().slice(0,10) + ' ~ 현재') : '') +
    ' | ' + stock.name + ' ' + (stockWeekly.length ? new Date(stockWeekly[0].x).toISOString().slice(0,10) : '?') +
    ' ~ | 주봉 | ' + (v1Scale === 'log' ? '로그' : '리니어');
  document.getElementById('v1-stock-label').textContent = stock.name;

  // Build longterm (outer) + lifecycle (inner) zones for this stock
  const zoneAnn = {};
  STOCK_ZONES.forEach((z, i) => {
    if (z.stockId !== stock.id) return;
    if (stock.cycleId && z.cycleId && z.cycleId !== stock.cycleId) return;
    // Outer 중장기 박스 — 인디고 톤 (지수 사이클 박스와 동일 시각 언어)
    if (z.longterm && z.longterm.start && z.longterm.end) {
      const lt = z.longterm;
      const closed = lt.status === '종료';
      let statusSuffix = lt.status;
      if (lt.rs_recovery) statusSuffix += ' • RS ' + lt.rs_recovery.slice(2);
      const ltLabel = z.label + ' [' + statusSuffix + ']';
      zoneAnn['lt_' + i] = {
        type: 'box',
        xMin: new Date(lt.start).getTime(),
        xMax: new Date(lt.end).getTime(),
        backgroundColor: 'rgba(40, 53, 147, 0.07)',
        borderColor: 'rgba(40, 53, 147, 0.75)',
        borderWidth: 1,
        borderDash: closed ? undefined : [6, 4],
        label: { display: true, content: ltLabel, position: { x: 'center', y: 'start' }, color: '#283593', font: { size: 11, weight: 'bold' }, backgroundColor: 'transparent' }
      };
    }
    // Inner lifecycle box (관성~전고점 트라이) — 보라 점선
    if (false && z.lifecycle && z.lifecycle.box_start && z.lifecycle.box_end) {  // 2026-11-04 Lifecycle 표시 제거 (공통 파란 박스만)
      zoneAnn['lc_' + i] = {
        type: 'box',
        xMin: new Date(z.lifecycle.box_start).getTime(),
        xMax: new Date(z.lifecycle.box_end).getTime(),
        backgroundColor: 'rgba(155, 89, 182, 0.08)',
        borderColor: 'rgba(155, 89, 182, 0.55)',
        borderWidth: 1,
        borderDash: [3, 3],
        label: { display: true, content: 'LC', position: 'start', color: '#9B59B6', font: { size: 9 }, backgroundColor: 'transparent' }
      };
    }
  });

  // 전체 데이터를 항상 전달 — 토글은 dataset.hidden 으로 제어
  const nasdaqWeekly = toWeekly(NASDAQ_RAW);
  const sp500Weekly = toWeekly(SP500_RAW);
  const kosdaqWeekly = toWeekly(KOSDAQ_RAW);

  // 미국 박스는 US_MARKET_CYCLES 기반 — nasdaq/sp500 공통이므로 한 번만 호출
  const usAnn = buildAllCyclesIndexAnn('nasdaq', 'v1');
  const krAnn = Object.assign({}, buildAllCyclesIndexAnn('kospi',  'v1'), buildAllCyclesIndexAnn('kosdaq', 'v1'));
  const usIndexCh = makeIndexChart('v1-us-price', nasdaqWeekly, sp500Weekly, v1Scale, 'v1', 'us-price', usAnn);
  const priceCh = makeIndexChart('v1-price', kospiWeekly, kosdaqWeekly, v1Scale, 'v1', 'price', krAnn);
  const stockCh = makePriceChart('v1-stock', stockWeekly, stock.name, color, zoneAnn, v1Scale, 'v1', 'stock');
  const volCh = makeVolumeChart('v1-volume', stockWeekly, 'v1');

  chartRegistry.v1 = [usIndexCh, priceCh, stockCh, volCh];

  // === 합집합 X축 padding — 4 패널 시점 sync (한국 영업일 ∪ 미국 영업일) ===
  const _v1UnionXSet = new Set();
  kospiWeekly.forEach(d => _v1UnionXSet.add(d.x));
  nasdaqWeekly.forEach(d => _v1UnionXSet.add(d.x));
  const _v1UnionX = Array.from(_v1UnionXSet).sort((a, b) => a - b);
  const _v1GhostData = _v1UnionX.map(t => ({ x: t, y: null }));
  [usIndexCh, priceCh, stockCh, volCh].forEach(ch => {
    ch.data.datasets.push({
      label: '_xunion', data: _v1GhostData,
      borderColor: 'transparent', backgroundColor: 'transparent',
      pointRadius: 0, fill: false, _xunion: true,
      yAxisID: ch.options.scales.y ? 'y' : undefined,
      order: 999
    });
    ch.update('none');
  });

  // x-축 정렬: 4개 패널 모두 동일 구간 강제
  const allDataArrays = [nasdaqWeekly, sp500Weekly, kospiWeekly, kosdaqWeekly, stockWeekly].filter(a => a.length);
  if (allDataArrays.length > 0) {
    const xMinMs = Math.min(...allDataArrays.map(a => a[0].x));
    const xMaxMs = Math.max(...allDataArrays.map(a => a[a.length-1].x));
    [usIndexCh, priceCh, stockCh, volCh].forEach(ch => {
      ch.options.scales.x.min = xMinMs;
      ch.options.scales.x.max = xMaxMs;
      ch.update('none');
    });
  }

  // Legend
  let legendHTML = '<div class="legend-item"><div class="legend-dot" style="background:#ffa500"></div>NASDAQ</div>';
  legendHTML += '<div class="legend-item"><div class="legend-dot" style="background:#00aa44"></div>S&P500</div>';
  legendHTML += '<div class="legend-item"><div class="legend-dot" style="background:#F39C12"></div>KOSPI</div>';
  legendHTML += '<div class="legend-item"><div class="legend-dot" style="background:#4ECDC4"></div>KOSDAQ</div>';
  legendHTML += '<div class="legend-item"><div class="legend-dot" style="background:' + color + '"></div>' + stock.name + '</div>';
  ['5','10','20','60','120'].forEach(p => {
    legendHTML += '<div class="legend-item"><div class="legend-line" style="background:' + MA_COLORS['ma' + p] + '"></div>MA' + p + '</div>';
  });
  legendHTML += '<div class="legend-item"><div class="legend-line" style="background:' + VOL_UP + '"></div>거래대금 ▲</div>';
  legendHTML += '<div class="legend-item"><div class="legend-line" style="background:' + VOL_DN + '"></div>거래대금 ▼</div>';
  document.getElementById('v1-legend').innerHTML = legendHTML;

  attachZoomEvents(document.getElementById('v1-us-price'), () => usIndexCh, 'v1');
  attachZoomEvents(document.getElementById('v1-price'), () => priceCh, 'v1');
  attachZoomEvents(document.getElementById('v1-stock'), () => stockCh, 'v1');
  attachZoomEvents(document.getElementById('v1-volume'), () => volCh, 'v1');
}

// ===== 토글 함수 =====
function _setIndexVisibility(ch, indexId, visible) {
  // _indexId가 일치하는 모든 dataset (캔들 + MA5/10/20/60/120) 일괄 hide/show
  if (!ch) return;
  ch.data.datasets.forEach((ds, i) => {
    if (ds._indexId === indexId) {
      ds.hidden = !visible;
      if (typeof ch.setDatasetVisibility === 'function') {
        ch.setDatasetVisibility(i, visible);
      } else {
        const m = ch.getDatasetMeta(i);
        if (m) m.hidden = !visible;
      }
    }
  });
  ch.update('none');
}

function toggleUSIndex(view, index) {
  const btn = document.getElementById(view + '-us-' + index);
  const key = 'us_' + index;
  toggleStates[view][key] = !toggleStates[view][key];
  if (btn) btn.classList.toggle('active', toggleStates[view][key]);
  if (chartRegistry[view] && chartRegistry[view][0]) {
    _setIndexVisibility(chartRegistry[view][0], index, toggleStates[view][key]);
  }
}

function toggleKRIndex(view, index) {
  const btn = document.getElementById(view + '-kr-' + index);
  const key = 'kr_' + index;
  toggleStates[view][key] = !toggleStates[view][key];
  if (btn) btn.classList.toggle('active', toggleStates[view][key]);
  if (chartRegistry[view] && chartRegistry[view][1]) {
    _setIndexVisibility(chartRegistry[view][1], index, toggleStates[view][key]);
  }
}

// ===== VIEW 2 =====
let v2Scale = 'linear';
let v2Interval = 'daily';
let v2CurrentCycle = null;
let v2CurrentStock = null;
let v2Expanded = false;

function initV2() {
  const container = document.getElementById('v2-cycle-btns');
  const allBtn = document.createElement('button');
  allBtn.className = 'cycle-btn';
  allBtn.textContent = '전체 사이클';
  allBtn.style.fontWeight = '700';
  allBtn.onclick = () => selectAllCycles(allBtn);
  container.appendChild(allBtn);
  CYCLES.forEach(c => {
    const btn = document.createElement('button');
    btn.className = 'cycle-btn';
    btn.textContent = c.name;
    btn.onclick = () => selectCycle(c.id, btn);
    container.appendChild(btn);
  });
}

function selectCycle(cycleId, btn) {
  document.querySelectorAll('#v2-cycle-btns .cycle-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  _allSetMode(false);
  v2CurrentCycle = CYCLES.find(c => c.id === cycleId);
  v2Expanded = false;
  document.getElementById('v2-expand').classList.remove('active');

  const sb = document.getElementById('v2-stock-btns');
  sb.innerHTML = '';
  // 매매 구간 시작이 빠른 순 → 매매 구간 없는 종목은 뒤로 (원래 순서 유지)
  const _tz = (typeof TRADE_ZONES !== 'undefined' ? TRADE_ZONES : []).filter(t => t.cycleId === v2CurrentCycle.id);
  const _first = id => { const d = _tz.filter(t => t.stockId === id).map(t => t.start).sort(); return d.length ? d[0] : '9999'; };
  const _ordered = v2CurrentCycle.stocks.map((s, i) => [s, i]).sort((p, q) => (_first(p[0].id) < _first(q[0].id) ? -1 : _first(p[0].id) > _first(q[0].id) ? 1 : p[1] - q[1])).map(x => x[0]);
  _ordered.forEach((s, i) => {
    const color = stockColorMap[s.id];
    const b = document.createElement('button');
    b.className = 'stock-btn';
    b.style.setProperty('--sc', color);
    b.textContent = formatStockLabel(s);
    if (i === 0) { b.classList.add('on'); v2CurrentStock = s; }
    b.onclick = () => {
      document.querySelectorAll('#v2-stock-btns .stock-btn').forEach(x => x.classList.remove('on'));
      b.classList.add('on');
      v2CurrentStock = s;
      renderV2();
    };
    sb.appendChild(b);
  });
  if (_ordered.length > 0) v2CurrentStock = _ordered[0];
  renderV2();
}

function setV2Scale(scale) {
  v2Scale = scale;
  document.getElementById('v2-linear').classList.toggle('active', scale === 'linear');
  document.getElementById('v2-log').classList.toggle('active', scale === 'log');
  renderV2();
}
function setV2Interval(interval) {
  v2Interval = interval;
  document.getElementById('v2-daily').classList.toggle('active', interval === 'daily');
  document.getElementById('v2-weekly').classList.toggle('active', interval === 'weekly');
  renderV2();
}
function toggleExpand() {
  v2Expanded = !v2Expanded;
  document.getElementById('v2-expand').classList.toggle('active');
  renderV2();
}

// ===== 전체 사이클 (2026-11-04) — 지수 전체 + 주도주 모멘텀 구간만 연결 =====
let _allCharts = [], _allX = null;
function _allSetMode(on) {
  const v = document.getElementById('view-v2');
  document.getElementById('v2-all').style.display = on ? '' : 'none';
  document.getElementById('v2-main').style.display = on ? 'none' : '';
  const sb = document.getElementById('v2-stock-btns'); if (sb) sb.parentElement.style.display = on ? 'none' : '';
  v.querySelectorAll('.ctrl-row').forEach(r => r.style.display = on ? 'none' : '');
}
function _allTs(d) { d = String(d).replace(/-/g, ''); return Date.UTC(+d.slice(0, 4), +d.slice(4, 6) - 1, +d.slice(6, 8)); }
function _allWeekly(raw, a, b) {
  const o = []; let lk = null;
  (raw || []).forEach(r => {
    const t = _allTs(r[0]); if ((a && t < a) || (b && t > b) || !r[4]) return;
    const wk = Math.floor((t / 864e5 + 3) / 7);
    if (wk === lk) o[o.length - 1] = { x: t, y: r[4] }; else o.push({ x: t, y: r[4] });
    lk = wk;
  });
  return o;
}
function _allApplyX(min, max) {
  _allX = (min == null) ? null : [min, max];
  _allCharts.forEach(c => { c.options.scales.x.min = min == null ? c.$x0 : min; c.options.scales.x.max = max == null ? c.$x1 : max; c.update('none'); });
}
function _allResetZoom() { _allApplyX(null, null); }
function _allBindZoom(chart) {
  const cv = chart.canvas, wrap = cv.parentElement;
  let sel = wrap.querySelector('.v2all-sel');
  if (!sel) { sel = document.createElement('div'); sel.className = 'v2all-sel'; wrap.appendChild(sel); }
  let x0 = null;
  const px = e => e.clientX - cv.getBoundingClientRect().left;
  cv.onmousedown = e => { x0 = px(e); sel.style.left = (cv.offsetLeft + x0) + 'px'; sel.style.width = '0px'; sel.style.display = 'block'; };
  cv.onmousemove = e => { if (x0 == null) return; const x = px(e); sel.style.left = (cv.offsetLeft + Math.min(x0, x)) + 'px'; sel.style.width = Math.abs(x - x0) + 'px'; };
  const end = e => {
    if (x0 == null) return; sel.style.display = 'none';
    const x = px(e), sc = chart.scales.x;
    if (Math.abs(x - x0) > 6) { const a = sc.getValueForPixel(Math.min(x0, x)), b = sc.getValueForPixel(Math.max(x0, x)); _allApplyX(a, b); }
    x0 = null;
  };
  cv.onmouseup = end; cv.onmouseleave = e => { if (x0 != null) { sel.style.display = 'none'; x0 = null; } };
  cv.ondblclick = () => _allResetZoom();
  cv.onwheel = e => {
    e.preventDefault();
    const sc = chart.scales.x, c = sc.getValueForPixel(px(e)), lo = sc.min, hi = sc.max, f = e.deltaY > 0 ? 1.25 : 0.8;
    let a = c - (c - lo) * f, b = c + (hi - c) * f;
    if (a <= chart.$x0 && b >= chart.$x1) { _allResetZoom(); return; }
    _allApplyX(Math.max(a, chart.$x0), Math.min(b, chart.$x1));
  };
}
function _allMerge(zones) {
  const w = [];
  zones.forEach(z => { const l = w[w.length - 1]; if (l && z.a <= l.b) { l.b = Math.max(l.b, z.b); l.n.push(z.name); } else w.push({ a: z.a, b: z.b, n: [z.name] }); });
  w.forEach(x => x.days = Math.round((x.b - x.a) / 864e5));
  return w;
}
let _allUp = true, _allTr = true;
function _allToggle(k) {
  if (k === 'up') _allUp = !_allUp; else _allTr = !_allTr;
  if (!_allUp && !_allTr) { if (k === 'up') _allTr = true; else _allUp = true; }
  const btn = document.querySelector('#v2-cycle-btns .cycle-btn'); if (btn) selectAllCycles(btn);
}
function selectAllCycles(btn) {
  document.querySelectorAll('#v2-cycle-btns .cycle-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  _allSetMode(true);
  const keepX = _allX;
  _allCharts.forEach(c => c.destroy()); _allCharts = [];
  ['up', 'tr'].forEach(k => { const e = document.getElementById('v2all-t-' + k); if (e) e.classList.toggle('active', k === 'up' ? _allUp : _allTr); });
  const X0 = Date.UTC(1985, 0, 1), X1 = Date.now() + 120 * 864e5;
  const nameOf = id => ((UNIQUE_STOCKS.find(u => u.id === id) || {}).name) || id;
  const colOf = id => (typeof stockColorMap !== 'undefined' && stockColorMap[id]) || '#c9d1d9';
  const zones = STOCK_ZONES.filter(z => z.longterm && z.longterm.start && z.longterm.end && STOCKS_RAW[z.stockId])
    .map(z => ({ id: z.stockId, label: z.label || z.stockId, a: _allTs(z.longterm.start), b: _allTs(z.longterm.end), color: colOf(z.stockId), name: nameOf(z.stockId) }))
    .sort((p, q) => p.a - q.a);
  zones.forEach(z => z.days = Math.round((z.b - z.a) / 864e5));
  const trades = (typeof TRADE_ZONES !== 'undefined' ? TRADE_ZONES : []).filter(t => STOCKS_RAW[t.stockId])
    .map(t => ({ id: t.stockId, label: nameOf(t.stockId) + ' 매매', a: _allTs(t.start), b: _allTs(t.end), color: colOf(t.stockId), name: nameOf(t.stockId) }))
    .sort((p, q) => p.a - q.a);
  trades.forEach(t => t.days = Math.round((t.b - t.a) / 864e5));
  const avg = a => a.length ? Math.round(a.reduce((s, v) => s + v, 0) / a.length) : 0;
  const med = a => { if (!a.length) return 0; const s = a.slice().sort((p, q) => p - q); return s[Math.floor(s.length / 2)]; };
  const yr = d => (d / 365).toFixed(1) + '년';
  const stat = (list, title, extra) => {
    const w = _allMerge(list.map(z => Object.assign({}, z))); if (!w.length) return { w: [], g: [], html: '' };
    const g = []; for (let i = 1; i < w.length; i++) g.push(Math.round((w[i].a - w[i - 1].b) / 864e5));
    const tot = w.reduce((s, x) => s + x.days, 0), span = Math.max(1, Math.round((w[w.length - 1].b - w[0].a) / 864e5));
    return { w, g, html: '<b>[' + title + ']</b> ' + extra + ' → 합친 구간 <b>' + w.length + '개</b> · 1회 평균 <b>' + avg(w.map(x => x.days)) + '일</b>(중앙값 ' + med(w.map(x => x.days)) + '일) · '
      + '다음까지 대기 평균 <b>' + avg(g) + '일</b>(' + yr(avg(g)) + ', 중앙값 ' + med(g) + '일, 최장 ' + (g.length ? Math.max.apply(null, g) : 0) + '일) · '
      + new Date(w[0].a).getUTCFullYear() + '~' + new Date(w[w.length - 1].b).getUTCFullYear() + ' 중 ' + Math.round(tot / span * 100) + '%' };
  };
  const lastT = trades.length ? new Date(trades[trades.length - 1].b).toISOString().slice(0, 7) : '-';
  const sU = stat(zones, '상승 구간', '주도주 장기 구간 ' + zones.length + '개');
  const sT = stat(trades, '매매 구간', 'BT 정리 ' + trades.length + '건(~' + lastT + ' 입력)');
  document.getElementById('v2all-stats').innerHTML = [_allUp ? sU.html : '', _allTr ? sT.html : ''].filter(Boolean).join('<br>');
  const boxes = {};
  if (_allUp) zones.forEach((z, i) => { boxes['z' + i] = { type: 'box', xMin: z.a, xMax: z.b, backgroundColor: z.color + '1f', borderWidth: 0 }; });
  if (_allTr) trades.forEach((t, i) => { boxes['tz' + i] = { type: 'box', xMin: t.a, xMax: t.b, backgroundColor: 'rgba(46,160,67,0.22)', borderColor: 'rgba(63,185,80,0.7)', borderWidth: 1 }; });
  const xs = () => ({ type: 'time', min: X0, max: X1, time: { unit: 'year', displayFormats: { year: 'yy', month: 'yy.MM' } },
               ticks: { color: '#8b949e', font: { size: 9 }, maxRotation: 0, autoSkip: true, maxTicksLimit: 44 }, grid: { color: '#21262d' } });
  const ys = (cb) => ({ type: 'logarithmic', ticks: { color: '#8b949e', font: { size: 9 }, maxTicksLimit: 5, callback: cb }, grid: { color: '#21262d' } });
  const base = (ann, tip) => ({ responsive: true, maintainAspectRatio: false, animation: false, parsing: false,
    interaction: { mode: 'nearest', axis: 'x', intersect: false },
    plugins: { legend: { display: false }, annotation: { annotations: ann },
               tooltip: { callbacks: { title: it => new Date(it[0].parsed.x).toISOString().slice(0, 10), label: tip } } } });
  const fmt = v => Number(v).toLocaleString();
  const mk = (id, cfg) => { const el = document.getElementById(id); if (!el) return; const c = new Chart(el.getContext('2d'), cfg); c.$x0 = X0; c.$x1 = X1; _allCharts.push(c); _allBindZoom(c); };
  [['v2all-nasdaq', NASDAQ_RAW, '#58a6ff'], ['v2all-kospi', KOSPI_RAW, '#f0883e'], ['v2all-kosdaq', KOSDAQ_RAW, '#a371f7']].forEach(([id, raw, col]) => {
    const opt = base(Object.assign({}, boxes), it => fmt(Math.round(it.parsed.y)));
    opt.scales = { x: xs(), y: ys(v => fmt(v)) };
    mk(id, { type: 'line', data: { datasets: [{ data: _allWeekly(raw), borderColor: col, borderWidth: 1, pointRadius: 0, tension: 0 }] }, options: opt });
  });
  const ds = [], labs = {};
  const segs = _allUp ? zones : trades;
  segs.forEach((z, i) => {
    const w = _allWeekly(STOCKS_RAW[z.id], z.a, z.b); if (!w.length) return;
    const b0 = w[0].y;
    ds.push({ label: z.label + ' (' + z.days + '일)', data: w.map(p => ({ x: p.x, y: p.y / b0 * 100 })), borderColor: z.color, borderWidth: 1.4, pointRadius: 0, tension: 0 });
    labs['l' + i] = { type: 'label', xValue: z.a, yValue: 100, content: z.name + '(' + z.days + '일)', color: z.color, font: { size: 9, weight: '600' },
                      position: { x: 'start', y: 'end' }, yAdjust: -6 - (i % 3) * 11, backgroundColor: 'rgba(13,17,23,0.65)', padding: 1 };
  });
  const tb = {};
  if (_allTr && _allUp) trades.forEach((t, i) => { tb['tl' + i] = { type: 'label', xValue: (t.a + t.b) / 2, yAdjust: 0, yValue: 100, content: '매매 ' + t.days + '일',
      color: '#e6edf3', font: { size: 9, weight: '600' }, backgroundColor: 'rgba(26,127,55,0.85)', padding: 2, position: { x: 'center', y: 'start' } }; });
  const opt = base(Object.assign({}, boxes, tb, labs), it => it.dataset.label + ' ' + (it.parsed.y / 100).toFixed(2) + '배');
  opt.scales = { x: xs(), y: ys(v => (Number(v) / 100).toFixed(Number(v) < 100 ? 1 : 0) + '배') };
  mk('v2all-stock', { type: 'line', data: { datasets: ds }, options: opt });
  const wa = {};
  const row = (s, key, y0, y1, fill, line, show) => {
    if (!show) return;
    s.w.forEach((w, i) => {
      wa[key + i] = { type: 'box', xMin: w.a, xMax: w.b, yMin: y0, yMax: y1, backgroundColor: fill, borderColor: line, borderWidth: 1,
                      label: { display: true, content: w.days + '일', color: '#e6edf3', font: { size: 9 }, position: 'center' } };
      if (i) { const p = s.w[i - 1];
        wa[key + 'g' + i] = { type: 'box', xMin: p.b, xMax: w.a, yMin: y0 + (y1 - y0) * 0.3, yMax: y1 - (y1 - y0) * 0.3, backgroundColor: 'rgba(227,179,65,0.16)', borderWidth: 0,
                              label: { display: true, content: '대기 ' + s.g[i - 1] + '일', color: '#e3b341', font: { size: 9 }, position: 'center' } }; }
    });
  };
  const both = _allUp && _allTr;
  row(sU, 'u', both ? 0.53 : 0.15, both ? 0.95 : 0.85, 'rgba(56,139,253,0.45)', '#58a6ff', _allUp);
  row(sT, 't', both ? 0.05 : 0.15, both ? 0.47 : 0.85, 'rgba(63,185,80,0.55)', '#3fb950', _allTr);
  const wopt = base(wa, () => '');
  wopt.plugins.tooltip = { enabled: false };
  wopt.scales = { x: xs(), y: { min: 0, max: 1, display: false } };
  mk('v2all-win', { type: 'line', data: { datasets: [{ data: [{ x: X0, y: null }, { x: X1, y: null }], pointRadius: 0 }] }, options: wopt });
  if (keepX) _allApplyX(keepX[0], keepX[1]);
}

function renderV2() {
  if (!v2CurrentCycle || !v2CurrentStock) return;
  destroyView('v2');
  zoomStates.v2 = { zoomed: false };
  document.getElementById('v2-zoom').style.display = 'none';

  const cycle = v2CurrentCycle;
  const stock = v2CurrentStock;
  const color = stockColorMap[stock.id];
  const stockRaw = STOCKS_RAW[stock.id];
  const stockMeta = META[stock.id];
  if (!stockRaw) return;

  let rangeStart, rangeEnd;
  if (v2Expanded && stockMeta) {
    rangeStart = stockMeta.start;
    const endD = new Date(cycle.end); endD.setFullYear(endD.getFullYear() + 2);
    rangeEnd = endD.toISOString().slice(0,10);
  } else {
    const startD = new Date(cycle.start); startD.setFullYear(startD.getFullYear() - 2);
    rangeStart = startD.toISOString().slice(0,10);
    const endD = new Date(cycle.end); endD.setFullYear(endD.getFullYear() + 2);
    rangeEnd = endD.toISOString().slice(0,10);
  }

  const kospiF = filterByDate(KOSPI_RAW, rangeStart, rangeEnd);
  const kosdaqF = filterByDate(KOSDAQ_RAW, rangeStart, rangeEnd);
  const nasdaqF = filterByDate(NASDAQ_RAW, rangeStart, rangeEnd);
  const sp500F = filterByDate(SP500_RAW, rangeStart, rangeEnd);
  const stockF = filterByDate(stockRaw, rangeStart, rangeEnd);

  // 전체 데이터를 항상 전달 — 토글은 dataset.hidden 으로 제어
  const nasdaqProc = v2Interval === 'weekly' ? toWeekly(nasdaqF) : toDaily(nasdaqF);
  const sp500Proc = v2Interval === 'weekly' ? toWeekly(sp500F) : toDaily(sp500F);
  const kospiProc = v2Interval === 'weekly' ? toWeekly(kospiF) : toDaily(kospiF);
  const kosdaqProc = v2Interval === 'weekly' ? toWeekly(kosdaqF) : toDaily(kosdaqF);
  const stockProc = v2Interval === 'weekly' ? toWeekly(stockF) : toDaily(stockF);

  document.getElementById('v2-title').textContent = cycle.name + ' — ' + stock.name;
  const expandLabel = v2Expanded ? ('상장일(' + (stockMeta ? stockMeta.start : '?') + ')부터') : '사이클 ±2년';
  document.getElementById('v2-meta').textContent =
    '사이클 구간: ' + cycle.start + ' ~ ' + cycle.end + ' | ' + expandLabel + ' | ' +
    (v2Interval === 'daily' ? '일봉' : '주봉') + ' | ' + (v2Scale === 'log' ? '로그' : '리니어');
  document.getElementById('v2-stock-label').textContent = stock.name;

  // Cycle zone annotation (KOSPI 자동 탐지: 3-Step Cascade + 2단계 휩쏘)
  // status 종료 = 실선, 조정중/진행중 = 점선
  const cycClosed = cycle.status === '종료';
  const cycLabel = cycle.name + (cycle.status ? ' [' + cycle.status + ']' : '');
  const ann = {
    cycleZone: {
      type: 'box',
      xMin: new Date(cycle.start).getTime(), xMax: new Date(cycle.end).getTime(),
      backgroundColor: 'rgba(40, 53, 147, 0.07)',
      borderColor: 'rgba(40, 53, 147, 0.75)', borderWidth: 1,
      borderDash: cycClosed ? undefined : [4, 4],
      label: { display: true, content: cycLabel, position: 'start', color: '#283593', font: { size: 10, weight: 'bold' } }
    }
  };
  const stockAnn = {};
  // Outer 중장기 박스 — 지수 사이클 박스와 동일 인디고 톤 (시각 언어 통일)
  if (stock.longterm && stock.longterm.start && stock.longterm.end) {
    const lt = stock.longterm;
    const closed = lt.status === '종료';
    stockAnn.longtermZone = {
      type: 'box',
      xMin: new Date(lt.start).getTime(), xMax: new Date(lt.end).getTime(),
      backgroundColor: 'rgba(40, 53, 147, 0.07)',
      borderColor: 'rgba(40, 53, 147, 0.75)',
      borderWidth: 1,
      borderDash: closed ? undefined : [6, 4],
      label: { display: true, content: fmtStockLabel(stock.era, stock.name) + ' [' + lt.status + ']', position: 'end', color: '#283593', font: { size: 11, weight: 'bold' }, backgroundColor: 'transparent' }
    };
  }
  // Lifecycle box (관성~전고점 트라이)
  if (false && stock.lifecycle && stock.lifecycle.box_start && stock.lifecycle.box_end) {  // 2026-11-04 Lifecycle·F·전고점 트라이 제거
    const lc = stock.lifecycle;
    stockAnn.lifecycleZone = {
      type: 'box',
      xMin: new Date(lc.box_start).getTime(), xMax: new Date(lc.box_end).getTime(),
      backgroundColor: 'rgba(155, 89, 182, 0.08)', borderColor: 'rgba(155, 89, 182, 0.55)',
      borderWidth: 1, borderDash: [3, 3],
      label: { display: true, content: 'Lifecycle', position: 'start', color: '#9B59B6', font: { size: 9 }, backgroundColor: 'transparent' }
    };
    // F marker
    if (lc.F) {
      stockAnn.lifecycleF = {
        type: 'line', scaleID: 'x',
        value: new Date(lc.F).getTime(),
        borderColor: 'rgba(231, 76, 60, 0.55)', borderWidth: 1, borderDash: [2, 2],
        label: { display: true, content: 'F', position: 'start', color: '#E74C3C', font: { size: 9, weight: 'bold' }, backgroundColor: 'transparent', yAdjust: 10 }
      };
    }
    // peak_try marker
    if (lc.peak_try) {
      stockAnn.lifecyclePT = {
        type: 'line', scaleID: 'x',
        value: new Date(lc.peak_try).getTime(),
        borderColor: 'rgba(155, 89, 182, 0.55)', borderWidth: 1, borderDash: [2, 2],
        label: { display: true, content: '전고점 트라이', position: 'start', color: '#9B59B6', font: { size: 9, weight: 'bold' }, backgroundColor: 'transparent', yAdjust: 25 }
      };
    }
  }

  // 미국 박스: US_MARKET_CYCLES 와 cycle 의 ±2년 윈도우 overlap 사이클들 — 한 번 호출
  const usAnn = buildCycleIndexAnn(cycle, 'nasdaq', 'v2');
  // 한국 박스: KOSPI/KOSDAQ 각각의 indexZones 별도
  const krAnn = Object.assign({}, buildCycleIndexAnn(cycle, 'kospi', 'v2'));
  const _kqAnn = buildCycleIndexAnn(cycle, 'kosdaq', 'v2');
  if (_kqAnn.cycleZoneIdx) krAnn.cycleZoneIdxKq = _kqAnn.cycleZoneIdx;
  const usIndexCh = makeIndexChart('v2-us-price', nasdaqProc, sp500Proc, v2Scale, 'v2', 'us-price', usAnn);
  const priceCh = makeIndexChart('v2-price', kospiProc, kosdaqProc, v2Scale, 'v2', 'price', krAnn);
  // 매매 구간 (BT 정리) — 진한 초록 박스
  (typeof TRADE_ZONES !== 'undefined' ? TRADE_ZONES : []).filter(t => t.stockId === stock.id && t.cycleId === cycle.id).forEach((t, i) => {
    const a = new Date(t.start).getTime(), b = new Date(t.end).getTime();
    stockAnn['trade' + i] = { type: 'box', xMin: a, xMax: b, backgroundColor: 'rgba(46, 160, 67, 0.28)', borderColor: 'rgba(46, 160, 67, 0.95)', borderWidth: 1.5,
      label: { display: true, content: '매매 ' + Math.round((b - a) / 864e5) + '일', position: { x: 'center', y: 'start' }, color: '#1a7f37', font: { size: 10, weight: 'bold' }, backgroundColor: 'rgba(255,255,255,0.75)' } };
  });
  const stockCh = makePriceChart('v2-stock', stockProc, stock.name, color, stockAnn, v2Scale, 'v2', 'stock');
  const volCh = makeVolumeChart('v2-volume', stockProc, 'v2');
  chartRegistry.v2 = [usIndexCh, priceCh, stockCh, volCh];

  // === 합집합 X축 padding — 4 패널 시점 sync (한국 영업일 ∪ 미국 영업일) ===
  // chart.js timeseries 는 모든 dataset 의 X 값 union 을 X축 카테고리로 사용.
  // ghost dataset 을 모든 패널에 동일하게 주입하면 4 패널이 같은 X 시퀀스를 가짐.
  const _unionXSet = new Set();
  kospiProc.forEach(d => _unionXSet.add(d.x));
  nasdaqProc.forEach(d => _unionXSet.add(d.x));
  const unionX = Array.from(_unionXSet).sort((a, b) => a - b);
  const ghostData = unionX.map(t => ({ x: t, y: null }));
  [usIndexCh, priceCh, stockCh, volCh].forEach(ch => {
    ch.data.datasets.push({
      label: '_xunion', data: ghostData,
      borderColor: 'transparent', backgroundColor: 'transparent',
      pointRadius: 0, fill: false, _xunion: true,
      yAxisID: ch.options.scales.y ? 'y' : undefined,
      order: 999
    });
    ch.update('none');
  });

  // x-축 정렬: 4개 패널 모두 동일한 [rangeStart, rangeEnd]로 강제
  const xMinMs = new Date(rangeStart).getTime();
  const xMaxMs = new Date(rangeEnd).getTime();
  [usIndexCh, priceCh, stockCh, volCh].forEach(ch => {
    ch.options.scales.x.min = xMinMs;
    ch.options.scales.x.max = xMaxMs;
    ch.update('none');
  });

  // Legend
  let lg = '<div class="legend-item"><div class="legend-dot" style="background:#ffa500"></div>NASDAQ</div>';
  lg += '<div class="legend-item"><div class="legend-dot" style="background:#00aa44"></div>S&P500</div>';
  lg += '<div class="legend-item"><div class="legend-dot" style="background:#F39C12"></div>KOSPI</div>';
  lg += '<div class="legend-item"><div class="legend-dot" style="background:#4ECDC4"></div>KOSDAQ</div>';
  lg += '<div class="legend-item"><div class="legend-dot" style="background:' + color + '"></div>' + stock.name + '</div>';
  ['5','10','20','60','120'].forEach(p => {
    lg += '<div class="legend-item"><div class="legend-line" style="background:' + MA_COLORS['ma' + p] + '"></div>MA' + p + '</div>';
  });
  lg += '<div class="legend-item"><div class="legend-line" style="background:' + VOL_UP + '"></div>거래대금 ▲</div>';
  lg += '<div class="legend-item"><div class="legend-line" style="background:' + VOL_DN + '"></div>거래대금 ▼</div>';
  document.getElementById('v2-legend').innerHTML = lg;

  attachZoomEvents(document.getElementById('v2-us-price'), () => usIndexCh, 'v2');
  attachZoomEvents(document.getElementById('v2-price'), () => priceCh, 'v2');
  attachZoomEvents(document.getElementById('v2-stock'), () => stockCh, 'v2');
  attachZoomEvents(document.getElementById('v2-volume'), () => volCh, 'v2');
}

// ===== TAB SWITCHING =====
function switchView(evt, viewId) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.view-panel').forEach(p => p.classList.remove('active'));
  document.getElementById('view-' + viewId).classList.add('active');
  evt.target.classList.add('active');
  if (viewId === 'vtype') renderSecType();
  if (viewId === 'vterm') renderSecTerm();
}

// ===== 산업 사이클 매트릭스 (SECTOR_VIEW_V1, 2026-11-03) =====
const SEC_TERM_ORDER = ['장기', '중기', '단기', '1회'];
const SEC_TERM_COLOR = { '장기': '#7986cb', '중기': '#4db6ac', '단기': '#ffb74d', '1회': '#a1887f' };
const SEC_TYPE_COLOR = { '재가동형': '#58a6ff', '개척형': '#3fb950' };
const SEC_TERM_DESC = { '장기': '14~30년', '중기': '4~8년', '단기': '2~5년', '1회': '한 번' };
const SEC_X_MIN = new Date('1985-01-01').getTime(), SEC_X_MAX = new Date('2027-06-30').getTime();
const secRendered = {};
function _secDate(ym, endOfMonth) {
  const p = ym.split('-').map(Number);
  return endOfMonth ? new Date(p[0], p[1], 0).getTime() : new Date(p[0], p[1] - 1, 1).getTime();
}
function _secGapText(sp) {
  const st = sp.cycles.map(c => Number(c.start.slice(0, 4)) + (Number(c.start.slice(5, 7)) - 1) / 12);
  if (st.length < 2) return sp.cycles.length + '회';
  const g = [];
  for (let i = 1; i < st.length; i++) g.push(Math.round(st[i] - st[i - 1]));
  return '간격 ' + g.join(' / ') + '년';
}
function _secCard(sp, canvasId, big) {
  const col = SEC_TERM_COLOR[sp.term] || '#8b949e', tcol = SEC_TYPE_COLOR[sp.type] || '#8b949e';
  const starts = sp.cycles.map(c => c.start.slice(0, 4)).join(' · ');
  const hasM = sp.mcap && sp.mcap.length;
  const body = (hasM || (sp.series && sp.series.length)) ? '<div class="sec-canvas' + (big ? ' big' : '') + '"><canvas id="' + canvasId + '"></canvas></div>'
                                               : '<div class="sec-empty">데이터 준비 중</div>';
  return '<div class="sec-card"><div class="sec-head"><span class="sec-name">' + sp.sector + '</span>'
    + '<span class="sec-stock" title="' + (sp.members || []).join(', ') + '">' + (hasM ? '시총 합산 ' + (sp.members || []).length + '종목' : sp.name) + '</span>'
    + '<span class="sec-tag" style="color:' + tcol + ';border-color:' + tcol + '66">' + sp.type + '</span>'
    + '<span class="sec-tag" style="color:' + col + ';border-color:' + col + '66">' + sp.term + '</span></div>'
    + '<div class="sec-gap">업사이클 시작 ' + starts + ' · ' + _secGapText(sp) + '</div>'
    + body + (sp.note ? '<div class="sec-note">' + sp.note + '</div>' : '') + '</div>';
}
function _secChart(sp, canvasId) {
  const el = document.getElementById(canvasId);
  if (!el) return;
  const _ts = d => new Date(d.slice(0, 4) + '-' + d.slice(4, 6) + '-' + d.slice(6, 8)).getTime();
  const hasM = sp.mcap && sp.mcap.length;
  const _gap = arr => { const o = []; arr.forEach((p, i) => { if (i && p.x - arr[i - 1].x > 75 * 864e5) o.push({ x: p.x - 864e5, y: null }); o.push(p); }); return o; };
  const data = hasM ? _gap(sp.mcap.map(r => ({ x: _ts(r[0]), y: r[1] / 10000 })))
                    : (sp.series || []).map(r => ({ x: _ts(r[0]), y: r[1] }));
  const share = hasM ? _gap(sp.mcap.map(r => ({ x: _ts(r[0]), y: r[2] }))) : [];
  const col = SEC_TERM_COLOR[sp.term] || '#8b949e';
  const lastX = data.length ? data[data.length - 1].x : SEC_X_MAX;
  const ann = {};
  sp.cycles.forEach((c, i) => {
    const open = !c.end;
    ann['b' + i] = {
      type: 'box', xMin: _secDate(c.start, false), xMax: open ? lastX : _secDate(c.end, true),
      backgroundColor: col + '30', borderColor: col + 'b0', borderWidth: 1, borderDash: open ? [4, 3] : undefined,
      label: { display: true, content: "'" + c.start.slice(2, 4) + (c.label ? ' ' + c.label : ''), position: { x: 'start', y: 'start' },
               yAdjust: (i % 2) * 14, color: '#e6edf3', font: { size: 10 }, padding: 2, backgroundColor: 'rgba(13,17,23,0.55)' }
    };
  });
  new Chart(el.getContext('2d'), {
    type: 'line',
    data: { datasets: hasM ? [
        { label: '섹터 시총(조원, 좌)', data, yAxisID: 'y', borderColor: '#c9d1d9', borderWidth: 1.2, pointRadius: 0, tension: 0, spanGaps: false },
        { label: '시장 비중(%, 우)', data: share, yAxisID: 'y2', borderColor: '#f0883e', borderWidth: 1, borderDash: [3, 2], pointRadius: 0, tension: 0, spanGaps: false }
      ] : [{ data, borderColor: '#c9d1d9', borderWidth: 1, pointRadius: 0, tension: 0 }] },
    options: {
      responsive: true, maintainAspectRatio: false, animation: false, parsing: false,
      interaction: { mode: 'nearest', axis: 'x', intersect: false },
      plugins: {
        legend: { display: !!hasM, position: 'top', align: 'end', labels: { color: '#8b949e', font: { size: 9 }, boxWidth: 10, boxHeight: 2, padding: 6 } },
        tooltip: { callbacks: { title: items => new Date(items[0].parsed.x).toISOString().slice(0, 10),
          label: it => hasM ? (it.dataset.yAxisID === 'y2' ? '시장 비중 ' + it.parsed.y.toFixed(2) + '%' : '섹터 시총 ' + it.parsed.y.toLocaleString(undefined, { maximumFractionDigits: 1 }) + '조원')
                            : Math.round(it.parsed.y).toLocaleString() } },
        annotation: { annotations: ann }
      },
      scales: {
        x: { type: 'time', min: SEC_X_MIN, max: SEC_X_MAX, time: { unit: 'year', displayFormats: { year: 'yy' } },
             ticks: { color: '#6e7681', font: { size: 9 }, maxRotation: 0, autoSkip: true, maxTicksLimit: 22 }, grid: { color: '#21262d' } },
        y: { type: 'logarithmic', position: 'left', ticks: { color: '#6e7681', font: { size: 9 }, maxTicksLimit: 4,
             callback: v => { const n = Number(v); if (hasM) return (n >= 10 ? Math.round(n) : n.toFixed(1)) + '조'; return n >= 10000 ? Math.round(n / 10000) + '만' : n.toLocaleString(); } },
             grid: { color: '#21262d' } },
        y2: { display: !!hasM, type: 'linear', position: 'right', min: 0, ticks: { color: '#f0883e', font: { size: 9 }, maxTicksLimit: 4, callback: v => Number(v).toFixed(0) + '%' },
              grid: { drawOnChartArea: false } }
      }
    }
  });
}
function renderSecType() {
  if (secRendered.type) return;
  secRendered.type = true;
  const host = document.getElementById('sec-type');
  host.style.gridTemplateColumns = 'repeat(4, 1fr)';
  const cols = [
    ['재가동형', '장기', SEC_TYPE_COLOR['재가동형'], '재가동형 · 장기', SEC_TERM_DESC['장기']],
    ['재가동형', '중기', SEC_TYPE_COLOR['재가동형'], '재가동형 · 중기', SEC_TERM_DESC['중기']],
    ['재가동형', '단기', SEC_TYPE_COLOR['재가동형'], '재가동형 · 단기', SEC_TERM_DESC['단기']],
    ['개척형', null, SEC_TYPE_COLOR['개척형'], '개척형', '처음부터 공급이 거의 없던 산업'],
  ];
  let html = '';
  const plan = [];
  cols.forEach(([t, tm, color, title, desc]) => {
    html += '<div class="sec-col"><h3 style="color:' + color + '">' + title + '<span class="sub">' + desc + '</span></h3>';
    SECTOR_CYCLES.forEach((s, i) => {
      if (s.type !== t || (tm && s.term !== tm)) return;
      const id = 'secc_type_' + i; html += _secCard(s, id); plan.push([s, id]);
    });
    html += '</div>';
  });
  host.innerHTML = html;
  plan.forEach(([s, id]) => _secChart(s, id));
  _secBindModal(host, 'secc_type_');
}
function _secBindModal(host, prefix) {
  host.querySelectorAll('.sec-card').forEach(card => {
    const cv = card.querySelector('canvas');
    if (!cv) return;
    const idx = Number(cv.id.replace(prefix, ''));
    card.addEventListener('click', () => openSecModal(idx));
  });
}
function renderSecTerm() {
  if (secRendered.term) return;
  secRendered.term = true;
  const host = document.getElementById('sec-term');
  host.style.gridTemplateColumns = 'repeat(4, 1fr)';
  let html = '';
  const plan = [];
  SEC_TERM_ORDER.forEach(tm => {
    html += '<div class="sec-col"><h3 style="color:' + SEC_TERM_COLOR[tm] + '">' + tm + '<span class="sub">' + SEC_TERM_DESC[tm] + '</span></h3>';
    SECTOR_CYCLES.forEach((s, i) => { if (s.term !== tm) return; const id = 'secc_term_' + i; html += _secCard(s, id); plan.push([s, id]); });
    html += '</div>';
  });
  host.innerHTML = html;
  plan.forEach(([s, id]) => _secChart(s, id));
  // 카드 클릭 → 화면 폭 전체 팝업으로 확대
  _secBindModal(host, 'secc_term_');
}

// ===== 섹터 카드 확대 팝업 =====
let _secModalChart = null;
function closeSecModal() {
  const m = document.getElementById('sec-modal');
  if (!m) return;
  m.classList.remove('open');
  if (_secModalChart) { _secModalChart.destroy(); _secModalChart = null; }
}
function openSecModal(idx) {
  const sp = SECTOR_CYCLES[idx];
  if (!sp) return;
  let m = document.getElementById('sec-modal');
  if (!m) {
    m = document.createElement('div');
    m.id = 'sec-modal';
    m.innerHTML = '<div class="sec-modal-box"><div class="sec-modal-top"><div id="sec-modal-head"></div>'
      + '<button class="sec-modal-x" onclick="closeSecModal()">닫기 ✕</button></div>'
      + '<div class="sec-modal-canvas"><canvas id="sec-modal-cv"></canvas></div><div class="sec-note" id="sec-modal-note"></div></div>';
    m.addEventListener('click', e => { if (e.target === m) closeSecModal(); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') closeSecModal(); });
    document.body.appendChild(m);
  }
  const col = SEC_TERM_COLOR[sp.term] || '#8b949e', tcol = SEC_TYPE_COLOR[sp.type] || '#8b949e';
  document.getElementById('sec-modal-head').innerHTML = '<span class="sec-name" style="font-size:16px">' + sp.sector + '</span> '
    + '<span class="sec-stock">' + ((sp.mcap && sp.mcap.length) ? '시총 합산: ' + (sp.members || []).join(', ') : sp.name) + '</span> '
    + '<span class="sec-tag" style="color:' + tcol + ';border-color:' + tcol + '66">' + sp.type + '</span> '
    + '<span class="sec-tag" style="color:' + col + ';border-color:' + col + '66">' + sp.term + '</span>'
    + '<div class="sec-gap">업사이클 시작 ' + sp.cycles.map(c => c.start.slice(0, 4)).join(' · ') + ' · ' + _secGapText(sp) + '</div>';
  document.getElementById('sec-modal-note').textContent = sp.note || '';
  m.classList.add('open');
  if (_secModalChart) { _secModalChart.destroy(); _secModalChart = null; }
  _secChart(sp, 'sec-modal-cv');
  _secModalChart = Chart.getChart('sec-modal-cv') || null;
}

// ===== INIT =====
initV1();
initV2();
{ const _b0 = document.querySelector('#v2-cycle-btns .cycle-btn'); if (_b0) selectAllCycles(_b0); }  // 첫 화면 = 주도주 · 전체 사이클
</script>
</body>
</html>"""

# ===== 5. WRITE OUTPUT =====
# --output <path>: override default output path (used by build_leading_stocks_update.py
# to generate a temp HTML for partial-patch refactor).
import argparse as _argparse
_p = _argparse.ArgumentParser(add_help=False)
_p.add_argument("--output", default=None)
_args, _ = _p.parse_known_args()

if _args.output:
    output_path = _args.output
    output_dir = os.path.dirname(output_path) or '.'
    if output_dir and not os.path.isdir(output_dir):
        os.makedirs(output_dir, exist_ok=True)
else:
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'mnt', 'Documents--3 시장 사이클 전략')
    if not os.path.isdir(output_dir):
        output_dir = os.path.dirname(__file__)
    output_path = os.path.join(output_dir, 'Leading_stocks.html')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

file_size = os.path.getsize(output_path)
print(f"Created: {output_path}")
print(f"Size: {file_size / 1024 / 1024:.1f} MB")
print(f"Stocks: {len(stocks_data)}, KOSPI: {len(kospi_data)} days")
print(f"LEADING_STOCKS entries: {len(LEADING_STOCKS)}, Cycles: {len(cycle_order)}, Unique stocks: {len(unique_stocks)}")
