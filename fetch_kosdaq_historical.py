#!/usr/bin/env python3
"""one-shot: yfinance ^KQ11 2014~ 일별 종가 → data/kosdaq_historical.json (순환매 스캔 차트용)."""
import json
from pathlib import Path
import yfinance as yf

df = yf.Ticker("^KQ11").history(start="2014-01-01", auto_adjust=False)
rows = [[d.strftime("%Y-%m-%d"), round(float(c), 2)] for d, c in df["Close"].dropna().items()]
assert len(rows) > 2500, f"too few rows: {len(rows)}"
Path("data/kosdaq_historical.json").write_text(
    json.dumps({"_meta": {"symbol": "^KQ11", "rows": len(rows)}, "data": rows},
               ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print("saved", len(rows), rows[0], rows[-1])
