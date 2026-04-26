#!/usr/bin/env python3
"""
Market_cycle.html 자동 갱신 스크립트
- yfinance로 ^GSPC (S&P500), ^IXIC (NASDAQ), ^KS11 (KOSPI), ^KQ11 (KOSDAQ) historical fetch
- Market_cycle.html 안의 FULL_HISTORY (월말 종가) + CYCLES priceDatasets (active 사이클의 weekly) patch
- 마지막 데이터 이후만 incremental append (정합성 보호)

실행:
  python build_market_cycle_update.py [--target Market_cycle.html]

GitHub Actions cron 매일 KST 17:00 (UTC 08:00) 호출.

필요 패키지:
  pip install yfinance pandas
"""
import argparse
import json
import re
import sys
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

# yfinance import는 main에서 (lazy)


YAHOO_TICKERS = {
    "SP500": "^GSPC",
    "NASDAQ": "^IXIC",
    "KOSPI": "^KS11",
    "KOSDAQ": "^KQ11",
}


def fetch_yfinance(ticker, start_yyyymmdd, end_yyyymmdd):
    """yfinance에서 일별 OHLC 받기. 종가만 리턴."""
    import yfinance as yf
    df = yf.download(ticker, start=start_yyyymmdd, end=end_yyyymmdd, progress=False, auto_adjust=False)
    if df is None or df.empty:
        return []
    out = []
    for idx, row in df.iterrows():
        d = idx.strftime("%Y-%m-%d") if hasattr(idx, "strftime") else str(idx)[:10]
        try:
            close = float(row["Close"]) if not (row["Close"] is None or (isinstance(row["Close"], float) and row["Close"] != row["Close"])) else None
        except Exception:
            close = None
        if close is None:
            # multi-index column case
            try:
                close = float(row[("Close", ticker)])
            except Exception:
                continue
        out.append([d, round(close, 2)])
    return out


def to_monthly_eom(daily_pairs):
    """일별 → 월말 종가 (FULL_HISTORY 형식)."""
    by_month = {}
    for d, c in daily_pairs:
        ym = d[:7]
        if ym not in by_month or d > by_month[ym][0]:
            by_month[ym] = (d, c)
    return [[ym + "-01", by_month[ym][1]] for ym in sorted(by_month.keys())]


def to_weekly_eow(daily_pairs):
    """일별 → 주의 마지막 거래일 종가 (CYCLES weekly 형식)."""
    by_week = {}
    for d, c in daily_pairs:
        dt = datetime.strptime(d, "%Y-%m-%d")
        iso_year, iso_week, _ = dt.isocalendar()
        k = (iso_year, iso_week)
        if k not in by_week or d > by_week[k][0]:
            by_week[k] = (d, c)
    return [[by_week[k][0], by_week[k][1]] for k in sorted(by_week.keys())]


def merge_series(existing, new):
    """existing + new (date 중복 시 new 우선). 정렬 + dedup."""
    m = {d: v for d, v in existing}
    for d, v in new:
        m[d] = v
    return [[d, m[d]] for d in sorted(m.keys())]


def patch_html(html_path, dry_run=False):
    html = Path(html_path).read_text(encoding="utf-8")

    # FULL_HISTORY parse
    m = re.search(r"const FULL_HISTORY = (\{.*?\});\n", html, re.DOTALL)
    if not m:
        print("[ERROR] FULL_HISTORY 못찾음")
        sys.exit(1)
    fh_text = m.group(1)
    fh = json.loads(fh_text)

    # CYCLES parse
    m2 = re.search(r"const CYCLES = (\[.*?\]);\nconst FULL_HISTORY", html, re.DOTALL)
    if not m2:
        print("[ERROR] CYCLES 못찾음")
        sys.exit(1)
    cycles_text = m2.group(1)
    cycles = json.loads(cycles_text)

    today = datetime.now().strftime("%Y-%m-%d")
    today_dt = datetime.now()

    fh_changed = False
    cy_changed = 0

    for idx_key, ticker in YAHOO_TICKERS.items():
        if idx_key not in fh:
            print(f"  [skip] FULL_HISTORY[{idx_key}] 없음")
            continue
        existing = fh[idx_key]  # [[date, value], ...]
        last_date = max(d for d, v in existing) if existing else "1985-01-01"
        # 다음날부터 오늘까지 받기
        last_dt = datetime.strptime(last_date, "%Y-%m-%d")
        start_dt = last_dt + timedelta(days=1)
        # 같은 달 안에 미세 갱신 위해 1주일 이전부터
        start_dt = min(start_dt, last_dt - timedelta(days=7))
        if start_dt > today_dt:
            print(f"  [{idx_key}] 이미 최신 ({last_date}), skip")
            continue

        start_str = start_dt.strftime("%Y-%m-%d")
        end_str = (today_dt + timedelta(days=1)).strftime("%Y-%m-%d")
        print(f"  [{idx_key}] yfinance fetch {ticker} {start_str}~{end_str}")
        daily = fetch_yfinance(ticker, start_str, end_str)
        if not daily:
            print(f"    (no new data)")
            continue
        print(f"    {len(daily)} new daily rows ({daily[0][0]} ~ {daily[-1][0]})")

        # FULL_HISTORY: 월말 종가
        new_monthly = to_monthly_eom(daily)
        merged = merge_series(existing, new_monthly)
        if merged != existing:
            fh[idx_key] = merged
            fh_changed = True
            print(f"    FULL_HISTORY[{idx_key}] {len(existing)} → {len(merged)}")

        # CYCLES priceDatasets: end가 1년 이내인 사이클의 활성 갱신
        new_weekly = to_weekly_eow(daily)
        cutoff = (today_dt - timedelta(days=365)).strftime("%Y-%m-%d")
        for c in cycles:
            if c.get("end", "") < cutoff:
                continue
            if idx_key not in c.get("indices", []):
                continue
            for ds in c.get("priceDatasets", []):
                if ds.get("label") != idx_key:
                    continue
                old = ds.get("data", [])
                merged_w = merge_series(old, new_weekly)
                if merged_w != old:
                    ds["data"] = merged_w
                    cy_changed += 1

    if not (fh_changed or cy_changed):
        print("\n변경 없음 — exit 1")
        return False

    # 새 JSON 직렬화 + replace
    new_fh_text = json.dumps(fh, ensure_ascii=False)
    new_cy_text = json.dumps(cycles, ensure_ascii=False)
    html_new = html.replace(fh_text, new_fh_text)
    html_new = html_new.replace(cycles_text, new_cy_text)

    print(f"\n변경 — FULL_HISTORY={fh_changed}, CYCLES priceDatasets ds 갱신={cy_changed}")
    if dry_run:
        print("[dry-run] 저장 안 함")
        return True

    Path(html_path).write_text(html_new, encoding="utf-8")
    print(f"✓ 저장: {html_path}")
    return True


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--target", default="Market_cycle.html")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    if not os.path.exists(args.target):
        print(f"[ERROR] {args.target} 없음")
        sys.exit(1)

    print(f"[*] 대상: {args.target}")
    print(f"[*] 시각: {datetime.now(timezone.utc).isoformat()}")
    changed = patch_html(args.target, dry_run=args.dry_run)
    sys.exit(0 if changed else 1)


if __name__ == "__main__":
    main()
