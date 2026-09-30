#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""us_breadth_nyse_build.py — NYSE 종목군 시장폭 (2026-09-30 신설)

대시보드 US Market Breadth 카드를 StockCharts $NYA200R / $NYA50R 와 같은 종목군으로 맞추기 위한
별도 파이프라인. 기존 us_breadth.json(S&P500 503종목)은 그대로 둔다 — F&G Breadth 팩터·
Goldman breadth·NH/NL 이 그 파일을 읽고, Goldman 은 정의상 SPX 구성종목이어야 한다.

[왜] 2026-09-30 종가 기준 SPX 판 200MA 41.9% / 50MA 21.3% vs StockCharts NYSE 37.08% / 20.14%.
     SPX 는 대형 우량주라 NYSE 전체보다 3~5%p 높게 나온다 (과매도 임계를 15 대신 20 으로 썼던 이유).
     BT: "첨부한 NYSE 숫자로 보고 싶다. 소수점 일치까지는 원하지 않는다."

[종목군] nasdaqtrader otherlisted.txt 에서 NYSE(Exchange=N) 보통주.
  제외: ETF · Test Issue · 우선주/워런트/유닛/권리/채권류(이름·심볼) · 폐쇄형펀드(이름에 Fund) ·
        SPAC(Acquisition Corp/Company) · 우선주 DR(단 American Depositary = ADR 은 포함)
  → 약 2,000~2,200 종목. StockCharts 는 종목군을 공개하지 않으므로 소수점 일치는 불가, 레벨·방향 일치가 목표.
  nasdaqtrader 실패 시 직전 심볼 목록 캐시(data/us_breadth_nyse_symbols.json)를 재사용한다.

[계산] StockCharts 정의에 맞춰 SPX 판과 두 가지를 다르게 한다.
  - 이평은 **전체 창**(200일/50일)이 찬 종목만 센다 (SPX 판은 min_periods=60/20).
  - 분모 = 해당 이평이 유효한 종목 수 (SPX 판은 종가가 있는 모든 종목).
  생존편향 있음(현재 상장 목록을 과거에 소급) — 최근 구간 비교용이므로 수용, meta 에 명시.

[갱신] 종목이 SPX 의 4배라 매일 풀 백필은 30분+ → 증분.
  기본  : 최근 450 달력일(≈310 거래일)을 받아 재계산 → 마지막 60 거래일을 덮어쓰고 이후를 덧붙인다.
  FULL=1: 2015-01-01 부터 풀 백필 (첫 실행·복구용).

[가드] (하나라도 걸리면 파일을 쓰지 않고 exit≠0)
  - 종목 신선도: 마지막 거래일 기준 3영업일 넘게 끊긴 종목이 10% 초과
  - 회귀: 새 last_date < 기존 last_date
  - 규모: 유효 종목(200MA) 1,000 미만

출력  data/us_breadth_nyse.json          — us_breadth.json 과 같은 키 이름(dates, pct_above_200ma, pct_above_50ma,
                                           new_highs_pct, new_lows_pct) + n_valid_200/n_valid_50 + meta
      data/us_breadth_nyse_health.json   — 런 상태
      data/us_breadth_nyse_symbols.json  — 심볼 목록 캐시
"""
import io
import json
import os
import re
import sys
import time
import urllib.request
from datetime import date, datetime, timedelta, timezone

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(THIS_DIR, "data")
OUT_PATH = os.path.join(DATA_DIR, "us_breadth_nyse.json")
HEALTH_PATH = os.path.join(DATA_DIR, "us_breadth_nyse_health.json")
SYMS_PATH = os.path.join(DATA_DIR, "us_breadth_nyse_symbols.json")

SYMDIR_URL = "https://www.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"
SYMDIR_HEADER = ["ACT Symbol", "Security Name", "Exchange", "CQS Symbol", "ETF",
                 "Round Lot Size", "Test Issue", "NASDAQ Symbol"]

FULL_START = "2015-01-01"
INCR_CAL_DAYS = 450          # 증분 모드 다운로드 창 (MA200 이 찰 만큼 + 여유)
INCR_REPLACE_DAYS = 60       # 증분 모드에서 기존 값을 덮어쓸 최근 거래일 수
MA_200, MA_50, WINDOW_52W = 200, 50, 252
BATCH = 100
STALE_BDAYS = 3
STALE_PCT_MAX = 10.0
MIN_VALID = 1000

# 이름 기반 제외 — 우선주/워런트/유닛/권리/채권류, 폐쇄형 펀드, SPAC
NAME_EXCL = re.compile(
    r"\b(preferred|pfd|warrants?|units?|rights?|notes|debentures?|subordinated|senior)\b"
    r"|%|\bfund\b|acquisition corp|acquisition company", re.I)
CQS_OK = re.compile(r"^[A-Z]{1,5}(\.[A-Z])?$")   # 소문자 p(우선주)·$ 등 특수 접미 제외


def _log(m):
    print(f"[{datetime.now(timezone.utc):%H:%M:%S}] {m}", flush=True)


def _atomic_write_json(path, obj, compact=True):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        if compact:
            json.dump(obj, f, ensure_ascii=False, separators=(",", ":"))
        else:
            json.dump(obj, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


def _load_json(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


# ---------------------------------------------------------------- 종목군
def parse_symdir(text):
    """otherlisted.txt → (yfinance 티커 목록, 제외 샘플). 순수 함수 (테스트용)."""
    lines = [l for l in text.splitlines() if l.strip()]
    hdr = lines[0].split("|")
    if hdr[:len(SYMDIR_HEADER)] != SYMDIR_HEADER:
        raise ValueError(f"otherlisted 헤더 변경: {hdr}")
    ix = {n: i for i, n in enumerate(hdr)}
    kept, dropped = [], []
    for l in lines[1:]:
        if l.startswith("File Creation Time"):
            continue
        r = l.split("|")
        if len(r) < len(SYMDIR_HEADER):
            continue
        if r[ix["Exchange"]] != "N" or r[ix["ETF"]] != "N" or r[ix["Test Issue"]] != "N":
            continue
        name, cqs = r[ix["Security Name"]], r[ix["CQS Symbol"]]
        dep_pref = re.search(r"depositary shares", name, re.I) and not re.search(r"american depositary", name, re.I)
        if not CQS_OK.match(cqs) or NAME_EXCL.search(name) or dep_pref:
            dropped.append(f"{cqs} {name[:50]}")
            continue
        kept.append(cqs.replace(".", "-"))          # yfinance: BRK.B → BRK-B
    return sorted(set(kept)), dropped


def load_universe():
    try:
        req = urllib.request.Request(SYMDIR_URL, headers={"User-Agent": "Mozilla/5.0 (market-dashboard)"})
        with urllib.request.urlopen(req, timeout=30) as r:
            text = r.read().decode("utf-8", "replace")
        syms, dropped = parse_symdir(text)
        if len(syms) < 1500:
            raise ValueError(f"심볼 수 이상 {len(syms)}")
        _log(f"universe: nasdaqtrader {len(syms)} kept / {len(dropped)} dropped")
        _log("  dropped 샘플: " + " | ".join(dropped[:15]))
        _atomic_write_json(SYMS_PATH, {"date": date.today().isoformat(), "source": SYMDIR_URL,
                                       "n": len(syms), "symbols": syms})
        return syms, "nasdaqtrader"
    except Exception as e:
        cache = _load_json(SYMS_PATH)
        if cache and cache.get("symbols"):
            _log(f"universe: nasdaqtrader 실패({e}) → 캐시 {cache['date']} {cache['n']}종목 재사용")
            return cache["symbols"], f"cache({cache['date']})"
        raise SystemExit(f"[ERROR] 종목군 확보 실패, 캐시도 없음: {e}")


# ---------------------------------------------------------------- 가격
def download_closes(tickers, start, end):
    import pandas as pd
    import yfinance as yf
    got, failed = {}, []

    def _batch(chunk):
        for attempt in range(3):
            try:
                df = yf.download(chunk, start=start, end=end, group_by="ticker", auto_adjust=True,
                                 progress=False, threads=True)
                break
            except Exception as e:                                   # noqa: BLE001
                _log(f"  batch retry {attempt + 1}: {e}")
                time.sleep(5 * (attempt + 1))
        else:
            return list(chunk)
        miss = []
        for t in chunk:
            try:
                s = (df["Close"] if len(chunk) == 1 else df[t]["Close"]).dropna()
                if len(s):
                    got[t] = s
                else:
                    miss.append(t)
            except (KeyError, ValueError):
                miss.append(t)
        return miss

    for i in range(0, len(tickers), BATCH):
        chunk = tickers[i:i + BATCH]
        failed += _batch(chunk)
        if (i // BATCH) % 5 == 0:
            _log(f"  {min(i + BATCH, len(tickers))}/{len(tickers)} 수신 {len(got)}")
        time.sleep(0.5)
    if failed:
        _log(f"  빈 응답 {len(failed)}종목 1회 재시도")
        time.sleep(10)
        still = []
        for i in range(0, len(failed), 50):
            still += _batch(failed[i:i + 50])
        failed = still
    _log(f"downloaded {len(got)}/{len(tickers)} (실패 {len(failed)})")
    close = pd.DataFrame(got).sort_index()
    if getattr(close.index, "tz", None) is not None:
        close.index = close.index.tz_localize(None)
    return close, failed


# ---------------------------------------------------------------- 계산
def compute(close):
    """close: date × ticker DataFrame → dict of lists. 순수 함수 (테스트용)."""
    import numpy as np
    ma200 = close.rolling(MA_200, min_periods=MA_200).mean()
    ma50 = close.rolling(MA_50, min_periods=MA_50).mean()
    v200 = ma200.notna() & close.notna()
    v50 = ma50.notna() & close.notna()
    n200 = v200.sum(axis=1)
    n50 = v50.sum(axis=1)
    a200 = ((close > ma200) & v200).sum(axis=1) / n200.replace(0, np.nan) * 100.0
    a50 = ((close > ma50) & v50).sum(axis=1) / n50.replace(0, np.nan) * 100.0
    rmax = close.rolling(WINDOW_52W, min_periods=WINDOW_52W).max()
    rmin = close.rolling(WINDOW_52W, min_periods=WINDOW_52W).min()
    v52 = rmax.notna() & close.notna()
    n52 = v52.sum(axis=1).replace(0, np.nan)
    nh = ((close >= rmax - 1e-6) & v52).sum(axis=1) / n52 * 100.0
    nl = ((close <= rmin + 1e-6) & v52).sum(axis=1) / n52 * 100.0

    def lst(s, nd=3):
        return [None if (x is None or x != x) else round(float(x), nd) for x in s.tolist()]

    return {
        "dates": [d.strftime("%Y-%m-%d") for d in close.index],
        "pct_above_200ma": lst(a200), "pct_above_50ma": lst(a50),
        "new_highs_pct": lst(nh), "new_lows_pct": lst(nl),
        "n_valid_200": [int(x) for x in n200.tolist()], "n_valid_50": [int(x) for x in n50.tolist()],
    }


SERIES_KEYS = ["pct_above_200ma", "pct_above_50ma", "new_highs_pct", "new_lows_pct", "n_valid_200", "n_valid_50"]


def merge(prev, new, replace_days):
    """prev(기존 JSON) 에 new(증분 계산) 를 병합. new 의 마지막 replace_days 거래일 + 그 이후를 채택.
    순수 함수 (테스트용)."""
    if not prev or not prev.get("dates"):
        return new
    cut = new["dates"][-replace_days] if len(new["dates"]) >= replace_days else new["dates"][0]
    keep = [i for i, d in enumerate(prev["dates"]) if d < cut]
    take = [i for i, d in enumerate(new["dates"]) if d >= cut]
    out = {"dates": [prev["dates"][i] for i in keep] + [new["dates"][i] for i in take]}
    for k in SERIES_KEYS:
        pv = prev.get(k) or [None] * len(prev["dates"])
        out[k] = [pv[i] for i in keep] + [new[k][i] for i in take]
    return out


def bdays_between(a, b):
    """a < b 인 두 date 사이 영업일 수 (주말만 고려)."""
    n, d = 0, a
    while d < b:
        d += timedelta(days=1)
        if d.weekday() < 5:
            n += 1
    return n


# ---------------------------------------------------------------- main
def main():
    import pandas as pd
    full = os.environ.get("FULL", "0") == "1"
    prev = _load_json(OUT_PATH)
    if not prev:
        full = True
    health = {"run_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "mode": "full" if full else "incremental", "status": "RUNNING"}

    syms, uni_src = load_universe()
    end = (date.today() + timedelta(days=1)).isoformat()
    start = FULL_START if full else (date.today() - timedelta(days=INCR_CAL_DAYS)).isoformat()
    _log(f"mode={health['mode']}  {start} → {end}  tickers={len(syms)}")

    close, failed = download_closes(syms, start, end)
    if close.empty:
        raise SystemExit("[ERROR] 가격 데이터 없음")

    # 종목 신선도 게이트
    last_idx = close.index.max().date()
    last_valid = close.apply(lambda s: s.last_valid_index())
    stale = [t for t, d in last_valid.items() if d is None or bdays_between(d.date(), last_idx) > STALE_BDAYS]
    stale_pct = len(stale) / max(len(close.columns), 1) * 100.0
    health.update({"universe_source": uni_src, "n_universe": len(syms), "n_downloaded": int(close.shape[1]),
                   "n_failed": len(failed), "failed_sample": failed[:20],
                   "last_date": last_idx.isoformat(), "stale_n": len(stale), "stale_pct": round(stale_pct, 2),
                   "stale_sample": stale[:20]})
    _log(f"last_date={last_idx}  stale {len(stale)}/{close.shape[1]} ({stale_pct:.1f}%)")

    res = compute(close)
    n_last = res["n_valid_200"][-1]
    health["n_valid_200_last"] = n_last

    fail = None
    if stale_pct > STALE_PCT_MAX:
        fail = f"FAIL_STALE ({stale_pct:.1f}% > {STALE_PCT_MAX}%)"
    elif n_last < MIN_VALID:
        fail = f"FAIL_SMALL (유효 {n_last} < {MIN_VALID})"
    elif prev and prev.get("dates") and res["dates"][-1] < prev["dates"][-1]:
        fail = f"FAIL_REGRESSION ({res['dates'][-1]} < 기존 {prev['dates'][-1]})"
    if fail:
        health["status"] = fail
        _atomic_write_json(HEALTH_PATH, health, compact=False)
        raise SystemExit(f"[ERROR] {fail} — us_breadth_nyse.json 을 쓰지 않는다")

    merged = res if full else merge(prev, res, INCR_REPLACE_DAYS)
    out = dict(merged)
    out["meta"] = {
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "universe": "NYSE common stocks — nasdaqtrader otherlisted (Exchange=N), ETF·우선주·워런트·유닛·권리·"
                    "채권류·폐쇄형펀드·SPAC 제외, ADR 포함",
        "universe_source": uni_src, "universe_size": len(syms), "downloaded": int(close.shape[1]),
        "method": "종가 > SMA(200|50), 전체 창이 찬 종목만 분모 (StockCharts $NYA200R/$NYA50R 정의 근사)",
        "survivorship_bias": "현재 상장 목록을 과거에 소급 — 과거 구간은 실제보다 높게 나올 수 있음",
        "compare_to": "StockCharts $NYA200R / $NYA50R — 종목군 비공개라 소수점 일치 불가, 레벨·방향 일치 목표",
        "mode": health["mode"], "start": merged["dates"][0], "end": merged["dates"][-1],
    }
    _atomic_write_json(OUT_PATH, out)
    health["status"] = "OK"
    health["last_values"] = {"date": out["dates"][-1], "pct_above_200ma": out["pct_above_200ma"][-1],
                             "pct_above_50ma": out["pct_above_50ma"][-1],
                             "n_valid_200": out["n_valid_200"][-1], "n_valid_50": out["n_valid_50"][-1]}
    _atomic_write_json(HEALTH_PATH, health, compact=False)
    tail = list(zip(out["dates"][-20:], out["pct_above_200ma"][-20:], out["pct_above_50ma"][-20:]))
    _log("최근 20거래일 (date, 200MA%, 50MA%) — StockCharts 대조용:")
    for d, a, b in tail:
        _log(f"  {d}  {a}  {b}")
    _log(f"WROTE {OUT_PATH}  {out['dates'][0]}~{out['dates'][-1]}  {len(out['dates'])}행  "
         f"{os.path.getsize(OUT_PATH):,} bytes")


if __name__ == "__main__":
    main()
