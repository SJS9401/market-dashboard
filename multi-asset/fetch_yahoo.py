"""
Yahoo Finance 데이터 fetch (yfinance 사용).

표준 출력:
  [[YYYYMMDD, open, high, low, close, volume], ...]

거래량 단위: 원본 그대로 (주식 = shares, ETF/futures = contracts, crypto = USD).
Multiasset.html 측에서 단위 라벨 매칭. (참고: ls_data_v3.json 의 한국 종목은 키움식 억원 단위로 normalize 되어 있는데, 멀티에셋은 자산군별 단위가 다양해서 원본 보존 권장.)

사용 예:
    from fetch_yahoo import fetch_yahoo_ohlcv
    data, meta = fetch_yahoo_ohlcv('CL=F', start='2020-01-01', end='2026-05-15')
"""

import sys
from datetime import datetime, timedelta


def fetch_yahoo_ohlcv(ticker, start='1990-01-01', end=None, interval='1d'):
    """
    Yahoo Finance 에서 OHLCV 데이터 fetch.

    Args:
        ticker: '^GSPC', 'CL=F', 'BTC-USD', '000660.KS' 등
        start:  'YYYY-MM-DD' (기본 1990-01-01)
        end:    'YYYY-MM-DD' (기본 오늘)
        interval: '1d' (일봉) | '1wk' (주봉) | '1mo' (월봉)

    Returns:
        (data, meta) tuple
        data: [[YYYYMMDD, O, H, L, C, V], ...] (volume=0 이면 yfinance 가 NaN 으로 반환 → 0 으로 대체)
        meta: {'ticker': ..., 'source': 'yfinance', 'start': YYYYMMDD, 'end': YYYYMMDD, 'count': N}
    """
    try:
        import yfinance as yf
    except ImportError:
        print("ERROR: yfinance 미설치. `pip install yfinance` 후 재시도", file=sys.stderr)
        return [], {'ticker': ticker, 'source': 'yfinance', 'error': 'yfinance not installed'}

    if end is None:
        end = datetime.utcnow().strftime('%Y-%m-%d')

    try:
        df = yf.download(
            ticker,
            start=start,
            end=end,
            interval=interval,
            auto_adjust=False,   # raw OHLC (adjusted 별도 처리)
            progress=False,
            threads=False,
        )
    except Exception as e:
        print(f"ERROR fetching {ticker}: {e}", file=sys.stderr)
        return [], {'ticker': ticker, 'source': 'yfinance', 'error': str(e)}

    if df is None or df.empty:
        print(f"WARN: {ticker} returned empty dataframe", file=sys.stderr)
        return [], {'ticker': ticker, 'source': 'yfinance', 'error': 'empty'}

    # MultiIndex columns 가능 (auto_adjust 옵션 따라) — flatten
    if hasattr(df.columns, 'levels'):
        df.columns = df.columns.get_level_values(0)

    # 한국 주식 (.KS/.KQ) 은 키움식 거래대금 단위 (억원) 로 정규화 — Close × Volume / 1e8
    is_kr_equity = ticker.endswith('.KS') or ticker.endswith('.KQ')
    # 미국 개별 주식 + ETF 는 USD 백만 단위로 정규화 — Close × Volume / 1e6
    # 제외: 지수 (^), 선물 (=F), FX (=X / DX-), 크립토 (-USD)
    # 명시적 list 로 안전하게 한정 (자산 추가 시 여기에 등록)
    US_NORMALIZED_TICKERS = {
        # 미국 개별 주식
        'TSLA', 'NVDA', 'GME', 'TLRY',
        # ETF (주식·원자재·채권 ETF 모두 거래대금 USD 백만)
        'ARKK', 'GLD', 'SLV', 'URA', 'DBC', 'TLT',
    }
    is_us_normalized = ticker in US_NORMALIZED_TICKERS
    data = []
    for ts, row in df.iterrows():
        try:
            date_str = ts.strftime('%Y%m%d')
            o = float(row['Open'])  if row['Open']  == row['Open']  else None
            h = float(row['High'])  if row['High']  == row['High']  else None
            l = float(row['Low'])   if row['Low']   == row['Low']   else None
            c = float(row['Close']) if row['Close'] == row['Close'] else None
            v = float(row['Volume']) if row.get('Volume', 0) == row.get('Volume', 0) else 0
            # NaN 데이터 행은 skip
            if c is None:
                continue
            if o is None: o = c
            if h is None: h = c
            if l is None: l = c
            if v != v: v = 0   # NaN guard
            # 한국 주식: shares → 거래대금 (억원) 변환
            if is_kr_equity and c > 0 and v > 0:
                v = (c * v) / 100_000_000
            # 미국 주식·ETF: shares → 거래대금 (USD 백만) 변환
            elif is_us_normalized and c > 0 and v > 0:
                v = (c * v) / 1_000_000
            data.append([date_str, round(o, 6), round(h, 6), round(l, 6), round(c, 6), round(v, 2)])
        except Exception as e:
            print(f"WARN row skipped ({ts}): {e}", file=sys.stderr)
            continue

    meta = {
        'ticker': ticker,
        'source': 'yfinance',
        'interval': interval,
        'start': data[0][0] if data else None,
        'end': data[-1][0] if data else None,
        'count': len(data),
    }
    return data, meta


def fetch_yahoo_with_retry(ticker, start='1990-01-01', end=None, interval='1d', max_retries=3, retry_sleep=2):
    """Rate limit / 일시적 실패 대응 재시도 wrapper."""
    import time
    for attempt in range(max_retries):
        data, meta = fetch_yahoo_ohlcv(ticker, start=start, end=end, interval=interval)
        if data and 'error' not in meta:
            return data, meta
        if attempt < max_retries - 1:
            time.sleep(retry_sleep * (attempt + 1))
    return data, meta


if __name__ == '__main__':
    # CLI 테스트 — `python fetch_yahoo.py CL=F 2020-01-01`
    if len(sys.argv) < 2:
        print("Usage: python fetch_yahoo.py <ticker> [start] [end]")
        sys.exit(1)
    ticker = sys.argv[1]
    start = sys.argv[2] if len(sys.argv) > 2 else '2020-01-01'
    end = sys.argv[3] if len(sys.argv) > 3 else None
    data, meta = fetch_yahoo_ohlcv(ticker, start=start, end=end)
    print(f"Meta: {meta}")
    if data:
        print(f"First row: {data[0]}")
        print(f"Last row:  {data[-1]}")
