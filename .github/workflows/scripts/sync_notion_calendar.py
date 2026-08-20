# -*- coding: utf-8 -*-
"""
Notion 이벤트 캘린더 DB → dashboard.html / index.html 의 const events=[...] 배열 갱신.
GitHub Actions 에서 매일 07:30 KST 실행. 필요 환경변수: NOTION_TOKEN
"""
import json
import os
import re
import sys

import requests

DATABASE_ID = "6c2fc2267c2d4fe58f601db7d8ce56d7"
NOTION_VERSION = "2022-06-28"
TARGET_FILES = ["dashboard.html", "index.html"]


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


def js_escape(s):
    return s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ")


def build_events_js(rows):
    events = []
    for row in rows:
        p = row["properties"]
        ev = title_to_str(p.get("이벤트", {}))
        if not ev:
            continue
        d_disp = rich_text_to_str(p.get("날짜", {}))
        cat = select_to_str(p.get("카테고리", {})) or "기타"
        note = rich_text_to_str(p.get("비고", {}))
        sort_key = date_start(p.get("정렬일", {})) or "9999-12-31"
        events.append((sort_key, d_disp, cat, ev, note))

    events.sort(key=lambda x: x[0])

    parts = []
    for _, d_disp, cat, ev, note in events:
        parts.append(
            "{d:'%s',cat:'%s',ev:'%s',note:'%s'}"
            % (js_escape(d_disp), js_escape(cat), js_escape(ev), js_escape(note))
        )
    return "const events=[" + ",".join(parts) + "];"


def patch_file(path, events_js):
    if not os.path.exists(path):
        print(f"[WARN] {path} not found, skip")
        return False
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    new_html, n = re.subn(
        r"const\s+events\s*=\s*\[.*?\];", events_js, html, count=1, flags=re.DOTALL
    )
    if n == 0:
        print(f"[ERROR] const events=[...] block not found in {path}")
        return False
    if new_html == html:
        print(f"[OK] {path} unchanged")
        return True
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"[OK] {path} updated")
    return True


def main():
    token = os.environ.get("NOTION_TOKEN")
    if not token:
        print("[ERROR] NOTION_TOKEN env var missing")
        sys.exit(1)

    rows = fetch_all_rows(token)
    print(f"[INFO] fetched {len(rows)} calendar rows from Notion")
    events_js = build_events_js(rows)

    ok = True
    for path in TARGET_FILES:
        ok = patch_file(path, events_js) and ok
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
