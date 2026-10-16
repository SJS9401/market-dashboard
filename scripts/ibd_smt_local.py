#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IBD Stock Market Today — 로컬 PC 실행 래퍼 (2026-10-09 신설)
----------------------------------------------------------
GitHub 서버(클라우드 IP)는 YouTube 가 봇으로 차단한다(2026-10-09 프로브 2회 확인).
그래서 BT PC 의 작업 스케줄러가 KST 화~토 06:40 에 이 파일을 실행한다.

  1) 로컬 리포 git pull (최신 스크립트 반영)
  2) scripts/ibd_smt_relay.py 실행 — 5분 간격 재시도, 마지막 확인 08:00 KST (미국 서머타임 해제 기간 08:30)
     (2026-10-10 BT 지시: 15분 → 07:20까지 연장. 10/9 방송(65분)은 06:15 종료 후
      35분이 지나도 자동자막이 안 나와 06:55 마감에 걸렸다. 데일리가 IBD를 맨 마지막에 읽는다)
  3) data/ibd_smt_*.json 변경분만 commit → push (토큰은 Scheduled/.github_token)
  4) 로그: Scheduled/deploy_logs/ibd_smt_YYYYMMDD.log

(2026-10-16 BT 지시: 07:20 → 08:00. 10/15 회차는 06:48 업로드. 서머타임이 끝나면 방송이 1시간
늦어져 자막이 07:40~07:55 예상 → 그 기간은 08:30으로 자동 전환. 데일리가 못 읽은 날은 08:40 클라우드
예약 작업 「ibd-backfill-cloud」가 아카이브 ⑤-3을 채운다)

데일리 프리뷰(07:01 시작)는 수집 묶음이 끝난 뒤 맨 마지막(07:18~07:22 전후)에
GitHub Pages 의 data/ibd_smt_latest.json 을 읽는다. 07:20까지 못 받으면 데일리에는 「IBD 자막 미수신」, 08:40 사후 채우기가 보완한다.
※ 작업 스케줄러 「IBD-SMT-Relay」의 실행 시간 제한은 2시간이어야 한다(1시간이면 07:40에 강제 종료).
"""
import os, subprocess, sys, datetime

REPO = r"C:\Users\ruzby\Documents\Claude\market-dashboard"
SCHED = r"C:\Users\ruzby\Documents\Claude\Scheduled"
TOKEN_FILE = os.path.join(SCHED, ".github_token")
LOG_DIR = os.path.join(SCHED, "deploy_logs")
REMOTE = "github.com/SJS9401/market-dashboard.git"

DEADLINE_DST = (8, 2)    # 미국 서머타임 기간: KST 08:00 전후 마지막 확인 (5분 간격 오차 흡수)
DEADLINE_STD = (8, 32)   # 서머타임 해제 기간(11월 첫 일요일 ~ 3월 둘째 일요일): 방송 1시간 늦음 → 08:30

def us_dst(d):
    """미국 서머타임 여부 — 3월 둘째 일요일 ~ 11월 첫 일요일 (tz 데이터 없이 계산)"""
    mar = datetime.date(d.year, 3, 8)
    nov = datetime.date(d.year, 11, 1)
    start = mar + datetime.timedelta((6 - mar.weekday()) % 7)
    end = nov + datetime.timedelta((6 - nov.weekday()) % 7)
    return start < d <= end

os.makedirs(LOG_DIR, exist_ok=True)
LOG = os.path.join(LOG_DIR, f"ibd_smt_{datetime.datetime.now():%Y%m%d}.log")


def log(msg):
    line = f"[{datetime.datetime.now():%H:%M:%S}] {msg}"
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def run(cmd, env=None, secret=None, timeout=None):
    shown = " ".join(cmd)
    if secret:
        shown = shown.replace(secret, "***")
    r = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env=env, timeout=timeout)
    out = (r.stdout + r.stderr).strip()
    if secret:
        out = out.replace(secret, "***")
    log(f"$ {shown} -> rc={r.returncode}")
    if out:
        log(out[-3000:])
    return r.returncode


def main():
    log("===== start =====")
    if not os.path.isdir(os.path.join(REPO, ".git")):
        log("[ERROR] local repo not found"); return 1
    run(["git", "pull", "--rebase", "--autostash"], timeout=120)

    now = datetime.datetime.now()   # PC 시계 = KST
    DEADLINE = DEADLINE_DST if us_dst(now.date()) else DEADLINE_STD
    dl = now.replace(hour=DEADLINE[0], minute=DEADLINE[1], second=0, microsecond=0)
    wait_min = max(1, int((dl - now).total_seconds() // 60))   # 마감이 지났으면 1회만 확인
    log(f"마감 {DEADLINE[0]:02d}:{DEADLINE[1]:02d} KST — 최대 {wait_min}분 재시도")
    env = dict(os.environ, PYTHONIOENCODING="utf-8", MAX_WAIT_MIN=str(wait_min), PROBE="0")
    run([sys.executable, os.path.join("scripts", "ibd_smt_relay.py")], env=env, timeout=(wait_min + 10) * 60)

    # ibd 파일만 커밋한다 — 다른 작업(대시보드 배포 등) 파일은 건드리지 않는다
    subprocess.run(["git", "reset", "-q"], cwd=REPO)
    run(["git", "add", "--", "data/ibd_smt_*.json"])
    staged = subprocess.run(["git", "diff", "--cached", "--name-only"], cwd=REPO,
                            capture_output=True, text=True).stdout.split()
    if not staged:
        log("no ibd changes — skip push"); return 0
    run(["git", "-c", "user.name=ibd-smt-local", "-c", "user.email=actions@users.noreply.github.com",
         "commit", "-m", "ibd_smt local [skip ci]"])

    try:
        token = open(TOKEN_FILE, encoding="utf-8").read().strip()
    except Exception:
        log("[ERROR] token file missing"); return 1
    url = f"https://x-access-token:{token}@{REMOTE}"
    for i in range(1, 6):
        if run(["git", "push", url, "HEAD:main"], secret=token, timeout=120) == 0:
            log(f"pushed (attempt {i})"); return 0
        run(["git", "pull", "--rebase", "--autostash", url, "main"], secret=token, timeout=120)
    log("[ERROR] push failed 5x"); return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        log(f"[FATAL] {type(e).__name__}: {e}")
        sys.exit(1)
