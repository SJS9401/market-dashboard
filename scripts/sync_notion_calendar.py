# -*- coding: utf-8 -*-
"""
Notion 이벤트 캘린더 DB -> data/events_calendar.json 생성.
GitHub Actions 에서 매일 07:30 KST 실행. 필요 환경변수: NOTION_TOKEN

2026-09-13 구조 변경: 예전에는 dashboard.html / index.html 의 `const events=[...]` 를
정규식으로 직접 치환했는데, deploy_dashboard.bat 의 xcopy 가 BT 로컬(Scheduled) 사본으로
두 HTML 을 덮어써서 배포할 때마다 동기화분이 통째로 날아갔다.
data/*.json 은 deploy 의 보호 목록(extract_protected_files.ps1)이 지켜주므로
이벤트 배열을 JSON 으로 분리하고 HTML 은 런타임에 fetch 한다.

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

DATABASE_ID = "6c2fc2267c2d4fe58f601db7d8ce56d7"
NOTION_VERSION = "2022-06-28"
OUT_PATH = os.path.join("data", "events_calendar.json")
NO_DATE = "9999-12-31"


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


def fetch_all_rows(token):
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }
    payload = {
        "filter": {
            "or": [
                {"property": "상태", "select": {"does_not_equal": "취소"}},
                {"property": "상태", "select": {"is_empty": True}},
            ]
        },
        "page_size": 100,
    }
    rows = []
    while True:
        r = requests.post(url, headers=headers, json=payload, timeout=30)
        r.raise_for_status()
        data = r.json()
        rows.extend(data["results"])
        if not data.get("has_more"):
            break
        payload["start_cursor"] = data["next_cursor"]
    return rows


def build_events(rows):
    items = []
    for row in rows:
        p = row["properties"]
        ev = title_to_str(p.get("이벤트", {}))
        if not ev:
            continue
        sort_key = date_start(p.get("정렬일", {})) or NO_DATE
        items.append(
            (
                sort_key,
                {
                    "d": rich_text_to_str(p.get("날짜", {})),
                    "sd": "" if sort_key == NO_DATE else sort_key[:10],
                    "cat": select_to_str(p.get("카테고리", {})) or "기타",
                    "ev": ev,
                    "note": rich_text_to_str(p.get("비고", {})),
                },
            )
        )
    items.sort(key=lambda x: x[0])
    return [e for _, e in items]


def main():
    token = os.environ.get("NOTION_TOKEN")
    if not token:
        print("[ERROR] NOTION_TOKEN env var missing")
        sys.exit(1)

    rows = fetch_all_rows(token)
    print(f"[INFO] fetched {len(rows)} calendar rows from Notion")
    events = build_events(rows)
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
        "source": f"Notion DB {DATABASE_ID}",
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
