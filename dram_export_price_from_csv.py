# -*- coding: utf-8 -*-
"""
반도체 수출 판가 — 엑셀/CSV 임포트

BT 가공 시트(관세청 원본)를 CSV 로 내보내면 data/dram_export_price.json 을 생성한다.
API 엔드포인트가 확정되기 전까지 이 경로를 쓴다.

사용법
------
1) 엑셀에서 해당 시트를 열고 "다른 이름으로 저장" > CSV UTF-8(쉼표로 분리)
   파일명: dram_export_price.csv  (이 스크립트와 같은 폴더 또는 --csv 로 경로 지정)
2) 실행:
       cd /d "C:\\Users\\ruzby\\Documents\\Claude\\Scheduled"
       python dram_export_price_from_csv.py
   또는
       python dram_export_price_from_csv.py --csv "C:\\경로\\파일.csv"

필요한 열 (헤더 이름은 부분 일치로 자동 인식, 순서 무관)
------------------------------------------------------
  필수 : 년월  (예: "2026년07월", "2026-07", "202607")
  아래 둘 중 하나 이상
    (A) 판가 열      : "금액(달러)/중량"  또는 "판가"
    (B) 금액 + 중량  : "수출금액"/"금액" 과 "중량"   → 판가를 직접 계산
  선택 : "판가 yoy"  (없으면 12개월 전 값으로 자동 계산)

산출
----
  monthly   : t, p(판가), yoy(%), amt, wgt
  quarterly : t, rev(분기 금액합), p(분기 판가), qoq(%), yoy(%)
              금액·중량이 없으면 분기 판가는 3개월 단순평균으로 대체(approx=true 표시)
"""
import csv
import io
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
OUT_PATH = DATA_DIR / "dram_export_price.json"
DEFAULT_CSV = SCRIPT_DIR / "dram_export_price.csv"


def norm_month(v):
    """'2026년07월' / '2026-07' / '202607' / '2026.07' -> '2026-07'"""
    if v is None:
        return None
    s = str(v).strip()
    if not s:
        return None
    d = re.sub(r"[^0-9]", "", s)
    if len(d) >= 6:
        y, m = d[:4], d[4:6]
        if "1900" <= y <= "2100" and "01" <= m <= "12":
            return y + "-" + m
    return None


def num(v):
    if v is None:
        return None
    s = str(v).replace(",", "").replace("%", "").strip()
    if s in ("", "-", "–", "—"):
        return None
    neg = s.startswith("(") and s.endswith(")")
    if neg:
        s = s[1:-1]
    try:
        x = float(s)
    except ValueError:
        return None
    return -x if neg else x


def read_rows(path):
    raw = Path(path).read_bytes()
    for enc in ("utf-8-sig", "cp949", "utf-8"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise SystemExit("[ERROR] 인코딩 판별 실패 — CSV UTF-8 로 저장해 주세요.")
    return list(csv.reader(io.StringIO(text)))


def find_header(rows):
    """헤더 행 인덱스와 열 매핑을 찾는다."""
    want = {
        "month": ["년월", "연월", "월", "기간", "date"],
        "price": ["금액(달러)/중량", "금액/중량", "판가"],
        "amt":   ["수출금액", "금액(달러)", "달러매출", "금액"],
        "wgt":   ["중량", "kg"],
        "yoy":   ["판가 yoy", "판가yoy", "yoy"],
    }
    for i, row in enumerate(rows[:15]):
        cells = [str(c).strip() for c in row]
        joined = " ".join(cells)
        if not any(k in joined for k in ("년월", "연월", "기간")):
            continue
        cmap = {}
        for key, cands in want.items():
            for j, c in enumerate(cells):
                cl = c.replace(" ", "").lower()
                if any(cand.replace(" ", "").lower() in cl for cand in cands):
                    if key not in cmap:
                        cmap[key] = j
        # '판가'가 'yoy'까지 잡는 것 방지
        if cmap.get("price") is not None and cmap.get("price") == cmap.get("yoy"):
            cmap.pop("yoy", None)
        if "month" in cmap and ("price" in cmap or ("amt" in cmap and "wgt" in cmap)):
            return i, cmap
    raise SystemExit("[ERROR] 헤더를 찾지 못했습니다. '년월'과 '판가'(또는 '금액'+'중량') 열이 필요합니다.")


def main():
    csv_path = DEFAULT_CSV
    for i, a in enumerate(sys.argv):
        if a == "--csv" and i + 1 < len(sys.argv):
            csv_path = Path(sys.argv[i + 1])
    if not csv_path.exists():
        raise SystemExit("[ERROR] CSV 없음: %s\n  엑셀 시트를 CSV UTF-8 로 저장한 뒤 다시 실행하세요." % csv_path)

    rows = read_rows(csv_path)
    hi, cmap = find_header(rows)
    print("[csv] %s  헤더 %d행  열매핑 %s" % (csv_path.name, hi + 1, cmap))

    rec = {}
    for row in rows[hi + 1:]:
        if not row:
            continue
        def g(key):
            j = cmap.get(key)
            return row[j] if (j is not None and j < len(row)) else None
        t = norm_month(g("month"))
        if not t:
            continue
        p = num(g("price"))
        amt = num(g("amt"))
        wgt = num(g("wgt"))
        if p is None and amt and wgt:
            p = amt / wgt
        if p is None:
            continue
        y = num(g("yoy"))
        # yoy 가 배수(5.14) 로 들어오면 % 로 환산
        if y is not None and abs(y) <= 30:
            y *= 100
        rec[t] = {"p": round(p, 2), "yoy": round(y, 1) if y is not None else None,
                  "amt": amt, "wgt": wgt}

    if not rec:
        raise SystemExit("[ERROR] 파싱된 행이 0건입니다. 열 매핑을 확인하세요.")

    months = sorted(rec)
    monthly = []
    for t in months:
        r = dict(rec[t])
        if r["yoy"] is None:
            py = "%04d-%s" % (int(t[:4]) - 1, t[5:])
            if py in rec and rec[py]["p"]:
                r["yoy"] = round((r["p"] / rec[py]["p"] - 1) * 100, 1)
        monthly.append({"t": t, "p": r["p"], "yoy": r["yoy"],
                        "amt": r["amt"], "wgt": r["wgt"]})

    # 분기 집계
    qagg, qapprox = {}, {}
    for t in months:
        r = rec[t]
        y, m = int(t[:4]), int(t[5:])
        key = "%04d-%02d" % (y, ((m - 1) // 3 + 1) * 3)
        a = qagg.setdefault(key, {"amt": 0.0, "wgt": 0.0, "ps": []})
        a["ps"].append(r["p"])
        if r["amt"] and r["wgt"]:
            a["amt"] += r["amt"]
            a["wgt"] += r["wgt"]
        else:
            qapprox[key] = True

    qkeys = sorted(qagg)
    qp = {}
    for k in qkeys:
        a = qagg[k]
        qp[k] = (a["amt"] / a["wgt"]) if a["wgt"] > 0 else (sum(a["ps"]) / len(a["ps"]))
    quarterly = []
    for i, k in enumerate(qkeys):
        qoq = round((qp[k] / qp[qkeys[i - 1]] - 1) * 100, 1) if i > 0 else None
        py = "%04d-%s" % (int(k[:4]) - 1, k[5:])
        yoy = round((qp[k] / qp[py] - 1) * 100, 1) if py in qp else None
        quarterly.append({"t": k, "rev": round(qagg[k]["amt"]) or None,
                          "p": round(qp[k], 2), "qoq": qoq, "yoy": yoy,
                          "approx": bool(qapprox.get(k))})

    out = {
        "meta": {
            "metric": "반도체 수출 판가 (수출금액 USD / 중량 kg)",
            "source": "관세청 무역통계 (BT 가공 시트 CSV 임포트)",
            "csv": csv_path.name,
            "note": "yoy/qoq 단위 = %. rev = 분기 수출금액(USD). approx=true 는 분기 판가를 월 단순평균으로 대체한 구간.",
            "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        },
        "monthly": monthly,
        "quarterly": quarterly,
    }
    OUT_PATH.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")),
                        encoding="utf-8")
    pk = max((r for r in monthly if r["yoy"] is not None), key=lambda r: r["yoy"], default=None)
    print("[OK] %s  monthly=%d (%s ~ %s)  quarterly=%d"
          % (OUT_PATH.name, len(monthly), monthly[0]["t"], monthly[-1]["t"], len(quarterly)))
    if pk:
        print("     판가 YoY 정점: %s  %+.1f%%" % (pk["t"], pk["yoy"]))
    print("     최근 3개월:", monthly[-3:])


if __name__ == "__main__":
    main()
