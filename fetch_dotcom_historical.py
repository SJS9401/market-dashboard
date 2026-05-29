#!/usr/bin/env python3
"""
fetch_dotcom_historical.py — CSCO / QCOM 1994-12-30 ~ 2002-06-30 historical 1회 fetch

Why:
  Current_cycle 페이지의 "닷컴 vs AI 주도주 비교" 카드용 정적 데이터.
  닷컴 시기(1995~2001)는 변하지 않으므로 정적 JSON으로 한 번만 commit.
  NVDA, MU 등 진행 중인 종목은 yahoo_dashboard_backfill.py 가 daily 갱신.

When to run:
  - 워크플로우 (.github/workflows/fetch_dotcom_historical.yml) 를 workflow_dispatch 로 1회 실행
  - 추가로 종목 비교 늘릴 때 (예: INTC, ORCL 등) 수동 트리거

Output:
  data/dotcom_historical.json
    {
      "_meta": {...},
      "data": {
        "CSCO": [[date, close], ...],
        "QCOM": [[date, close], ...]
      }
    }
"""

import json
import os
import sys
from datetime import datetime, timezone

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(THIS_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
OUT_PATH = os.path.join(DATA_DIR, "dotcom_historical.json")

# 닷컴 시기 1차/2차 주도주 (KB증권 그림 53/54 기준) + Nasdaq Composite
SYMBOLS = ["CSCO", "QCOM", "^IXIC"]

# Period: 1994-12-30 (1995 직전 거래일) ~ 2002-06-30 (정점 후 충분한 약세장 cover)
START = "1994-12-30"
END   = "2002-06-30"


def fetch_symbol(sym):
    """yfinance 로 종가 시계열 fetch → [[date, close], ...]."""
    import yfinance as yf
    import pandas as pd

    t = yf.Ticker(sym)
    h = t.history(start=START, end=END, interval="1d", auto_adjust=False)
    if h is None or len(h) == 0:
        return None
    out = []
    for ts, row in h.iterrows():
        if pd.isna(row.get("Close")):
            continue
        out.append([ts.strftime("%Y-%m-%d"), round(float(row["Close"]), 4)])
    return out


def main():
    try:
        import yfinance
    except ImportError:
        print("[ERROR] yfinance 필요: pip install yfinance pandas")
        sys.exit(2)

    print(f"[fetch_dotcom_historical] {START} ~ {END}")
    print(f"  symbols: {SYMBOLS}")

    data = {}
    for sym in SYMBOLS:
        print(f"  fetching {sym}...", flush=True)
        rows = fetch_symbol(sym)
        if not rows:
            print(f"  [ERROR] {sym}: empty")
            sys.exit(3)
        data[sym] = rows
        print(f"    {len(rows)}일 ({rows[0][0]} ~ {rows[-1][0]}, "
              f"first={rows[0][1]}, last={rows[-1][1]})")

    payload = {
        "_meta": {
            "description": "닷컴 시기 1차/2차 주도주 (KB증권 그림 53/54). build_current_cycle.py 입력.",
            "source": "yfinance",
            "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "range": f"{START} ~ {END}",
            "symbols": SYMBOLS,
            "format": "{symbol: [[date, close], ...]}"
        },
        "data": data
    }

    tmp = OUT_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, separators=(",", ":"))
    os.replace(tmp, OUT_PATH)
    print(f"\n[OK] Written: {OUT_PATH} ({os.path.getsize(OUT_PATH):,} bytes)")


if __name_