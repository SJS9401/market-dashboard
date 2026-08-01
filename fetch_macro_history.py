#!/usr/bin/env python3
"""
fetch_macro_history.py — 글로벌 사이클 비교용 매크로 장기 시계열 수집 (2026-08-01 신설)

배경:
  "닷컴 vs 현재" / "중국 인프라 vs 현재" 두 탭에서 세 사이클(1995~2002 / 2003~2008 / 2023~현재)의
  금리·크레딧·원자재를 같은 축으로 비교한다. FRED 는 브라우저에서 CORS 로 막히므로
  (yahoo_dashboard 와 동일한 문제) GitHub Actions 에서 서버사이드로 받아 JSON 으로 커밋한다.

수집:
  금리   DGS10(10Y) · DGS30(30Y) · DFF(FFR) · T10YIE(10Y BEI)
  크레딧 BAMLH0A0HYM2(HY OAS) · BAMLC0A0CM(IG OAS)
  원자재 DCOILWTICO(WTI) · PCOPPUSDM(구리) · PIORECRUSDM(철광석)

저장 정책:
  일별 시리즈는 주간(각 주 마지막 관측)으로 다운샘플 — 세 사이클 30년치를 담아도 파일이 가볍다.
  월별 시리즈(PCOPPUSDM·PIORECRUSDM)는 원본 그대로.

출력: data/macro_history.json
  {"meta": {...}, "series": {"<id>": {"label","unit","freq","data":[[date,value],...]}}}

CLI:
  py fetch_macro_history.py               # 전체
  py fetch_macro_history.py --ids DGS10   # 일부만
  py fetch_macro_history.py --dry-run
"""
import argparse
import csv
import io
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(THIS_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
OUT_PATH = os.path.join(DATA_DIR, "macro_history.json")

START = "1994-01-01"   # 닷컴 사이클 시작 이전부터

# id: (라벨, 단위, 주간 다운샘플 여부)
SERIES = {
    # ── 금리
    "DGS10":        ("미 10년물 국채금리", "%", True),
    "DGS30":        ("미 30년물 국채금리", "%", True),
    "DFF":          ("연방기금금리 (실효)", "%", True),
    "T10YIE":       ("10년 기대인플레 (BEI)", "%", True),
    # ── 크레딧
    "BAMLH0A0HYM2": ("하이일드 OAS", "%p", True),
    "BAMLC0A0CM":   ("IG 회사채 OAS", "%p", True),
    # ── 원자재
    "DCOILWTICO":   ("WTI 원유", "$/bbl", True),
    "PCOPPUSDM":    ("구리", "$/t", False),
    "PIORECRUSDM":  ("철광석", "$/t", False),
}

# cosd 만 주면 일부 시리즈(BAML 크레딧 계열)가 기본 창으로 잘려 최근 3년만 온다.
# coed(종료일)를 명시해야 전 구간이 내려온다. (2026-08-01 실측 — HY/IG OAS 가 157pt 로 잘렸음)
FRED_CSV = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={id}&cosd={start}&coed={end}"

# 시리즈별 최소 기대 포인트 — 미달 시 경고 (조용한 절단 재발 방지)
MIN_PTS = {
    "DGS10": 1500, "DGS30": 1200, "DFF": 1500, "T10YIE": 1000,
    "BAMLH0A0HYM2": 1400, "BAMLC0A0CM": 1400,
    "DCOILWTICO": 1500, "PCOPPUSDM": 350, "PIORECRUSDM": 350,
}


def _log(msg):
    print(f"[{datetime.now().isoformat(timespec='seconds')}] {msg}", flush=True)


def fetch_series(sid, start=START, retry=3):
    """FRED CSV → [[YYYY-MM-DD, float], ...]. 결측('.')은 제외."""
    end = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    url = FRED_CSV.format(id=sid, start=start, end=end)
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (market-dashboard macro fetcher)"})
    for a in range(1, retry + 1):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                raw = r.read().decode("utf-8", errors="replace")
            break
        except Exception as e:
            _log(f"  {sid}: {e} (attempt {a}/{retry})")
            if a == retry:
                return None
            time.sleep(3)

    rows = list(csv.reader(io.StringIO(raw)))
    if not rows or len(rows) < 2:
        return None
    # 헤더는 보통 ['observation_date' 또는 'DATE', '<ID>'] — 위치로 처리
    out = []
    for rec in rows[1:]:
        if len(rec) < 2:
            continue
        d, v = rec[0].strip(), rec[1].strip()
        if not d or v in (".", "", "NA"):
            continue
        try:
            out.append([d, float(v)])
        except ValueError:
            continue
    return out or None


def weekly(data):
    """각 ISO 주의 마지막 관측만 남긴다."""
    if not data:
        return data
    keep, cur_key, cur = [], None, None
    for d, v in data:
        y, w, _ = datetime.strptime(d, "%Y-%m-%d").isocalendar()
        k = (y, w)
        if cur_key is None:
            cur_key, cur = k, [d, v]
        elif k != cur_key:
            keep.append(cur)
            cur_key, cur = k, [d, v]
        else:
            cur = [d, v]
    if cur:
        keep.append(cur)
    return keep


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ids", default=None, help="콤마 구분, 특정 시리즈만")
    ap.add_argument("--start", default=START)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    ids = args.ids.split(",") if args.ids else list(SERIES.keys())
    _log(f"=== fetch_macro_history ({len(ids)} series, from {args.start}) ===")

    series, fails, short = {}, [], []
    for sid in ids:
        label, unit, do_weekly = SERIES.get(sid, (sid, "", True))
        _log(f"fetching {sid} ({label})...")
        d = fetch_series(sid, args.start)
        if not d:
            fails.append(sid)
            _log("  FAIL")
            continue
        n0 = len(d)
        if do_weekly:
            d = weekly(d)
        series[sid] = {
            "label": label, "unit": unit,
            "freq": "weekly" if do_weekly else "monthly",
            "data": d,
        }
        _log(f"  OK {n0} → {len(d)} pts | {d[0][0]} ~ {d[-1][0]}")
        need = MIN_PTS.get(sid)
        if need and len(d) < need:
            short.append(f"{sid}({len(d)}<{need}, 시작 {d[0][0]})")
            _log(f"  ⚠ 절단 의심 — 기대 {need}pt 이상")
        time.sleep(0.4)

    output = {
        "meta": {
            "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "start": args.start,
            "source": "FRED (St. Louis Fed)",
            "ok": len(series), "fail": fails, "short": short,
            "note": "일별 시리즈는 주간(주 마지막 관측)으로 다운샘플. 월별은 원본.",
        },
        "series": series,
    }

    _log(f"=== summary: {len(series)}/{len(ids)} ok ===")
    if fails:
        _log(f"  FAIL: {fails}")
    if short:
        _log(f"  ⚠ 절단 의심: {short}")

    if args.dry_run:
        _log(f"[dry-run] skip write to {OUT_PATH}")
        return

    tmp = OUT_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, separators=(",", ":"))
    os.replace(tmp, OUT_PATH)
    _log(f"wrote {OUT_PATH} ({os.path.getsize(OUT_PATH)/1024:.1f} KB)")

    if fails:
        sys.exit(1)


if __name__ == "__main__":
    main()
