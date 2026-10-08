# 배포 구조 메모 (2026-10-08 폴더 연결 이관)

## 원본(Source of truth)
- **마켓 대시보드 세션 파일** (HTML, py 스크립트, data/*.json, .github/workflows) — 이 레포 자체가 원본이다.
  - 수정은 이 클론(`Documents\Claude\market-dashboard`) 또는 GitHub 웹에서 한다.
  - `Documents\Claude\Scheduled` 의 같은 이름 파일은 더 이상 레포로 복사되지 않는다 (옛 사본, 무시).
- **실적 팔로업 세션 파일** — Earnings_followup.html / .js, earnings/, 캘린더는 기존대로 Scheduled 에서 복사된다.

## 배포
- `Scheduled\deploy_dashboard.bat` (repo-source 버전): git pull → 실적 세션 파일 복사 → GitHub Actions 관리 파일 복원 → git add/commit/push.
- 트리거: 평일 07:55 예약 작업, 배포 워처(1분 주기) 플래그, 수동 실행.
- 배포 요청 플래그: `_claude_bridge\_deploy_request.flag` (레포 쪽, Claude 가 만들 수 있음) 또는 `Scheduled\_deploy_request.flag`.
- 이전 버전 백업: `Scheduled\deploy_dashboard_bak_20261008.bat`, `Scheduled\deploy_watch_bak_20261008.bat`.
