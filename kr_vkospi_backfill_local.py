#!/usr/bin/env python3
"""
V-KOSPI 200 일별 Backfill — KRX OpenAPI raw HTTP 방식
mcap 백필 스크립트와 동일 패턴 (pykrx 의존 X, AUTH_KEY 사용).

신청 endpoint: 파생상품지수 시세정보 (drvprod_dd_trd)
응답 OutBlock_1 에서 IDX_NM == "V-KOSPI 200" row 의 CLSPRC_IDX 추출

사용법:
  py kr_vkospi_backfill_local.py --probe 20260424   # 응답 구조 + IDX_NM 리스트 확인
  py kr_vkospi_backfill_local.py --backfill 20100104 20260427
  py kr_vkospi_backfill_local.py --backfill 20100104 20260427 --overwrite

필요 패키지: 표준 라이브러리만 (urllib, json) — pip install 불필요

종료 후 data/kr_vkospi.json 생성 → GitHub data/kr_vkospi.json 업로드
예상 소요시간: 16년치 약 10~20분 (4000+ 영업일)

출력 구조:
{
  "generated_at": "2026-04-27T...Z",
  "source": "KRX OpenAPI - 파생상품지수 시세정보 (V-KOSPI 200)",
  "unit": "지수 포인트",
  "data": [["2010-01-04", 18.42], ...]
}
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
OUT_PATH = DATA_DIR / "kr_vkospi.json"

# AUTH_KEY 입력
AUTH_KEY = os.environ.get("KRX_AUTH_KEY") or ""
KEY_FILE = SCRIPT_DIR / ".krx_auth_key"
if not AUTH_KEY and KEY_FILE.exists():
    AUTH_KEY = KEY_FILE.read_text(encoding="utf-8").strip()

# KRX OpenAPI 호스트 + endpoint
HOST = "https://data-dbg.krx.co.kr"
ENDPOINT = "/svc/apis/idx/drvprod_dd_trd"

# V-KOSPI 200 매칭 후보 (서버 응답에서 IDX_NM 매칭)
# 실제 KRX 응답: "코스피 200 변동성지수"
VKOSPI_NAMES = (
    "코스피 200 변동성지수",
    "코스피200 변동성지수",
    "V-KOSPI 200",
    "V-KOSPI200",
    "V-KOSPI",
)


def http_get(url, headers, timeout=30):
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read().decode("utf-8")
            return r.status, raw
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace") if e.fp else ""
    except Exception as e:
        return -1, str(e)


def call(bas_dd):
    if not AUTH_KEY:
        raise RuntimeError("KRX_AUTH_KEY 환경변수 또는 .krx_auth_key 파일 필요")
    url = f"{HOST}{ENDPOINT}?basDd={bas_dd}"
    headers = {
        "AUTH_KEY": AUTH_KEY,
        "Accept": "application/json",
    }
    return http_get(url, headers)


def find_vkospi_row(rows):
    """V-KOSPI 200 row 1개 찾기. IDX_NM 정확 매칭 우선, 부분 매칭 fallback."""
    for r in rows:
        nm = (r.get("IDX_NM", "") or "").strip()
        if nm in VKOSPI_NAMES:
            return r
    # 부분 매칭 — "변동성지수" 포함하면서 코스피 200 관련
    for r in rows:
        nm = (r.get("IDX_NM", "") or "").strip()
        nm_clean = nm.replace(" ", "")
        if "변동성지수" in nm and ("코스피200" in nm_clean or "KOSPI200" in nm_clean.upper()):
            return r
        if "V-KOSPI" in nm or "VKOSPI" in nm_clean.upper():
            return r
    return None


def probe(bas_dd):
    print(f"\n[probe] basDd={bas_dd}")
    if not AUTH_KEY:
        print("[ERROR] KRX_AUTH_KEY 환경변수 또는 .krx_auth_key 파일 필요")
        sys.exit(1)
    print(f"[probe] AUTH_KEY length: {len(AUTH_KEY)}")
    print(f"[probe] endpoint: {ENDPOINT}")

    status, body = call(bas_dd)
    print(f"  HTTP {status}")
    if status != 200:
        print(f"  body: {body[:500]}")
        return False

    try:
        j = json.loads(body)
    except Exception as e:
        print(f"  json parse fail: {e}")
        print(f"  body[:500]: {body[:500]}")
        return False

    out = j.get("OutBlock_1") or j.get("output") or j.get("data")
    if not out:
        print(f"  응답 keys: {list(j.keys())}")
        print(f"  body[:500]: {body[:500]}")
        return False

    print(f"  ✓ rows: {len(out)}")
    print(f"  sample row keys: {list(out[0].keys())}")

    # 모든 IDX_NM 출력 (V-KOSPI 200 존재 여부 확인)
    print(f"\n  📋 전체 IDX_NM 리스트:")
    seen = set()
    for r in out:
        nm = (r.get("IDX_NM", "") or "").strip()
        if nm and nm not in seen:
            seen.add(nm)
            print(f"    {nm}")

    target = find_vkospi_row(out)
    if target:
        print(f"\n  ✓ V-KOSPI 200 row found:")
        for k, v in target.items():
            print(f"      {k}: {v}")
        cls = target.get("CLSPRC_IDX")
        if cls:
            try:
                v = float(str(cls).replace(",", ""))
                print(f"\n  ⓘ V-KOSPI 종가: {v}")
                if 5 < v < 100:
                    print(f"     ✓ 정상 범위 (V-KOSPI 평균 ~20, 위기 시 50~70)")
                else:
                    print(f"     ⚠️ 비정상 범위 — 단위 재확인 필요")
            except Exception:
                pass
        return True
    else:
        print(f"\n  ⚠️ V-KOSPI 200 row 못찾음. 위 IDX_NM 리스트 확인.")
        return False


def trading_days(start_dt, end_dt):
    cur = start_dt
    while cur <= end_dt:
        if cur.weekday() < 5:
            yield cur.strftime("%Y%m%d")
        cur += timedelta(days=1)


def backfill(start_yyyymmdd, end_yyyymmdd, overwrite=False):
    start_dt = datetime.strptime(start_yyyymmdd, "%Y%m%d")
    end_dt = datetime.strptime(end_yyyymmdd, "%Y%m%d")

    done = {}
    if not overwrite and OUT_PATH.exists():
        prev = json.loads(OUT_PATH.read_text(encoding="utf-8"))
        for d, v in prev.get("data", []):
            done[d] = v
        print(f"[*] 기존 {len(done)} 일자 발견 — 스킵")

    days = list(trading_days(start_dt, end_dt))
    total = len(days)
    print(f"[*] {total} 영업일 백필 시작 (V-KOSPI 200)")

    new_count = 0
    fail_count = 0
    last_save = time.time()

    for i, bas_dd in enumerate(days, 1):
        date_str = f"{bas_dd[:4]}-{bas_dd[4:6]}-{bas_dd[6:]}"
        if date_str in done and not overwrite:
            continue

        status, body = call(bas_dd)
        if status != 200:
            fail_count += 1
            if fail_count <= 5:
                print(f"  [fail] {bas_dd}: HTTP {status} — {body[:100]}")
            continue

        try:
            j = json.loads(body)
        except Exception:
            fail_count += 1
            continue

        rows = j.get("OutBlock_1") or j.get("output") or j.get("data") or []
        if not rows:
            continue

        target = find_vkospi_row(rows)
        if not target:
            continue
        cls = target.get("CLSPRC_IDX")
        if cls is None:
            continue
        try:
            v = float(str(cls).replace(",", ""))
            done[date_str] = round(v, 4)
            new_count += 1
        except Exception:
            continue

        if i % 50 == 0 or i == total:
            print(f"  [{i:5d}/{total}] {bas_dd} done={len(done)} new={new_count} fail={fail_count}")

        if time.time() - last_save > 30:
            save(done)
            last_save = time.time()

        time.sleep(0.05)

    save(done)
    print(f"\n[OK] 백필 완료: 총 {len(done)} 일자, 신규 {new_count}, 실패 {fail_count}")


def save(done):
    data = sorted(done.items())
    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "KRX OpenAPI - 파생상품지수 시세정보 (V-KOSPI 200 종가)",
        "unit": "지수 포인트",
        "n_rows": len(data),
        "data": [[d, v] for d, v in data],
    }
    tmp = OUT_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    tmp.replace(OUT_PATH)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--probe", metavar="YYYYMMDD", help="응답 구조 + IDX_NM 리스트 확인")
    p.add_argument("--backfill", nargs=2, metavar=("START", "END"), help="기간 백필 YYYYMMDD")
    p.add_argument("--overwrite", action="store_true", help="기존 파일 무시하고 처음부터")
    args = p.parse_args()

    if args.probe:
        ok = probe(args.probe)
        if ok:
            print(f"\n[*] V-KOSPI 매칭 성공 — 백필 가능")
            print(f"[*] 다음 명령으로 백필 실행:")
            print(f"    py {Path(__file__).name} --backfill 20100104 {datetime.now().strftime('%Y%m%d')}")
        return

    if args.backfill:
        backfill(args.backfill[0], args.backfill[1], overwrite=args.overwrite)
        return

    # 기본: 자동 probe + 16년 백필
    print("[*] 인자 없음 — 자동 probe + 2010~현재 백필")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
    ok = probe(yesterday)
    if not ok:
        print("[ERROR] probe 실패")
        sys.exit(1)
    today = datetime.now().strftime("%Y%m%d")
    backfill("20100104", today)


if __name__ == "__main__":
    main()
