#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IBD "Stock Market Today" transcript relay  (2026-10-09 신설)
----------------------------------------------------------
IBD 유튜브 채널의 장 마감 후 라이브 「Stock Market Today」 자막을 받아
data/ibd_smt_latest.json (+ 날짜별 사본)으로 저장한다.
데일리 프리뷰(클라우드)는 YouTube 에 직접 접근할 수 없으므로 이 파일을 GitHub Pages 로 읽는다.

방송 시각: 미 동부 16:05~16:30 ET (여름 20:05 UTC / 겨울 21:05 UTC)
GitHub cron 은 2~5시간 지연되므로 일찍 깨워 방송·자막이 올라올 때까지 대기 루프로 기다린다
(us_close_relay 와 같은 구조).

환경변수
  PROBE=1  : 대기 없이 최신 회차 1건으로 두 가지 자막 경로를 모두 시험하고 결과를
             data/ibd_smt_probe.json 에 기록 (GitHub 서버에서 YouTube 가 막히는지 확인용)
  FORCE=1  : 오늘 세션 파일이 이미 있어도 다시 받는다
"""
import json, os, sys, time, re, traceback, urllib.request
from datetime import datetime, timezone, timedelta

try:
    from zoneinfo import ZoneInfo
    NY = ZoneInfo("America/New_York")
except Exception:  # pragma: no cover
    NY = timezone(timedelta(hours=-4))

CHANNEL_STREAMS = "https://www.youtube.com/@investorsbusinessdaily/streams"
TITLE_KEY = "stock market today"
DATA_DIR = "data"
LATEST = os.path.join(DATA_DIR, "ibd_smt_latest.json")
PROBE_OUT = os.path.join(DATA_DIR, "ibd_smt_probe.json")

PROBE = os.environ.get("PROBE", "0") == "1"
FORCE = os.environ.get("FORCE", "0") == "1"
MAX_WAIT_MIN = int(os.environ.get("MAX_WAIT_MIN", "330"))   # GitHub 잡 하드리밋 360분 아래
POLL_MIN = 5
log_lines = []


def log(msg):
    line = f"[{datetime.now(timezone.utc).strftime('%H:%M:%S')}Z] {msg}"
    print(line, flush=True)
    log_lines.append(line)


# ---------------------------------------------------------------- 영상 찾기
def list_recent_streams(n=8):
    import yt_dlp
    opts = {"quiet": True, "skip_download": True, "extract_flat": "in_playlist",
            "playlistend": n, "noprogress": True}
    with yt_dlp.YoutubeDL(opts) as y:
        info = y.extract_info(CHANNEL_STREAMS, download=False)
    out = []
    for e in (info.get("entries") or []):
        if e and e.get("id"):
            out.append({"id": e["id"], "title": e.get("title") or ""})
    return out


def video_info(vid):
    import yt_dlp
    opts = {"quiet": True, "skip_download": True, "noprogress": True}
    with yt_dlp.YoutubeDL(opts) as y:
        return y.extract_info(f"https://www.youtube.com/watch?v={vid}", download=False)


def session_date_of(info):
    """방송 시작 시각(뉴욕 기준) 날짜 = 세션일."""
    ts = info.get("release_timestamp") or info.get("timestamp")
    if ts:
        return datetime.fromtimestamp(ts, timezone.utc).astimezone(NY).date().isoformat()
    ud = info.get("upload_date")
    if ud:
        return f"{ud[:4]}-{ud[4:6]}-{ud[6:]}"
    return None


def find_today_video(today_ny):
    for c in list_recent_streams():
        if TITLE_KEY not in c["title"].lower():
            continue
        info = video_info(c["id"])
        sd = session_date_of(info)
        log(f"후보 {c['id']} · {sd} · live_status={info.get('live_status')} · {c['title'][:60]}")
        if sd == today_ny:
            return info
        if PROBE:   # 프로브는 날짜 무관 최신 1건
            return info
        break       # 최신 SMT 가 오늘 것이 아니면 아직 안 올라온 것
    return None


# ---------------------------------------------------------------- 자막 받기
def transcript_via_api(vid):
    from youtube_transcript_api import YouTubeTranscriptApi
    try:  # v1.x
        ft = YouTubeTranscriptApi().fetch(vid, languages=["en"])
        return [(float(s.start), s.text) for s in ft]
    except AttributeError:  # v0.6.x
        rows = YouTubeTranscriptApi.get_transcript(vid, languages=["en"])
        return [(float(r["start"]), r["text"]) for r in rows]


def transcript_via_ytdlp(info):
    caps = (info.get("subtitles") or {}).get("en") or (info.get("automatic_captions") or {}).get("en") or []
    url = next((f["url"] for f in caps if f.get("ext") == "json3"), None)
    if not url:
        raise RuntimeError("json3 자막 트랙 없음")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    body = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")
    if not body.strip():
        raise RuntimeError("자막 응답이 비어 있음 (PO 토큰 요구로 추정)")
    j = json.loads(body)
    out = []
    for ev in j.get("events", []):
        segs = ev.get("segs")
        if not segs:
            continue
        t = "".join(s.get("utf8", "") for s in segs).strip()
        if t:
            out.append((ev.get("tStartMs", 0) / 1000.0, t))
    return out


def fmt(snips):
    lines = []
    for start, text in snips:
        m, s = divmod(int(start), 60)
        lines.append(f"[{m:02d}:{s:02d}] {text.replace(chr(10), ' ').strip()}")
    return "\n".join(lines)


def try_transcript(info):
    vid = info["id"]
    results = {}
    for name, fn in (("youtube_transcript_api", lambda: transcript_via_api(vid)),
                     ("yt_dlp_json3", lambda: transcript_via_ytdlp(info))):
        try:
            sn = fn()
            results[name] = {"ok": bool(sn), "segments": len(sn)}
            log(f"자막 경로 {name}: 성공 {len(sn)}구간")
            if sn and not PROBE:
                return name, sn, results
            if sn and PROBE and "_first" not in results:
                results["_first"] = (name, sn)
        except Exception as e:
            results[name] = {"ok": False, "error": f"{type(e).__name__}: {str(e)[:300]}"}
            log(f"자막 경로 {name}: 실패 — {type(e).__name__}: {str(e)[:200]}")
    first = results.pop("_first", None)
    if first:
        return first[0], first[1], results
    return None, None, results


def build_record(info, method, snips, today_ny):
    desc = info.get("description") or ""
    hosts = re.search(r"Hosts?:\s*(.+)", desc)
    ch = [{"title": c.get("title"), "start": int(c.get("start_time", 0))} for c in (info.get("chapters") or [])]
    rs, re_ = info.get("release_timestamp"), None
    dur = info.get("duration")
    if rs and dur:
        re_ = rs + int(dur)
    iso = lambda t: datetime.fromtimestamp(t, timezone.utc).isoformat() if t else None
    return {
        "base_date": session_date_of(info) or today_ny,
        "video_id": info["id"],
        "url": f"https://www.youtube.com/watch?v={info['id']}",
        "title": info.get("title"),
        "hosts": hosts.group(1).strip() if hosts else None,
        "live_start_utc": iso(rs),
        "live_end_utc_est": iso(re_),
        "duration_sec": dur,
        "chapters": ch,
        "transcript_method": method,
        "transcript_lang": "en (auto-generated)",
        "transcript": fmt(snips),
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
    }


def save(rec):
    os.makedirs(DATA_DIR, exist_ok=True)
    for p in (LATEST, os.path.join(DATA_DIR, f"ibd_smt_{rec['base_date']}.json")):
        with open(p, "w", encoding="utf-8") as f:
            json.dump(rec, f, ensure_ascii=False, indent=1)
    log(f"저장 완료 base_date={rec['base_date']} · {len(rec['transcript'])}자")


# ---------------------------------------------------------------- 메인
def probe():
    rec = {"probe_at_utc": datetime.now(timezone.utc).isoformat(), "steps": {}}
    try:
        info = find_today_video(None)
        rec["steps"]["list_and_info"] = {"ok": bool(info), "video_id": info and info.get("id"),
                                          "title": info and info.get("title")}
        if info:
            method, sn, res = try_transcript(info)
            rec["steps"]["transcript"] = res
            if sn:
                rec["sample"] = fmt(sn[:15])
    except Exception as e:
        rec["steps"]["fatal"] = f"{type(e).__name__}: {str(e)[:500]}"
        log(f"영상 정보 실패: {type(e).__name__}: {str(e)[:200]}")
        # 영상 정보가 막혀도 자막 API 단독 경로는 따로 시험한다
        try:
            cands = [c for c in list_recent_streams() if TITLE_KEY in c["title"].lower()]
            rec["steps"]["list_only"] = {"ok": bool(cands), "first": cands[0] if cands else None}
            if cands:
                sn = transcript_via_api(cands[0]["id"])
                rec["steps"]["transcript_api_only"] = {"ok": bool(sn), "segments": len(sn)}
                rec["sample"] = fmt(sn[:15])
        except Exception as e2:
            rec["steps"]["transcript_api_only"] = {"ok": False, "error": f"{type(e2).__name__}: {str(e2)[:500]}"}
    rec["log"] = log_lines
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(PROBE_OUT, "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=1)
    log("프로브 결과 저장")


def main():
    if PROBE:
        return probe()
    now = datetime.now(timezone.utc)
    today_ny = now.astimezone(NY).date().isoformat()
    if datetime.now(NY).weekday() >= 5:
        log("주말 — 종료"); return
    if not FORCE and os.path.exists(LATEST):
        try:
            if json.load(open(LATEST, encoding="utf-8")).get("base_date") == today_ny:
                log(f"[SKIP] {today_ny} 이미 있음"); return
        except Exception:
            pass
    # 자막이 올라올 것으로 보는 시각 = 뉴욕 16:35 (방송 종료 16:30 + 여유). 서머타임은 뉴욕 시계가 자동 흡수
    ready_ny = datetime.now(NY).replace(hour=16, minute=35, second=0, microsecond=0)
    wait = ready_ny.astimezone(timezone.utc) - now
    if wait > timedelta(minutes=MAX_WAIT_MIN - 30):
        log(f"[SKIP] 너무 이른 발화 — 예상 준비 시각까지 {wait} · 다음 슬롯에 맡김"); return
    limit = now + timedelta(minutes=MAX_WAIT_MIN)   # 데일리(06:55 KST 마지노선) 이후 착지해도 파일은 남긴다(위클리·수동 조회용)
    if wait > timedelta(0):
        log(f"예상 준비 시각까지 대기 {wait}")
        time.sleep(wait.total_seconds())
    tries = 0
    while True:
        tries += 1
        try:
            info = find_today_video(today_ny)
            if info and info.get("live_status") not in ("is_live", "is_upcoming"):
                method, sn, res = try_transcript(info)
                if sn and len(sn) >= 40:
                    save(build_record(info, method, sn, today_ny)); return
                log(f"자막 아직 없음/부족 ({res})")
            else:
                log(f"오늘({today_ny}) 회차 아직 없음 또는 방송 중")
        except Exception as e:
            log(f"오류: {type(e).__name__}: {str(e)[:200]}")
        if datetime.now(timezone.utc) + timedelta(minutes=POLL_MIN) > limit:
            log(f"[GIVE UP] {tries}회 시도 — 마지노선 도달. 파일 미갱신"); return
        time.sleep(POLL_MIN * 60)


if __name__ == "__main__":
    main()
