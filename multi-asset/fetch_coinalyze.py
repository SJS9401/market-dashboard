"""
Coinalyze API client — 크립토 파생 OI + Funding rate.

Coinalyze: https://api.coinalyze.net/v1/doc/
- 무료 (API key 가입 후 발급)
- 40 calls/min rate limit
- daily 데이터 영구 보관 (2021 BTC climax 가능)
- intraday 데이터는 1500~2000 datapoints 만 보관
- 인증: header 'api_key' (query param 은 401)

Exchange ID 매핑 (확인 2026-05-17):
  A = Binance   6 = Bybit   3 = OKX     4 = Huobi
  F = Bitfinex  0 = BitMEX  S = Aster   W = WOO X   Y = Gate.io

표준 출력 schema:
  단일:       [[YYYYMMDD, close_value], ...]
  Aggregated: [[YYYYMMDD, sum_of_close_values], ...]    # 여러 거래소 합산

OI 단위: BASE_ASSET (BTC = BTC contracts, ETH = ETH contracts)
Funding 단위: % per 8h 추정 (가입 후 웹 차트와 비교해 확정 권장)

환경변수: COINALYZE_API_KEY (.env 에서 자동 load)

사용 예:
    python fetch_coinalyze.py BTCUSDT_PERP.A 2021-01-01           # single
    python fetch_coinalyze.py "BTCUSDT_PERP.A,BTCUSDT.6" 2021-01  # multi (합산)
"""

import os
import sys
import json
import time
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError, URLError


BASE = 'https://api.coinalyze.net/v1'


def _load_api_key():
    """COINALYZE_API_KEY 를 환경변수 또는 .env 에서 load."""
    key = os.environ.get('COINALYZE_API_KEY')
    if key:
        return key
    here = os.path.dirname(os.path.abspath(__file__))
    for root in [here, os.path.dirname(here), os.path.dirname(os.path.dirname(here))]:
        env_path = os.path.join(root, '.env')
        if os.path.exists(env_path):
            try:
                with open(env_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith('COINALYZE_API_KEY'):
                            val = line.split('=', 1)[1].strip()
                            return val.strip('"').strip("'")
            except Exception:
                continue
    return None


API_KEY = _load_api_key()


def _ts_to_yyyymmdd(t):
    return datetime.fromtimestamp(int(t), tz=timezone.utc).strftime('%Y%m%d')


def fetch_coinalyze_raw(endpoint, symbols, interval='daily', from_ts=None, to_ts=None):
    """
    Multi-symbol 지원 raw fetch. Coinalyze 응답 형식 그대로 반환.

    Args:
        endpoint: 'open-interest-history' | 'funding-rate-history'
        symbols:  single string 또는 list
        interval: 'daily' | '1hour' | ...
        from_ts:  unix seconds
        to_ts:    unix seconds (기본 현재)

    Returns:
        (raw, meta) — raw 는 [{symbol, history:[{t,o,h,l,c}]}, ...] 형식
    """
    if not API_KEY:
        return [], {'error': 'COINALYZE_API_KEY not set'}

    if isinstance(symbols, list):
        symbols_str = ','.join(symbols)
    else:
        symbols_str = symbols

    if to_ts is None:
        to_ts = int(time.time())
    if from_ts is None:
        from_ts = to_ts - 7 * 365 * 86400

    params = {
        'symbols':  symbols_str,
        'interval': interval,
        'from':     int(from_ts),
        'to':       int(to_ts),
    }
    url = BASE + '/' + endpoint + '?' + urlencode(params)

    try:
        req = Request(url, headers={
            'User-Agent': 'multi-asset-cycle/1.0',
            'api_key':    API_KEY,
        })
        with urlopen(req, timeout=30) as resp:
            raw = json.loads(resp.read().decode('utf-8'))
    except HTTPError as e:
        body = ''
        try:
            body = e.read().decode('utf-8')[:200]
        except Exception:
            pass
        return [], {'symbols': symbols_str, 'endpoint': endpoint,
                    'error': 'HTTP ' + str(e.code) + ' ' + body}
    except (URLError, ValueError) as e:
        return [], {'symbols': symbols_str, 'endpoint': endpoint, 'error': str(e)}

    if not raw:
        return [], {'symbols': symbols_str, 'endpoint': endpoint, 'error': 'empty response'}

    meta = {
        'symbols':  symbols_str,
        'endpoint': endpoint,
        'interval': interval,
        'source':   'coinalyze',
        'n_symbols_returned': len(raw) if isinstance(raw, list) else 1,
    }
    return raw, meta


def _extract_close_series(raw):
    """raw 응답에서 [(date_str, close_value), ...] 단일 symbol 추출."""
    if not raw:
        return []
    entry = raw[0] if isinstance(raw, list) and raw else raw
    if not isinstance(entry, dict):
        return []
    history = entry.get('history', [])
    data = []
    for h in history:
        try:
            t = h.get('t')
            if t is None:
                continue
            val = h.get('c')
            if val is None:
                val = h.get('o')
            if val is None:
                val = h.get('value')
            if val is None:
                continue
            data.append([_ts_to_yyyymmdd(t), float(val)])
        except Exception:
            continue
    return data


def fetch_oi_history(symbol, **kwargs):
    """Single-symbol OI history (close 값). 호환용 wrapper."""
    raw, meta = fetch_coinalyze_raw('open-interest-history', symbol, **kwargs)
    data = _extract_close_series(raw)
    meta['count'] = len(data)
    if data:
        meta['start'] = data[0][0]
        meta['end']   = data[-1][0]
    if not data and 'error' not in meta:
        meta['error'] = 'no parseable history'
    return data, meta


def fetch_funding_history(symbol, **kwargs):
    """Single-symbol funding rate history (close 값)."""
    raw, meta = fetch_coinalyze_raw('funding-rate-history', symbol, **kwargs)
    data = _extract_close_series(raw)
    meta['count'] = len(data)
    if data:
        meta['start'] = data[0][0]
        meta['end']   = data[-1][0]
    if not data and 'error' not in meta:
        meta['error'] = 'no parseable history'
    return data, meta


def fetch_oi_aggregated(symbols, **kwargs):
    """
    여러 거래소 OI 합산. 1 API call 로 multi-symbol fetch 후 date 별 합산.

    Args:
        symbols: list (예: ['BTCUSDT_PERP.A', 'BTCUSDT.6', 'BTCUSDT_PERP.3', 'BTCUSDT_PERP.4'])

    Returns:
        ([[YYYYMMDD, sum_of_close_OI], ...], meta)
        — 각 date 에 valid 한 모든 거래소의 close OI 합산
        — 일부 거래소에만 데이터 있는 경우 그 합산
    """
    raw, meta = fetch_coinalyze_raw('open-interest-history', symbols, **kwargs)
    if not raw:
        return [], meta

    # date → sum
    by_date = {}
    symbol_dates = {}  # 디버깅용 — 각 symbol 의 date 범위
    for entry in (raw if isinstance(raw, list) else [raw]):
        if not isinstance(entry, dict):
            continue
        sym = entry.get('symbol', '?')
        history = entry.get('history', [])
        for h in history:
            t = h.get('t')
            c = h.get('c')
            if t is None or c is None:
                continue
            try:
                date_str = _ts_to_yyyymmdd(t)
                by_date[date_str] = by_date.get(date_str, 0.0) + float(c)
                if sym not in symbol_dates:
                    symbol_dates[sym] = [date_str, date_str]
                else:
                    if date_str < symbol_dates[sym][0]: symbol_dates[sym][0] = date_str
                    if date_str > symbol_dates[sym][1]: symbol_dates[sym][1] = date_str
            except Exception:
                continue

    data = sorted([[d, v] for d, v in by_date.items()])
    meta['count'] = len(data)
    meta['symbol_ranges'] = symbol_dates
    if data:
        meta['start'] = data[0][0]
        meta['end']   = data[-1][0]
    if not data and 'error' not in meta:
        meta['error'] = 'no parseable history'
    return data, meta


def fetch_with_retry(fn, *args, max_retries=3, retry_sleep=2, **kwargs):
    """Rate limit (40/min) / 일시 실패 대응 wrapper."""
    data, meta = [], {}
    for attempt in range(max_retries):
        data, meta = fn(*args, **kwargs)
        if data and 'error' not in meta:
            return data, meta
        err = str(meta.get('error', ''))
        sleep_for = retry_sleep * (attempt + 1)
        if '429' in err:
            sleep_for *= 5
        if attempt < max_retries - 1:
            time.sleep(sleep_for)
    return data, meta


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python fetch_coinalyze.py <symbol> [start_YYYY-MM-DD]")
        print("  python fetch_coinalyze.py <sym1,sym2,sym3> [start_YYYY-MM-DD]   # aggregated 합산")
        print("")
        print("Symbols (확인 2026-05-17):")
        print("  BTC Binance:  BTCUSDT_PERP.A")
        print("  BTC Bybit:    BTCUSDT.6")
        print("  BTC OKX:      BTCUSDT_PERP.3")
        print("  BTC Huobi:    BTCUSDT_PERP.4")
        sys.exit(1)

    if not API_KEY:
        print("ERROR: COINALYZE_API_KEY not found in .env", file=sys.stderr)
        sys.exit(1)

    symbol_arg = sys.argv[1]
    from_ts = None
    if len(sys.argv) > 2:
        start = sys.argv[2]
        from_ts = int(datetime.strptime(start, '%Y-%m-%d').replace(tzinfo=timezone.utc).timestamp())

    is_aggregated = (',' in symbol_arg)

    if is_aggregated:
        print('=== Aggregated OI (multi-exchange sum) ===')
        symbols = symbol_arg.split(',')
        data, meta = fetch_oi_aggregated(symbols, from_ts=from_ts)
    else:
        print('=== Open Interest ===')
        data, meta = fetch_oi_history(symbol_arg, from_ts=from_ts)
    print('Meta:', meta)
    if data:
        print('First:', data[0])
        print('Last: ', data[-1])

    print('\n=== Funding Rate (single, primary symbol) ===')
    primary = symbol_arg.split(',')[0]
    fdata, fmeta = fetch_funding_history(primary, from_ts=from_ts)
    print('Meta:', fmeta)
    if fdata:
        print('First:', fdata[0])
        print('Last: ', fdata[-1])
