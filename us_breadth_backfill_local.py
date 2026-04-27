"""
us_breadth_backfill_local.py
--------------------------------
US market breadth backfill — Goldman-style breadth metric + % above 200MA + % above 50MA.

Goldman breadth = (SPX % from 52wH)  −  median(constituent % from 52wH)
    단위: %p. 값이 음(-)으로 깊을수록 대형주 대비 종목 평균이 더 깊게 눌려있음 → 주도폭 좁음.

출력: us_breadth.json
  {
    "meta": { "updated": "YYYY-MM-DD", "universe_size": N, "window_days": 252 },
    "dates":   ["YYYY-MM-DD", ...],      # 거래일 (SPX 기준)
    "spx":     [float, ...],             # S&P500 종가
    "spx_mdd": [float, ...],             # 전고 대비 % (0 또는 음)
    "pct_above_200ma": [float, ...],     # 구성종목 중 200일선 위 비율 (0-100)
    "pct_above_50ma":  [float, ...],     # 구성종목 중 50일선 위 비율 (0-100)
    "goldman_breadth": [float, ...],     # SPX %52wH - median(종목 %52wH)
    "new_highs_pct":   [float, ...],     # 그 날 52주 신고가 갱신 종목 비율 (0-100) — F&G Strength factor용
    "new_lows_pct":    [float, ...],     # 그 날 52주 신저가 갱신 종목 비율 (0-100) — F&G Strength factor용
    "ism_pmi_monthly": [[date, val], ...]# Market_cycle.html에서 추출한 월별 ISM PMI
  }

CLI
  py us_breadth_backfill_local.py --probe
  py us_breadth_backfill_local.py --test     # 최근 3년만 빠르게 (개발용)
  py us_breadth_backfill_local.py --backfill 2015-01-01 2026-04-17

생존편향 주의 (현재 단계)
  이 v1 은 "현재" 스냅샷의 S&P500 구성종목 리스트를 사용합니다.
  과거 시점에 이미 지수에서 빠진 종목(예: 파산·인수)은 포함되지 않으므로
  실제 Goldman 지표 대비 breadth 가 약간 덜 비관적으로 나옵니다.
  (추세 방향성은 유지. 정확히 복제하려면 historical constituents CSV 필요 → 추후 v2.)
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timedelta

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(THIS_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
OUT_PATH = os.path.join(DATA_DIR, "us_breadth.json")
ISM_PMI_SRC = os.path.join(THIS_DIR, "ism_pmi_extracted.json")   # 있으면 사용. 없으면 HTML 추출 시도.
CYCLE_HTML = os.path.join(THIS_DIR, "Market_cycle.html")         # ISM PMI 원본 HTML

WINDOW_52W = 252
MA_200 = 200
MA_50 = 50

# S&P500 티커 리스트 — Wikipedia (자동 업데이트 대체 소스)
WIKI_SPX = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

# ----------------------------------------------------------------------
# Utilities
# ----------------------------------------------------------------------

def _log(msg: str) -> None:
    print(f"[{datetime.now():%H:%M:%S}] {msg}", flush=True)


def _atomic_write_json(path: str, obj) -> None:
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, separators=(",", ":"))
    os.replace(tmp, path)


def _load_json(path: str):
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ----------------------------------------------------------------------
# 1) ISM PMI 월별 데이터 (Market_cycle.html 내장 데이터 재활용)
# ----------------------------------------------------------------------

def extract_ism_pmi() -> list:
    """이미 ism_pmi_extracted.json 이 있으면 그대로 사용, 없으면 Market_cycle.html 에서 추출."""
    cached = _load_json(ISM_PMI_SRC)
    if cached:
        _log(f"ISM PMI cached: {len(cached)} rows ({cached[0][0]} ~ {cached[-1][0]})")
        return cached

    if not os.path.exists(CYCLE_HTML):
        _log("Market_cycle.html not found — skipping ISM PMI")
        return []

    with open(CYCLE_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    idx = html.find('"ISM_PMI"')
    if idx < 0:
        _log("ISM_PMI key not found in Market_cycle.html")
        return []
    start = html.find("[", idx)
    depth = 0
    end = start
    for i, c in enumerate(html[start:], start=start):
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    arr = json.loads(html[start:end])
    _atomic_write_json(ISM_PMI_SRC, arr)
    _log(f"ISM PMI extracted: {len(arr)} rows → {ISM_PMI_SRC}")
    return arr


# ----------------------------------------------------------------------
# 2) S&P500 티커 리스트 (Wikipedia)
# ----------------------------------------------------------------------

def fetch_spx_tickers() -> list:
    """Wikipedia 에서 현재 S&P500 구성종목 리스트 수집. yfinance 포맷(BRK.B→BRK-B)으로 정규화."""
    import requests
    try:
        import pandas as pd
    except ImportError:
        _log("ERROR: pandas 필요. `pip install pandas --break-system-packages`")
        sys.exit(1)

    _log("Fetching SPX tickers from Wikipedia...")
    r = requests.get(WIKI_SPX, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    tables = pd.read_html(r.text)
    df = tables[0]  # 첫 테이블이 현재 구성종목
    tickers = df["Symbol"].astype(str).str.replace(".", "-", regex=False).tolist()
    tickers = [t.strip() for t in tickers if t and t != "nan"]
    _log(f"SPX tickers: {len(tickers)}")
    return sorted(set(tickers))


# ----------------------------------------------------------------------
# 3) yfinance 배치 다운로드
# ----------------------------------------------------------------------

def download_prices(tickers: list, start: str, end: str, batch_size: int = 50):
    """yfinance 로 종가 시계열 다운로드. Close DataFrame 반환 (index=date, cols=ticker)."""
    try:
        import yfinance as yf
        import pandas as pd
    except ImportError:
        _log("ERROR: yfinance 필요. `pip install yfinance pandas --break-system-packages`")
        sys.exit(1)

    all_close = {}
    total = len(tickers)
    for i in range(0, total, batch_size):
        chunk = tickers[i:i + batch_size]
        _log(f"downloading {i+1}-{min(i+batch_size, total)}/{total}...")
        for attempt in range(3):
            try:
                df = yf.download(
                    chunk,
                    start=start,
                    end=end,
                    group_by="ticker",
                    auto_adjust=True,
                    progress=False,
                    threads=True,
                )
                break
            except Exception as e:
                _log(f"  attempt {attempt+1} failed: {e}; retrying...")
                time.sleep(3)
        else:
            _log(f"  batch {i} FAILED — skipping")
            continue

        # single vs multi ticker 처리
        if len(chunk) == 1:
            t = chunk[0]
            if "Close" in df.columns:
                all_close[t] = df["Close"].dropna()
        else:
            for t in chunk:
                try:
                    s = df[t]["Close"].dropna()
                    if len(s) > 0:
                        all_close[t] = s
                except (KeyError, ValueError):
                    pass
        time.sleep(0.3)

    _log(f"downloaded {len(all_close)}/{total} tickers")
    close_df = pd.DataFrame(all_close)
    close_df.index = close_df.index.tz_localize(None) if close_df.index.tz else close_df.index
    return close_df


# ----------------------------------------------------------------------
# 4) Breadth 계산 (메인 로직)
# ----------------------------------------------------------------------

def compute_breadth(close_df, spx_close) -> dict:
    """
    close_df : 구성종목 Close DataFrame (date × ticker)
    spx_close: SPX Close Series (date)
    returns: dict of aligned series
    """
    import pandas as pd
    import numpy as np

    # 공통 일자 (SPX 기준)
    idx = spx_close.index.sort_values()
    close_df = close_df.reindex(idx)

    # --- 52w rolling max/min 기반 %from52wH + NH/NL ---
    roll_max = close_df.rolling(WINDOW_52W, min_periods=60).max()
    roll_min = close_df.rolling(WINDOW_52W, min_periods=60).min()
    pct_from_52wH = (close_df / roll_max - 1.0) * 100.0   # 0 이하 값 (부호 유지)

    spx_roll_max = spx_close.rolling(WINDOW_52W, min_periods=60).max()
    spx_pct_from_52wH = (spx_close / spx_roll_max - 1.0) * 100.0

    goldman = spx_pct_from_52wH - pct_from_52wH.median(axis=1)

    # --- 52주 신고가/신저가 갱신 종목 수 → 비율(%) ---
    # close == roll_max 면 그 날 52주 고점 (신고가). 부동소수점 허용오차 포함.
    valid_count = close_df.notna().sum(axis=1)
    new_highs_mask = (close_df >= roll_max - 1e-6) & close_df.notna()
    new_lows_mask  = (close_df <= roll_min + 1e-6) & close_df.notna()
    # safe divide: valid_count == 0 이면 0
    nh_pct = (new_highs_mask.sum(axis=1) / valid_count.replace(0, np.nan) * 100.0).fillna(0)
    nl_pct = (new_lows_mask.sum(axis=1)  / valid_count.replace(0, np.nan) * 100.0).fillna(0)

    # --- MA 위 비율 ---
    ma200 = close_df.rolling(MA_200, min_periods=60).mean()
    ma50  = close_df.rolling(MA_50,  min_periods=20).mean()
    above_200 = (close_df > ma200).sum(axis=1) / close_df.notna().sum(axis=1) * 100.0
    above_50  = (close_df > ma50).sum(axis=1)  / close_df.notna().sum(axis=1) * 100.0

    # --- SPX MDD (cummax 기준) ---
    cummax = spx_close.cummax()
    spx_mdd = (spx_close / cummax - 1.0) * 100.0

    def clean(s):
        """NaN → None, 숫자는 round"""
        return [None if pd.isna(v) else round(float(v), 3) for v in s]

    return {
        "dates": [d.strftime("%Y-%m-%d") for d in idx],
        "spx": clean(spx_close),
        "spx_mdd": clean(spx_mdd),
        "pct_above_200ma": clean(above_200),
        "pct_above_50ma": clean(above_50),
        "goldman_breadth": clean(goldman),
        "new_highs_pct": clean(nh_pct),
        "new_lows_pct":  clean(nl_pct),
    }


# ----------------------------------------------------------------------
# 5) 엔트리포인트: probe / test / backfill
# ----------------------------------------------------------------------

def cmd_probe() -> None:
    """연결·패키지 확인용."""
    _log("== probe ==")
    try:
        import yfinance, pandas, requests
        _log(f"yfinance {yfinance.__version__}  pandas {pandas.__version__}  requests {requests.__version__}")
    except ImportError as e:
        _log(f"MISSING: {e}")
        sys.exit(1)
    ts = fetch_spx_tickers()
    _log(f"sample tickers: {ts[:10]}")
    _log("ISM PMI preview:")
    arr = extract_ism_pmi()
    if arr:
        _log(f"  first: {arr[0]}  last: {arr[-1]}")
    _log("== probe OK ==")


def run_backfill(start: str, end: str, max_tickers: int = 0) -> None:
    import pandas as pd

    _log(f"== backfill {start} → {end} ==")
    tickers = fetch_spx_tickers()
    if max_tickers > 0:
        tickers = tickers[:max_tickers]
        _log(f"  (limited to first {max_tickers} tickers for test)")

    # SPX 지수 다운로드
    import yfinance as yf
    _log("downloading ^GSPC ...")
    spx = yf.download("^GSPC", start=start, end=end, auto_adjust=True, progress=False)["Close"]
    if hasattr(spx, "columns"):
        spx = spx.iloc[:, 0]
    spx.index = spx.index.tz_localize(None) if spx.index.tz else spx.index
    _log(f"  SPX rows: {len(spx)}")

    close_df = download_prices(tickers, start, end)

    result = compute_breadth(close_df, spx)

    ism = extract_ism_pmi()
    result["ism_pmi_monthly"] = ism
    result["meta"] = {
        "updated": datetime.now().strftime("%Y-%m-%d"),
        "universe_size": int(close_df.shape[1]),
        "universe_note": "current S&P500 constituents (survivorship-biased v1)",
        "window_days": WINDOW_52W,
        "start": start,
        "end": end,
    }

    _atomic_write_json(OUT_PATH, result)
    _log(f"SAVED → {OUT_PATH}  ({len(result['dates'])} rows, {result['meta']['universe_size']} tickers)")


def main():
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--probe", action="store_true", help="환경/티커/ISM 확인")
    g.add_argument("--test", action="store_true", help="최근 3년, 상위 50종목만 (빠른 검증)")
    g.add_argument("--backfill", nargs=2, metavar=("START", "END"),
                   help="YYYY-MM-DD YYYY-MM-DD  10년 풀 백필")
    args = p.parse_args()

    if args.probe:
        cmd_probe()
    elif args.test:
        end = datetime.now().strftime("%Y-%m-%d")
        start = (datetime.now() - timedelta(days=3 * 365 + 30)).strftime("%Y-%m-%d")
        run_backfill(start, end, max_tickers=50)
    elif args.backfill:
        run_backfill(args.backfill[0], args.backfill[1])


if __name__ == "__main__":
    main()
