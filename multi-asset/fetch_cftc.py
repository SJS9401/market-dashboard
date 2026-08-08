"""
CFTC COT (Commitments of Traders) Legacy Futures-only fetch via Socrata API.

API endpoint: https://publicreporting.cftc.gov/resource/6dca-aqww.json
Free, no auth required for low-volume use. App token 권장이지만 미적용.

Report 종류:
  Legacy (이 모듈): Commercial / Non-Commercial / Non-Reportable 3분류
    - Commercial = 헤지 목적 (생산자·소비자)
    - Non-Commercial = 투기 자금 (Hedge fund 등) ← Speculator net 의 주체
    - Non-Reportable = 소액 매매 (소형 트레이더)
  Disaggregated (별도 endpoint, 미구현): Producer / Swap Dealer / MM / Other
    - 정밀하지만 학습 단계엔 Legacy 가 직관적

Cadence: Weekly. CFTC 가 매주 화요일(휴장 시 직전 영업일) 종가 기준 데이터를
  금요일 오후 3:30 ET 에 발표. report_date_as_yyyy_mm_dd 는 화요일.

표준 출력 schema:
  [[YYYYMMDD, open_interest, noncomm_long, noncomm_short, noncomm_net,
    comm_long, comm_short, comm_net, nonrept_long, nonrept_short], ...]
  → 일봉 가격 차트에 overlay 시 forward-fill (last known weekly value)

사용 예:
    from fetch_cftc import fetch_cot_legacy
    data, meta = fetch_cot_legacy('067651', start='2020-01-01')  # WTI
"""

import sys
import json
import time
from datetime import datetime
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError, URLError


CFTC_LEGACY_URL = 'https://publicreporting.cftc.gov/resource/6dca-aqww.json'

# 응답 필드 (Legacy Futures-Only) — Socrata column name 확인됨
COT_FIELDS = [
    'report_date_as_yyyy_mm_dd',
    'open_interest_all',
    'noncomm_positions_long_all',
    'noncomm_positions_short_all',
    'comm_positions_long_all',
    'comm_positions_short_all',
    'nonrept_positions_long_all',
    'nonrept_positions_short_all',
]


def fetch_cot_legacy(contract_code, start='2000-01-01', end=None, limit=50000):
    """
    Fetch CFTC Legacy Futures-Only COT data for a specific contract.

    Args:
        contract_code: CFTC contract market code, 6-digit string (e.g., '067651' for WTI)
        start:         'YYYY-MM-DD' (default 2000-01-01)
        end:           'YYYY-MM-DD' (default today)
        limit:         max records (default 50000 — 25년치 weekly 충분)

    Returns:
        (data, meta) tuple
        data: sorted ascending by date. Weekly cadence.
        meta: {'contract_code', 'source', 'report_type', 'fields', 'start', 'end', 'count'}
    """
    if end is None:
        end = datetime.utcnow().strftime('%Y-%m-%d')

    where = (
        "cftc_contract_market_code = '" + contract_code + "' "
        "AND report_date_as_yyyy_mm_dd >= '" + start + "' "
        "AND report_date_as_yyyy_mm_dd <= '" + end + "'"
    )
    params = {
        '$select': ','.join(COT_FIELDS),
        '$where': where,
        '$order': 'report_date_as_yyyy_mm_dd ASC',
        '$limit': str(limit),
    }
    url = CFTC_LEGACY_URL + '?' + urlencode(params)

    try:
        req = Request(url, headers={'User-Agent': 'multi-asset-cycle/1.0'})
        with urlopen(req, timeout=30) as resp:
            raw = json.loads(resp.read().decode('utf-8'))
    except (HTTPError, URLError, ValueError) as e:
        print('ERROR CFTC fetch ' + contract_code + ': ' + str(e), file=sys.stderr)
        return [], {'contract_code': contract_code, 'source': 'cftc-socrata', 'error': str(e)}

    if not raw:
        print('WARN: CFTC ' + contract_code + ' returned empty', file=sys.stderr)
        return [], {'contract_code': contract_code, 'source': 'cftc-socrata', 'error': 'empty'}

    data = []
    for row in raw:
        try:
            # Socrata returns ISO-8601 — convert to YYYYMMDD
            d_iso = row.get('report_date_as_yyyy_mm_dd', '')
            if not d_iso:
                continue
            date_str = d_iso[:10].replace('-', '')

            def _toi(key):
                v = row.get(key, 0)
                if v is None or v == '':
                    return 0
                return int(float(v))

            oi = _toi('open_interest_all')
            ncl = _toi('noncomm_positions_long_all')
            ncs = _toi('noncomm_positions_short_all')
            cl = _toi('comm_positions_long_all')
            cs = _toi('comm_positions_short_all')
            nrl = _toi('nonrept_positions_long_all')
            nrs = _toi('nonrept_positions_short_all')
            ncnet = ncl - ncs
            cnet = cl - cs
            data.append([date_str, oi, ncl, ncs, ncnet, cl, cs, cnet, nrl, nrs])
        except Exception as e:
            print('WARN row skipped: ' + str(e), file=sys.stderr)
            continue

    meta = {
        'contract_code': contract_code,
        'source': 'cftc-socrata',
        'report_type': 'legacy_futures_only',
        'cadence': 'weekly',
        'fields': ['date', 'OI', 'ncomm_long', 'ncomm_short', 'ncomm_net',
                   'comm_long', 'comm_short', 'comm_net', 'nonrept_long', 'nonrept_short'],
        'start': data[0][0] if data else None,
        'end': data[-1][0] if data else None,
        'count': len(data),
    }
    return data, meta


def fetch_cot_with_retry(contract_code, start='2000-01-01', end=None, max_retries=3, retry_sleep=2):
    """Rate limit / 일시적 실패 대응 재시도 wrapper."""
    for attempt in range(max_retries):
        data, meta = fetch_cot_legacy(contract_code, start=start, end=end)
        if data and 'error' not in meta:
            return data, meta
        if attempt < max_retries - 1:
            time.sleep(retry_sleep * (attempt + 1))
    return data, meta


if __name__ == '__main__':
    # CLI: python fetch_cftc.py 067651 2020-01-01
    if len(sys.argv) < 2:
        print('Usage: python fetch_cftc.py <contract_code> [start] [end]')
        print('')
        print('Common Legacy codes:')
        print('  WTI    067651   GOLD   088691   SILVER  084691')
        print('  NATGAS 023651   GBP    096742   JPY     097741')
        print('  10Y    043602   30Y    020601')
        sys.exit(1)
    code = sys.argv[1]
    start = sys.argv[2] if len(sys.argv) > 2 else '2010-01-01'
    end = sys.argv[3] if len(sys.argv) > 3 else None
    data, meta = fetch_cot_legacy(code, start=start, end=end)
    print('Meta:', meta)
    if data:
        print('First:', data[0])
        print('Last: ', data[-1])
