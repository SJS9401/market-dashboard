# -*- coding: utf-8 -*-
"""
Notion 이벤트 캘린더 DB + 실적 캘린더 DB -> data/events_calendar.json 생성.
GitHub Actions 에서 매일 07:30 KST 실행. 필요 환경변수: NOTION_TOKEN

2026-09-13 구조 변경: 예전에는 dashboard.html / index.html 의 `const events=[...]` 를
정규식으로 직접 치환했는데, deploy_dashboard.bat 의 xcopy 가 BT 로컬(Scheduled) 사본으로
두 HTML 을 덮어써서 배포할 때마다 동기화분이 통째로 날아갔다.
data/*.json 은 deploy 의 보호 목록(extract_protected_files.ps1)이 지켜주므로
이벤트 배열을 JSON 으로 분리하고 HTML 은 런타임에 fetch 한다.

2026-10-22 (BT 승인): 실적 일정의 단일 출처 = 실적 캘린더 DB.
  - 이벤트 캘린더의 카테고리 「실적」 행은 대시보드에 싣지 않는다(위클리·데일리가 묶어 넣은 행이
    실적 캘린더와 따로 놀며 날짜가 어긋났다 — 10/22 MSFT·GOOGL·AMZN 사례).
  - 대신 실적 캘린더 DB(어닝스 위스퍼 대조로 매일 갱신)를 날짜별로 묶어 「실적」 행으로 넣는다.
    한 날짜(한국 시간) = 한 행: "새벽(미 장후) A·B / 장전 C / 시점 미정 D" — 날짜 추정 종목은 이름 뒤에 *.
  - 실적 캘린더를 못 읽으면(권한·네트워크) 예전처럼 이벤트 캘린더의 「실적」 행을 그대로 쓴다.

출력 스키마
{"generated_at": ISO8601Z, "source": str, "count": int,
"events": [{"d": 표시용 자유 텍스트, "sd": 정렬일 YYYY-MM-DD 또는 "",
"cat": 카테고리, "ev": 이벤트명, "note": 비고}, ...]}
sd = 렌더러가 필터/요일 계산에 쓰는 값. 정렬일이 비면 "" (렌더러가 M/D fallback 후
'진행형' 목록으로 분리).
"""
import datetime
import json
import os
import sys

import requests

DATABASE_ID = "6c2fc2267c2d4fe58f601db7d8ce56d7"           # 이벤트 캘린더
EARNINGS_DATABASE_ID = "f378de3f1f614e4c8d38a916f63b589f"  # 실적 캘린더
NOTION_VERSION = "2022-06-28"
OUT_PATH = os.path.join("data", "events_calendar.json")
NO_DATE = "9999-12-31"
EARNINGS_BACK_DAYS = 7      # 지난 실적은 대시보드가 어차피 숨긴다 — 오늘 −7일부터만 받는다
EARNINGS_AHEAD_DAYS = 60
TIMING_ORDER = [("AMC", "새벽(미 장후)"), ("BMO", "장전"), ("장중", "장중"), ("미정", "시점 미정")]


def rich_text_to_str(prop):
    return "".join(t.get("plain_text", "") for t in prop.get("rich_text", [])).strip()


def title_to_str(prop):
    return "".join(t.get("plain_text", "") for t in prop.get("title", [])).strip()


def select_to_str(prop):
    sel = prop.get("select")
    return sel["name"] if sel else ""


def date_start(prop):
    d = prop.get("date")
    return d["start"] if d else ""


def notion_headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def query_all(token, database_id, payload):
    url = f"https://api.notion.com/v1/databases/{database_id}/query"
    payload = dict(payload, page_size=100)
    rows = []
    while True:
        r = requests.post(url, headers=notion_headers(token), json=payload, timeout=30)
        r.raise_for_status()
        data = r.json()
        rows.extend(data["results"])
        if not data.get("has_more"):
            break
        payload["start_cursor"] = data["next_cursor"]
    return rows


def fetch_all_rows(token):
    return query_all(token, DATABASE_ID, {
        "filter": {
            "or": [
                {"property": "상태", "select": {"does_not_equal": "취소"}},
                {"property": "상태", "select": {"is_empty": True}},
            ]
        },
    })


def fetch_earnings_rows(token):
    today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).date()
    start = (today - datetime.timedelta(days=EARNINGS_BACK_DAYS)).isoformat()
    end = (today + datetime.timedelta(days=EARNINGS_AHEAD_DAYS)).isoformat()
    return query_all(token, EARNINGS_DATABASE_ID, {
        "filter": {
            "and": [
                {"property": "발표일", "date": {"on_or_after": start}},
                {"property": "발표일", "date": {"on_or_before": end}},
            ]
        },
    })


def build_events(rows, skip_earnings):
    items = []
    for row in rows:
        p = row["properties"]
        ev = title_to_str(p.get("이벤트", {}))
        if not ev:
            continue
        cat = select_to_str(p.get("카테고리", {})) or "기타"
        if skip_earnings and cat == "실적":
            continue
        sort_key = date_start(p.get("정렬일", {})) or NO_DATE
        items.append(
            (
                sort_key,
                {
                    "d": rich_text_to_str(p.get("날짜", {})),
                    "sd": "" if sort_key == NO_DATE else sort_key[:10],
                    "cat": cat,
                    "ev": ev,
                    "note": rich_text_to_str(p.get("비고", {})),
                },
            )
        )
    return items


def build_earnings_events(rows):
    by_date = {}
    for row in rows:
        p = row["properties"]
        name = title_to_str(p.get("종목", {}))
        sd = date_start(p.get("발표일", {}))[:10]
        point = rich_text_to_str(p.get("포인트", {}))
        if not name or not sd or point.startswith("⛔"):   # ⛔ = 실적 캘린더 작업이 표시한 중복 행
            continue
        timing = select_to_str(p.get("시점", {})) or "미정"
        if timing not in dict(TIMING_ORDER):
            timing = "미정"
        status = select_to_str(p.get("검증상태", {}))
        label = name + ("*" if status == "추정" else "")
        by_date.setdefault(sd, {}).setdefault(timing, []).append(label)

    items = []
    for sd in sorted(by_date):
        groups = by_date[sd]
        parts = [f"{ko} " + "·".join(groups[key]) for key, ko in TIMING_ORDER if groups.get(key)]
        n = sum(len(v) for v in groups.values())
        y, m, d = sd.split("-")
        items.append(
            (
                sd,
                {
                    "d": f"{int(m)}/{d}",
                    "sd": sd,
                    "cat": "실적",
                    "ev": " / ".join(parts),
                    "note": f"실적 캘린더 {n}종목 — 날짜는 한국 시간. 새벽(미 장후) = 미국 전날 장 마감 후 발표. * = 날짜 추정(미확정)",
                },
            )
        )
    return items


def main():
    token = os.environ.get("NOTION_TOKEN")
    if not token:
        print("[ERROR] NOTION_TOKEN env var missing")
        sys.exit(1)

    rows = fetch_all_rows(token)
    print(f"[INFO] fetched {len(rows)} calendar rows from Notion")

    earnings_items, source = [], f"Notion DB {DATABASE_ID}"
    try:
        e_rows = fetch_earnings_rows(token)
        earnings_items = build_earnings_events(e_rows)
        print(f"[INFO] fetched {len(e_rows)} earnings rows -> {len(earnings_items)} dated earnings lines")
        source += f" + earnings DB {EARNINGS_DATABASE_ID}"
        skip_earnings = True
    except Exception as e:  # 권한·네트워크 실패 시 예전 방식(이벤트 캘린더의 실적 행) 유지
        print(f"[WARN] earnings DB read failed ({type(e).__name__}: {e}) -- falling back to event-calendar earnings rows")
        skip_earnings = False

    items = build_events(rows, skip_earnings) + earnings_items
    items.sort(key=lambda x: x[0])
    events = [e for _, e in items]
    dated = sum(1 for e in events if e["sd"])
    print(f"[INFO] {len(events)} events ({dated} dated, {len(events) - dated} undated)")

    if not events:
        print("[ERROR] no events built -- refusing to overwrite output")
        sys.exit(1)

    payload = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
        "source": source,
        "count": len(events),
        "events": events,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, separators=(",", ":"))
        f.write("\n")
    print(f"[OK] {OUT_PATH} written ({len(events)} events)")


if __name__ == "__main__":
    main()
