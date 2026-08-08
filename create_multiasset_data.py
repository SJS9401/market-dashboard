#!/usr/bin/env python3
"""
Multi-asset 데이터 오케스트레이터.

실행:
    cd C:\\Users\\ruzby\\Documents\\Claude\\Scheduled
    python create_multiasset_data.py                    # 전체 fetch
    python create_multiasset_data.py --only WTI SPX     # 특정 자산만
    python create_multiasset_data.py --macros-only      # 매크로만 (기존 자산 보존)
    python create_multiasset_data.py --assets-only      # 자산만 (기존 매크로 보존)
    python create_multiasset_data.py --since 2020-01-01

출력 스키마:
    {
      "assets": { "WTI": [[YYYYMMDD,O,H,L,C,V], ...], ... },
      "macros": { "CPI": [[YYYYMMDD,V,V,V,V,0], ...], ... },
      "meta":   { "WTI": {...}, "CPI": {...}, ... },
      "generated_at": "...",
      "version": "v1"
    }

partial fetch (--macros-only / --assets-only / --only) 시 기존 JSON 의
다른 카테고리 데이터는 자동 보존.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'multi-asset'))

from multiasset_assets import ASSETS, BENCHMARKS, KR_INDICES
from multiasset_macros import MACROS
from multiasset_cot import COT_CONTRACTS
from multiasset_crypto import CRYPTO_DERIV
from fetch_yahoo import fetch_yahoo_with_retry
from fetch_fred import fetch_fred_series
from fetch_cftc import fetch_cot_with_retry
from fetch_coinalyze import fetch_oi_aggregated, fetch_funding_history, fetch_with_retry as fetch_coinalyze_retry


def utcnow_iso():
    """Python 3.14 deprecation 회피."""
    try:
        from datetime import UTC
        return datetime.now(UTC).replace(tzinfo=None).isoformat(timespec='seconds')
    except ImportError:
        return datetime.utcnow().isoformat(timespec='seconds')


def main():
    parser = argparse.ArgumentParser(description='Multi-asset cycle 데이터 생성')
    parser.add_argument('--only', nargs='*', help='특정 자산/매크로/COT/crypto 키만 fetch')
    parser.add_argument('--macros-only', action='store_true', help='매크로만 fetch (기타 보존)')
    parser.add_argument('--assets-only', action='store_true', help='자산만 fetch (기타 보존)')
    parser.add_argument('--cot-only',    action='store_true', help='COT 만 fetch (기타 보존)')
    parser.add_argument('--crypto-only', action='store_true', help='Crypto 만 fetch (기타 보존)')
    parser.add_argument('--no-cot',      action='store_true', help='COT skip (CFTC API 일시 장애 시)')
    parser.add_argument('--no-crypto',   action='store_true', help='Crypto skip (Coinalyze 일시 장애 시)')
    parser.add_argument('--since', default='1900-01-01', help='시작일 YYYY-MM-DD (default 1900: long-history 자산 max 받기)')
    parser.add_argument('--out', default=None, help='출력 JSON 경로 override')
    parser.add_argument('--include-kr-indices', action='store_true', help='KOSPI/KOSDAQ 도 fetch')
    args = parser.parse_args()

    output = {
        'assets': {},
        'macros': {},
        'cot':    {},
        'crypto': {},
        'meta':   {},
        'generated_at': utcnow_iso(),
        'version': 'v1',
    }

    # 기존 JSON 병합 — partial fetch 시 다른 카테고리 보존
    existing_path = HERE / 'data' / 'multiasset_data_v1.json'
    if (args.macros_only or args.assets_only or args.cot_only or args.crypto_only or args.only) and existing_path.exists():
        try:
            with open(existing_path, 'r', encoding='utf-8') as f:
                existing = json.load(f)
            output['assets'] = existing.get('assets', {})
            output['macros'] = existing.get('macros', {})
            output['cot']    = existing.get('cot', {})
            output['crypto'] = existing.get('crypto', {})
            output['meta']   = existing.get('meta', {})
            print(f"\n=== Loaded existing JSON ({existing_path.name}) — preserving prior data ===")
            print(f"  prior assets: {len(output['assets'])}, prior macros: {len(output['macros'])}, prior cot: {len(output['cot'])}, prior crypto: {len(output['crypto'])}, prior meta: {len(output['meta'])}")
        except Exception as e:
            print(f"WARN: failed to load existing JSON ({e}) — starting fresh", file=sys.stderr)

    # ========================================================
    # 자산 fetch (Yahoo)
    # ========================================================
    if not args.macros_only and not args.cot_only and not args.crypto_only:
        targets = list(ASSETS.keys())
        if args.only:
            targets = [t for t in targets if t in args.only]

        print(f"\n=== Fetching {len(targets)} assets (Yahoo + FRED long-history) ===")
        for i, key in enumerate(targets, 1):
            spec = ASSETS[key]
            ticker = spec['ticker']
            source = spec.get('source', 'yfinance')
            src_tag = '[FRED]' if source == 'fred' else '[YH]  '
            print(f"  [{i:3d}/{len(targets)}] {key:14s} <- {ticker:18s} {src_tag} ...", end='', flush=True)
            if source == 'fred':
                # Phase E-1: FRED close → OHLC (O=H=L=C=close, V=0). long-history 자산용.
                fred_data, fred_meta = fetch_fred_series(ticker, transform='level', start=args.since)
                data = [[r[0], r[1], r[1], r[1], r[1], 0] for r in fred_data]
                meta = fred_meta
            elif source == 'manual':
                # Phase E-3: manual CSV/XLSX (Shiller, Macrotrends 등). monthly close-only.
                from fetch_manual import fetch_manual
                data, meta = fetch_manual(spec)
            else:
                data, meta = fetch_yahoo_with_retry(ticker, start=args.since)
            if data:
                output['assets'][key] = data
                output['meta'][key] = {
                    'category': 'asset',
                    'desc': spec.get('desc', ''),
                    **meta,
                }
                if 'note' in spec:
                    output['meta'][key]['note'] = spec['note']
                print(f"  {meta['count']:5d} bars  ({meta.get('start','')} -> {meta.get('end','')})")
            else:
                output['meta'][key] = {
                    'category': 'asset',
                    'desc': spec.get('desc', ''),
                    'ticker': ticker,
                    'source': 'yfinance',
                    'error': meta.get('error', 'unknown'),
                }
                print(f"  FAIL ({meta.get('error', 'unknown')})")

        if args.include_kr_indices:
            for key, spec in KR_INDICES.items():
                if args.only and key not in args.only:
                    continue
                ticker = spec['ticker']
                print(f"  KR index: {key:14s} <- {ticker:14s} ...", end='', flush=True)
                data, meta = fetch_yahoo_with_retry(ticker, start=args.since)
                if data:
                    output['assets'][key] = data
                    output['meta'][key] = {'category': 'kr_index', 'desc': spec.get('desc', ''), **meta}
                    print(f"  {meta['count']:5d} bars")
                else:
                    print(f"  FAIL ({meta.get('error', 'unknown')})")

    # ========================================================
    # 매크로 fetch (FRED)
    # ========================================================
    if not args.assets_only and not args.cot_only and not args.crypto_only:
        targets = list(MACROS.keys())
        if args.only:
            targets = [t for t in targets if t in args.only]

        print(f"\n=== Fetching {len(targets)} macros (FRED) ===")
        for i, key in enumerate(targets, 1):
            spec = MACROS[key]
            series = spec['series']
            transform = spec.get('transform', 'level')
            print(f"  [{i:3d}/{len(targets)}] {key:12s} <- {series:14s} [{transform:5s}] ...", end='', flush=True)
            data, meta = fetch_fred_series(series, transform=transform, start=args.since)
            if data:
                output['macros'][key] = data
                output['meta'][key] = {
                    'category': 'macro',
                    'desc': spec.get('desc', ''),
                    'unit': spec.get('unit', ''),
                    'freq': spec.get('freq', ''),
                    **meta,
                }
                print(f"  {meta['count']:5d} pts  ({meta.get('start','')} -> {meta.get('end','')})")
            else:
                output['meta'][key] = {
                    'category': 'macro',
                    'desc': spec.get('desc', ''),
                    'series': series,
                    'source': 'fred',
                    'error': meta.get('error', 'unknown'),
                }
                print(f"  FAIL ({meta.get('error', 'unknown')})")

    # ========================================================
    # COT fetch (CFTC Socrata) — Phase B-1
    # ========================================================
    if not args.assets_only and not args.macros_only and not args.crypto_only and not args.no_cot:
        targets = list(COT_CONTRACTS.keys())
        if args.only:
            targets = [t for t in targets if t in args.only]

        if targets:
            print(f"\n=== Fetching {len(targets)} COT contracts (CFTC) ===")
            for i, key in enumerate(targets, 1):
                spec = COT_CONTRACTS[key]
                code = spec['code']
                print(f"  [{i:3d}/{len(targets)}] {key:12s} <- code {code} ...", end='', flush=True)
                data, meta = fetch_cot_with_retry(code, start=args.since)
                cot_meta_key = 'COT_' + key  # asset 키와 충돌 방지 (예: 'COT_WTI' vs asset 'WTI')
                if data:
                    output['cot'][key] = data
                    output['meta'][cot_meta_key] = {
                        'category': 'cot',
                        'asset_key': key,
                        'desc': spec.get('desc', ''),
                        **meta,
                    }
                    if 'note' in spec:
                        output['meta'][cot_meta_key]['note'] = spec['note']
                    print(f"  {meta['count']:5d} weeks ({meta.get('start','')} -> {meta.get('end','')})")
                else:
                    output['meta'][cot_meta_key] = {
                        'category': 'cot',
                        'asset_key': key,
                        'desc': spec.get('desc', ''),
                        'contract_code': code,
                        'source': 'cftc-socrata',
                        'error': meta.get('error', 'unknown'),
                    }
                    print(f"  FAIL ({meta.get('error', 'unknown')})")
        else:
            print(f"\n=== COT skip (no targets match --only filter) ===")

    # ========================================================
    # Crypto fetch (Coinalyze) — Phase C-2
    # ========================================================
    if not args.assets_only and not args.macros_only and not args.cot_only and not args.no_crypto:
        targets = list(CRYPTO_DERIV.keys())
        if args.only:
            targets = [t for t in targets if t in args.only]

        if targets:
            print(f"\n=== Fetching {len(targets)} crypto contracts (Coinalyze, 4-exch aggregated) ===")
            for i, key in enumerate(targets, 1):
                spec = CRYPTO_DERIV[key]
                oi_symbols = spec['oi_symbols']
                fund_symbol = spec['funding_symbol']

                # OI aggregated (multi-exchange sum)
                from datetime import datetime as _dt
                since_ts = int(_dt.strptime(args.since, '%Y-%m-%d').timestamp()) if args.since else None
                print(f"  [{i:2d}/{len(targets)}] {key:6s} OI  <- {len(oi_symbols)} symbols aggregated ...", end='', flush=True)
                print(f"  [{i:2d}/{len(targets)}] {key:6s} OI  <- {len(oi_symbols)} symbols aggregated ...", end='', flush=True)
                oi_data, oi_meta = fetch_coinalyze_retry(fetch_oi_aggregated, oi_symbols, from_ts=since_ts)
                print(f"  {oi_meta.get('count', 0):5d} days  ({oi_meta.get('start','')} -> {oi_meta.get('end','')})")

                # Funding rate (single symbol, primary exchange)
                print(f"          {key:6s} Fnd <- {fund_symbol} ...", end='', flush=True)
                fund_data, fund_meta = fetch_coinalyze_retry(fetch_funding_history, fund_symbol, from_ts=since_ts)
                print(f"  {fund_meta.get('count', 0):5d} days  ({fund_meta.get('start','')} -> {fund_meta.get('end','')})")

                # Schema: crypto[key] = { oi: [[date, val], ...], funding: [...] }
                output['crypto'][key] = {
                    'oi':      oi_data,
                    'funding': fund_data,
                }
                cm_key = 'CRYPTO_' + key
                output['meta'][cm_key] = {
                    'category':       'crypto',
                    'asset_key':      key,
                    'desc':           spec.get('desc', ''),
                    'oi_symbols':     oi_symbols,
                    'funding_symbol': fund_symbol,
                    'source':         'coinalyze',
                    'oi_unit':        'BASE_ASSET (BTC/ETH contracts)',
                    'funding_unit':   '% per 8h',
                    'oi_count':       oi_meta.get('count', 0),
                    'fund_count':     fund_meta.get('count', 0),
                    'start':          oi_meta.get('start', ''),
                    'end':            oi_meta.get('end', ''),
                }
                if 'note' in spec:
                    output['meta'][cm_key]['note'] = spec['note']
                if 'error' in oi_meta:
                    output['meta'][cm_key]['oi_error'] = oi_meta['error']
                if 'error' in fund_meta:
                    output['meta'][cm_key]['fund_error'] = fund_meta['error']
        else:
            print(f"\n=== Crypto skip (no targets match --only filter) ===")

    # ========================================================
    # 출력
    # ========================================================
    output['generated_at'] = utcnow_iso()

    out_paths = []
    if args.out:
        out_paths.append(Path(args.out))
    else:
        out_paths.append(HERE / 'data' / 'multiasset_data_v1.json')
        repo_dir = HERE.parent / 'market-dashboard' / 'data'
        if repo_dir.exists():
            out_paths.append(repo_dir / 'multiasset_data_v1.json')

    print(f"\n=== Writing output ===")
    for p in out_paths:
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, separators=(',', ':'))
        size_mb = p.stat().st_size / (1024 * 1024)
        print(f"  -> {p}  ({size_mb:.2f} MB)")

    n_assets = sum(1 for v in output['meta'].values() if v.get('category') == 'asset' and 'error' not in v)
    n_macros = sum(1 for v in output['meta'].values() if v.get('category') == 'macro' and 'error' not in v)
    n_cot    = sum(1 for v in output['meta'].values() if v.get('category') == 'cot'   and 'error' not in v)
    n_crypto = sum(1 for v in output['meta'].values() if v.get('category') == 'crypto' and 'oi_error' not in v and 'fund_error' not in v)
    n_errors = sum(1 for v in output['meta'].values() if 'error' in v or 'oi_error' in v or 'fund_error' in v)
    print(f"\n=== Summary ===")
    print(f"  Assets OK : {n_assets}")
    print(f"  Macros OK : {n_macros}")
    print(f"  COT    OK : {n_cot}")
    print(f"  Crypto OK : {n_crypto}")
    print(f"  Errors    : {n_errors}")
    print(f"  Generated : {output['generated_at']}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
