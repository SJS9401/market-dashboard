"""
Multi-asset cycle 자산 레지스트리.

create_multiasset_data.py 가 이 모듈을 import 해서 자산별 데이터를 fetch.
Multiasset.html 의 MULTIASSET_EVENTS 에 있는 `asset` 필드와 key 가 일치해야 함.

새 자산 추가 시:
1. ASSETS 딕셔너리에 항목 추가 (ticker + source 지정)
2. Multiasset.html 의 MULTIASSET_EVENTS 에서 해당 asset 키 사용
3. create_multiasset_data.py 재실행

업데이트 시 항목 모두 수정.
"""

# ============================================================
# 자산별 데이터 소스 매핑
# ============================================================
# Schema:
#   'ASSET_KEY': {
#       'ticker':    Yahoo/CoinGecko 등 source-specific identifier
#       'source':    'yfinance' | 'coingecko' | 'manual'
#       'desc':      사람 읽기용 설명
#       'note':      (옵션) 데이터 가용성 메모 (defunct, proxy 등)
#   }

ASSETS = {
    # ===== 미국 주식·지수 =====
    'SPX':         {'ticker': '^GSPC',    'source': 'yfinance', 'desc': 'S&P 500'},
    'NASDAQ':      {'ticker': '^IXIC',    'source': 'yfinance', 'desc': 'NASDAQ Composite'},
    'DJI':         {'ticker': '^DJI',     'source': 'yfinance', 'desc': 'Dow Jones Industrial Average'},
    'N225':        {'ticker': '^N225',    'source': 'yfinance', 'desc': 'Nikkei 225'},
    'TSLA':        {'ticker': 'TSLA',     'source': 'yfinance', 'desc': 'Tesla Inc.'},
    'NVDA':        {'ticker': 'NVDA',     'source': 'yfinance', 'desc': 'NVIDIA Corp'},
    'GME':         {'ticker': 'GME',      'source': 'yfinance', 'desc': 'GameStop'},
    'TLRY':        {'ticker': 'TLRY',     'source': 'yfinance', 'desc': 'Tilray'},
    'ARKK':        {'ticker': 'ARKK',     'source': 'yfinance', 'desc': 'ARK Innovation ETF'},

    # ===== 한국 지수 (자산군 벤치마크) =====
    'KOSPI':         {'ticker': '^KS11', 'source': 'yfinance', 'desc': 'KOSPI'},
    'KOSDAQ':        {'ticker': '^KQ11', 'source': 'yfinance', 'desc': 'KOSDAQ'},

    # ===== 한국 주식 =====
    'POSCO':         {'ticker': '005490.KS', 'source': 'yfinance', 'desc': 'POSCO 홀딩스'},
    # 'DOOSAN_INFRA':  Yahoo 미러링 끊김 (2026-05-15 검증). 향후 KRX OpenAPI 로 재추가 검토.
    #                  당시 Yahoo 응답: "Quote not found for symbol: 042670.KS"
    #                  2009_kr_china_2nd 이벤트는 데이터 미연결 상태로 두고 placeholder 처리.
    'KAKAO':         {'ticker': '035720.KS', 'source': 'yfinance', 'desc': '카카오'},
    'ECOPRO':        {'ticker': '086520.KQ', 'source': 'yfinance', 'desc': '에코프로'},
    'HD_HEAVY':      {'ticker': '329180.KS', 'source': 'yfinance', 'desc': 'HD현대중공업',
                      'note': '구 현대중공업 009540 분할 (2017). 분할 전은 009540.KS 별도 fetch 필요'},
    'HANWHA_OCEAN':  {'ticker': '042660.KS', 'source': 'yfinance', 'desc': '한화오션 (구 대우조선해양)'},
    'DOOSAN_E':      {'ticker': '034020.KS', 'source': 'yfinance', 'desc': '두산에너빌리티 (구 두산중공업)'},
    'SK_HYNIX':      {'ticker': '000660.KS', 'source': 'yfinance', 'desc': 'SK하이닉스'},
    'SAMSUNG_ELEC':  {'ticker': '005930.KS', 'source': 'yfinance', 'desc': '삼성전자'},

    # ===== 원자재 =====
    'GLD':         {'ticker': 'GLD',      'source': 'yfinance', 'desc': 'SPDR Gold Shares ETF (금 spot proxy)'},
    'SLV':         {'ticker': 'SLV',      'source': 'yfinance', 'desc': 'iShares Silver Trust ETF (은 spot proxy)'},
    'WTI':         {'ticker': 'CL=F',     'source': 'yfinance', 'desc': 'WTI Crude Oil Futures (front month)'},
    'BCOM':        {'ticker': 'DBC',      'source': 'yfinance', 'desc': 'BCOM proxy — Invesco DB Commodity Index ETF',
                    'note': '^BCOM 직접 fetch 불안정. DBC ETF (1:1 추종 아니지만 동조)'},
    'LBR':         {'ticker': 'LBR=F',    'source': 'yfinance', 'desc': 'Lumber Futures',
                    'note': '2022년 LBS=F → LBR=F 로 ticker 변경. 과거 데이터는 sparse'},
    'URA':         {'ticker': 'URA',      'source': 'yfinance', 'desc': 'Global X Uranium ETF'},
    'NATGAS':      {'ticker': 'NG=F',     'source': 'yfinance', 'desc': 'Natural Gas Futures (자매 자산)'},
    'WHEAT':       {'ticker': 'ZW=F',     'source': 'yfinance', 'desc': 'Wheat Futures (자매 자산)'},

    # ===== 크립토 =====
    'BTC':         {'ticker': 'BTC-USD',  'source': 'yfinance', 'desc': 'Bitcoin',
                    'note': 'Yahoo BTC-USD 는 2014.09부터. 2013 climax 는 CoinGecko 별도 필요'},
    'ETH':         {'ticker': 'ETH-USD',  'source': 'yfinance', 'desc': 'Ethereum',
                    'note': '2017.11+ 데이터'},

    # ===== FX =====
    'GBPUSD':      {'ticker': 'GBPUSD=X', 'source': 'yfinance', 'desc': 'British Pound / US Dollar'},
    'USDJPY':      {'ticker': 'JPY=X',    'source': 'yfinance', 'desc': 'US Dollar / Japanese Yen'},
    'DXY':         {'ticker': 'DX-Y.NYB', 'source': 'yfinance', 'desc': 'US Dollar Index'},

    # ===== 채권 =====
    'TLT':         {'ticker': 'TLT',      'source': 'yfinance', 'desc': 'iShares 20+ Year Treasury Bond ETF'},
    'MOVE':        {'ticker': '^MOVE',    'source': 'yfinance', 'desc': 'MOVE Index — 채권 옵션 IV (채권의 VIX)',
                    'note': 'BofA Merrill Lynch Option Volatility Estimate. 2022 채권 폭락 때 160 돌파 (2008 위기 이후 최초). Yahoo 가용 범위 ~2003+. 채권 climax 결정적 시그널.'},

    # ===== Legacy / defunct (proxy 사용) =====
    'BTH_STEEL':   {'ticker': '^DJI',     'source': 'yfinance', 'desc': 'Bethlehem Steel (defunct 2003) → DJI proxy',
                    'note': '1915 매매 학습용. 실제 BTH 가격은 historical archive 필요. 현재는 DJI 로 대체'},
    'ABX':         {'ticker': 'XLF',      'source': 'yfinance', 'desc': 'Subprime ABX index (illiquid) → XLF 금융 ETF proxy',
                    'note': '2007-09 subprime climax 학습용. ABX 정밀 데이터는 Markit 유료. XLF 가 시장 충격 가시화 대용'},

    # ===== Long-history (FRED close-only, 1990 이전 사이클 분석용) =====
    # source='fred' — fetch_fred 사용, close 만 받아 OHLC 형태 (O=H=L=C) 로 변환. 캔들 body 없이 line 형태로 표시.
    'N225_LONG':   {'ticker': 'NIKKEI225',         'source': 'fred', 'desc': 'Nikkei 225 long history (1949+)',
                    'note': '1985-89 Japan Nikkei climax 분석용. close-only.'},
    'GBPUSD_LONG': {'ticker': 'DEXUSUK',           'source': 'fred', 'desc': 'GBP/USD long history (1971+, USD per GBP)',
                    'note': '1992 Soros GBP 공매도 분석용. FRED DEXUSUK = USD/GBP (값 1.6 = $1.6 per £1).'},
    'USDJPY_LONG': {'ticker': 'DEXJPUS',           'source': 'fred', 'desc': 'USD/JPY long history (1971+, JPY per USD)',
                    'note': '1995-98 USDJPY carry bubble 분석용. FRED DEXJPUS = JPY/USD (값 110 = ¥110 per $1).'},
    'GLD_LONG':    {'ticker': 'GOLDAMGBD228NLBM', 'source': 'fred', 'desc': 'Gold London AM Fix (1968+, USD/oz)',
                    'note': '1978-80 Gold $850 인플레 climax 분석용. London Bullion Market.'},
    'SLV_LONG':    {'ticker': 'SLVPRUSD',          'source': 'fred', 'desc': 'Silver USD per ounce long history',
                    'note': '1979-80 Silver Hunt corner 분석용. 정확한 FRED series ID 미확정 — 첫 fetch 시 확인 권장.'},

    # ===== Phase E-3: Manual CSV/XLSX (1990 이전 사이클 보강) =====
    # 각 file 은 multi-asset/manual_data/ 에 위치. source='manual' + parser 지정.
    # 모두 monthly close-only — 캔들 body 없이 line chart 로 표시.
    'SPX_SHILLER': {'ticker': 'ie_data.xlsx',             'source': 'manual', 'parser': 'shiller',
                    'desc': 'S&P Composite long history (Shiller 1871+ monthly)',
                    'note': '1907 Panic, 1914-16 WW1 Bethlehem Steel, 1924-29 Roaring 20s climax 분석용. Robert Shiller online data.'},
    'GLD_MANUAL':  {'ticker': 'gold_monthly.csv.csv',     'source': 'manual', 'parser': 'macrotrends',
                    'desc': 'Gold USD/oz long history (Macrotrends 100Y monthly, 1915+)',
                    'note': '1978-80 Gold $850 인플레 climax 분석용. 1915-1959 는 annual avg repeated.'},
    'SLV_MANUAL':  {'ticker': 'silver_monthly_real.csv.csv', 'source': 'manual', 'parser': 'macrotrends',
                    'desc': 'Silver USD/oz long history (Macrotrends 100Y monthly, 1915+)',
                    'note': '1979-80 Silver Hunt corner climax 분석용. 1980-01 $35.28 verified.'},
}


# ============================================================
# 자산군 벤치마크 (Stack 2 — 자산군 인덱스)
# ============================================================
# 메인 자산이 속한 자산군의 광역 벤치마크. 메인 자산이 자산군 전체 흐름과
# diverge 하는지 시각 비교.
BENCHMARKS = {
    'eq-gl':  'SPX',      # 글로벌 주식 — SP500 (광역 베이스)
    'eq-kr':  'KOSPI',    # 한국 주식 — KOSPI (별도 fetch 필요, 아래)
    'cm':     'BCOM',     # 원자재 — Bloomberg Commodity Index (DBC proxy)
    'cr':     'BTC',      # 크립토 — BTC 가 dominance proxy (혹은 별도 Total MC)
    'fx':     'DXY',      # FX — 달러 인덱스
    'bd':     'TLT',      # 채권 — 미국 장기채 ETF
}

# 한국 주식 벤치마크용
KR_INDICES = {
    'KOSPI':  {'ticker': '^KS11',    'source': 'yfinance', 'desc': 'KOSPI'},
    'KOSDAQ': {'ticker': '^KQ11',    'source': 'yfinance', 'desc': 'KOSDAQ'},
}


# ============================================================
# 글로벌 베이스 라인 (Stack 1 — 모든 이벤트 고정)
# ============================================================
# View-specific defaults. Multiasset.html 의 stack 1 토글 (NASDAQ / S&P500)
# 과 대응. 추후 채권에서는 10Y, FX 에서는 DXY 같이 변경 가능.

GLOBAL_BASE = ['SPX', 'NASDAQ']  # 디폴트 둘 다 fetch (UI 토글 가능)
