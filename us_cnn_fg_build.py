#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""us_cnn_fg_build.py — CNN Business Fear & Greed Index 총점 수집 (2026-09-17 신설)

우리 7-factor F&G 와 나란히 비교하기 위한 외부 대조군. 총점만 저장한다
(서브지표는 필요할 때 CNN 사이트에서 직접 본다 — 2026-09-17 BT).

엔드포인트 (실측)
  .../index/fearandgreed/graphdata              → 최근 1년 (252p)
  .../index/fearandgreed/graphdata/YYYY-MM-DD   → 그 날짜부터
  ★ 소급 한계 2020-09-21. 2018 로 요청하면 500 — CNN 자체 아카이브가 그때 시작이다.
  ★ 전체 소급 응답은 약 910KB. 일상 갱신은 기본 URL(1년)로 충분하고,
    기존 파일과 병합하므로 매번 전체를 받을 필요가 없다.

★ 브라우저 UA 필수 가능성 — dataviz 엔드포인트는 기본 python UA 를 막을 수 있다.
  네이버와 같은 대응(UA + Referer). 첫 실행은 dispatch 로 확인할 것.

출력: data/us_cnn_fg.json
  { generated_at, source, current:{date,score,rating}, n_rows, data:[[date, score], ...] }
"""
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone

BASE = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata"
BACKFILL_FROM = "2020-09-19"          # 실측 소급 한계(2020-09-21) 직전
OUT_PATH = os.path.join("data", "us_cnn_fg.json")
HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"),
    "Accept": "application/json, text/plain, */*",
    "Referer": "https://edition.cnn.com/markets/fear-and-greed",
    "Accept-Language": "en-US,en;q=0.9",
}


def _log(m):
    print(f"[{datetime.now(timezone.utc):%H:%M:%S}] {m}", flush=True)


def fetch(path="", max_retry=3):
    url = BASE + path
    last = None
    for a in range(max_retry):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:                                  # noqa: BLE001
            last = e
            _log(f"  ! fetch 실패 ({a + 1}/{max_retry}) {path or '(기본)'}: {e}")
            time.sleep(2 * (a + 1))
    raise RuntimeError(f"CNN fetch 실패: {last}")


def to_rows(payload):
    """historical 배열 → {date: score}. 하루 여러 포인트면 마지막 값이 이긴다."""
    hist = ((payload.get("fear_and_greed_historical") or {}).get("data")) or []
    out = {}
    for p in hist:
        x, y = p.get("x"), p.get("y")
        if x is None or y is None:
            continue
        d = datetime.fromtimestamp(x / 1000, timezone.utc).strftime("%Y-%m-%d")
        out[d] = round(float(y), 2)
    return out


def main():
    full = os.environ.get("FULL", "0") == "1"
    merged = {}

    if os.path.exists(OUT_PATH) and not full:
        try:
            prev = json.load(open(OUT_PATH, encoding="utf-8"))
            for d, s in (prev.get("data") or []):
                merged[d] = s
            _log(f"기존 {len(merged)}행 로드")
        except Exception as e:                                  # noqa: BLE001
            _log(f"기존 파일 무시 ({e})")

    if not merged or full:
        _log(f"전체 소급 수집 ({BACKFILL_FROM}~)")
        payload = fetch("/" + BACKFILL_FROM)
    else:
        _log("증분 수집 (최근 1년)")
        payload = fetch()

    rows = to_rows(payload)
    if not rows:
        raise SystemExit("historical 비어 있음 — 스키마 변경 의심, 저장 중단")
    before = len(merged)
    merged.update(rows)
    _log(f"수신 {len(rows)}행 → 병합 {before} → {len(merged)}행")

    if len(merged) < 200:
        raise SystemExit(f"행 수 이상({len(merged)}) — 저장 중단")

    fg = payload.get("fear_and_greed") or {}
    data = sorted(merged.items())
    cur_date, cur_score = data[-1]
    out = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "CNN Business Fear & Greed Index (production.dataviz.cnn.io)",
        "note": "총점만 저장. 서브지표는 CNN 사이트에서 직접 확인 (2026-09-17 BT).",
        "current": {
            "date": cur_date,
            "score": round(float(fg.get("score", cur_score)), 1),
            "rating": fg.get("rating", ""),
        },
        "n_rows": len(data),
        "data": [[d, s] for d, s in data],
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    tmp = OUT_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    os.replace(tmp, OUT_PATH)
    _log(f"WROTE {OUT_PATH}  {data[0][0]}~{cur_date}  {len(data)}행  "
         f"현재 {out['current']['score']} {out['current']['rating']}  "
         f"{os.path.getsize(OUT_PATH):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
