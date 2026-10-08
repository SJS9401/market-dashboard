# 배포 구조 메모 (2026-10-08 폴더 연결 이관)

## 원본(Source of truth)
- **마켓 대시보드 세션 파일** (HTML, py 스크립트, data/*.json, .github/workflows) — 이 레포 자체가 원본이다.
  - 수정은 이 클론(`Documents\Claude\market-dashboard`) 또는 GitHub 웹에서 한다.
  - `Documents\Claude\Scheduled` 의 같은 이름 파일은 더 이상 레포로 복사되지 않는다 (옛 사본, 무시).
- **실적 팔로업 세션** — 작업 폴더 `Documents\Claude\earnings` 에서 md/html/png 만 레포 `earnings/` 로 미러된다 (비공개 폴더·company-overview-source 제외). Earnings_followup.html/.js 는 레포에서 직접 수정.

## 배포
- `Scheduled\deploy_dashboard.bat` (repo-source 버전): git pull → 실적 세션 파일 복사 → GitHub Actions 관리 파일 복원 → git add/commit/push.
- 트리거: 평일 07:55 예약 작업, 배포 워처(1분 주기) 플래그, 수동 실행.
- 배포 요청 플래그: `_claude_bridge\_deploy_request.flag` (레포 쪽, Claude 가 만들 수 있음) 또는 `Scheduled\_deploy_request.flag`.
- 이전 버전 백업: `Scheduled\deploy_dashboard_bak_20261008.bat`, `Scheduled\deploy_watch_bak_20261008.bat`.

## 수정 경로 (2026-10-08, 클라우드 우선)
- **기본: GitHub 웹에서 직접 수정** (크롬, 아무 컴퓨터). 집 PC 가 꺼져 있어도 된다.
- 보조: PC 가 켜져 있을 때 이 클론을 고치고 `_claude_bridge\_deploy_request.flag` 로 배포.
- 데이터 갱신은 전부 GitHub Actions (+ cron-job.org 06:55 dispatch). PC 무관.
- PC 에 남은 역할: 실적 페이지 업로드(평일 07:05 배포)뿐. 클라우드 세션 GitHub 쓰기 기능이 나오면 이관 예정.
