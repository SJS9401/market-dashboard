#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IBD Stock Market Today — 로컬 PC 실행 래퍼 (2026-10-09 신설)
----------------------------------------------------------
GitHub 서버(클라우드 IP)는 YouTube 가 봇으로 차단한다(2026-10-09 프로브 2회 확인).
그래서 BT PC 의 작업 스케줄러가 KST 화~토 06:40 에 이 파일을 실행한다.

  1) 로컬 리포 git pull (최신 스크립트 반영)
  2) scripts/ibd_smt_relay.py 실행 — 최대 15분 재시도 (06:55 KST 전 종료)
  3) data/ibd_smt_*.json 변경분만 commit → push (토큰은 Scheduled/.github_token)
  4) 로그: Scheduled/deploy_logs/ibd_smt_YYYYMMDD.log

데일리 프리뷰(07:01)는 GitHub Pages 의 data/ibd_smt_latest.json 을 읽는다.
"""
import os, subprocess, sys, datetime

REPO = r"C:\Users\ruzby\Documents\Claude\market-dashboard"
SCHED = r"C:\Users\ruzby\Documents\Claude\Scheduled"
TOKEN_FILE = os.path.join(SCHED, ".github_token")
LOG_DIR = os.path.join(SCHED, "deploy_logs")
REMOTE = "github.com/SJS9401/market-dashboard.git"

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

    env = dict(os.environ, PYTHONIOENCODING="utf-8", MAX_WAIT_MIN="15", PROBE="0")
    run([sys.executable, os.path.join("scripts", "ibd_smt_relay.py")], env=env, timeout=20 * 60)

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
