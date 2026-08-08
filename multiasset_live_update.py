#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
멀티에셋 라이브 갱신 (base / live 2-파일 구조의 live 쪽)
=========================================================

왜 분리했나
-----------
`data/multiasset_data_v1.json` 은 18MB (349,312행, SPX 는 1927년부터)다.
이걸 매일 통째로 커밋하면 repo 가 감당이 안 되고, 페이지도 매번 18MB 를 받는다.
그래서 역사(base)와 최근(live)을 나눈다.

    data/multiasset_data_v1.json   base — 역사 전체. 갱신 드묾 (create_multiasset_data.py)
    data/multiasset_live_v1.json   live — 트레일링 윈도우만. 매일 자동 갱신 (이 스크립트)

Multiasset.html 의 loadMaData() 가 둘을 병렬로 받아 날짜 기준으로 merge 한다.
겹치는 구간은 **live 가 이긴다** — 수정주가 계수 변화가 자동 반영되는 효과.

대상
----
    assets  yfinance / FRED 소스 전부 (source='manual' 은 정적이라 제외)
    macros  FRED 13종
    cot     CFTC 주간
    crypto  Coinalyze (API 키 없으면 자동 skip — 실패해도 나머지는 저장)

사용
----
    python multiasset_live_update.py                 # 기본 (트레일링 500일)
    python multiasset_live_update.py --days 900
    python multiasset_live_update.py --no-crypto
    python multiasset_live_update.py --dry-run
"""
import argparse
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'multi-asset'))

from multiasset_assets import ASSETS                      # noqa: E402
from multiasset_macros import MACROS                      # noqa: E402
from multiasset_cot import COT_CONTRACTS                  # noqa: E402
from multiasset_crypto import CRYPTO_DERIV                # noqa: E402
from fetch_yahoo import fetch_yahoo_with_retry            # noqa: E402
from fetch_fred import fetch_fred_series                  # noqa: E402
from fetch_cftc import fetch_cot_with_retry               # noqa: E402

OUT_PATH = HERE / 'data' / 'multiasset_live_v1.json'
BASE_PATH = HERE / 'data' / 'multiasset_data_v1.json'


def utcnow_iso():
    try:
        from datetime import UTC
        return datetime.now(UTC).replace(tzinfo=None).isoformat(timespec='seconds')
    except ImportError:
        return datetime.utcnow().isoformat(timespec='seconds')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--days', type=int, default=500, help='트레일링 윈도우 (기본 500일)')
    ap.add_argument('--no-crypto', action='store_true')
    ap.add_argument('--no-cot', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    since = (datetime.utcnow() - timedelta(days=args.days)).strftime('%Y-%m-%d')
    out = {'assets': {}, 'macros': {}, 'cot': {}, 'crypto': {}, 'meta': {},
           'cutoff': since, 'generated_at': utcnow_iso(), 'version': 'live-v1'}
    fails = []

    # ---- assets ---------------------------------------------------------
    live_assets = {k: v for k, v in ASSETS.items() if v.get('source') != 'manual'}
    print('=== assets: %d (manual %d 제외) since %s ==='
          % (len(live_assets), len(ASSETS) - len(live_assets), since))
    for i, (key, spec) in enumerate(live_assets.items(), 1):
        ticker, source = spec['ticker'], spec.get('source', 'yfinance')
        try:
            if source == 'fred':
                raw, meta = fetch_fred_series(ticker, transform='level', start=since)
                data = [[r[0], r[1], r[1], r[1], r[1], 0] for r in raw]
            else:
                data, meta = fetch_yahoo_with_retry(ticker, start=since)
        except Exception as exc:                                    # noqa: BLE001
            data, meta = None, {'error': str(exc)}
        if data:
            out['assets'][key] = data
            out['meta'][key] = {'category': 'asset', **meta}
            print('  [%2d/%d] %-14s %5d bars  %s -> %s'
                  % (i, len(live_assets), key, len(data), meta.get('start', ''), meta.get('end', '')))
        else:
            fails.append(key)
            print('  [%2d/%d] %-14s FAIL (%s)' % (i, len(live_assets), key, meta.get('error', '?')))

    # ---- macros ---------------------------------------------------------
    print('=== macros: %d ===' % len(MACROS))
    for key, spec in MACROS.items():
        try:
            data, meta = fetch_fred_series(spec['series'], transform=spec.get('transform', 'level'), start=since)
        except Exception as exc:                                    # noqa: BLE001
            data, meta = None, {'error': str(exc)}
        if data:
            out['macros'][key] = data
            out['meta'][key] = {'category': 'macro', **meta}
            print('  %-14s %5d pts  -> %s' % (key, len(data), meta.get('end', '')))
        else:
            fails.append(key)
            print('  %-14s FAIL (%s)' % (key, meta.get('error', '?')))

    # ---- COT ------------------------------------------------------------
    if not args.no_cot:
        print('=== cot: %d ===' % len(COT_CONTRACTS))
        for key, spec in COT_CONTRACTS.items():
            try:
                data, meta = fetch_cot_with_retry(spec['code'], start=since)
            except Exception as exc:                                # noqa: BLE001
                data, meta = None, {'error': str(exc)}
            if data:
                out['cot'][key] = data
                out['meta']['COT_' + key] = {'category': 'cot', 'asset_key': key, **meta}
                print('  %-14s %5d weeks -> %s' % (key, len(data), meta.get('end', '')))
            else:
                fails.append('COT_' + key)
                print('  %-14s FAIL (%s)' % (key, meta.get('error', '?')))

    # ---- crypto (Coinalyze — API 키 없으면 조용히 skip) --------------------
    if not args.no_crypto:
        print('=== crypto: %d ===' % len(CRYPTO_DERIV))
        try:
            from fetch_coinalyze import (fetch_oi_aggregated, fetch_funding_history,
                                         fetch_with_retry as cz_retry)
            since_ts = int(datetime.strptime(since, '%Y-%m-%d').timestamp())
            for key, spec in CRYPTO_DERIV.items():
                oi, oim = cz_retry(fetch_oi_aggregated, spec['oi_symbols'], from_ts=since_ts)
                fd, fdm = cz_retry(fetch_funding_history, spec['funding_symbol'], from_ts=since_ts)
                if oi or fd:
                    out['crypto'][key] = {'oi': oi or [], 'funding': fd or []}
                    out['meta']['CRYPTO_' + key] = {
                        'category': 'crypto', 'asset_key': key,
                        'oi_count': oim.get('count', 0), 'fund_count': fdm.get('count', 0),
                        'end': oim.get('end', ''),
                    }
                    print('  %-6s oi %d / funding %d -> %s' % (key, len(oi or []), len(fd or []), oim.get('end', '')))
                else:
                    fails.append('CRYPTO_' + key)
                    print('  %-6s FAIL (%s)' % (key, oim.get('error', '?')))
        except Exception as exc:                                    # noqa: BLE001
            print('  crypto skip: %s' % exc)

    # ---- 저장 -----------------------------------------------------------
    n_a, n_m = len(out['assets']), len(out['macros'])
    if n_a == 0 and n_m == 0:
        sys.exit('[ERROR] assets·macros 모두 0건 — 저장하지 않음')

    if args.dry_run:
        print('[dry-run] assets %d / macros %d / cot %d / crypto %d / fails %s'
              % (n_a, n_m, len(out['cot']), len(out['crypto']), fails))
        return

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = str(OUT_PATH) + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        json.dump(out, fh, ensure_ascii=False, separators=(',', ':'))
    os.replace(tmp, OUT_PATH)

    size_mb = OUT_PATH.stat().st_size / (1024 * 1024)
    print('[SAVED] %s  %.2f MB  (assets %d / macros %d / cot %d / crypto %d)'
          % (OUT_PATH.name, size_mb, n_a, n_m, len(out['cot']), len(out['crypto'])))
    if fails:
        print('[WARN] 실패 %d건: %s' % (len(fails), ', '.join(fails)))
    if BASE_PATH.exists():
        print('[INFO] base %s 는 미변경 (%.1f MB)' % (BASE_PATH.name, BASE_PATH.stat().st_size / (1024 * 1024)))


if __name__ == '__main__':
    main()
