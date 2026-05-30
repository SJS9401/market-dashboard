"""
yahoo_dashboard_backfill.py
---------------------------
dashboard.html 의 야후 의존 데이터를 자체 JSON 으로 cache.

배경 (2026-05-27):
  - 야후 query1.finance.yahoo.com 가 sjs9401.github.io origin 에 503 차단
  - corsproxy.io / api.allorigins.win 같은 무료 CORS proxy 들도 fragile (오늘 다운, 내일 부활)
  - 사이트 카드 로딩 멈춤 사고 재발 방지 위해 GitHub Actions 가 매일 yfinance 로 fetch + JSON commit
  - dashboard.html getData() 가 JSON cache 우선 사용 + CORS proxy 는 fallback

대상 symbol (dashboard.html Network 탭 기준):
  ^KS11      KOSPI Composite
  EWY        S Korea iShares ETF (KOSPI fallback)
  ^IXIC      Nasdaq Composite
  ^NDX       Nasdaq 100
  QQQ        Nasdaq 100 ETF (fallback)
  TLT        20+Y Treasury ETF (시장폭 카드)
  ^VIX       S&P VIX
  ^VIX9D     9-Day VIX
  HYG        High Yield Bond ETF (시장폭 카드)
  USDKRW=X   USD/KRW spot
  KRW=X      USD/KRW alt
  148070.KS  KOSEF 단기자금 (kr_breadth 보조 ?)

출력: data/yahoo_dashboard.json
  {
    "meta": {"updated": "YYYY-MM-DDTHH:MM:SSZ", "symbols": [...], "period": "10y"},
    "data": {
      "<symbol>": {
        "candles": [{"time":"YYYY-MM-DD", "open":N, "high":N, "low":N, "close":N}, ...],
        "price": N,    // 마지막 close
        "prev": N      // 마지막 직전 close
      },
      ...
    }
  }

CLI:
  py yahoo_dashboard_backfill.py
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(THIS_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
OUT_PATH = os.path.join(DATA_DIR, "yahoo_dashboard.json")

# dashboard.html 의 yahoo symbol 전수 (Network 탭 + FALLBACKS dict 분석 결과)
SYMBOLS = [
    "^KS11",        # KOSPI
    "EWY",          # S Korea ETF (KOSPI fallback)
    "^IXIC",        # Nasdaq Composite
    "^NDX",         # Nasdaq 100
    "QQQ",          # Nasdaq ETF (fallback)
    "TLT",          # Long-term Treasury
    "^VIX",         # VIX
    "^VIX9D",       # 9-Day VIX
    "HYG",          # High Yield Bond
    "USDKRW=X",     # USD/KRW spot
    "KRW=X",        # USD/KRW alt
    "148070.KS",    # KOSEF (KOSPI 200 채권)
    "NVDA",         # AI 1차 주도주 (vs 닷컴 CSCO) — Current_cycle 카드
    "MU",           # AI 2차 주도주 (vs 닷컴 QCOM) — Current_cycle 카드
    "000660.KS",    # SK하이닉스 — 한국 AI 메모리 주도주, MU와 같은 anchor (2024-06-11)
]


def _log(msg):
    print(f"[{datetime.now().isoformat(timespec='seconds')}] {msg}", flush=True)


def fetch_symbol(sym, period="10y", max_retry=2):
    """yfinance Ticker.history 로 OHLC 시계열 fetch.

    Returns {candles, price, prev} or None.
    """
    try:
        import yfinance as yf
        import pandas as pd
    except ImportError:
        _log("ERROR: yfinance/pandas 필요. `pip install yfinance pandas --break-system-packages`")
        sys.exit(2)

    for attempt in range(1, max_retry + 1):
        try:
            t = yf.Ticker(sym)
            h = t.history(period=period, interval="1d", auto_adjust=False)
            if h is None or len(h) == 0:
                _log(f"  {sym}: empty history (attempt {attempt}/{max_retry})")
                if attempt < max_retry:
                    time.sleep(2)
                    continue
                return None
            candles = []
            for ts, row in h.iterrows():
                # NaN skip
                if pd.isna(row.get("Open")) or pd.isna(row.get("Close")):
                    continue
                candles.append({
                    "time": ts.strftime("%Y-%m-%d"),
                    "open": float(row["Open"]),
                    "high": float(row["High"]),
                    "low":  float(row["Low"]),
                    "close": float(row["Close"]),
                })
            if not candles:
                return None
            price = candles[-1]["close"]
            prev = candles[-2]["close"] if len(candles) >= 2 else price
            return {"candles": candles, "price": price, "prev": prev}
        except Exception as e:
            _log(f"  {sym}: {e} (attempt {attempt}/{max_retry})")
            if attempt < max_retry:
                time.sleep(3)
                continue
            return None


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--period", default="10y", help="yfinance period (default 10y)")
    ap.add_argument("--symbols", default=None, help="콤마 구분, 특정 symbol 만 fetch")
    ap.add_argument("--dry-run", action="store_true", help="JSON 저장 안 함")
    args = ap.parse_args()

    symbols = args.symbols.split(",") if args.symbols else SYMBOLS
    _log(f"=== yahoo_dashboard_backfill ({len(symbols)} symbols, period={args.period}) ===")

    data = {}
    ok_count = 0
    fail_list = []
    for sym in symbols:
        _log(f"fetching {sym}...")
        result = fetch_symbol(sym, period=args.period)
        if result:
            data[sym] = result
            ok_count += 1
            _log(f"  OK: {len(result['candles'])} candles, price={result['price']:.2f}")
        else:
            fail_list.append(sym)
            _log(f"  FAIL")
        # Rate limit politeness
        time.sleep(0.5)

    output = {
        "meta": {
            "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "symbols": symbols,
            "period": args.period,
            "ok": ok_count,
            "fail": fail_list,
        },
        "data": data,
    }

    _log(f"=== summary: {ok_count}/{len(symbols)} symbols ok ===")
    if fail_list:
        _log(f"  FAIL: {fail_list}")

    if args.dry_run:
        _log(f"[dry-run] skipping write to {OUT_PATH}")
        return

    # Atomic write
    tmp = OUT_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, separators=(",", ":"))
    os.replace(tmp, OUT_PATH)
    size_kb = os.path.getsize(OUT_PATH) / 1024
    _log(f"wrote {OUT_PATH} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
