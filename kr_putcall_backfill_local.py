#!/usr/bin/env python3
"""
Put/Call Ratio 일별 Backfill — KRX OpenAPI raw HTTP 방식
mcap 백필 스크립트와 동일 패턴 (pykrx 의존 X, AUTH_KEY 사용).

신청 endpoint: 옵션 일별매매정보 (opt_bydd_trd) — 도메인 'drv'
응답 OutBlock_1 의 RGHT_TP_NM (CALL/PUT) 별 ACC_TRDVOL 합산
Put/Call ratio = ΣPUT_TRDVOL / ΣCALL_TRDVOL  (일별)
이후 대시보드 측에서 20일 SMA 적용.

사용법:
  py kr_putcall_backfill_local.py --probe 20260424   # 응답 구조 + RGHT_TP_NM 분포 확인
  py kr_putcall_backfill_local.py --backfill 20100104 20260427

종료 후 data/kr_putcall.json 생성 → GitHub data/kr_putcall.json 업로드
예상 소요시간: 16년치 약 10~20분

출력 구조:
{
  "generated_at": "2026-04-27T...Z",
  "source": "KRX OpenAPI - 옵션 일별매매정보 (Put/Call ratio)",
  "unit": "비율 (PUT 거래량 / CALL 거래량)",
  "data": [
    ["2010-01-04", { "pc": 0.83, "put_vol": 1234567, "call_vol": 1493975 }],
    ...
  ]
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
OUT_PATH = DATA_DIR / "kr_putcall.json"

AUTH_KEY = os.environ.get("KRX_AUTH_KEY") or ""
KEY_FILE = SCRIPT_DIR / ".krx_auth_key"
if not AUTH_KEY and KEY_FILE.exists():
    AUTH_KEY = KEY_FILE.read_text(encoding="utf-8").strip()

HOST = "https://data-dbg.krx.co.kr"
# 메모: 옵션 endpoint 는 'drv' 도메인 — 'idx' 가 아님
ENDPOINT = "/svc/apis/drv/opt_bydd_trd"


def http_get(url, headers, timeout=60):
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


def aggregate_pc(rows):
    """Put/Call 거래량 합산.
    KOSPI200 옵션 (코스피200 옵션) 만 집계. 주식옵션 제외 가능성 (전체 합산도 시도).
    """
    put_vol = 0
    call_vol = 0
    # 카테고리별 분리 집계 (코스피200 옵션 vs 주식옵션 등) — IDX_NM 또는 ISU_CD prefix 로 구분
    for r in rows:
        rt = (r.get("RGHT_TP_NM", "") or "").strip().upper()
        try:
            vol = int(str(r.get("ACC_TRDVOL", "0")).replace(",", ""))
        except Exception:
            continue
        if rt == "PUT" or rt == "P" or "풋" in rt:
            put_vol += vol
        elif rt == "CALL" or rt == "C" or "콜" in rt:
            call_vol += vol
    return put_vol, call_vol


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

    # RGHT_TP_NM 분포
    tp_count = {}
    for r in out:
        tp = (r.get("RGHT_TP_NM", "") or "").strip()
        tp_count[tp] = tp_count.get(tp, 0) + 1
    print(f"\n  📋 RGHT_TP_NM 분포: {tp_count}")

    # 첫 row 샘플
    print(f"\n  샘플 row 3개:")
    for r in out[:3]:
        print("    " + ", ".join(f"{k}={v}" for k, v in r.items() if k in ("BAS_DD","RGHT_TP_NM","ISU_CD","ISU_NM","ACC_TRDVOL","IMP_VOLT","CLSPRC")))

    put_vol, call_vol = aggregate_pc(out)
    print(f"\n  ⓘ 집계 결과:")
    print(f"     PUT  거래량 합계: {put_vol:,}")
    print(f"     CALL 거래량 합계: {call_vol:,}")
    if call_vol > 0:
        pc = put_vol / call_vol
        print(f"     P/C ratio: {pc:.4f}")
        if 0.3 < pc < 3.0:
            print(f"     ✓ 정상 범위 (P/C 평균 ~0.8~1.2)")
        else:
            print(f"     ⚠️ 비정상 범위 — 매칭 로직 재확인 필요")
    return call_vol > 0 and put_vol > 0


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
        for entry in prev.get("data", []):
            d, v = entry[0], entry[1]
            done[d] = v
        print(f"[*] 기존 {len(done)} 일자 발견 — 스킵")

    days = list(trading_days(start_dt, end_dt))
    total = len(days)
    print(f"[*] {total} 영업일 백필 시작 (Put/Call ratio)")

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

        put_vol, call_vol = aggregate_pc(rows)
        if call_vol <= 0:
            continue

        pc = round(put_vol / call_vol, 4)
        done[date_str] = {
            "pc": pc,
            "put_vol": put_vol,
            "call_vol": call_vol,
        }
        new_count += 1

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
        "source": "KRX OpenAPI - 옵션 일별매매정보 (Put/Call ratio)",
        "unit": "비율 (PUT 거래량 / CALL 거래량)",
        "n_rows": len(data),
        "data": [[d, v] for d, v in data],
    }
    tmp = OUT_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    tmp.replace(OUT_PATH)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--probe", metavar="YYYYMMDD")
    p.add_argument("--backfill", nargs=2, metavar=("START", "END"))
    p.add_argument("--overwrite", action="store_true")
    args = p.parse_args()

    if args.probe:
        ok = probe(args.probe)
        if ok:
            print(f"\n[*] Put/Call 매칭 성공 — 백필 가능")
            print(f"[*] 다음 명령으로 백필 실행:")
            print(f"    py {Path(__file__).name} --backfill 20100104 {datetime.now().strftime('%Y%m%d')}")
        return

    if args.backfill:
        backfill(args.backfill[0], args.backfill[1], overwrite=args.overwrite)
        return

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
