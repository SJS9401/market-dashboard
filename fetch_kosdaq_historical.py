#!/usr/bin/env python3
"""one-shot v2: yfinance ^KS11 + ^KQ11 2014~ 일별 OHLC → data/kr_index_ohlc.json (순환매 스캔 캔들차트용)."""
import json
from pathlib import Path
import yfinance as yf

out = {}
for sym, key in (("^KS11", "kospi"), ("^KQ11", "kosdaq")):
    df = yf.Ticker(sym).history(start="2014-01-01", auto_adjust=False)
    rows = []
    for ts, r in df.iterrows():
        if any(map(lambda v: v != v, (r["Open"], r["High"], r["Low"], r["Close"]))):
            continue
        rows.append([ts.strftime("%Y-%m-%d"), round(float(r["Open"]), 2), round(float(r["High"]), 2),
                     round(float(r["Low"]), 2), round(float(r["Close"]), 2)])
    assert len(rows) > 2500, f"{sym} too few: {len(rows)}"
    out[key] = rows
    print(sym, len(rows), rows[-1])
Path("data/kr_index_ohlc.json").write_text(
    json.dumps(out, separators=(",", ":")), encoding="utf-8")
print("saved kr_index_ohlc.json")
