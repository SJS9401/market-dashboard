#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
us_intraday_build.py — 미국 4대 지수 장중 봉 수집 (2026-09-16 신설)
------------------------------------------------------------------
dashboard.html 나스닥 컬럼 상단 "인트라데이" 카드용 데이터.

  - 5분봉: ^GSPC ^IXIC ^DJI ^RUT  (야후 네이티브 interval=5m, range=1d — 직전 세션 79봉)
  - 15분봉: ^IXIC 단독            (네이티브 interval=15m, range=1mo + MA 5/20/60/120)

설계 메모
  * 야후는 3분봉을 지원하지 않는다 (유효 간격: 1m 2m 5m 15m 30m 60m 90m 1h 4h 1d ...).
    5분/15분은 네이티브라 집계 레이어가 없다 = 오차원 자체가 없다.
  * dashboard 가 야후를 직접 fetch 하면 sjs9401.github.io origin 이 차단된다.
    그래서 yahoo_dashboard.json 과 똑같이 Actions 가 받아서 JSON 으로 커밋한다.
  * ★ 15분봉이 range=1mo 인 이유 — 세션당 27봉뿐이라 MA60(2.2세션)·MA120(4.5세션)이
    한 세션 안에서는 계산 자체가 불가능하다. 한 달치를 연속으로 받아 MA 를 구한 뒤
    최근 KEEP_B15 봉만 잘라 보낸다. 장 마감~다음 개장 갭을 건너뛰고 이어 붙이는 건
    HTS 의 장중 이평선과 같은 방식이다.
  * ★ 미완성 세션은 절대 쓰지 않는다. meta.currentTradingPeriod.regular.end 를 지나야만 write.
    Actions cron 이 최대 2시간 지연 발화하므로 마감 전에 깨는 슬롯이 실제로 생긴다.
    부분 세션을 덮어쓰면 "어제 장중 그림"이 반토막 난 채로 남는다.

출력: data/us_intraday.json
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

SYMBOLS = [
    ("^GSPC", "GSPC", "S&P 500"),
    ("^IXIC", "IXIC", "나스닥 종합"),
    ("^DJI",  "DJI",  "다우존스"),
    ("^RUT",  "RUT",  "러셀2000"),
]
B15_SYMBOL = "IXIC"          # 15분봉 + 이평선은 나스닥 종합만 (2026-09-16 BT)
B15_RANGE = "1mo"            # MA120 = 120봉 = 약 4.5세션 → 한 달치 필요
B15_MAS = [5, 20, 60, 120]
KEEP_B15 = 270               # 계산 후 남길 봉수 (약 10세션)
HOSTS = ["query1.finance.yahoo.com", "query2.finance.yahoo.com"]
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/125.0 Safari/537.36")
OUT_PATH = os.path.join("data", "us_intraday.json")


def _log(msg):
    print(f"[{datetime.now(timezone.utc):%H:%M:%S}] {msg}", flush=True)


def fetch_chart(symbol, interval, rng="1d", max_retry=3):
    """야후 chart API. host 2개 x 재시도."""
    last_err = None
    for attempt in range(max_retry):
        host = HOSTS[attempt % len(HOSTS)]
        url = (f"https://{host}/v8/finance/chart/"
               f"{urllib.request.quote(symbol)}?interval={interval}&range={rng}")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=20) as r:
                payload = json.load(r)
            result = (payload.get("chart") or {}).get("result") or []
            if not result:
                err = (payload.get("chart") or {}).get("error")
                raise ValueError(f"empty result: {err}")
            return result[0]
        except Exception as e:                                  # noqa: BLE001
            last_err = e
            _log(f"  ! {symbol} {interval} 실패 ({host}, {attempt + 1}/{max_retry}): {e}")
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"{symbol} {interval} fetch 실패: {last_err}")


def to_bars(result):
    """chart result -> [[t, o, h, l, c], ...]  (null 봉 제거, 소수 2자리)"""
    ts = result.get("timestamp") or []
    q = ((result.get("indicators") or {}).get("quote") or [{}])[0]
    o, h, l, c = (q.get(k) or [] for k in ("open", "high", "low", "close"))
    bars = []
    for i, t in enumerate(ts):
        if i >= len(c) or c[i] is None:
            continue
        if o[i] is None or h[i] is None or l[i] is None:
            continue
        bars.append([int(t), round(o[i], 2), round(h[i], 2), round(l[i], 2), round(c[i], 2)])
    return bars


def moving_avg(values, window):
    """단순이동평균. 앞쪽 window-1 개는 None (차트에서 그냥 비워진다)."""
    out, acc = [], 0.0
    for i, v in enumerate(values):
        acc += v
        if i >= window:
            acc -= values[i - window]
        out.append(round(acc / window, 2) if i >= window - 1 else None)
    return out


def session_closed(meta, now_utc):
    """정규장 마감을 지났는가. 지나지 않았으면 이 런은 아무것도 쓰지 않는다."""
    period = ((meta.get("currentTradingPeriod") or {}).get("regular") or {})
    end = period.get("end")
    if end is None:
        return None, None
    return now_utc >= int(end), int(end)


def main():
    now_utc = int(time.time())
    force = os.environ.get("FORCE", "0") == "1"
    out = {"meta": {}, "symbols": {}}
    first_meta = None

    for symbol, key, name in SYMBOLS:
        _log(f"{symbol} …")
        result = fetch_chart(symbol, "5m", "1d")
        meta = result.get("meta") or {}
        b5 = to_bars(result)
        if not b5:
            raise RuntimeError(f"{symbol} 5m: 유효 봉 0개")

        closed, end = session_closed(meta, now_utc)
        if closed is False and not force:
            left = (end - now_utc) // 60 if end else "?"
            _log(f"SKIP — 정규장 마감 전 (약 {left}분 남음). 부분 세션은 쓰지 않는다.")
            return 0
        if closed is None:
            _log("  ! currentTradingPeriod 없음 — 마감 판정 생략")

        prev_close = meta.get("chartPreviousClose")
        last_close = b5[-1][4]
        chg = (last_close - prev_close) if prev_close else None
        first_meta = first_meta or meta

        out["symbols"][key] = {
            "symbol": symbol,
            "name": name,
            "prev_close": round(prev_close, 2) if prev_close else None,
            "last": last_close,
            "chg": round(chg, 2) if chg is not None else None,
            "chg_pct": round(chg / prev_close * 100, 2) if chg is not None and prev_close else None,
            "high": max(b[2] for b in b5),
            "low": min(b[3] for b in b5),
            "b5": b5,
        }
        _log(f"  ok  5m={len(b5)}봉 last={last_close}")

        # 15분봉 + 이평선 — 나스닥만
        if key == B15_SYMBOL:
            r15 = fetch_chart(symbol, "15m", B15_RANGE)
            b15 = to_bars(r15)
            if len(b15) < max(B15_MAS):
                _log(f"  ! 15m {len(b15)}봉 — MA{max(B15_MAS)} 산출 불가, 이평선 생략")
                mas = {}
            else:
                closes = [b[4] for b in b15]
                mas = {f"ma{w}": moving_avg(closes, w) for w in B15_MAS}
            cut = max(0, len(b15) - KEEP_B15)
            out["symbols"][key]["b15"] = b15[cut:]
            out["symbols"][key]["b15_ma"] = {k: v[cut:] for k, v in mas.items()}
            _log(f"  ok  15m={len(b15)}봉 수신 → {len(b15) - cut}봉 저장, "
                 f"MA={list(mas) or '없음'}")

    gmt = (first_meta or {}).get("gmtoffset", 0)
    session_open = out["symbols"]["GSPC"]["b5"][0][0]
    out["meta"] = {
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ"),
        "session": datetime.fromtimestamp(session_open + gmt, timezone.utc).strftime("%Y-%m-%d"),
        "tz": (first_meta or {}).get("exchangeTimezoneName", "America/New_York"),
        "gmtoffset": gmt,
        "intervals": ["5m", "15m"],
        "b15_symbol": B15_SYMBOL,
        "b15_mas": B15_MAS,
        "source": "yahoo chart api (native 5m/15m — 집계 없음)",
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    tmp = OUT_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    os.replace(tmp, OUT_PATH)
    _log(f"WROTE {OUT_PATH}  session={out['meta']['session']}  "
         f"{os.path.getsize(OUT_PATH):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
