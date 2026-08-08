"""
Multi-asset 매크로 드라이버 (Stack 5) 시리즈 레지스트리 — FRED API 기반.

전체 Type 분류 (5-Type macro driver framework):
  A. 유동성/QE          : M2, Fed BS, Fed Funds, Real Yields
  B. 인플레/공급 충격    : CPI, Fed Funds, DXY, Real Yields
  C. 기술/사이클         : Fed Funds, NASDAQ 상대, VIX, 10Y
  D. 위기/정책 충격      : 10Y, DXY, VIX, Credit spreads
  E. 통화/캐리           : 양국 yield diff, DXY, 정책 divergence

각 macro 시리즈는 FRED series ID + 변환 방식 명시.
"""

# ============================================================
# 매크로 시리즈 (Stack 5 패널 candidates)
# ============================================================
# Schema:
#   'KEY': {
#       'series':    FRED series ID (https://fred.stlouisfed.org/series/<ID>)
#       'transform': 'level' (그대로) | 'yoy' (YoY % 변환) | 'mom' (MoM %)
#       'desc':      사람 읽기용 설명
#       'unit':      표시 단위 (%, ratio, level)
#       'freq':      'D' (일별) | 'M' (월별) — 데이터 발표 빈도
#   }

MACROS = {
    # --- Type A. 유동성/QE ---
    'M2':       {'series': 'M2SL',     'transform': 'yoy',   'desc': 'M2 통화량 YoY %',          'unit': '%', 'freq': 'M'},
    'WALCL':    {'series': 'WALCL',    'transform': 'yoy',   'desc': 'Fed Balance Sheet YoY %',  'unit': '%', 'freq': 'W'},
    'FEDFUNDS': {'series': 'FEDFUNDS', 'transform': 'level', 'desc': 'Effective Fed Funds Rate', 'unit': '%', 'freq': 'M'},
    'DFII10':   {'series': 'DFII10',   'transform': 'level', 'desc': '10Y TIPS Real Yield',      'unit': '%', 'freq': 'D'},

    # --- Type B. 인플레/공급 충격 ---
    'CPI':      {'series': 'CPIAUCSL', 'transform': 'yoy',   'desc': 'CPI YoY %',                'unit': '%', 'freq': 'M'},
    'PCE':      {'series': 'PCEPI',    'transform': 'yoy',   'desc': 'PCE 헤드라인 YoY %',        'unit': '%', 'freq': 'M'},
    'PCEPI_CORE':{'series':'PCEPILFE', 'transform': 'yoy',   'desc': 'Core PCE YoY %',           'unit': '%', 'freq': 'M'},

    # --- Type C/D. 금리·신용·변동성 ---
    'DGS10':    {'series': 'DGS10',    'transform': 'level', 'desc': '10Y Treasury Yield',       'unit': '%', 'freq': 'D'},
    'DGS2':     {'series': 'DGS2',     'transform': 'level', 'desc': '2Y Treasury Yield',        'unit': '%', 'freq': 'D'},
    'T10Y2Y':   {'series': 'T10Y2Y',   'transform': 'level', 'desc': '10Y-2Y spread (=경기 침체 시그널)','unit':'%','freq':'D'},
    'VIXCLS':   {'series': 'VIXCLS',   'transform': 'level', 'desc': 'CBOE VIX',                 'unit': 'pt','freq': 'D'},
    'BAMLH0A0HYM2':{'series':'BAMLH0A0HYM2','transform':'level','desc':'High Yield credit spread','unit':'%','freq':'D'},

    # --- Type E. 통화 ---
    # DXY 는 자산군 벤치마크 (assets.py)에서 처리. 여기는 FRED-only 매크로.
    'DTWEXBGS': {'series': 'DTWEXBGS', 'transform': 'level', 'desc': 'USD Broad Trade-Weighted Index','unit':'pt','freq':'D'},
}


# ============================================================
# Macro Type → 표준 panel 4-set 매핑 (Multiasset.html stack 5 에서 활용)
# ============================================================
# 각 이벤트의 macroType (A/B/C/D/E) 에 따라 자동 표시할 매크로 4종.
MACRO_TYPE_PANELS = {
    'A': ['M2', 'WALCL', 'FEDFUNDS', 'DFII10'],           # 유동성 / QE
    'B': ['CPI', 'FEDFUNDS', 'DFII10', 'DTWEXBGS'],       # 인플레 / 공급 충격 (DXY 대용)
    'C': ['FEDFUNDS', 'DGS10', 'VIXCLS', 'T10Y2Y'],       # 기술 / 사이클
    'D': ['DGS10', 'VIXCLS', 'BAMLH0A0HYM2', 'DTWEXBGS'], # 위기 / 정책 충격
    'E': ['T10Y2Y', 'DTWEXBGS', 'FEDFUNDS', 'DGS10'],     # 통화 / 캐리 (양국 yield diff 는 별도 처리)
}
