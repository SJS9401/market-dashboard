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
import io
import json
import os
import sys
import time
from datetime import datetime, timedelta

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(THIS_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
OUT_PATH = os.path.join(DATA_DIR, "us_breadth.json")
HEALTH_PATH = os.path.join(DATA_DIR, "us_breadth_health.json")    # v2 사이드카
ISM_PMI_SRC = os.path.join(THIS_DIR, "ism_pmi_extracted.json")   # 있으면 사용. 없으면 HTML 추출 시도.
CYCLE_HTML = os.path.join(THIS_DIR, "Market_cycle.html")         # ISM PMI 원본 HTML

WINDOW_52W = 252
MA_200 = 200
MA_50 = 50

# S&P500 티커 리스트 — Wikipedia (자동 업데이트 대체 소스)
WIKI_SPX = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

# v2 임계값
STALE_DAYS_HARD     = 7   # SPX last_date 와 today 차이 7일 초과 = 해당 소스 stale
CONSTITUENT_STALE_PCT_MAX = 10.0  # 503 종목 중 stale 비율 10% 초과 시 fail
CONSTITUENT_STALE_BDAYS   = 3     # ticker last_date < SPX last_date - 3 영업일이면 stale

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
    # pandas 2.x: read_html이 string을 파일경로로 해석하므로 StringIO로 감싸야 함
    tables = pd.read_html(io.StringIO(r.text))
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


# ----------------------------------------------------------------------
# v2: SPX 다중 소스 폴백 (Stooq → yfinance → Stooq retry)
# ----------------------------------------------------------------------

def _fetch_spx_stooq(start: str, end: str):
    """Stooq CSV 에서 ^SPX 일봉 시계열 fetch.

    URL 형식: https://stooq.com/q/d/l/?s=^spx&i=d&d1=YYYYMMDD&d2=YYYYMMDD
    응답: CSV ('Date,Open,High,Low,Close,Volume', 날짜 오름차순)

    Returns
    -------
    pd.Series  (index=DatetimeIndex tz-naive, values=Close float, 빈 응답 시 빈 Series)
    """
    import pandas as pd
    import requests

    d1 = start.replace("-", "")
    d2 = end.replace("-", "")
    url = f"https://stooq.com/q/d/l/?s=^spx&i=d&d1={d1}&d2={d2}"
    r = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    body = r.text.strip()
    # Stooq returns "No data" or empty on error
    if not body or body.lower().startswith("no data") or "\n" not in body:
        return pd.Series(dtype=float, name="Close")
    # Parse via pandas (handles header row)
    try:
        df = pd.read_csv(io.StringIO(body))
    except Exception:
        return pd.Series(dtype=float, name="Close")
    if df.empty or "Date" not in df.columns or "Close" not in df.columns:
        return pd.Series(dtype=float, name="Close")
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date", "Close"]).sort_values("Date")
    s = pd.Series(df["Close"].values, index=df["Date"].values, name="Close")
    s.index = s.index.tz_localize(None) if hasattr(s.index, "tz") and s.index.tz else s.index
    return s


def _fetch_spx_yfinance(start: str, end: str):
    """yfinance ^GSPC 일봉 시계열 fetch. 실패 시 빈 Series."""
    import pandas as pd
    try:
        import yfinance as yf
    except ImportError:
        return pd.Series(dtype=float, name="Close")
    try:
        df = yf.download(
            "^GSPC", start=start, end=end,
            auto_adjust=True, progress=False,
        )
    except Exception:
        return pd.Series(dtype=float, name="Close")
    if df is None or df.empty:
        return pd.Series(dtype=float, name="Close")
    s = df["Close"]
    if hasattr(s, "columns"):
        s = s.iloc[:, 0]
    s.index = s.index.tz_localize(None) if s.index.tz else s.index
    return s


def _fetch_spx_multi(start: str, end: str, attempts_log: list):
    """SPX 일봉 다중 소스 폴백.

    순서:
      1) Stooq            (1차, 인증 X, Yahoo 와 인프라 분리)
      2) yfinance ^GSPC   (2차, 기존 경로)
      3) Stooq retry      (3차, 일시 네트워크 장애 대비)

    각 소스마다 last_date 가 today - STALE_DAYS_HARD (7일) 초과 stale 이면 다음 소스로.
    모두 실패 시 sys.exit(1).

    attempts_log: list[dict] — 각 시도 결과 기록 (Health JSON 출력용).
    """
    today = datetime.utcnow().date()
    sources = [
        ("stooq",     _fetch_spx_stooq,    0),
        ("yfinance",  _fetch_spx_yfinance, 0),
        ("stooq",     _fetch_spx_stooq,    5),  # 5s backoff
    ]

    for i, (name, fn, backoff) in enumerate(sources, 1):
        if backoff:
            time.sleep(backoff)
        _log(f"SPX source attempt {i}/3: {name} ...")
        attempt = {"source": name, "attempt": i, "ok": False, "rows": 0, "last": None, "error": None}
        try:
            spx = fn(start, end)
        except Exception as e:
            attempt["error"] = f"exception: {e}"
            _log(f"  {name} EXCEPTION: {e}")
            attempts_log.append(attempt)
            continue

        rows = len(spx)
        attempt["rows"] = rows
        if rows == 0:
            attempt["error"] = "empty"
            _log(f"  {name} returned EMPTY")
            attempts_log.append(attempt)
            continue

        last_date = spx.index[-1].date()
        days_stale = (today - last_date).days
        attempt["last"] = str(last_date)
        attempt["days_stale"] = days_stale
        _log(f"  {name} rows: {rows}  last: {last_date}  (today-last={days_stale}d)")

        if days_stale > STALE_DAYS_HARD:
            attempt["error"] = f"stale (>{STALE_DAYS_HARD}d)"
            attempts_log.append(attempt)
            _log(f"  {name} too stale, trying next source")
            continue

        attempt["ok"] = True
        attempts_log.append(attempt)
        _log(f"  ✓ using {name} as SPX source")
        return spx, name

    # 모든 소스 실패
    _log(f"::error::all SPX sources stale or failed. attempts: {attempts_log}")
    sys.exit(1)


# ----------------------------------------------------------------------
# v2: 503 종목 stale ratio 게이트
# ----------------------------------------------------------------------

def _validate_constituents_freshness(close_df, spx_last_date) -> dict:
    """
    503 종목별 last_date를 SPX last_date와 비교, stale 비율 산출.

    Stale 정의: 종목 last_date < SPX last_date - CONSTITUENT_STALE_BDAYS 영업일
    (영업일 단위로 비교; 주말/공휴일은 정상이므로 무시)

    Returns dict: {total, stale, stale_pct, threshold_pct, ok, stale_tickers (sample 10)}
    """
    import pandas as pd

    spx_last = pd.Timestamp(spx_last_date)
    # SPX last 에서 N 영업일 빼기 (BDay 사용)
    threshold = spx_last - pd.tseries.offsets.BDay(CONSTITUENT_STALE_BDAYS)

    stale = []
    total = 0
    for col in close_df.columns:
        s = close_df[col].dropna()
        total += 1
        if len(s) == 0:
            stale.append(col)
            continue
        ticker_last = s.index[-1]
        if ticker_last < threshold:
            stale.append(col)

    stale_pct = (len(stale) / total * 100.0) if total > 0 else 0.0
    ok = stale_pct <= CONSTITUENT_STALE_PCT_MAX
    return {
        "total": total,
        "stale": len(stale),
        "stale_pct": round(stale_pct, 2),
        "threshold_pct": CONSTITUENT_STALE_PCT_MAX,
        "ok": ok,
        "stale_tickers_sample": stale[:10],
    }


def run_backfill(start: str, end: str, max_tickers: int = 0) -> None:
    """v2: 다중 소스 SPX + 종목 stale 게이트 + health JSON 사이드카."""
    import pandas as pd

    run_started = datetime.utcnow()
    _log(f"== backfill v2 {start} → {end} ==")

    tickers = fetch_spx_tickers()
    if max_tickers > 0:
        tickers = tickers[:max_tickers]
        _log(f"  (limited to first {max_tickers} tickers for test)")

    # --- Layer A: SPX 다중 소스 폴백 ---
    spx_attempts = []
    spx, spx_source = _fetch_spx_multi(start, end, spx_attempts)
    spx_last_date = spx.index[-1].date()

    # --- 503 종목 다운로드 (yfinance 배치, 기존 동작) ---
    close_df = download_prices(tickers, start, end)

    # --- Layer B: 종목 stale ratio 게이트 ---
    constituent_health = _validate_constituents_freshness(close_df, spx_last_date)
    _log(f"constituents: total={constituent_health['total']} "
         f"stale={constituent_health['stale']} ({constituent_health['stale_pct']}%) "
         f"threshold={constituent_health['threshold_pct']}%")
    if not constituent_health["ok"]:
        _log(f"::error::data quality degraded: {constituent_health['stale_pct']}% of "
             f"constituents are stale (>{CONSTITUENT_STALE_BDAYS}bd behind SPX last_date={spx_last_date}). "
             f"sample: {constituent_health['stale_tickers_sample']}")
        # health JSON 도 fail 상태로 기록한 뒤 exit
        _write_health_json(
            run_started=run_started, status="FAIL_CONSTITUENT_STALE",
            spx_source=spx_source, spx_attempts=spx_attempts,
            constituents=constituent_health,
            last_date=str(spx_last_date),
            extra={"reason": "constituent_stale_pct_exceeded"},
        )
        sys.exit(3)

    # --- Breadth 계산 ---
    result = compute_breadth(close_df, spx)

    # --- 회귀 방어: 기존 파일 last_date 보다 새 결과 last_date 가 빠르면 거부 ---
    new_last = result["dates"][-1] if result["dates"] else None
    prev = _load_json(OUT_PATH)
    if prev and prev.get("dates") and new_last:
        prev_last = prev["dates"][-1]
        if new_last < prev_last:
            _log(f"::error::regression detected: new last_date={new_last} < prev last_date={prev_last}. "
                 f"Refusing to overwrite. (max_tickers={max_tickers})")
            _write_health_json(
                run_started=run_started, status="FAIL_REGRESSION",
                spx_source=spx_source, spx_attempts=spx_attempts,
                constituents=constituent_health,
                last_date=new_last,
                extra={"reason": "regression", "prev_last": prev_last},
            )
            sys.exit(2)
        if new_last == prev_last:
            _log(f"  no new trading day (last_date unchanged: {new_last}) — proceeding to update meta only")

    ism = extract_ism_pmi()
    result["ism_pmi_monthly"] = ism
    result["meta"] = {
        "updated": datetime.now().strftime("%Y-%m-%d"),
        "universe_size": int(close_df.shape[1]),
        "universe_note": "current S&P500 constituents (survivorship-biased v1)",
        "window_days": WINDOW_52W,
        "start": start,
        "end": end,
        "spx_source": spx_source,                   # v2: 어느 소스에서 SPX 가져왔는지
        "constituent_stale_pct": constituent_health["stale_pct"],
    }

    _atomic_write_json(OUT_PATH, result)
    _log(f"SAVED → {OUT_PATH}  ({len(result['dates'])} rows, {result['meta']['universe_size']} tickers, "
         f"last={new_last}, spx_src={spx_source})")

    # --- Layer C: Health JSON 사이드카 ---
    _write_health_json(
        run_started=run_started, status="OK",
        spx_source=spx_source, spx_attempts=spx_attempts,
        constituents=constituent_health,
        last_date=new_last,
    )


def _write_health_json(run_started, status, spx_source, spx_attempts,
                       constituents, last_date, extra=None):
    """v2 사이드카: 매 런마다 갱신되는 파이프라인 헬스 스코어."""
    today = datetime.utcnow().date()
    last_d = datetime.strptime(last_date, "%Y-%m-%d").date() if last_date else None
    bd = 0
    if last_d:
        cur = last_d
        while cur < today:
            cur += timedelta(days=1)
            if cur.weekday() < 5:
                bd += 1
    health = {
        "schema_version": 2,
        "last_run_started": run_started.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "last_run_finished": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "status": status,                      # OK / FAIL_REGRESSION / FAIL_CONSTITUENT_STALE / FAIL_SPX
        "spx_source_used": spx_source,
        "spx_attempts": spx_attempts,
        "constituents_total": constituents.get("total"),
        "constituents_stale": constituents.get("stale"),
        "stale_pct": constituents.get("stale_pct"),
        "last_date": last_date,
        "business_days_stale": bd,
        "stale_tickers_sample": constituents.get("stale_tickers_sample", []),
    }
    if extra:
        health.update(extra)
    _atomic_write_json(HEALTH_PATH, health)
    _log(f"HEALTH → {HEALTH_PATH}  status={status} spx_src={spx_source} "
         f"stale_pct={constituents.get('stale_pct')}% bd_stale={bd}")


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
