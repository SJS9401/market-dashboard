#!/usr/bin/env python3
"""
선물 (K200) 외국인 순매수 백필 — 네이버 금융 투자자별 매매동향 (sosok=03).

페이지: finance.naver.com/sise/investorDealTrendDay.naver?bizdate=YYYYMMDD&sosok=03&page=N
  한 페이지 = 10 거래일 (개인/외국인/기관계/... 순매수). 값 단위는 페이지 라벨에서 자동 감지.

출력: data/kr_futures_flow.json
{
  "generated_at", "source", "unit",
  "data": [["2026-07-24", {"frgn": -162, "prsn": 335, "orgn": -131}], ...]
}

사용법:
  py kr_futures_flow_backfill.py --probe             # 1페이지 + 단위 라벨 확인
  py kr_futures_flow_backfill.py --backfill 2024     # 해당 연도 1/1 까지
  py kr_futures_flow_backfill.py --update            # 최근 3페이지 (cron 용)
"""
import argparse
import json
import re
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
OUT_PATH = DATA_DIR / "kr_futures_flow.json"

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36",
      "Referer": "https://finance.naver.com/sise/"}


def fetch_page(page, bizdate=None):
    bd = bizdate or datetime.now().strftime("%Y%m%d")
    url = f"https://finance.naver.com/sise/investorDealTrendDay.naver?bizdate={bd}&sosok=03&page={page}"
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode("euc-kr", errors="replace")


def parse_rows(html):
    """[(date_str, {frgn, prsn, orgn}), ...] — 헤더 순서: 날짜/개인/외국인/기관계/..."""
    out = []
    for m in re.finditer(r"<tr[^>]*>\s*<td[^>]*>(\d{2}\.\d{2}\.\d{2})</td>(.*?)</tr>", html, re.S):
        d, rest = m.group(1), m.group(2)
        nums = re.findall(r"<td[^>]*>\s*(?:<span[^>]*>)?\s*([\-+][\d,]+|[\d,]+)\s*(?:</span>)?\s*</td>", rest)
        if len(nums) < 3:
            continue
        try:
            prsn = int(nums[0].replace(",", ""))
            frgn = int(nums[1].replace(",", ""))
            orgn = int(nums[2].replace(",", ""))
        except Exception:
            continue
        yy, mm, dd = d.split(".")
        date_str = f"20{yy}-{mm}-{dd}"
        out.append((date_str, {"frgn": frgn, "prsn": prsn, "orgn": orgn}))
    return out


def detect_unit(html):
    m = re.search(r"단위\s*[:：]\s*([^<\s]+)", re.sub(r"<[^>]+>", " ", html))
    return m.group(1).strip() if m else "unknown"


def save(merged, unit):
    rows = sorted(merged.items())
    out = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "네이버 금융 투자자별 매매동향 — 선물 (sosok=03)",
        "unit": unit,
        "n_rows": len(rows),
        "data": [[d, v] for d, v in rows],
    }
    tmp = OUT_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    tmp.replace(OUT_PATH)
    print(f"[OK] {OUT_PATH.name}: {len(rows)} rows ({rows[0][0]} ~ {rows[-1][0]})")


def load_existing():
    if OUT_PATH.exists():
        prev = json.loads(OUT_PATH.read_text(encoding="utf-8"))
        return {d: v for d, v in prev.get("data", [])}, prev.get("unit", "unknown")
    return {}, None


def cmd_probe():
    html = fetch_page(1)
    unit = detect_unit(html)
    rows = parse_rows(html)
    print(f"단위 라벨: {unit}")
    print(f"rows: {len(rows)}")
    for d, v in rows[:3]:
        print(f"  {d}: 외국인 {v['frgn']:+,} / 개인 {v['prsn']:+,} / 기관 {v['orgn']:+,}")


def cmd_backfill(until_year):
    merged, unit = load_existing()
    print(f"[*] 기존 {len(merged)} rows")
    target = f"{until_year}-01-01"
    for page in range(1, 200):
        html = fetch_page(page)
        if page == 1 and not unit:
            unit = detect_unit(html)
        rows = parse_rows(html)
        if not rows:
            print(f"  page {page}: empty — 종료")
            break
        added = 0
        for d, v in rows:
            if d not in merged:
                added += 1
            merged[d] = v
        oldest = min(d for d, _ in rows)
        print(f"  page {page}: {len(rows)} rows (~{oldest}), 신규 {added}")
        if oldest <= target:
            print(f"[*] 목표 {target} 도달")
            break
        if page % 5 == 0:
            save(merged, unit)
        time.sleep(0.4)
    save(merged, unit)


def cmd_update():
    merged, unit = load_existing()
    for page in (1, 2, 3):
        html = fetch_page(page)
        if not unit:
            unit = detect_unit(html)
        for d, v in parse_rows(html):
            merged[d] = v
        time.sleep(0.3)
    save(merged, unit)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--probe", action="store_true")
    g.add_argument("--backfill", metavar="YEAR")
    g.add_argument("--update", action="store_true")
    args = ap.parse_args()
    if args.probe:
        cmd_probe()
    elif args.backfill:
        cmd_backfill(args.backfill)
    else:
        cmd_update()
