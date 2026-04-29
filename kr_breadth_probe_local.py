#!/usr/bin/env python3
"""
KRX OpenAPI 종목별 일별매매정보 probe
==========================================
Phase B — KR ADR + KR NH/NL을 한 endpoint로 묶어 처리하기 위한 사전 검증.

후보 endpoint:
  - /svc/apis/sto/stk_bydd_trd  (유가증권시장 종목별 일별매매정보)
  - /svc/apis/sto/ksq_bydd_trd  (코스닥 종목별 일별매매정보)
  - 다른 패턴도 시도: /svc/apis/sto/all_bydd_trd, /svc/apis/sto/stk_isu_dd_trd 등

목표:
  1. endpoint HTTP 200 응답 가능 여부
  2. 응답 OutBlock_1 필드 — 특히 FLUC_RT(등락률), TDD_CLSPRC(종가), ISU_CD(종목코드) 존재 확인
  3. 종목 수 (KOSPI ~800개, KOSDAQ ~1500개 예상)

사용:
  py kr_breadth_probe_local.py             # 자동 (어제 영업일)
  py kr_breadth_probe_local.py 20260424    # 특정 일자 지정

전제: .krx_auth_key 파일 또는 KRX_AUTH_KEY 환경변수
"""
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent

AUTH_KEY = os.environ.get("KRX_AUTH_KEY") or ""
KEY_FILE = SCRIPT_DIR / ".krx_auth_key"
if not AUTH_KEY and KEY_FILE.exists():
    AUTH_KEY = KEY_FILE.read_text(encoding="utf-8").strip()

HOST = "https://data-dbg.krx.co.kr"

# 후보 endpoint (우선순위 순)
ENDPOINT_CANDIDATES = [
    ("KOSPI 종목별 일별매매",   "/svc/apis/sto/stk_bydd_trd"),
    ("KOSDAQ 종목별 일별매매",  "/svc/apis/sto/ksq_bydd_trd"),
    ("KONEX 종목별 일별매매",   "/svc/apis/sto/knx_bydd_trd"),
    # 대체 후보 — 명세 변동 시
    ("KOSPI 일별 (alt1)",       "/svc/apis/sto/stk_dd_trd"),
    ("KOSPI 일별 (alt2)",       "/svc/apis/sto/stk_bydd"),
]

# 핵심 검증 필드 (있어야 ADR + NH/NL 가능)
CHECK_FIELDS = {
    "FLUC_RT":      "등락률 (ADR 계산 핵심)",
    "TDD_CLSPRC":   "종가 (NH/NL rolling max/min 계산)",
    "ISU_CD":       "종목코드",
    "ISU_NM":       "종목명",
    "TDD_HGPRC":    "고가",
    "TDD_LWPRC":    "저가",
    "ACC_TRDVOL":   "거래량",
    "MKTCAP":       "시가총액 (universe filter용)",
}


def http_get(url, headers, timeout=30):
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        return e.code, (e.read().decode("utf-8", errors="replace") if e.fp else "")
    except Exception as e:
        return -1, str(e)


def probe(endpoint, bas_dd, label=""):
    if not AUTH_KEY:
        print("[ERROR] KRX_AUTH_KEY 미설정 (.krx_auth_key 파일 또는 env)")
        sys.exit(1)
    url = f"{HOST}{endpoint}?basDd={bas_dd}"
    headers = {"AUTH_KEY": AUTH_KEY, "Accept": "application/json"}
    print(f"\n{'=' * 60}")
    print(f"[{label or endpoint}]  basDd={bas_dd}")
    print(f"  URL: {url}")
    status, body = http_get(url, headers)
    print(f"  HTTP {status}")
    if status != 200:
        print(f"  body[:300]: {body[:300]}")
        if status == 401:
            print(f"  -> 401: AUTH_KEY 무효 또는 endpoint 미승인 (KRX 마이페이지 확인)")
        elif status == 403:
            print(f"  -> 403: 이 endpoint 이용신청 안 됐을 가능성")
        elif status == 404:
            print(f"  -> 404: endpoint 경로 오류 — 다른 후보 시도")
        return False
    try:
        j = json.loads(body)
    except Exception as e:
        print(f"  json parse fail: {e}")
        return False
    rows = j.get("OutBlock_1") or j.get("output") or j.get("data")
    if not rows:
        print(f"  응답 keys: {list(j.keys())}")
        print(f"  body[:300]: {body[:300]}")
        return False
    print(f"  ✓ rows: {len(rows)}")
    if rows:
        first_keys = list(rows[0].keys())
        print(f"  응답 필드 ({len(first_keys)}개): {first_keys}")
        # 핵심 필드 매핑 확인
        print(f"\n  [필드 검증]")
        ok_count = 0
        for k, desc in CHECK_FIELDS.items():
            mark = "✓" if k in first_keys else "✗"
            if k in first_keys:
                ok_count += 1
            print(f"    {mark} {k:15s} — {desc}")
        print(f"\n  핵심 필드 {ok_count}/{len(CHECK_FIELDS)} 발견")
        # 샘플 row 3개
        print(f"\n  [샘플 row 3개]")
        for r in rows[:3]:
            cmp = {k: r.get(k) for k in ("BAS_DD", "ISU_CD", "ISU_NM",
                                         "TDD_CLSPRC", "FLUC_RT", "ACC_TRDVOL",
                                         "MKTCAP") if k in r}
            print(f"    {cmp}")
        # 등락률 분포 sanity check
        if "FLUC_RT" in first_keys:
            try:
                rates = [float(str(r.get("FLUC_RT", "0")).replace(",", "")) for r in rows
                         if r.get("FLUC_RT") not in (None, "")]
                if rates:
                    up = sum(1 for x in rates if x > 0)
                    dn = sum(1 for x in rates if x < 0)
                    fl = sum(1 for x in rates if x == 0)
                    print(f"\n  [등락률 sanity]")
                    print(f"    상승 {up} / 하락 {dn} / 보합 {fl}  (총 {len(rates)})")
                    if dn > 0:
                        adr_proxy = round(up / dn * 100, 2)
                        print(f"    당일 ADR proxy = {adr_proxy} (정상 80~120 범위)")
            except Exception as e:
                print(f"    등락률 분석 실패: {e}")
        return True
    return False


def yesterday_business_day():
    """어제(평일) yyyymmdd. 토일이면 직전 금요일."""
    d = datetime.now() - timedelta(days=1)
    while d.weekday() >= 5:  # 5=Sat, 6=Sun
        d -= timedelta(days=1)
    return d.strftime("%Y%m%d")


def main():
    bas_dd = sys.argv[1] if len(sys.argv) > 1 else yesterday_business_day()
    print(f"[*] AUTH_KEY length: {len(AUTH_KEY)}")
    print(f"[*] basDd: {bas_dd}")

    success_endpoints = []
    for label, ep in ENDPOINT_CANDIDATES:
        ok = probe(ep, bas_dd, label)
        if ok:
            success_endpoints.append((label, ep))

    print("\n" + "=" * 60)
    print("[probe 종합 결과]")
    if success_endpoints:
        for label, ep in success_endpoints:
            print(f"  ✓ {label}  →  {ep}")
        print("\n[*] 다음 단계: 발견된 endpoint로 백필 스크립트 작성")
    else:
        print("  ✗ 모든 후보 endpoint 실패")
        print("  [*] KRX 마이페이지 (openapi.krx.co.kr) → 이용현황 확인:")
        print("      - 주식(stock) 카테고리에서 종목별 일별매매정보 신청 상태")
        print("      - 미승인이면 신청 후 1~2일 대기")


if __name__ == "__main__":
    main()
