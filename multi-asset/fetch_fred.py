"""
FRED API 데이터 fetch (requests 사용, yfinance 미사용).

FRED_API_KEY 가 .env 또는 환경변수에 있어야 함.
(인프라 핸드오프 응답에 따르면 이미 FRED_API_KEY 가 등록되어 있음)

표준 출력 (OHLCV 스키마와 정합):
  [[YYYYMMDD, value, value, value, value, 0], ...]
  ← FRED 시리즈는 close-only 이므로 O=H=L=C=value, volume=0

변환 옵션:
  - 'level' : 원본 값 그대로
  - 'yoy'   : Year-over-Year 변화율 (%) — 12개월 lag 비교
  - 'mom'   : Month-over-Month 변화율 (%) — 1개월 lag 비교

사용 예:
    from fetch_fred import fetch_fred_series
    data, meta = fetch_fred_series('CPIAUCSL', transform='yoy', start='2020-01-01')
"""

import os
import sys
from datetime import datetime, timedelta


def _get_fred_key():
    """환경변수 또는 .env 파일에서 FRED_API_KEY 로드."""
    key = os.environ.get('FRED_API_KEY')
    if key:
        return key
    # .env 파일 시도 (Scheduled 디렉토리 또는 multi-asset 상위)
    here = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(here, '.env'),
        os.path.join(here, '..', '.env'),
        os.path.join(here, '..', '..', '.env'),
    ]
    for env_path in candidates:
        if os.path.exists(env_path):
            try:
                with open(env_path) as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith('FRED_API_KEY='):
                            return line.split('=', 1)[1].strip().strip('"').strip("'")
            except Exception:
                pass
    return None


def fetch_fred_series(series_id, transform='level', start='1990-01-01', end=None):
    """
    FRED 시리즈 fetch.

    Args:
        series_id:  'M2SL', 'CPIAUCSL', 'FEDFUNDS' 등
        transform:  'level' | 'yoy' | 'mom'
        start, end: 'YYYY-MM-DD'

    Returns:
        (data, meta) tuple
        data: [[YYYYMMDD, v, v, v, v, 0], ...]
        meta: {'series': ..., 'source': 'fred', 'transform': ..., 'start': ..., 'end': ..., 'count': N}
    """
    try:
        import requests
    except ImportError:
        print("ERROR: requests 미설치. `pip install requests` 후 재시도", file=sys.stderr)
        return [], {'series': series_id, 'source': 'fred', 'error': 'requests not installed'}

    api_key = _get_fred_key()
    if not api_key:
        print("ERROR: FRED_API_KEY 미설정. .env 또는 환경변수에 설정 필요", file=sys.stderr)
        return [], {'series': series_id, 'source': 'fred', 'error': 'FRED_API_KEY missing'}

    if end is None:
        end = datetime.utcnow().strftime('%Y-%m-%d')

    url = 'https://api.stlouisfed.org/fred/series/observations'
    params = {
        'series_id': series_id,
        'api_key': api_key,
        'file_type': 'json',
        'observation_start': start,
        'observation_end': end,
    }
    try:
        r = requests.get(url, params=params, timeout=30)
        r.raise_for_status()
        body = r.json()
    except Exception as e:
        print(f"ERROR fetching FRED {series_id}: {e}", file=sys.stderr)
        return [], {'series': series_id, 'source': 'fred', 'error': str(e)}

    observations = body.get('observations', [])
    if not observations:
        print(f"WARN: FRED {series_id} returned no observations", file=sys.stderr)
        return [], {'series': series_id, 'source': 'fred', 'error': 'no observations'}

    # 원시 (date, value) 추출
    raw = []
    for obs in observations:
        try:
            v = float(obs['value'])
            d = obs['date'].replace('-', '')  # YYYYMMDD
            raw.append((d, v))
        except (ValueError, KeyError):
            # FRED 는 결측치를 '.' 로 표시
            continue

    if not raw:
        return [], {'series': series_id, 'source': 'fred', 'error': 'all values missing'}

    # 변환
    if transform == 'yoy':
        # 약 12개월 (월별이면 12, 일별이면 252 영업일) 이전과 비교
        # FRED 시리즈는 시리즈마다 빈도가 다른데, 단순히 date string 기준으로 1년 전 찾기
        date_to_val = {d: v for d, v in raw}
        transformed = []
        for d, v in raw:
            try:
                yyyy = int(d[:4])
                mmdd = d[4:]
                prev_d = f"{yyyy-1}{mmdd}"
                prev_v = date_to_val.get(prev_d)
                if prev_v is None:
                    # 1년 전 정확한 날짜 없으면 가장 가까운 ±5일 찾기
                    prev_dt = datetime.strptime(d, '%Y%m%d') - timedelta(days=365)
                    for offset in range(-5, 6):
                        cand = (prev_dt + timedelta(days=offset)).strftime('%Y%m%d')
                        if cand in date_to_val:
                            prev_v = date_to_val[cand]
                            break
                if prev_v is None or prev_v == 0:
                    continue
                yoy = ((v / prev_v) - 1.0) * 100.0
                transformed.append((d, round(yoy, 4)))
            except Exception:
                continue
        raw = transformed
    elif transform == 'mom':
        # 직전 관측치 대비
        transformed = []
        prev_v = None
        for d, v in raw:
            if prev_v is not None and prev_v != 0:
                transformed.append((d, round(((v / prev_v) - 1.0) * 100.0, 4)))
            prev_v = v
        raw = transformed
    # else 'level' — 그대로

    # OHLCV 스키마로 변환 (O=H=L=C=value, V=0)
    data = []
    for d, v in raw:
        data.append([d, v, v, v, v, 0])

    meta = {
        'series': series_id,
        'source': 'fred',
        'transform': transform,
        'start': data[0][0] if data else None,
        'end': data[-1][0] if data else None,
        'count': len(data),
    }
    return data, meta


if __name__ == '__main__':
    # CLI 테스트 — `python fetch_fred.py CPIAUCSL yoy 2020-01-01`
    if len(sys.argv) < 2:
        print("Usage: python fetch_fred.py <series_id> [transform] [start]")
        print("  transform = level | yoy | mom (default level)")
        sys.exit(1)
    series = sys.argv[1]
    transform = sys.argv[2] if len(sys.argv) > 2 else 'level'
    start = sys.argv[3] if len(sys.argv) > 3 else '2020-01-01'
    data, meta = fetch_fred_series(series, transform=transform, start=start)
    print(f"Meta: {meta}")
    if data:
        print(f"First row: {data[0]}")
        print(f"Last row:  {data[-1]}")
