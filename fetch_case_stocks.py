#!/usr/bin/env python3
"""one-shot: Big Move 1차 관성 케이스 5종목 일별 OHLCV → data/kr_stock_cases.json."""
import json
from pathlib import Path
import yfinance as yf

SYMS = {"086520.KQ": "에코프로", "196170.KQ": "알테오젠", "042660.KS": "한화오션",
        "034020.KS": "두산에너빌리티", "000660.KS": "SK하이닉스"}
out = {}
for sym, name in SYMS.items():
    df = yf.Ticker(sym).history(start="2021-06-01", auto_adjust=False)
    rows = []
    for ts, r in df.iterrows():
        if r["Close"] != r["Close"]:
            continue
        rows.append([ts.strftime("%Y-%m-%d"), round(float(r["Open"]), 1), round(float(r["High"]), 1),
                     round(float(r["Low"]), 1), round(float(r["Close"]), 1), int(r["Volume"])])
    assert len(rows) > 600, f"{sym}: {len(rows)}"
    out[name] = {"sym": sym, "rows": rows}
    print(sym, name, len(rows), rows[-1][0])
Path("data/kr_stock_cases.json").write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print("saved")
