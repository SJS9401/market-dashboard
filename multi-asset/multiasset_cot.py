"""
CFTC COT contract registry — asset key → CFTC Legacy 6-digit contract code.

Phase B-1 (현재): WTI 만 1차 등록. fetch_cftc 검증 후 Phase B-2 에서 확장.

CFTC 코드 source: https://www.cftc.gov/dea/futures/deacmesf.htm (Legacy Futures-Only)
6-digit format. Disaggregated 와 동일 코드 사용 (report 종류만 다름).

ASSETS (multiasset_assets.py) 의 키와 매칭되도록 동일 key 명명.
Phase B-2 에서 GOLD/SILVER/NATGAS/GBPUSD/USDJPY/ZN/ZB 추가 예정.
"""

COT_CONTRACTS = {
    # ===== Phase B-1: WTI 1차 검증 =====
    'WTI': {
        'code': '067651',
        'desc': 'Crude Oil, Light Sweet — NYMEX',
        'note': 'Phase B-1 검증 대상. 2022 WTI deep-dive 의 핵심 자료.',
    },

    # ===== Phase B-2 확장 후보 (검증 후 활성화) =====
    # 'GOLD':   {'code': '088691', 'desc': 'Gold — COMEX'},
    # 'SILVER': {'code': '084691', 'desc': 'Silver — COMEX'},
    # 'NATGAS': {'code': '023651', 'desc': 'Natural Gas — NYMEX'},
    # 'GBPUSD': {'code': '096742', 'desc': 'British Pound — CME'},
    # 'USDJPY': {'code': '097741', 'desc': 'Japanese Yen — CME'},
    # 'ZN':     {'code': '043602', 'desc': '10-Year T-Note — CBT'},
    # 'ZB':     {'code': '020601', 'desc': '30-Year T-Bond — CBT'},
}
