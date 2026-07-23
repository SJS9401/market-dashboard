#!/usr/bin/env python3
"""
US F&G Oscillator 빌더 — NASDAQ (태린이아빠 방법론의 미국판, KR 빌더와 대칭)

5개 변수 (모두 data/yahoo_dashboard.json 에서):
  - ^IXIC 125일 MA 괴리율                    (↑ = 탐욕)
  - Put/Call proxy: ^VIX9D / ^VIX ratio      (↑ = 단기 공포 → invert)
  - ^VIX                                      (↑ = 공포 → invert)
  - ZN=F − ZF=F (10년-5년 미 국채선물 연속물) (↑ = 탐욕)
  - ^IXIC RSI 10일                            (↑ = 탐욕)

각각 rolling 252영업일 min-max 정규화 → 동일가중 평균 → MACD(12,26,9) 히스토그램.

출력: data/us_fg_oscillator.json
  { "generated_at", "method", "n_rows", "data": [["date", {"osc":x, "fg":y}], ...] }

사용법:
  py us_fg_oscillator_build.py            # 빌드
  py us_fg_oscillator_build.py --debug    # 변수별 커버리지 출력
"""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
OUT_PATH = DATA_DIR / "us_fg_oscillator.json"

NORM_WINDOW = 252
MA_DEV_WINDOW = 125
RSI_WINDOW = 10
MACD_FAST, MACD_SLOW, MACD_SIGNAL = 12, 26, 9
SIGNS = {"ma_dev": +1, "pc_proxy": -1, "vix": -1, "bond_spread": +1, "rsi": +1}


def load_yahoo():
    p = DATA_DIR / "yahoo_dashboard.json"
    if not p.exists():
        raise FileNotFoundError(f"{p} 없음")
    return json.loads(p.read_text(encoding="utf-8"))


def closes_map(yd, sym):
    d = yd["data"].get(sym)
    if not d:
        return {}
    return {c["time"]: c["close"] for c in d.get("candles", [])}


def sma(values, window):
    out = [None] * len(values)
    s = 0.0
    for i, v in enumerate(values):
        s += v
        if i >= window:
            s -= values[i - window]
        if i >= window - 1:
            out[i] = s / window
    return out


def rsi(closes, window):
    out = [None] * len(closes)
    if len(closes) <= window:
        return out
    gains, losses = 0.0, 0.0
    for i in range(1, window + 1):
        chg = closes[i] - closes[i - 1]
        if chg >= 0:
            gains += chg
        else:
            losses -= chg
    avg_g, avg_l = gains / window, losses / window
    out[window] = 100.0 if avg_l == 0 else 100 - 100 / (1 + avg_g / avg_l)
    for i in range(window + 1, len(closes)):
        chg = closes[i] - closes[i - 1]
        g = chg if chg > 0 else 0.0
        l = -chg if chg < 0 else 0.0
        avg_g = (avg_g * (window - 1) + g) / window
        avg_l = (avg_l * (window - 1) + l) / window
        out[i] = 100.0 if avg_l == 0 else 100 - 100 / (1 + avg_g / avg_l)
    return out


def ema_series(values, span):
    out = [None] * len(values)
    k = 2.0 / (span + 1)
    prev = None
    for i, v in enumerate(values):
        if v is None:
            continue
        prev = v if prev is None else v * k + prev * (1 - k)
        out[i] = prev
    return out


def rolling_minmax_norm(dates, values, window):
    out = {}
    vals = []
    for i, d in enumerate(dates):
        v = values[i]
        vals.append(v)
        if v is None:
            continue
        lo_i = max(0, i - window + 1)
        window_vals = [x for x in vals[lo_i:i + 1] if x is not None]
        if len(window_vals) < window // 2:
            continue
        mn, mx = min(window_vals), max(window_vals)
        out[d] = 0.5 if mx - mn < 1e-12 else (v - mn) / (mx - mn)
    return out


def build(debug=False):
    yd = load_yahoo()

    # ── 1. ^IXIC (기준 시간축) ──
    ixic = yd["data"]["^IXIC"]["candles"]
    x_dates = [c["time"] for c in ixic]
    x_closes = [c["close"] for c in ixic]

    ma = sma(x_closes, MA_DEV_WINDOW)
    ma_dev_raw = [None if ma[i] is None else (x_closes[i] - ma[i]) / ma[i] for i in range(len(x_closes))]
    rsi_raw = rsi(x_closes, RSI_WINDOW)

    # ── 2. VIX / VIX9D ──
    vix_map = closes_map(yd, "^VIX")
    v9d_map = closes_map(yd, "^VIX9D")
    pc_proxy_map = {}
    for d, v in vix_map.items():
        v9 = v9d_map.get(d)
        if v9 is not None and v > 0:
            pc_proxy_map[d] = v9 / v

    # ── 3. Bond spread (ZN - ZF) ──
    zn_map = closes_map(yd, "ZN=F")
    zf_map = closes_map(yd, "ZF=F")
    bond_map = {}
    for d, zn in zn_map.items():
        zf = zf_map.get(d)
        if zf is not None:
            bond_map[d] = zn - zf
    if debug:
        print(f"[debug] bond coverage: {len(bond_map)} days, vix: {len(vix_map)}, pc_proxy: {len(pc_proxy_map)}")

    # ── 4. 정규화 ──
    norm = {}
    norm["ma_dev"] = rolling_minmax_norm(x_dates, ma_dev_raw, NORM_WINDOW)
    norm["rsi"] = rolling_minmax_norm(x_dates, rsi_raw, NORM_WINDOW)
    for key, m in (("pc_proxy", pc_proxy_map), ("vix", vix_map), ("bond_spread", bond_map)):
        ds = sorted(m)
        norm[key] = rolling_minmax_norm(ds, [m[d] for d in ds], NORM_WINDOW)

    if debug:
        for k, m in norm.items():
            ds = sorted(m)
            print(f"[debug] {k}: {len(m)} days ({ds[0] if ds else '-'} ~ {ds[-1] if ds else '-'})")

    # ── 5. 합성 (^IXIC 거래일 기준, 3+ factors) ──
    fg_dates, fg_vals = [], []
    for d in x_dates:
        parts = []
        for key, sign in SIGNS.items():
            v = norm[key].get(d)
            if v is None:
                continue
            parts.append(v if sign > 0 else 1.0 - v)
        if len(parts) >= 3:
            fg_dates.append(d)
            fg_vals.append(sum(parts) / len(parts))

    # ── 6. MACD 히스토그램 ──
    ema_f = ema_series(fg_vals, MACD_FAST)
    ema_s = ema_series(fg_vals, MACD_SLOW)
    macd_line = [None if (ema_f[i] is None or ema_s[i] is None) else ema_f[i] - ema_s[i] for i in range(len(fg_vals))]
    signal = ema_series(macd_line, MACD_SIGNAL)
    hist = [None if (macd_line[i] is None or signal[i] is None) else macd_line[i] - signal[i] for i in range(len(fg_vals))]

    rows = []
    for i, d in enumerate(fg_dates):
        if hist[i] is None or i < MACD_SLOW + MACD_SIGNAL:
            continue
        rows.append([d, {"osc": round(hist[i], 6), "fg": round(fg_vals[i], 4)}])

    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "method": (
            f"US 5-factor equal-weight FG index (^IXIC 125MA dev, VIX9D/VIX inv, VIX inv, "
            f"ZN-ZF spread, RSI{RSI_WINDOW}), rolling {NORM_WINDOW}d min-max norm, "
            f"MACD({MACD_FAST},{MACD_SLOW},{MACD_SIGNAL}) histogram"
        ),
        "n_rows": len(rows),
        "data": rows,
    }
    tmp = OUT_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    tmp.replace(OUT_PATH)
    print(f"[OK] {OUT_PATH.name}: {len(rows)} rows")
    if rows:
        print(f"  첫 일자: {rows[0][0]}, 마지막: {rows[-1][0]} → osc={rows[-1][1]['osc']}, fg={rows[-1][1]['fg']}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--debug", action="store_true")
    args = ap.parse_args()
    build(debug=args.debug)
