# -*- coding: utf-8 -*-
"""
반도체 수출 판가 backfill (관세청 무역통계 tradedata.go.kr)

목적:
    DRAM ASP 대체 지표. 반도체 수출 '금액(달러) / 중량(kg)' = 판가($/kg).
    기존 asp_dram.json (PDF 소스, 2025-12 중단)을 대체한다.

출력: data/dram_export_price.json
    {
      "meta": {...},
      "monthly":   [{"t":"2026-07","p":86970.27,"yoy":484.0,"amt":...,"wgt":...}, ...],
      "quarterly": [{"t":"2026-06","rev":31852040510,"p":72908.30,"qoq":57.5,"yoy":422.0}, ...]
    }

실행:
    python dram_export_price_backfill.py            # 전체 백필 (2008-01 ~ 현재)
    python dram_export_price_backfill.py --from 202401   # 부분 갱신

주의:
    - tradedata.go.kr 은 POST 폼 API. 인증키 불필요.
    - 샌드박스(Claude 실행환경)에서는 egress 차단으로 접근 불가.
      반드시 BT PC 또는 GitHub Actions runner 에서 실행할 것.
    - HS 코드는 MTI/HS 중 HS 4단위 8542(집적회로) 기준. DRAM 단독은 8542.32.
      SEMI_HS 상수로 전환 가능.
"""
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
OUT_PATH = DATA_DIR / "dram_export_price.json"

ENDPOINT = "https://tradedata.go.kr/cts/hmpg/retrieveTentativeValues.do"
ITEM_ENDPOINT = "https://tradedata.go.kr/cts/hmpg/retrieveItemStats.do"

START_YYYYMM = "200801"

# 8542 = 전자집적회로 (반도체). DRAM 단독으로 좁히려면 "854232".
SEMI_HS = "8542"

HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://tradedata.go.kr",
    "Referer": "https://tradedata.go.kr/",
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"),
}


def post_json(url, payload, retries=3):
    body = urllib.parse.urlencode(payload).encode("utf-8")
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, data=body, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=40) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:          # noqa: BLE001
            last = e
            time.sleep(1.5 * (i + 1))
    raise RuntimeError("POST 실패 %s : %s" % (url, last))


def month_range(fr, to):
    y, m = int(fr[:4]), int(fr[4:])
    ey, em = int(to[:4]), int(to[4:])
    out = []
    while (y, m) <= (ey, em):
        out.append("%04d%02d" % (y, m))
        m += 1
        if m > 12:
            m = 1
            y += 1
    return out


def fetch_item_monthly(hs, fr, to):
    """품목(HS)별 월간 수출 금액(USD)과 중량(kg).

    반환: {"YYYYMM": {"amt": float, "wgt": float}}
    응답 스키마는 사이트 개편에 따라 바뀔 수 있으므로 키를 유연하게 탐색한다.
    """
    payload = {
        "statsKind": "ETS_MNK_1050000A",   # 품목별
        "imexTpcd": "E",                   # 수출
        "priodKind": "MON",
        "priodFr": fr,
        "priodTo": to,
        "priodDate": "3",                  # 월 확정 (1~말일)
        "hsSgn": hs,
        "itemCd": hs,
        "showPagingLine": "1000",
        "sortColumn": "",
        "sortOrder": "",
    }
    raw = post_json(ITEM_ENDPOINT, payload)
    rows = None
    for key in ("resultList", "list", "data", "rows", "items"):
        if isinstance(raw, dict) and isinstance(raw.get(key), list):
            rows = raw[key]
            break
    if rows is None and isinstance(raw, list):
        rows = raw
    if rows is None:
        raise RuntimeError("응답에서 목록을 찾지 못함. keys=%s" % (list(raw)[:20] if isinstance(raw, dict) else type(raw)))

    def pick(d, cands):
        for c in cands:
            if c in d and d[c] not in (None, "", "-"):
                return d[c]
        for k, v in d.items():
            lk = k.lower()
            if any(c.lower() in lk for c in cands) and v not in (None, "", "-"):
                return v
        return None

    def num(v):
        if v is None:
            return None
        if isinstance(v, (int, float)):
            return float(v)
        s = str(v).replace(",", "").strip()
        try:
            return float(s)
        except ValueError:
            return None

    out = {}
    for d in rows:
        per = pick(d, ["priodNm", "priod", "period", "yyyymm", "basePeriod"])
        if per is None:
            continue
        per = str(per).replace("-", "").replace(".", "")[:6]
        amt = num(pick(d, ["expDlr", "expAmt", "exportAmount", "dlr", "amount"]))
        wgt = num(pick(d, ["expWgt", "expWt", "weight", "wgt"]))
        if amt is None:
            continue
        out[per] = {"amt": amt, "wgt": wgt}
    return out


def build(monthly_raw):
    months = sorted(monthly_raw)
    by = {}
    for t in months:
        r = monthly_raw[t]
        p = (r["amt"] / r["wgt"]) if (r.get("wgt") or 0) > 0 else None
        by[t] = p

    monthly = []
    for t in months:
        p = by[t]
        if p is None:
            continue
        py = "%04d%02d" % (int(t[:4]) - 1, int(t[4:]))
        prev = by.get(py)
        yoy = round((p / prev - 1) * 100, 1) if prev else None
        monthly.append({
            "t": t[:4] + "-" + t[4:],
            "p": round(p, 2),
            "yoy": yoy,
            "amt": monthly_raw[t]["amt"],
            "wgt": monthly_raw[t]["wgt"],
        })

    # 분기 집계: 분기 판가 = 분기 금액 합 / 분기 중량 합
    qmap = {}
    for t in months:
        r = monthly_raw[t]
        if not r.get("wgt"):
            continue
        y, m = int(t[:4]), int(t[4:])
        qm = ((m - 1) // 3 + 1) * 3
        key = "%04d-%02d" % (y, qm)
        a = qmap.setdefault(key, {"amt": 0.0, "wgt": 0.0})
        a["amt"] += r["amt"]
        a["wgt"] += r["wgt"]

    qkeys = sorted(qmap)
    qprice = {k: (qmap[k]["amt"] / qmap[k]["wgt"]) for k in qkeys if qmap[k]["wgt"] > 0}
    quarterly = []
    for i, k in enumerate(qkeys):
        if k not in qprice:
            continue
        p = qprice[k]
        qoq = None
        if i > 0 and qkeys[i - 1] in qprice:
            qoq = round((p / qprice[qkeys[i - 1]] - 1) * 100, 1)
        py = "%04d-%s" % (int(k[:4]) - 1, k[5:])
        yoy = round((p / qprice[py] - 1) * 100, 1) if py in qprice else None
        quarterly.append({"t": k, "rev": round(qmap[k]["amt"]), "p": round(p, 2),
                          "qoq": qoq, "yoy": yoy})
    return monthly, quarterly


def main():
    fr = START_YYYYMM
    for i, a in enumerate(sys.argv):
        if a == "--from" and i + 1 < len(sys.argv):
            fr = sys.argv[i + 1]
    today = date.today()
    to = "%04d%02d" % (today.year, today.month)

    print("[dram_export_price] HS %s  %s ~ %s" % (SEMI_HS, fr, to))
    raw = {}
    # 사이트가 장기 구간을 한 번에 안 주는 경우가 있어 연 단위로 끊어 요청
    y0, y1 = int(fr[:4]), int(to[:4])
    for y in range(y0, y1 + 1):
        a = max(fr, "%04d01" % y)
        b = min(to, "%04d12" % y)
        try:
            part = fetch_item_monthly(SEMI_HS, a, b)
            raw.update(part)
            print("  %s : %d개월" % (y, len(part)))
        except Exception as e:      # noqa: BLE001
            print("  [WARN] %s 실패: %s" % (y, e))
        time.sleep(0.4)

    if not raw:
        print("[ERROR] 수집 0건 — 응답 스키마 변경 가능성. ITEM_ENDPOINT/키 매핑 점검 필요.")
        sys.exit(1)

    monthly, quarterly = build(raw)

    # 기존 파일에 수기 입력분이 있으면 API 값이 없는 구간만 보존
    prev_manual = []
    if OUT_PATH.exists():
        try:
            old = json.loads(OUT_PATH.read_text(encoding="utf-8"))
            have = {r["t"] for r in monthly}
            prev_manual = [r for r in old.get("monthly", []) if r["t"] not in have]
        except Exception:       # noqa: BLE001
            pass
    if prev_manual:
        monthly = sorted(monthly + prev_manual, key=lambda r: r["t"])
        print("  기존 수기 입력 %d개월 보존" % len(prev_manual))

    out = {
        "meta": {
            "metric": "반도체 수출 판가 (수출금액 USD / 중량 kg)",
            "hs": SEMI_HS,
            "source": "관세청 무역통계 tradedata.go.kr (품목별 월간 수출)",
            "note": "yoy/qoq 단위 = %. 분기 판가는 분기 금액합/중량합. rev = 분기 수출금액(USD).",
            "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        },
        "monthly": monthly,
        "quarterly": quarterly,
    }
    OUT_PATH.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")),
                        encoding="utf-8")
    print("[OK] %s  monthly=%d  quarterly=%d  last=%s"
          % (OUT_PATH.name, len(monthly), len(quarterly),
             monthly[-1] if monthly else "-"))


if __name__ == "__main__":
    main()
