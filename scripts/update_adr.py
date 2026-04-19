#!/usr/bin/env python3
"""
ADR 일일 증분 업데이트.

마지막 저장 날짜 이후 ~ 오늘까지 1일 단위로 breadth 조회하고 ADR(20) 재계산.
backfill_adr.py의 resume 경로를 그대로 사용.
"""
import sys
from pathlib import Path

# backfill 로직 재사용
sys.path.insert(0, str(Path(__file__).resolve().parent))
from backfill_adr import main

if __name__ == "__main__":
    # 증분 모드: years 파라미터 0.1 (충분히 작게 — 기존 데이터 resume 로직이 실제 범위 결정)
    main(years=1)
