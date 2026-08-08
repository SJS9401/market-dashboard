# -*- coding: utf-8 -*-
"""
dotcom_price.json 라이브 시리즈 일일 갱신
==========================================
Current_cycle.html / Dotcom_vs_now.html 이 쓰는 data/dotcom_price.json 에서
현재 진행 중인 5개 시리즈만 트레일링 윈도우로 갱신한다.

  갱신 대상 : IXIC, KS11, NVDA, MU, HYNIX   (yfinance, adjclose 반영)
  불변 대상 : IXIC_OLD, CSCO, QCOM          (1989~2002 정적 — 절대 건드리지 않음)

설계 메모
---------
* 트레일링 윈도우(기본 45일)를 **재조회 후 교체**한다. append 가 아니라 replace 인 이유:
  배당락 등으로 수정주가 계수가 바뀌어도 최근 구간이 자동으로 자기치유된다.
* 윈도우 밖 과거 데이터는 손대지 않는다. 전체 재빌드가 필요하면 --full 로 별도 실행.
* 한 종목이 실패해도 나머지는 저장한다 (부분 성공 허용). 전 종목 실패 시에만 exit 1.
* 파일 쓰기는 .tmp + os.replace 로 원자적 처리 — 중단돼도 JSON 이 깨지지 않는다.

사용
----
    python dotcom_price_update.py                # 기본 (트레일링 45일)
    python dotcom_price_update.py --days 120     # 윈도우 확대
    python dotcom_price_update.py --dry-run      # 저장 없이 진단만
"""
import argparse
import io
import json
import os
import sys
from datetime import datetime, timedelta, timezone

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(SCRIPT_DIR, "data", "dotcom_price.json")

# 파일 내 시리즈 키 -> yfinance 티커
LIVE = {
    "IXIC":  "^IXIC",
    "KS11":  "^KS11",
    "NVDA":  "NVDA",
    "MU":    "MU",
    "HYNIX": "000660.KS",
}
FROZEN = ("IXIC_OLD", "CSCO", "QCOM")


def fetch(ticker, days):
    """[[YYYY-MM-DD, o, h, l, c], ...] — 수정주가 반영, 결측 행 제외."""
    import yfinance as yf

    start = (datetime.now(timezone.utc) - timedelta(days=days + 10)).strftime("%Y-%m-%d")
    df = yf.download(ticker, start=start, interval="1d",
                     auto_adjust=True, progress=False, threads=False)
    if df is None or df.empty:
        raise RuntimeError("빈 응답")
    if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
        df.columns = df.columns.get_level_values(0)

    rows = []
    for idx, r in df.iterrows():
        vals = [r.get("Open"), r.get("High"), r.get("Low"), r.get("Close")]
        if any(v is None or v != v for v in vals):      # NaN 제외
            continue
        rows.append([idx.strftime("%Y-%m-%d")] + [round(float(v), 4) for v in vals])
    if not rows:
        raise RuntimeError("유효 행 0건")
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=45, help="트레일링 윈도우 (기본 45일)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not os.path.exists(OUT_PATH):
        sys.exit("[ERROR] 없음: %s — 최초 파일은 별도 빌드 필요" % OUT_PATH)

    with io.open(OUT_PATH, encoding="utf-8") as fh:
        doc = json.load(fh)
    series = doc["series"]

    # 정적 시리즈 지문 — 갱신 후 무결성 확인용
    frozen_before = {k: (series[k]["n"], series[k]["to"]) for k in FROZEN if k in series}

    ok, failed, changed = [], [], 0
    for key, ticker in LIVE.items():
        if key not in series:
            print("[SKIP] %-6s 파일에 없음" % key)
            continue
        ser = series[key]
        try:
            fresh = fetch(ticker, args.days)
        except Exception as exc:                                  # noqa: BLE001
            failed.append(key)
            print("[FAIL] %-6s %s -> %s" % (key, ticker, exc))
            continue

        cutoff = fresh[0][0]
        kept = [r for r in ser["data"] if r[0] < cutoff]
        merged = kept + fresh
        before_n, before_to = ser["n"], ser["to"]
        if merged != ser["data"]:
            changed += 1
        ser["data"] = merged
        ser["n"] = len(merged)
        ser["to"] = merged[-1][0]
        ok.append(key)
        print("[OK]   %-6s %s -> %s  (n %d -> %d, 교체 %d행)  종가 %s"
              % (key, before_to, ser["to"], before_n, ser["n"], len(fresh), merged[-1][4]))

    if not ok:
        sys.exit("[ERROR] 전 종목 실패 — 파일 미변경")

    # 정적 시리즈가 건드려지지 않았는지 확인
    for k, sig in frozen_before.items():
        now = (series[k]["n"], series[k]["to"])
        if now != sig:
            sys.exit("[ERROR] 정적 시리즈 %s 변형됨: %s -> %s" % (k, sig, now))

    doc.setdefault("meta", {})["updated"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    doc["meta"]["live_series"] = sorted(LIVE)

    if args.dry_run:
        print("[dry-run] 저장 생략 (변경 %d 시리즈)" % changed)
        return

    tmp = OUT_PATH + ".tmp"
    with io.open(tmp, "w", encoding="utf-8", newline="") as fh:
        fh.write(json.dumps(doc, ensure_ascii=False, separators=(",", ":")))
    os.replace(tmp, OUT_PATH)
    print("[SAVED] %s  %.1f KB  성공 %d / 실패 %d %s"
          % (os.path.basename(OUT_PATH), os.path.getsize(OUT_PATH) / 1024.0,
             len(ok), len(failed), failed or ""))


if __name__ == "__main__":
    main()
