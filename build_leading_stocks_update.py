#!/usr/bin/env python3
"""
ls_data_v3.json 자동 갱신 — yfinance .KS/.KQ로 incremental fetch
- 각 종목의 마지막 거래일 + 1 ~ 오늘까지 새 일자만 추가
- 출력 형식: [YYYYMMDD, O, H, L, C, volume_eok]  (volume_eok = volume × close ÷ 1e8)
- meta.{stock_id}.{end, count} 자동 업데이트

실행:
  python build_leading_stocks_update.py [--target ls_data_v3.json] [--dry-run]

GitHub Actions cron 매일 KST 17:30 호출.

필요 패키지: yfinance, pandas
"""
import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


def fetch_yfinance(ticker, start_yyyymmdd, end_yyyymmdd):
    """yfinance OHLCV 받기. 반환: [(YYYYMMDD, O, H, L, C, vol_eok)]"""
    import yfinance as yf
    df = yf.download(ticker, start=start_yyyymmdd, end=end_yyyymmdd,
                     progress=False, auto_adjust=False)
    if df is None or df.empty:
        return []
    out = []
    for idx, row in df.iterrows():
        d = idx.strftime("%Y%m%d") if hasattr(idx, "strftime") else str(idx)[:10].replace("-", "")
        try:
            o = row["Open"]; h = row["High"]; l = row["Low"]; c = row["Close"]; v = row.get("Volume", 0)
            # multi-index column 처리 (yfinance가 가끔 ('Open', ticker) 형태)
            if hasattr(o, "iloc"):
                o = o.iloc[0]; h = h.iloc[0]; l = l.iloc[0]; c = c.iloc[0]; v = v.iloc[0] if hasattr(v, "iloc") else v
            o = float(o); h = float(h); l = float(l); c = float(c); v = float(v or 0)
            if any(x != x for x in (o, h, l, c)):  # NaN
                continue
        except Exception:
            continue
        # 거래대금(억) = 거래량 × 종가 ÷ 1e8
        vol_eok = round(v * c / 1e8, 2)
        out.append([d, round(o), round(h), round(l), round(c), vol_eok])
    return out


def patch(fp, dry_run=False):
    data = json.loads(Path(fp).read_text(encoding="utf-8"))
    stocks = data.get("stocks", {})
    meta = data.get("meta", {})
    if not stocks:
        print("[ERROR] stocks 없음")
        return False

    today = datetime.now().date()
    today_str = today.strftime("%Y%m%d")
    print(f"[*] 오늘: {today_str}, 종목 수: {len(stocks)}")

    changed_stocks = 0
    new_rows_total = 0

    for stock_id, ts in stocks.items():
        if stock_id == "last_merge":  # meta 마커
            continue
        if not isinstance(ts, list) or not ts:
            continue
        info = meta.get(stock_id, {})
        ticker = info.get("ticker")
        if not ticker:
            print(f"  [skip] {stock_id}: ticker 없음")
            continue

        last_date = ts[-1][0] if isinstance(ts[-1], list) else None
        if not last_date:
            continue
        try:
            last_dt = datetime.strptime(last_date, "%Y%m%d").date()
        except ValueError:
            continue

        if last_dt >= today:
            continue

        start = (last_dt + timedelta(days=1)).strftime("%Y-%m-%d")
        end = (today + timedelta(days=1)).strftime("%Y-%m-%d")

        try:
            new_rows = fetch_yfinance(ticker, start, end)
        except Exception as e:
            print(f"  [fail] {stock_id} ({ticker}): {e}")
            continue

        if not new_rows:
            continue

        # 기존 마지막 일자 이후만 (안전망)
        new_rows = [r for r in new_rows if r[0] > last_date]
        if not new_rows:
            continue

        ts.extend(new_rows)
        meta_entry = meta.get(stock_id, {})
        if meta_entry:
            meta_entry["end"] = new_rows[-1][0]
            meta_entry["count"] = len(ts)
        changed_stocks += 1
        new_rows_total += len(new_rows)
        print(f"  ✓ {stock_id:20s} ({ticker}) +{len(new_rows)} rows ({new_rows[0][0]}~{new_rows[-1][0]})")

    if changed_stocks == 0:
        print("\n변경 없음")
        return False

    data["generated"] = datetime.now(timezone.utc).isoformat()
    print(f"\n총 변경: {changed_stocks} 종목, {new_rows_total} new rows")

    if dry_run:
        print("[dry-run] 저장 안 함")
        return True

    # JSON 저장 — separators 압축으로 크기 절약
    Path(fp).write_text(
        json.dumps(data, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8"
    )
    sz = Path(fp).stat().st_size
    print(f"✓ 저장: {fp} ({sz:,} bytes)")
    return True


def rebuild_html():
    """create_leading_stocks.py 실행 → Leading_stocks.html 재생성"""
    import subprocess
    builder = Path(__file__).parent / "create_leading_stocks.py"
    if not builder.exists():
        print(f"[WARN] {builder} 없음 — HTML 재빌드 skip")
        return False
    print(f"\n[*] HTML 재빌드: {builder}")
    r = subprocess.run([sys.executable, str(builder)], capture_output=True, text=True, cwd=str(builder.parent))
    print(r.stdout[-500:] if r.stdout else "")
    if r.returncode != 0:
        print(f"[ERROR] HTML 재빌드 실패: {r.stderr[-500:]}")
        return False
    return True


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--target", default="ls_data_v3.json")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--no-rebuild", action="store_true", help="HTML 재빌드 skip (테스트용)")
    args = p.parse_args()

    if not Path(args.target).exists():
        print(f"[ERROR] {args.target} 없음")
        sys.exit(1)

    print(f"[*] 대상: {args.target}")
    print(f"[*] 시각: {datetime.now(timezone.utc).isoformat()}")
    changed = patch(args.target, dry_run=args.dry_run)

    if changed and not args.dry_run and not args.no_rebuild:
        rebuild_html()

    sys.exit(0 if changed else 1)


if __name__ == "__main__":
    main()
