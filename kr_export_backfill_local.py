#!/usr/bin/env python3
"""
KR 수출/수입 YoY Backfill — LOCAL runner
관세청 tradedata.go.kr 내부 AJAX 엔드포인트 직접 호출.
인증 불필요, 한국/미국 IP 상관없이 호출 가능 (현재까지 확인).

사용법:
  옵션 1) kr_export_backfill_local.bat 을 더블클릭
  옵션 2) 터미널에서 `py kr_export_backfill_local.py` 실행

종료 후 같은 폴더에 kr_export.json 생성 → GitHub의 data/kr_export.json 에 업로드
예상 소요시간: 10초 미만 (월별 API, 1회 호출에 100개월+ 반환)

출력 구조 (kr_export.json):
{
  "generated_at": "2026-04-20T...Z",
  "monthly_confirmed": [{"period":"YYYY-MM","priod_dt":"01~31","total_usd_k":N,"yoy":float|null}, ...],
  "partial_1_20":      [{"period":"YYYY-MM","priod_dt":"01~20","total_usd_k":N,"yoy":float|null}, ...],
  "partial_1_10":      [{"period":"YYYY-MM","priod_dt":"01~10","total_usd_k":N,"yoy":float|null}, ...]
}
* YoY = 같은 cutoff의 전년 동월 대비 (%). 기준연도(=2016)는 YoY=null.
* total_usd_k = USD 천 단위 (실제 $ × 1000).
"""
import json
import sys
import time
import urllib.request
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
OUT_PATH = SCRIPT_DIR / "kr_export.json"

ENDPOINT = "https://tradedata.go.kr/cts/hmpg/retrieveTentativeValues.do"
START_YYYYMM = "201601"

# (JSON key, priodDate 파라미터, 한글 라벨)
CUTOFFS = [
    ("monthly_confirmed", "3", "월 확정 (1~말일)"),
    ("partial_1_20",      "2", "1~20일 잠정"),
    ("partial_1_10",      "1", "1~10일 잠정"),
]


def fetch_range(priod_fr, priod_to, priod_date, imex_tpcd="E"):
    """Fetch KR export/import totals for given YYYYMM range and cutoff.
    Returns list of dicts: {period, priod_dt, total_usd_k}
    """
    body = urllib.parse.urlencode({
        "statsKind": "ETS_MNK_1050000A",  # 품목별 (총액만 쓰므로 A로 충분)
        "imexTpcd": imex_tpcd,             # E=수출, I=수입
        "priodKind": "MON",
        "priodFr": priod_fr,
        "priodTo": priod_to,
        "priodDate": priod_date,
        "showPagingLine": "500",
        "sortColumn": "",
        "sortOrder": "",
    }).encode("utf-8")

    req = urllib.request.Request(
        ENDPOINT,
        data=body,
        headers={
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Origin": "https://tradedata.go.kr",
            "Referer": "https://tradedata.go.kr/cts/index.do",
            "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/122.0.0.0 Safari/537.36"),
            "X-Requested-With": "XMLHttpRequest",
        },
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.loads(resp.read().decode("utf-8"))

    items = payload.get("items", []) or []
    out = []
    for it in items:
        priod_mon = str(it.get("priodMon", "") or "")
        if len(priod_mon) != 6 or not priod_mon.isdigit():
            continue
        raw_amt = str(it.get("itemUsdAmt00", "") or "").replace(",", "").strip()
        if not raw_amt:
            continue
        try:
            total = int(raw_amt)
        except ValueError:
            continue
        out.append({
            "period": f"{priod_mon[:4]}-{priod_mon[4:6]}",
            "priod_dt": str(it.get("priodDt", "") or ""),
            "total_usd_k": total,
        })
    return out


def add_yoy(series):
    """Add YoY % in-place: compares each month to same YYYY-1-MM in the same cutoff."""
    by_period = {r["period"]: r for r in series}
    for r in series:
        yr, mo = r["period"].split("-")
        prev_key = f"{int(yr)-1}-{mo}"
        prev = by_period.get(prev_key)
        if prev and prev.get("total_usd_k", 0) > 0:
            r["yoy"] = round(
                (r["total_usd_k"] / prev["total_usd_k"] - 1) * 100, 2
            )
        else:
            r["yoy"] = None
    return series


def current_yyyymm():
    now = datetime.now()
    return f"{now.year:04d}{now.month:02d}"


def main():
    end_ym = current_yyyymm()
    print(f"[plan] KR 수출 YoY 백필: {START_YYYYMM} → {end_ym}")
    print(f"[endpoint] {ENDPOINT}")
    print(f"[output] {OUT_PATH}")
    print()

    out = {"generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")}

    for key, priod_date, label in CUTOFFS:
        print(f"[fetch] {label}  (priodDate={priod_date})")
        try:
            series = fetch_range(START_YYYYMM, end_ym, priod_date)
        except Exception as e:
            print(f"  [error] {e}", file=sys.stderr)
            series = []
        series.sort(key=lambda r: r["period"])
        series = add_yoy(series)
        out[key] = series
        print(f"  → {len(series)}개월 수집")
        if series:
            latest = series[-1]
            amt_m = latest["total_usd_k"] / 1000  # 천 USD → 백만 USD
            yoy_s = f"{latest['yoy']:+.2f}%" if latest.get("yoy") is not None else "—"
            print(f"  latest {latest['period']} ({latest['priod_dt']}): "
                  f"${amt_m:,.0f}M   YoY={yoy_s}")
        time.sleep(0.5)
        print()

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))

    print(f"[saved] {OUT_PATH}")
    print()
    print("[summary]")
    for key, _, label in CUTOFFS:
        series = out.get(key, [])
        with_yoy = [r for r in series if r.get("yoy") is not None]
        print(f"  {label:<20s}: {len(series):>3d}개월  (YoY 계산 {len(with_yoy)}건)")

    print()
    print("✓ 성공! kr_export.json 을 GitHub 리포 data/ 폴더에 업로드하세요.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[중단] 사용자가 중지했습니다.")
    except Exception as e:
        print(f"\n[ERROR] {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()

    print()
    try:
        input("아무 키나 누르면 창이 닫힙니다...")
    except EOFError:
        pass
