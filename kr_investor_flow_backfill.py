#!/usr/bin/env python3
"""
코스피 투자자별 매매동향 (외국인 순매수) 백필 — KIS OpenAPI.

API: 시장별 투자자매매동향(일별) FHPTJ04040000 [국내주식-075]
  한 호출 = 기준일로부터 과거 300 거래일 → 날짜 페이징으로 과거 확장.

출력: data/kr_investor_flow.json
{
  "generated_at": "...",
  "source": "KIS OpenAPI FHPTJ04040000 (KOSPI)",
  "unit": "억원 (net buy, 외국인/개인/기관)",
  "data": [["2025-01-02", {"frgn": -1234.5, "prsn": 890.1, "orgn": 344.2, "close": 2400.1}], ...]
}
값 단위: frgn_ntby_tr_pbmn (백만원) ÷ 100 = 억원.

사용법:
  py kr_investor_flow_backfill.py --probe            # 1 페이지 확인
  py kr_investor_flow_backfill.py --backfill 2026    # 지정 연도 1/1 까지 페이징 백필
  py kr_investor_flow_backfill.py --update           # 최신 300일 재fetch + merge (cron 용)
"""
import argparse
import json
import os
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
OUT_PATH = DATA_DIR / "kr_investor_flow.json"
FUT_PATH = DATA_DIR / "kr_futures_flow.json"   # 네이버 선물 (계약) — kr_futures_flow_backfill.py 산출
KRX_FUT_MULT = 250000                          # K200 선물 승수 (1pt = 25만원)
BASE = "https://openapi.koreainvestment.com:9443"
TOKEN_CACHE = SCRIPT_DIR / ".kis_token.json"


def load_keys():
    ak = os.environ.get("KIS_APP_KEY") or ""
    sk = os.environ.get("KIS_APP_SECRET") or ""
    if ak and sk:
        return ak, sk
    for name in (".kis_keys", ".kis_keys.txt"):
        p = SCRIPT_DIR / name
        if p.exists():
            lines = [l.strip() for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
            if len(lines) >= 2:
                return lines[0], lines[1]
    raise SystemExit("[ERROR] KIS_APP_KEY/SECRET env 또는 .kis_keys 필요")


def get_token(appkey, appsecret):
    if TOKEN_CACHE.exists():
        try:
            c = json.loads(TOKEN_CACHE.read_text(encoding="utf-8"))
            if time.time() - c.get("issued_at", 0) < 23 * 3600:
                return c["access_token"]
        except Exception:
            pass
    print("[token] 신규 발급...")
    body = json.dumps({"grant_type": "client_credentials", "appkey": appkey, "appsecret": appsecret}).encode()
    req = urllib.request.Request(f"{BASE}/oauth2/tokenP", data=body,
                                 headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=30) as r:
        j = json.loads(r.read().decode("utf-8"))
    token = j["access_token"]
    TOKEN_CACHE.write_text(json.dumps({"access_token": token, "issued_at": time.time()}), encoding="utf-8")
    return token


def fetch_page(token, appkey, appsecret, date_yyyymmdd, iscd="0001"):
    """기준일로부터 과거 300 거래일 조회. rows (최신순) 반환. iscd: 0001=코스피, 2001=코스피200."""
    params = (f"FID_COND_MRKT_DIV_CODE=U&FID_INPUT_ISCD={iscd}"
              f"&FID_INPUT_DATE_1={date_yyyymmdd}&FID_INPUT_ISCD_1=KSP"
              f"&FID_INPUT_DATE_2={date_yyyymmdd}&FID_INPUT_ISCD_2={iscd}")
    url = f"{BASE}/uapi/domestic-stock/v1/quotations/inquire-investor-daily-by-market?{params}"
    req = urllib.request.Request(url, headers={
        "Content-Type": "application/json",
        "authorization": f"Bearer {token}",
        "appkey": appkey,
        "appsecret": appsecret,
        "tr_id": "FHPTJ04040000",
        "custtype": "P",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        j = json.loads(r.read().decode("utf-8"))
    if j.get("rt_cd") != "0":
        raise RuntimeError(f"API error: {j.get('msg1')}")
    return j.get("output") or []


def row_to_entry(row):
    d = row["stck_bsop_date"]
    date_str = f"{d[:4]}-{d[4:6]}-{d[6:]}"
    def num(k):
        try:
            return round(float(str(row.get(k, "0")).replace(",", "")) / 100.0, 1)  # 백만원 → 억원
        except Exception:
            return None
    try:
        close = float(str(row.get("bstp_nmix_prpr", "0")).replace(",", ""))
    except Exception:
        close = None
    return date_str, {
        "frgn": num("frgn_ntby_tr_pbmn"),
        "prsn": num("prsn_ntby_tr_pbmn"),
        "orgn": num("orgn_ntby_tr_pbmn"),
        "close": close,
    }


def merge_futures(merged, k200_map):
    """kr_futures_flow.json (계약) 을 읽어 K200 환산 (억원) 후 각 날짜에 fut/total 추가.

    fut(억원) = 계약수 × K200지수 × 250,000원 ÷ 1e8
    total = 현물 frgn + fut. K200 지수 없는 날은 최근값 forward-fill.
    """
    if not FUT_PATH.exists():
        print("[merge] kr_futures_flow.json 없음 — 현물만 저장")
        return merged
    fut = json.loads(FUT_PATH.read_text(encoding="utf-8"))
    fut_map = {d: v for d, v in fut.get("data", [])}
    last_k200 = None
    n_merged = 0
    for d in sorted(merged.keys()):
        if k200_map.get(d):
            last_k200 = k200_map[d]
        f = fut_map.get(d)
        if f is None or last_k200 is None:
            continue
        ctr = f.get("frgn")
        if ctr is None:
            continue
        fut_amt = round(ctr * last_k200 * KRX_FUT_MULT / 1e8, 1)  # 억원
        e = merged[d]
        e["fut"] = fut_amt
        e["fut_ctr"] = ctr
        e["total"] = round((e.get("frgn") or 0) + fut_amt, 1)
        n_merged += 1
    print(f"[merge] 선물 환산 합산: {n_merged}일 (마지막 K200={last_k200})")
    return merged


def fetch_k200_map(token, ak, sk, pages=4):
    """K200 지수 (iscd 2001) 시계열 — 환산용. 페이징으로 과거 확장."""
    k200 = {}
    cursor = datetime.now().strftime("%Y%m%d")
    for _ in range(pages):
        try:
            rows = fetch_page(token, ak, sk, cursor, iscd="2001")
        except Exception as e:
            print(f"[k200] fetch fail: {e}")
            break
        if not rows:
            break
        oldest = None
        for r in rows:
            d = r["stck_bsop_date"]
            ds = f"{d[:4]}-{d[4:6]}-{d[6:]}"
            try:
                k200[ds] = float(str(r.get("bstp_nmix_prpr", "0")).replace(",", ""))
            except Exception:
                pass
            oldest = min(oldest, ds) if oldest else ds
        prev = datetime.strptime(oldest.replace("-", ""), "%Y%m%d") - timedelta(days=1)
        cursor = prev.strftime("%Y%m%d")
        time.sleep(0.5)
    if k200:
        sample = sorted(k200.items())[-1]
        print(f"[k200] {len(k200)}일 확보, 최신 {sample[0]} = {sample[1]}")
        if not (200 < sample[1] < 3000):
            print("[k200] ⚠ 값 범위 이상 — iscd 2001 이 K200 이 아닐 수 있음. 환산 skip")
            return {}
    return k200


def save(merged):
    rows = sorted(merged.items())
    out = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "KIS OpenAPI 시장별 투자자매매동향(일별) FHPTJ04040000 (KOSPI)",
        "unit": "억원 (순매수 대금), close=코스피 종가",
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
        return {d: v for d, v in prev.get("data", [])}
    return {}


def cmd_probe():
    ak, sk = load_keys()
    token = get_token(ak, sk)
    today = datetime.now().strftime("%Y%m%d")
    rows = fetch_page(token, ak, sk, today)
    print(f"rows: {len(rows)}")
    d1, v1 = row_to_entry(rows[0])
    dn, vn = row_to_entry(rows[-1])
    print(f"최신: {d1} → {v1}")
    print(f"페이지 끝: {dn} → {vn}")


def cmd_backfill(until_year):
    ak, sk = load_keys()
    token = get_token(ak, sk)
    merged = load_existing()
    print(f"[*] 기존 {len(merged)} rows")
    cursor = datetime.now().strftime("%Y%m%d")
    target = f"{until_year}0101"
    for page in range(1, 30):
        rows = fetch_page(token, ak, sk, cursor)
        if not rows:
            print(f"  page {page}: empty — 종료")
            break
        added = 0
        oldest = None
        for r in rows:
            d, v = row_to_entry(r)
            if d not in merged:
                added += 1
            merged[d] = v
            oldest = min(oldest, d) if oldest else d
        print(f"  page {page}: {len(rows)} rows (~{oldest}), 신규 {added}")
        save(merged)
        oldest_yyyymmdd = oldest.replace("-", "")
        if oldest_yyyymmdd <= target:
            print(f"[*] 목표 {target} 도달")
            break
        # 다음 페이지 기준일 = 이번 페이지 최고(가장 과거) 일자의 전일
        prev_day = datetime.strptime(oldest_yyyymmdd, "%Y%m%d") - timedelta(days=1)
        cursor = prev_day.strftime("%Y%m%d")
        time.sleep(0.6)


def cmd_update():
    ak, sk = load_keys()
    token = get_token(ak, sk)
    merged = load_existing()
    rows = fetch_page(token, ak, sk, datetime.now().strftime("%Y%m%d"))
    added = 0
    for r in rows:
        d, v = row_to_entry(r)
        if d not in merged:
            added += 1
        merged[d] = v
    k200 = fetch_k200_map(token, ak, sk, pages=2)
    merged = merge_futures(merged, k200)
    save(merged)
    print(f"[update] 신규/갱신 반영 (신규 {added})")


def cmd_mergefut():
    """백필 후 1회 — K200 4페이지 (약 3년) + 선물 전체 환산 합산."""
    ak, sk = load_keys()
    token = get_token(ak, sk)
    merged = load_existing()
    k200 = fetch_k200_map(token, ak, sk, pages=4)
    merged = merge_futures(merged, k200)
    save(merged)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--probe", action="store_true")
    g.add_argument("--backfill", metavar="YEAR", help="이 연도 1/1 까지 페이징 백필 (ex. 2024)")
    g.add_argument("--update", action="store_true")
    g.add_argument("--mergefut", action="store_true", help="선물 환산 합산 1회 (백필 후)")
    args = ap.parse_args()
    if args.probe:
        cmd_probe()
    elif args.backfill:
        cmd_backfill(args.backfill)
    elif args.mergefut:
        cmd_mergefut()
    else:
        cmd_update()
