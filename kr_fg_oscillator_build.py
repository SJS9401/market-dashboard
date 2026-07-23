#!/usr/bin/env python3
"""
피어앤그리드 (Fear & Greed) 오실레이터 빌더 — KOSPI
태린이아빠 채널 방법론 (2026-07-23 공유) 구현:

  1) 5개 변수를 각각 0~1 정규화 (rolling 252영업일 min-max):
     - 지수의 125일 이동평균 대비 괴리율  (↑ = 탐욕)
     - Put/Call 비율                       (↑ = 공포 → invert)
     - 변동성지수 V-KOSPI                  (↑ = 공포 → invert)
     - 10년 국채선물지수 - 5년 국채선물지수 (↑ = 탐욕)
     - RSI 10일                            (↑ = 탐욕)
  2) 동일가중 평균 → 합성 Fear & Greed Index (0~1)
  3) MACD(12,26,9) 적용 → 히스토그램 = 최종 오실레이터
     (절대 심리 수준이 아니라 심리 개선/둔화 속도를 보여줌)

입력 (data/):
  yahoo_dashboard.json   ^KS11 candles (125MA 괴리율 + RSI10)
  kr_putcall.json        [date, {pc, ...}]
  kr_vkospi.json         [date, value]
  kr_ktb_futures.json    [date, {ktb10, ktb5, ktb3}]

출력: data/kr_fg_oscillator.json
{
  "generated_at": "...",
  "method": "...",
  "data": [["2016-01-04", {"osc": 0.0123, "fg": 0.55}], ...]
}

사용법:
  py kr_fg_oscillator_build.py            # 빌드
  py kr_fg_oscillator_build.py --debug    # 변수별 커버리지 출력
"""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
OUT_PATH = DATA_DIR / "kr_fg_oscillator.json"

# ── 설정 ──
NORM_WINDOW = 252        # 정규화 rolling window (영업일)
MA_DEV_WINDOW = 125      # 이동평균 괴리율 기준
RSI_WINDOW = 10
MACD_FAST, MACD_SLOW, MACD_SIGNAL = 12, 26, 9
# 변수 방향: +1 = 값이 클수록 탐욕, -1 = 값이 클수록 공포 (invert)
SIGNS = {"ma_dev": +1, "putcall": -1, "vkospi": -1, "ktb_spread": +1, "rsi": +1}


def load_json(name):
    p = DATA_DIR / name
    if not p.exists():
        raise FileNotFoundError(f"{p} 없음")
    return json.loads(p.read_text(encoding="utf-8"))


def sma(values, window):
    """단순이동평균 — 앞부분은 None."""
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
    """Wilder's RSI."""
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
    """EMA — None 이 아닌 첫 값부터 시작."""
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
    """rolling window min-max 정규화 → 0~1. window 미만 구간은 None."""
    out = {}
    vals = []
    for i, d in enumerate(dates):
        v = values[i]
        vals.append(v)
        if v is None:
            continue
        lo_i = max(0, i - window + 1)
        window_vals = [x for x in vals[lo_i:i + 1] if x is not None]
        if len(window_vals) < window // 2:   # 데이터 절반 미만이면 skip
            continue
        mn, mx = min(window_vals), max(window_vals)
        if mx - mn < 1e-12:
            out[d] = 0.5
        else:
            out[d] = (v - mn) / (mx - mn)
    return out


def build(debug=False):
    # ── 1. KOSPI closes (^KS11) ──
    yd = load_json("yahoo_dashboard.json")
    candles = yd["data"]["^KS11"]["candles"]
    k_dates = [c["time"] for c in candles]
    k_closes = [c["close"] for c in candles]

    ma = sma(k_closes, MA_DEV_WINDOW)
    ma_dev_raw = [None if ma[i] is None else (k_closes[i] - ma[i]) / ma[i] for i in range(len(k_closes))]
    rsi_raw = rsi(k_closes, RSI_WINDOW)

    # ── 2. Put/Call ──
    pc_json = load_json("kr_putcall.json")
    pc_map = {}
    for d, v in pc_json.get("data", []):
        if isinstance(v, dict):
            pc_map[d] = v.get("pc")
        else:
            pc_map[d] = v

    # ── 3. V-KOSPI ──
    vk_json = load_json("kr_vkospi.json")
    vk_map = {d: v for d, v in vk_json.get("data", [])}

    # ── 4. KTB spread (10y - 5y, fallback 10y - 3y) ──
    ktb_json = load_json("kr_ktb_futures.json")
    ktb_map = {}
    for d, v in ktb_json.get("data", []):
        t10, t5, t3 = v.get("ktb10"), v.get("ktb5"), v.get("ktb3")
        if t10 is not None and t5 is not None:
            ktb_map[d] = t10 - t5
        elif t10 is not None and t3 is not None:
            ktb_map[d] = t10 - t3   # 5년 상장 전 fallback
    if debug:
        print(f"[debug] ktb coverage: {len(ktb_map)} days")

    # ── 5. 변수별 rolling 정규화 ──
    norm = {}
    norm["ma_dev"] = rolling_minmax_norm(k_dates, ma_dev_raw, NORM_WINDOW)
    norm["rsi"] = rolling_minmax_norm(k_dates, rsi_raw, NORM_WINDOW)

    pc_dates = sorted(pc_map)
    norm["putcall"] = rolling_minmax_norm(pc_dates, [pc_map[d] for d in pc_dates], NORM_WINDOW)
    vk_dates = sorted(vk_map)
    norm["vkospi"] = rolling_minmax_norm(vk_dates, [vk_map[d] for d in vk_dates], NORM_WINDOW)
    ktb_dates = sorted(ktb_map)
    norm["ktb_spread"] = rolling_minmax_norm(ktb_dates, [ktb_map[d] for d in ktb_dates], NORM_WINDOW)

    if debug:
        for k, m in norm.items():
            ds = sorted(m)
            print(f"[debug] {k}: {len(m)} days ({ds[0] if ds else '-'} ~ {ds[-1] if ds else '-'})")

    # ── 6. 합성 (KOSPI 거래일 기준, factor 3개 이상 있는 날만) ──
    fg_dates, fg_vals = [], []
    for d in k_dates:
        parts = []
        for key, sign in SIGNS.items():
            v = norm[key].get(d)
            if v is None:
                continue
            parts.append(v if sign > 0 else 1.0 - v)
        if len(parts) >= 3:
            fg_dates.append(d)
            fg_vals.append(sum(parts) / len(parts))

    # ── 7. MACD 히스토그램 ──
    ema_f = ema_series(fg_vals, MACD_FAST)
    ema_s = ema_series(fg_vals, MACD_SLOW)
    macd_line = [None if (ema_f[i] is None or ema_s[i] is None) else ema_f[i] - ema_s[i] for i in range(len(fg_vals))]
    signal = ema_series(macd_line, MACD_SIGNAL)
    hist = [None if (macd_line[i] is None or signal[i] is None) else macd_line[i] - signal[i] for i in range(len(fg_vals))]

    # ── 8. 출력 (MACD warmup 구간 제외) ──
    rows = []
    for i, d in enumerate(fg_dates):
        if hist[i] is None or i < MACD_SLOW + MACD_SIGNAL:
            continue
        rows.append([d, {"osc": round(hist[i], 6), "fg": round(fg_vals[i], 4)}])

    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "method": (
            f"5-factor equal-weight FG index (125MA dev, PutCall inv, VKOSPI inv, "
            f"KTB 10y-5y spread, RSI{RSI_WINDOW}), rolling {NORM_WINDOW}d min-max norm, "
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
