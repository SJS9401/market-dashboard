#!/usr/bin/env python3
"""
ADR(20) backfill — KOSPI+KOSDAQ 통합 breadth 기반 10년치 ADR 시리즈 생성.

ADR(20) = Σ(최근 20영업일 상승 종목수) / Σ(최근 20영업일 하락 종목수) × 100

output: data/kr_adr.json
각 레코드:
  { "date": "YYYY-MM-DD", "advance": N, "decline": N, "unchanged": N, "adr": float }
"""
import json
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
from pykrx import stock

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_PATH = REPO_ROOT / "data" / "kr_adr.json"

WINDOW = 20  # 20일 누적 (한국 표준 ADR)


def fetch_day_breadth(yyyymmdd: str) -> dict | None:
    """하루치 KOSPI+KOSDAQ 통합 breadth 조회."""
    try:
        df_k = stock.get_market_ohlcv_by_ticker(yyyymmdd, "KOSPI")
        df_q = stock.get_market_ohlcv_by_ticker(yyyymmdd, "KOSDAQ")
    except Exception as e:
        print(f"  [fetch error] {yyyymmdd}: {e}", file=sys.stderr)
        return None

    if df_k is None or df_q is None or df_k.empty or df_q.empty:
        return None

    df = pd.concat([df_k, df_q])
    # 거래정지/관리종목 제외: 거래량 0이거나 시가 0인 종목
    df = df[(df.get("거래량", 0) > 0) & (df.get("시가", 0) > 0)]

    if df.empty:
        return None

    chg = df["등락률"]
    adv = int((chg > 0).sum())
    dec = int((chg < 0).sum())
    unc = int((chg == 0).sum())

    return {"advance": adv, "decline": dec, "unchanged": unc}


def compute_adr_series(raw: list[dict]) -> list[dict]:
    """raw breadth list (날짜순) → ADR(20) 누적 시리즈."""
    out = []
    for i, row in enumerate(raw):
        if i < WINDOW - 1:
            # 윈도우 채우기 전에는 ADR 계산 불가
            out.append({**row, "adr": None})
            continue
        window_slice = raw[i - WINDOW + 1 : i + 1]
        sum_adv = sum(r["advance"] for r in window_slice)
        sum_dec = sum(r["decline"] for r in window_slice)
        adr = round(sum_adv / sum_dec * 100, 2) if sum_dec > 0 else None
        out.append({**row, "adr": adr})
    return out


def load_existing() -> list[dict]:
    if OUT_PATH.exists():
        with open(OUT_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save(records: list[dict]) -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, separators=(",", ":"))
    print(f"[saved] {OUT_PATH} ({len(records)} records)")


def main(years: int = 10) -> None:
    end = datetime.now()
    # pykrx는 오늘 장중 호출 시 데이터 미정일 수 있어 -1일 여유
    start = end - timedelta(days=365 * years + 30)

    # 기존 데이터 유무 확인
    existing = load_existing()
    existing_dates = {r["date"] for r in existing}
    if existing:
        last_date_str = max(existing_dates)
        last_date = datetime.strptime(last_date_str, "%Y-%m-%d")
        start = last_date + timedelta(days=1)
        print(f"[resume] last existing date: {last_date_str} — fetching from {start.date()}")
    else:
        print(f"[cold start] fetching {years}년치: {start.date()} → {end.date()}")

    # 영업일 리스트: 평일만 (실제 휴장일은 pykrx가 빈 DataFrame 반환으로 걸러짐)
    days = []
    cur = start
    while cur <= end:
        if cur.weekday() < 5:  # 월~금
            days.append(cur.strftime("%Y%m%d"))
        cur += timedelta(days=1)

    print(f"[plan] {len(days)} 영업일 후보 (휴장일 자동 스킵)")

    raw_new = []
    for i, day in enumerate(days):
        breadth = fetch_day_breadth(day)
        if breadth is None:
            print(f"  [{i+1}/{len(days)}] {day} — 휴장 or 데이터 없음")
            continue
        date_iso = f"{day[:4]}-{day[4:6]}-{day[6:8]}"
        record = {"date": date_iso, **breadth}
        raw_new.append(record)
        if (i + 1) % 50 == 0 or (i + 1) == len(days):
            print(
                f"  [{i+1}/{len(days)}] {date_iso} — adv={breadth['advance']} "
                f"dec={breadth['decline']} unc={breadth['unchanged']}"
            )
        time.sleep(0.15)  # KRX rate limit 완화

    # 병합 후 정렬, ADR 재계산 (윈도우 연속성 보장을 위해 전체 재계산)
    raw_all = [r for r in existing if "adr" not in r or r.get("adr") is None or True]
    # 기존 레코드에서 adv/dec/unc만 남기고 adr 재계산 대상화
    base_records = [
        {"date": r["date"], "advance": r["advance"], "decline": r["decline"], "unchanged": r["unchanged"]}
        for r in existing
    ]
    all_records = base_records + raw_new
    # 중복 제거 (date 기준), 날짜순 정렬
    seen = {}
    for r in all_records:
        seen[r["date"]] = r
    sorted_records = sorted(seen.values(), key=lambda x: x["date"])

    final = compute_adr_series(sorted_records)
    save(final)

    # 요약 출력
    with_adr = [r for r in final if r["adr"] is not None]
    if with_adr:
        first = with_adr[0]
        last = with_adr[-1]
        print(f"[summary] ADR 계산 {len(with_adr)}건 — {first['date']} ADR {first['adr']} → {last['date']} ADR {last['adr']}")


if __name__ == "__main__":
    years = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    main(years)
