#!/usr/bin/env python3
"""
국채선물지수 (10년/5년) 일별 Backfill — KRX OpenAPI raw HTTP 방식
kr_vkospi_backfill_local.py 와 동일 패턴 (같은 endpoint drvprod_dd_trd 재사용).

용도: 피어앤그리드 오실레이터의 "10년 국채선물지수 - 5년 국채선물지수" 변수.
V-KOSPI 와 같은 '파생상품지수 시세정보' 응답에서 IDX_NM 매칭으로 두 지수 추출.
→ 이미 신청된 KRX OpenAPI 서비스라 추가 신청 불필요 (가설 — probe 로 확인).

사용법:
  py kr_ktb_backfill_local.py --probe 20260722       # IDX_NM 리스트에서 국채선물지수 존재 확인
  py kr_ktb_backfill_local.py --backfill 20150101 20260723
  py kr_ktb_backfill_local.py --backfill 20150101 20260723 --overwrite

출력 구조 (data/kr_ktb_futures.json):
{
  "generated_at": "...",
  "source": "KRX OpenAPI - 파생상품지수 시세정보 (국채선물지수)",
  "names": {"ktb10": "<실제 IDX_NM>", "ktb5": "<실제 IDX_NM>"},
  "data": [["2015-01-02", {"ktb10": 108.42, "ktb5": 105.11}], ...]
}

주의: 5년국채선물 상장 (2022-02) 이전 일자는 ktb5 가 null — 오실레이터 빌더가
fallback (3년국채선물지수) 을 쓸 수 있도록 ktb3 도 함께 저장.
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
OUT_PATH = DATA_DIR / "kr_ktb_futures.json"

AUTH_KEY = os.environ.get("KRX_AUTH_KEY") or ""
KEY_FILE = SCRIPT_DIR / ".krx_auth_key"
if not AUTH_KEY and KEY_FILE.exists():
    AUTH_KEY = KEY_FILE.read_text(encoding="utf-8").strip()

HOST = "https://data-dbg.krx.co.kr"
ENDPOINT = "/svc/apis/idx/drvprod_dd_trd"   # V-KOSPI 와 동일 (이미 신청된 서비스)

# IDX_NM 매칭 후보 — 2026-07-23 probe 로 실제 명칭 확정
# ktb10: "10년국채선물지수" / ktb5: "5년 국채선물 추종 지수" / ktb3: "국채선물지수" (3년물 기반 F-KTB)
KTB10_NAMES = ("10년국채선물지수", "10년 국채선물지수", "국채선물 10년 지수")
KTB5_NAMES  = ("5년 국채선물 추종 지수", "5년국채선물지수", "5년 국채선물지수", "국채선물 5년 지수")
KTB3_NAMES  = ("국채선물지수", "3년국채선물지수", "3년 국채선물지수", "국채선물 3년 지수")

# 부분 매칭 시 파생·변형 상품 제외 키워드
EXCLUDE_KWS = ("인버스", "레버리지", "스티프닝", "플래트닝", "혼합", "2X", "3X",
               "TWAP", "커브", "커버드", "양매도", "TR", "혼합지수", "0.5X", "1.5X")


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
    headers = {"AUTH_KEY": AUTH_KEY, "Accept": "application/json"}
    return http_get(url, headers)


def _match(rows, names, keyword_all=None):
    """정확 매칭 우선, 공백 제거 부분 매칭 fallback (파생·변형 상품 제외)."""
    for r in rows:
        nm = (r.get("IDX_NM", "") or "").strip()
        if nm in names:
            return r
    if keyword_all:
        for r in rows:
            nm = (r.get("IDX_NM", "") or "").strip()
            nm_clean = nm.replace(" ", "")
            if any(x in nm for x in EXCLUDE_KWS):
                continue
            if all(k in nm_clean for k in keyword_all):
                return r
    return None


def extract(rows):
    """응답 rows 에서 ktb10/ktb5/ktb3 종가 추출. 없으면 None."""
    out = {}
    for key, names, kw in (
        ("ktb10", KTB10_NAMES, ("10년", "국채", "지수")),
        ("ktb5",  KTB5_NAMES,  ("5년", "국채", "지수")),
        ("ktb3",  KTB3_NAMES,  ("3년", "국채", "지수")),
    ):
        row = _match(rows, names, kw)
        if row is None:
            out[key] = None
            continue
        cls = row.get("CLSPRC_IDX")
        try:
            out[key] = round(float(str(cls).replace(",", "")), 4)
        except Exception:
            out[key] = None
        out[key + "_nm"] = (row.get("IDX_NM", "") or "").strip()
    return out


def probe(bas_dd):
    print(f"\n[probe] basDd={bas_dd}")
    if not AUTH_KEY:
        print("[ERROR] KRX_AUTH_KEY 환경변수 또는 .krx_auth_key 파일 필요")
        sys.exit(1)
    status, body = call(bas_dd)
    print(f"  HTTP {status}")
    if status != 200:
        print(f"  body: {body[:500]}")
        return False
    j = json.loads(body)
    rows = j.get("OutBlock_1") or j.get("output") or j.get("data") or []
    print(f"  rows: {len(rows)}")
    print(f"\n  전체 IDX_NM 리스트:")
    seen = set()
    for r in rows:
        nm = (r.get("IDX_NM", "") or "").strip()
        if nm and nm not in seen:
            seen.add(nm)
            marker = " ◀◀ 국채" if "국채" in nm else ""
            print(f"    {nm}{marker}")
    result = extract(rows)
    print(f"\n  추출 결과:")
    for k in ("ktb10", "ktb5", "ktb3"):
        print(f"    {k}: {result.get(k)}  (IDX_NM: {result.get(k+'_nm', 'NOT FOUND')})")
    ok = result.get("ktb10") is not None and (result.get("ktb5") is not None or result.get("ktb3") is not None)
    print(f"\n  {'✓ 사용 가능 — backfill 진행' if ok else '✗ 국채선물지수 미발견 — fut_bydd_trd (선물 일별매매정보) 서비스 신청 필요'}")
    return ok


def trading_days(start_dt, end_dt):
    cur = start_dt
    while cur <= end_dt:
        if cur.weekday() < 5:
            yield cur.strftime("%Y%m%d")
        cur += timedelta(days=1)


def save(done, names):
    data = sorted(done.items())
    out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "KRX OpenAPI - 파생상품지수 시세정보 (국채선물지수 10년/5년/3년 종가)",
        "unit": "지수 포인트",
        "names": names,
        "n_rows": len(data),
        "data": [[d, v] for d, v in data],
    }
    tmp = OUT_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    tmp.replace(OUT_PATH)


def backfill(start_yyyymmdd, end_yyyymmdd, overwrite=False):
    start_dt = datetime.strptime(start_yyyymmdd, "%Y%m%d")
    end_dt = datetime.strptime(end_yyyymmdd, "%Y%m%d")

    done = {}
    names = {}
    if not overwrite and OUT_PATH.exists():
        prev = json.loads(OUT_PATH.read_text(encoding="utf-8"))
        for d, v in prev.get("data", []):
            done[d] = v
        names = prev.get("names", {})
        print(f"[*] 기존 {len(done)} 일자 발견 — 스킵")

    days = list(trading_days(start_dt, end_dt))
    total = len(days)
    print(f"[*] {total} 영업일 백필 시작 (국채선물지수)")

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

        result = extract(rows)
        if result.get("ktb10") is None and result.get("ktb3") is None:
            continue  # 휴장일 또는 데이터 없음
        # 이름 기록 (최초 1회)
        for k in ("ktb10", "ktb5", "ktb3"):
            nm = result.get(k + "_nm")
            if nm and k not in names:
                names[k] = nm
        done[date_str] = {
            "ktb10": result.get("ktb10"),
            "ktb5": result.get("ktb5"),
            "ktb3": result.get("ktb3"),
        }
        new_count += 1

        if i % 50 == 0 or i == total:
            print(f"  [{i:5d}/{total}] {bas_dd} done={len(done)} new={new_count} fail={fail_count}")
        if time.time() - last_save > 30:
            save(done, names)
            last_save = time.time()
        time.sleep(0.05)

    save(done, names)
    print(f"\n[OK] 백필 완료: 총 {len(done)} 일자, 신규 {new_count}, 실패 {fail_count}")
    if done:
        last_d = sorted(done)[-1]
        print(f"  마지막 일자: {last_d} → {done[last_d]}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--probe", metavar="YYYYMMDD", help="응답 구조 + IDX_NM 리스트 확인")
    ap.add_argument("--backfill", nargs=2, metavar=("START", "END"), help="YYYYMMDD 구간 백필")
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()

    if args.probe:
        ok = probe(args.probe)
        sys.exit(0 if ok else 1)
    elif args.backfill:
        backfill(args.backfill[0], args.backfill[1], overwrite=args.overwrite)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
