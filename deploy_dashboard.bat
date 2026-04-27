@echo off
REM ============================================================
REM  deploy_dashboard.bat
REM  Auto-deploy script for SJS9401/market-dashboard repo
REM
REM  Flow:
REM    1. Load .github_token and refresh remote URL
REM    2. git pull (sync with remote)
REM    3. Copy html files from Scheduled to repo folder
REM    4. Commit and push if changes detected
REM
REM  Schedule: Mon-Fri 07:55 KST (30 min after Daily issue 07:24)
REM  Registration: run register_dashboard_scheduler.ps1 as admin
REM ============================================================

setlocal EnableDelayedExpansion

REM --- Path config ---
set "SRC_DIR=C:\Users\ruzby\Documents\Claude\Scheduled"
set "REPO_DIR=C:\Users\ruzby\Documents\Claude\market-dashboard"
set "TOKEN_FILE=%SRC_DIR%\.github_token"
set "LOG_DIR=%SRC_DIR%\deploy_logs"

REM --- Build date strings using PowerShell (wmic removed in Win11 24H2) ---
for /f "usebackq delims=" %%I in (`powershell -NoProfile -Command "Get-Date -Format yyyyMMddHHmmss"`) do set "DT=%%I"
set "YYYY=!DT:~0,4!"
set "MM=!DT:~4,2!"
set "DD=!DT:~6,2!"
set "HH=!DT:~8,2!"
set "NN=!DT:~10,2!"
set "SS=!DT:~12,2!"
set "TODAY=!YYYY!-!MM!-!DD!"
set "LOG_FILE=%LOG_DIR%\deploy_!YYYY!!MM!!DD!.log"

REM --- Ensure log directory ---
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"

echo. >> "%LOG_FILE%"
echo ============================================ >> "%LOG_FILE%"
echo [!YYYY!-!MM!-!DD! !HH!:!NN!:!SS!] deploy start >> "%LOG_FILE%"

REM --- Load token ---
if not exist "%TOKEN_FILE%" (
    echo [ERROR] .github_token not found: %TOKEN_FILE% >> "%LOG_FILE%"
    exit /b 1
)
set /p GITHUB_TOKEN=<"%TOKEN_FILE%"
if "!GITHUB_TOKEN!"=="" (
    echo [ERROR] .github_token is empty >> "%LOG_FILE%"
    exit /b 1
)

REM --- Enter repo directory ---
if not exist "%REPO_DIR%\.git" (
    echo [ERROR] git repo not found: %REPO_DIR% >> "%LOG_FILE%"
    echo [HINT] Run: git clone https://github.com/SJS9401/market-dashboard.git "%REPO_DIR%" >> "%LOG_FILE%"
    exit /b 1
)
cd /d "%REPO_DIR%" || (
    echo [ERROR] failed to enter repo: %REPO_DIR% >> "%LOG_FILE%"
    exit /b 1
)

REM --- Refresh remote URL (re-applies token from .github_token every run) ---
git remote set-url origin "https://!GITHUB_TOKEN!@github.com/SJS9401/market-dashboard.git" >> "%LOG_FILE%" 2>&1

REM --- git pull ---
echo [!HH!:!NN!:!SS!] git pull >> "%LOG_FILE%"
git pull origin main >> "%LOG_FILE%" 2>&1
if !errorlevel! neq 0 (
    echo [ERROR] git pull failed - possible conflict, manual check needed >> "%LOG_FILE%"
    exit /b 2
)

REM --- Copy html files ---
echo [!HH!:!NN!:!SS!] copying files >> "%LOG_FILE%"
if exist "%SRC_DIR%\index.html" (
    copy /Y "%SRC_DIR%\index.html" "%REPO_DIR%\index.html" >nul
    echo   - index.html copied >> "%LOG_FILE%"
) else (
    echo   [WARN] index.html source missing - skipped >> "%LOG_FILE%"
)
if exist "%SRC_DIR%\dashboard.html" (
    copy /Y "%SRC_DIR%\dashboard.html" "%REPO_DIR%\dashboard.html" >nul
    echo   - dashboard.html copied >> "%LOG_FILE%"
)
if exist "%SRC_DIR%\Market_cycle.html" (
    copy /Y "%SRC_DIR%\Market_cycle.html" "%REPO_DIR%\Market_cycle.html" >nul
    echo   - Market_cycle.html copied >> "%LOG_FILE%"
)
if exist "%SRC_DIR%\Leading_stocks.html" (
    copy /Y "%SRC_DIR%\Leading_stocks.html" "%REPO_DIR%\Leading_stocks.html" >nul
    echo   - Leading_stocks.html copied >> "%LOG_FILE%"
)

REM --- Mirror .github/workflows/ folder (자동 갱신 워크플로우 yml 일괄 동기화) ---
if exist "%SRC_DIR%\.github\workflows" (
    if not exist "%REPO_DIR%\.github\workflows" mkdir "%REPO_DIR%\.github\workflows"
    xcopy /Y /Q "%SRC_DIR%\.github\workflows\*.yml" "%REPO_DIR%\.github\workflows\" >>"%LOG_FILE%" 2>&1
    echo   - .github/workflows/*.yml mirrored >> "%LOG_FILE%"
)

REM --- Stage and check for changes ---
git add index.html dashboard.html Market_cycle.html Leading_stocks.html 2>>"%LOG_FILE%"
git add .github/workflows 2>>"%LOG_FILE%"
git diff --cached --quiet
if !errorlevel! equ 0 (
    echo [!HH!:!NN!:!SS!] no changes - skip commit >> "%LOG_FILE%"
    echo [!YYYY!-!MM!-!DD! !HH!:!NN!:!SS!] done ^(no changes^) >> "%LOG_FILE%"
    exit /b 0
)

REM --- Commit and push ---
echo [!HH!:!NN!:!SS!] git commit + push >> "%LOG_FILE%"
git commit -m "auto: !TODAY! dashboard update" >> "%LOG_FILE%" 2>&1
git push origin main >> "%LOG_FILE%" 2>&1
if !errorlevel! neq 0 (
    echo [ERROR] git push failed - check token/permissions >> "%LOG_FILE%"
    exit /b 3
)

echo [!YYYY!-!MM!-!DD! !HH!:!NN!:!SS!] deploy done ^(push success^) >> "%LOG_FILE%"
endlocal
exit /b 0
