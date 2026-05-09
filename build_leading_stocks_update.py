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


# 종목/지수 ID → 티커 매핑 (meta 에 ticker 누락 시 fallback).
# 키움 normalize 후에도 자동 갱신이 정확히 동작하도록 보장.
STOCK_TICKERS_FALLBACK = {
    # 지수
    "kospi":          "^KS11",
    "kosdaq":         "^KQ11",
    "sp500":          "^GSPC",
    "nasdaq":         "^IXIC",
    # 한국 종목 (LEADING_STOCKS 기준)
    "spc_samlib":      "005610.KS",
    "sk_telecom":      "017670.KS",
    "coway":           "021240.KS",
    "hyundai_elev":    "017800.KS",
    "hyundai_mipo":    "010620.KQ",
    "kia":             "000270.KS",
    "hanmi_science":   "008930.KS",
    "amorepacific":    "090430.KS",
    "celltrion":       "068270.KS",
    "sk_hynix":        "000660.KS",
    "seegene":         "096530.KQ",
    "hmm":             "011200.KS",
    "ecopro":          "086520.KQ",
    "hanmi_semi":      "042700.KQ",
    "alteogen":        "196170.KQ",
    "hanwha_ocean":    "042660.KS",
    "doosan_enerbil":  "034020.KS",
    "samsung_elec":    "005930.KS",
    "hyundai_const":   "000720.KS",
    "daishin_sec":     "003540.KS",
    "kepco":           "015760.KS",
    "posco":           "005490.KS",
    "hyundai_motor":   "005380.KS",
    "lg_chem":         "051910.KS",
    "s_oil":           "010950.KS",
}


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
        ticker = info.get("ticker") or STOCK_TICKERS_FALLBACK.get(stock_id)
        if not ticker:
            print(f"  [skip] {stock_id}: ticker 없음 (fallback에도 없음)")
            continue
        # meta 에 ticker 가 없었으면 채워 넣음 (다음 실행부터 빠르게)
        if "ticker" not in info:
            info["ticker"] = ticker
            meta[stock_id] = info

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
    """
    Leading_stocks.html 의 데이터 영역만 부분 patch (디자인/CSS/JS 보존).

    동작:
      1. create_leading_stocks.py 를 임시 경로 (--output) 에 호출 → 새 HTML 생성
      2. 새 HTML 에서 `// ===== DATA =====` ~ `// ===== HELPERS =====` 영역 추출
      3. 기존 Leading_stocks.html 의 같은 영역만 새 데이터로 교체 → 저장

    안전 fallback:
      - 기존 HTML 없거나, marker 못 찾거나, 임시 빌더 실패 시 → 통째 재생성 (구 동작)
    """
    import subprocess
    import re
    import tempfile

    builder = Path(__file__).parent / "create_leading_stocks.py"
    if not builder.exists():
        print(f"[WARN] {builder} 없음 — HTML 재빌드 skip")
        return False

    # 기존 HTML 위치 결정 (create_leading_stocks.py 와 동일 우선순위)
    candidate_dirs = [
        Path(__file__).parent.parent / "mnt" / "Documents--3 시장 사이클 전략",
        Path(__file__).parent,
    ]
    target_html = None
    for d in candidate_dirs:
        candidate = d / "Leading_stocks.html"
        if candidate.exists():
            target_html = candidate
            break

    # 임시 파일 경로 (새 HTML 생성용)
    with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as tmp:
        tmp_path = Path(tmp.name)

    try:
        print(f"\n[*] HTML 데이터 영역 patch 시도: {target_html or '(target 없음 → 통째 생성)'}")
        # --output 옵션으로 임시 경로 출력
        r = subprocess.run(
            [sys.executable, str(builder), "--output", str(tmp_path)],
            capture_output=True, text=True, cwd=str(builder.parent)
        )
        if r.returncode != 0:
            print(f"[ERROR] 임시 빌더 실행 실패: {r.stderr[-500:]}")
            return _rebuild_html_fallback(builder)

        new_html = tmp_path.read_text(encoding='utf-8')
        # 데이터 영역 추출 — `// ===== DATA =====` ~ `// ===== HELPERS =====` 사이
        marker_pattern = r'(// ===== DATA =====\n)([\s\S]*?)(\n// ===== HELPERS =====)'
        new_match = re.search(marker_pattern, new_html)
        if not new_match:
            print("[WARN] 임시 HTML 에서 데이터 영역 marker 못 찾음 — 통째 재생성으로 fallback")
            return _rebuild_html_fallback(builder)

        # target HTML 없으면 임시 HTML 자체를 target 위치로 이동 (첫 빌드)
        if target_html is None:
            target_html = candidate_dirs[0] / "Leading_stocks.html"
            target_html.parent.mkdir(parents=True, exist_ok=True)
            target_html.write_text(new_html, encoding='utf-8')
            print(f"✓ 첫 빌드 — 통째 생성: {target_html}")
            return True

        # 기존 HTML 의 데이터 영역만 교체
        old_html = target_html.read_text(encoding='utf-8')
        old_match = re.search(marker_pattern, old_html)
        if not old_match:
            print("[WARN] 기존 HTML 에서 marker 못 찾음 — 통째 재생성으로 fallback")
            return _rebuild_html_fallback(builder)

        # 새 데이터 영역으로 교체 (start_marker + new_data + end_marker)
        new_data_block = new_match.group(1) + new_match.group(2) + new_match.group(3)
        patched = (
            old_html[:old_match.start()]
            + new_data_block
            + old_html[old_match.end():]
        )

        target_html.write_text(patched, encoding='utf-8')
        sz = target_html.stat().st_size
        print(f"✓ 데이터 영역 patch 완료: {target_html} ({sz:,} bytes)")
        print(f"  - 디자인/CSS/JS 보존, 데이터 영역만 갱신")
        return True

    finally:
        try:
            tmp_path.unlink(missing_ok=True)
        except Exception:
            pass


def _rebuild_html_fallback(builder):
    """patch 실패 시 fallback — create_leading_stocks.py 를 default path 로 호출 (통째 재생성)"""
    import subprocess
    print(f"[*] fallback: create_leading_stocks.py 통째 재생성")
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
