#!/usr/bin/env python3
"""
Market_cycle.html 의 CYCLES 배열에서 메타데이터만 추출 → market_cycles.json

목적:
  Leading_stocks.html 빌더에서 미국/한국 사이클을 분리해 박스 표시할 때
  Market_cycle 의 분류 (id, name, indices) 를 직접 사용하기 위함.

추출 필드:
  id, name, type, start, end, peak, trough, category, subtype, indices

제외 (용량 큼):
  priceDatasets, volume, mddDatasets, etc

실행:
  py extract_market_cycles.py
"""
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SRC = SCRIPT_DIR / "Market_cycle.html"
DST = SCRIPT_DIR / "market_cycles.json"

KEEP_FIELDS = {
    "id", "name", "type", "start", "end", "peak", "trough",
    "category", "subtype", "indices",
    # 추가 메타 (있는 경우만)
    "mddMin", "leadingStock", "remark"
}


def find_cycles_array(text):
    """`const CYCLES = [...]` 의 배열 부분 (대괄호 포함) 추출.
    중첩 괄호 카운팅으로 정확한 끝 찾기."""
    m = re.search(r"const\s+CYCLES\s*=\s*\[", text)
    if not m:
        return None
    start = m.end() - 1  # '[' 위치
    depth = 0
    in_str = False
    str_ch = None
    esc = False
    for i in range(start, len(text)):
        c = text[i]
        if esc:
            esc = False
            continue
        if c == "\\":
            esc = True
            continue
        if in_str:
            if c == str_ch:
                in_str = False
            continue
        if c == '"' or c == "'":
            in_str = True
            str_ch = c
            continue
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                return text[start:i + 1]
    return None


def main():
    if not SRC.exists():
        print(f"[ERROR] {SRC} 없음")
        sys.exit(1)

    print(f"[*] 로드: {SRC}")
    text = SRC.read_text(encoding="utf-8")
    arr_str = find_cycles_array(text)
    if arr_str is None:
        print("[ERROR] CYCLES 배열을 찾을 수 없음")
        sys.exit(1)
    print(f"[*] CYCLES 배열 추출: {len(arr_str):,} bytes")

    cycles = json.loads(arr_str)
    print(f"[*] 사이클 {len(cycles)}개 파싱")

    # 메타데이터만 추출 + indices 가 SP500/NASDAQ 만 있으면 'us', KOSPI/KOSDAQ 만 있으면 'kr', 둘 다 있으면 'mixed'
    out = []
    us_count = kr_count = mixed_count = 0
    for c in cycles:
        meta = {k: c[k] for k in KEEP_FIELDS if k in c}
        idxs = set(meta.get("indices", []))
        has_us = bool(idxs & {"SP500", "NASDAQ"})
        has_kr = bool(idxs & {"KOSPI", "KOSDAQ"})
        if has_us and has_kr:
            meta["region"] = "global"
            mixed_count += 1
        elif has_us:
            meta["region"] = "us"
            us_count += 1
        elif has_kr:
            meta["region"] = "kr"
            kr_count += 1
        else:
            meta["region"] = "unknown"
        out.append(meta)

    print(f"  US-only : {us_count}")
    print(f"  KR-only : {kr_count}")
    print(f"  Global  : {mixed_count}")

    # 시작일 정렬
    out.sort(key=lambda c: c.get("start") or "")

    DST.write_text(
        json.dumps({"generated_from": "Market_cycle.html", "count": len(out), "cycles": out},
                   ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    sz = DST.stat().st_size
    print(f"\n[OK] 저장: {DST} ({sz/1024:.1f} KB)")
    print(f"  {len(out)} 사이클 메타데이터")

    # 미리보기
    print("\n샘플 (앞 5개):")
    for c in out[:5]:
        print(f"  [{c['region']:6s}] {c.get('start','?')} ~ {c.get('end','?')}  {c.get('name','?')} ({c.get('category','?')}/{c.get('subtype','?')})")


if __name__ == "__main__":
    main()
