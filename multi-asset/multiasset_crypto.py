"""
Coinalyze 크립토 파생 등록 — asset key → Coinalyze symbol 매핑.

Phase C-1: BTC, ETH 4-exchange aggregated OI + Binance funding.

Exchange ID 확인 결과 (2026-05-17):
  A = Binance, 6 = Bybit, 3 = OKX, 4 = Huobi
  0 = BitMEX (거의 비활성, 제외)
  F = Bitfinex, S = Aster, W = WOO X, Y = Gate.io

OI aggregation 전략:
  주요 4개 거래소 (Binance + Bybit + OKX + Huobi) close OI 합산
  → BTC perp 시장의 ~70%+ 점유, 1 API call 로 multi-symbol fetch
  → BitMEX 는 거의 비활성 (98 BTC vs Binance 92K BTC) 이라 제외

Funding rate:
  Binance 단독 사용 (시장 standard)
  거래소별 funding 다르지만 Binance 가 가장 영향력 큼

OI 단위: BTC contracts (oi_lq_vol_denominated_in: BASE_ASSET)
Funding 단위: % per 8h (Coinalyze 웹 차트와 비교해 확정 권장)
"""

CRYPTO_DERIV = {
    'BTC': {
        'oi_symbols': [
            'BTCUSDT_PERP.A',  # Binance
            'BTCUSDT.6',       # Bybit
            'BTCUSDT_PERP.3',  # OKX
            'BTCUSDT_PERP.4',  # Huobi
        ],
        'funding_symbol': 'BTCUSDT_PERP.A',  # Binance 단독
        'desc': 'BTC perpetual OI — 4-exchange aggregated (Binance+Bybit+OKX+Huobi)',
        'note': '시장 ~70%+ 커버. BitMEX 제외 (거의 비활성). OI 단위 = BTC contracts. '
                '2019-09 이후 데이터 가용 (Binance 시작 시점). 2017 climax 는 BitMEX 만 운영했고 archive 폐쇄.',
    },
    'ETH': {
        'oi_symbols': [
            'ETHUSDT_PERP.A',  # Binance
            'ETHUSDT.6',       # Bybit
            'ETHUSDT_PERP.3',  # OKX
            'ETHUSDT_PERP.4',  # Huobi
        ],
        'funding_symbol': 'ETHUSDT_PERP.A',
        'desc': 'ETH perpetual OI — 4-exchange aggregated',
        'note': '2019-11 이후 데이터 가용.',
    },

    # ===== Phase C-2 확장 후보 (필요 시 활성화) =====
    # 'SOL':  {'oi_symbols': ['SOLUSDT_PERP.A', 'SOLUSDT.6', 'SOLUSDT_PERP.3', 'SOLUSDT_PERP.4'],
    #          'funding_symbol': 'SOLUSDT_PERP.A',
    #          'desc': 'Solana perpetual aggregated'},
    # 'XRP':  {'oi_symbols': [...], ...},
    # 'DOGE': {'oi_symbols': [...], ...},
}
