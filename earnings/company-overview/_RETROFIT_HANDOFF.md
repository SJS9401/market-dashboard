# 기업개요 1번 섹션 retrofit 핸드오프 (Cross-Session)

> **목적**: company-overview 1번 섹션을 삼성전자 v4.8 수준 디폴트 quality로 표준화
> **작성**: 2026-05-24 반도체 섹션 세션에서 신설 + T1 반도체 8개 완료
> **공유 위치**: `Scheduled\earnings\company-overview\_RETROFIT_HANDOFF.md` (모든 섹터 세션에서 읽기 가능)

---

## 1. 발동 문구 (다른 섹터 세션에서 사용)

### 가장 명확한 trigger:

```
company-overview/_RETROFIT_HANDOFF.md 읽고 {섹터명} 1번 섹션 retrofit 진행
```

예시:
- **빅테크 세션**: `_RETROFIT_HANDOFF.md 읽고 T1 빅테크 7개 retrofit 진행`
- **전력 인프라 세션**: `_RETROFIT_HANDOFF.md 읽고 T2 전력 인프라 7개 retrofit 진행`

### 메모리 자동 적용 확인:

위 발동 문구 호출 시 [기업 개요 모드] 스킬이 자동으로 `feedback_company_overview_section1_standard.md` 메모리를 참조한다. 별도 확인 불필요.

---

## 2. 표준 5가지 요약 (메모리 룰 핵심)

전체 룰은 메모리 `feedback_company_overview_section1_standard.md` 참조. 핵심:

(1) **Summary Box 6지표** — 매출 CAGR, OPM 평균/정점/저점 (연도 명시), 사이클 주기, 회수
(2) **손익 표 narrative annotation** — 각 연도 옆 사이클 변곡점 마커 (← 1차 슈퍼사이클, ← 다운사이클 저점 등). 표 자체가 사이클 history book
(3) **분류 결정 sub-logic 4단계** — (1) 매출 큰 사업부 기준 (2) secular 변수 sub-rule (3) Boundary case 처리 Primary + Secondary (4) 글로벌 피어 cross-reference
(4) **밸류에이션 다이얼** — 사업부 mix → method 연결. PER/PBR/EV/EBITDA 단순 나열 금지. 삼성전자 비교 1줄 필수
(5) **재평가 트리거 = 분류 변경 조건** — 실적 추적용 변수 (HBM 점유율·ASP 등)는 6번 섹션. 1번 트리거는 "분류 자체가 바뀔 조건" (예: HBM 비중 50%+ 도달 시 Primary cyclical → Secular 격상)

---

## 3. 진행 현황 (2026-05-25 갱신)

### ✅ 완료 (24/24) — 100% retrofit 완료

| 종목 | 섹터 | 새 분류 |
|---|---|---|
| 삼성전자 | T1 반도체 | Primary 사이클 + Secondary 지속성장 일부 (**reference 표준**) |
| ASML (v2.1) | T2 반도체 소부장 | Primary Secular Growth + Secondary WFE Capex 사이클 |
| SK하이닉스 (v4.9) | T1 반도체 | Primary 사이클 + Secondary AI HBM secular |
| MU (v4.9) | T1 반도체 | Primary 사이클 + Secondary AI HBM secular |
| INTC (v4.9) | T1 반도체 | Primary 구조적 Turnaround + Secondary Foundry 전환 |
| STX (v4.9) | T1 반도체 | Primary 사이클 + 구조적 전환 + Secondary AI 콜드 스토리지 |
| SNDK (v4.9) | T1 반도체 | Primary 사이클 + Secondary AI Enterprise SSD |
| WDC (v4.9) | T1 반도체 | Primary 사이클 + 구조적 전환 + Secondary AI Cloud Storage |
| AMD (v4.9) | T1 반도체 | Primary 고성장 + secular + Secondary 사이클 일부 |
| ARM (v4.9) | T1 반도체 | Primary 지속성장 + Secular (사이클 거의 부재) |
| **AAPL (v4.8)** | **T1 빅테크** | **Primary 지속성장 + Secondary iPhone 모델·중국 거시 약한 사이클 (OPM range 7.9%pt)** |
| **MSFT (v4.8)** | **T1 빅테크** | **Primary 지속성장 + Secondary Cloud/AI secular sub-cycle (Nokia 일회성 제외 단조 우상향)** |
| **GOOGL (v4.8)** | **T1 빅테크** | **Primary 지속성장 + Secondary Cloud AI secular + Antitrust multiple cap** |
| **META (v4.8)** | **T1 빅테크** | **Primary 지속성장 + Secondary 사이클 (CapEx·RL 베팅 3회 명확, OPM range 24.9%pt)** |
| **AMZN (v4.8)** | **T1 빅테크** | **Primary multi-segment 지속성장 + Secondary 인프라 사이클 (AWS·물류 CapEx, 2회 명확)** |
| **TSLA (v4.8)** | **T1 빅테크** | **Primary 고성장 + 사이클 + Secondary AI/Robotaxi/Optimus optionality (OPM range 34.5%pt)** |
| **NVDA (v4.8)** | **T1 빅테크 + T1 반도체** | **Primary 고성장 secular + Secondary 3대 산업 사이클 (모바일·크립토·AI, OPM range 47.5%pt)** |
| **HE (v1.5)** | **T2 전력 인프라** | **Primary 지속성장 (Energy Transition) + Secondary 턴어라운드 후반 + 사이클 noise (Margin range +5.9%pt, 단조 우상향)** |
| **ABB (v1.5)** | **T2 전력 인프라** | **Primary 지속성장 (Electrification·Motion 글로벌 #1) + Secondary 일부 사이클 (PA) + Robotics 분사** |
| **GEV (v1.5)** | **T2 전력 인프라** | **Primary 턴어라운드 (분사 직후 + Wind 적자 정상화) + Secondary 지속성장 (Gas Power + Electrification)** |
| **SU (v1.5)** | **T2 전력 인프라** | **Primary 지속성장 (Energy Management + IA 글로벌 #1, 4축 멀티 secular) + Secondary 일부 사이클 (IA 18% + China 18%)** |
| **효성중공업 (v1.5)** | **T2 전력 인프라** | **Primary 사이클 (중공업+건설 mix, OPM range +11pp) + Secondary 지속성장 진입 (HICO Memphis + HVDC 한국 단독)** |
| **HD현대일렉트릭 (v1.5)** | **T2 전력 인프라** | **Primary 사이클 boundary (OPM range +33pp 초강세) + Secondary 지속성장 강세 (US 변압기 sweet spot + 회전기기 AI 데이터센터)** |
| **LS일렉트릭 (v1.5)** | **T2 전력 인프라** | **Primary 사이클 (한국 후발, OPM range +4.8pp 약함) + Secondary 지속성장 진입 중 (DC·자동화 secular)** |

### ⏳ Pending (0/24) — 완료

### 📝 신규 작성 시 자동 적용 (메모리 룰만으로 충분)

이미지 Tier 1·2·3의 나머지 종목 (기업개요 미작성, 약 34개) — 향후 [기업 개요 모드] 호출 시 자동 표준 적용. 별도 retrofit 불요.

---

## 4. Sample Reference (작성 시 참고)

### A. Cyclical pure-play (메모리·HDD): SK하이닉스, MU, STX, SNDK, WDC
- 사이클 진폭 OPM ±50~80%pt
- 손익 표 annotation: ← 1차 슈퍼사이클, ← 다운사이클 저점, ← AI 회복 등
- secular 변수: HBM 비중·Cloud 비중·AI Enterprise SSD

### B. Multi-segment cyclical: 삼성전자 (디폴트 표준)
- 사업부 mix 추론 (DX vs DS 매출 비중 + OP 비중 = 사이클 분류 결정)
- valuation 다이얼: PBR + PER 혼합

### C. Structural turnaround: INTC
- 12년 매출 CAGR 마이너스 = 사이클 아닌 구조적 침체
- valuation: PBR + Sum-of-Parts + Catalysts 가중

### D. Secular growth (high growth): AMD, NVDA, ARM
- 사이클 진폭 작음 (±10~30%pt)
- valuation: PER + DCF + TAM expansion

### E. Secular growth (asset-light IP): ARM
- 사이클 거의 부재, OPM 40%+ 소프트웨어 수준
- valuation: PER 100배+ premium 정당화

### F. Secular + cyclical mix (장비): ASML
- WFE Capex 사이클 + EUV 독점 secular 중첩
- Boundary case 처리 룰 명시 적용

---

## 5. 작업 흐름 (종목당 ~5분)

(1) 기존 `.md`의 1번 섹션 읽기 (보통 line 1~80)
(2) 손익 데이터 + 산업 narrative 추출
(3) 표준 5가지 적용한 새 1번 섹션 작성 + Edit
(4) 다른 종목 retrofit 누적 후 batch `.html` 재생성 (단일 Python script로 10초)

### batch .html 재생성 script (재사용 가능)

`outputs/batch_html_t1_semi.py` 참조 (반도체 세션에서 작성). tickers list만 바꿔서 사용.

---

## 6. 메모리 발동 확인 방법

다른 세션에서 retrofit 시작 전:

```
메모리 확인:
- feedback_company_overview_section1_standard.md (표준 5가지 룰)
- feedback_sector_memory_structure.md (섹터별 세션 운영)
- 삼성전자_기업개요.md (디폴트 reference, 같은 폴더)
```

발동 문구 호출 시 위 3개가 자동 로드됨. 추가 안내 없이 진행 가능.

---

## 7. 본 핸드오프 파일 갱신 룰

각 섹터 retrofit 완료 시 본 파일의 "진행 현황" 섹션에 ✅ 추가. 모든 24개 종목 완료 후 본 파일 삭제 가능 (메모리 룰만 남기면 됨).

---

## 8. 디자인 표준 통일 (2026-05-25 추가) ★ 신규 룰

### A. 표준 디자인 (삼성전자 v4.8 dark theme)

**.html companion 디자인은 삼성전자 표준을 디폴트로 적용**한다. brand color variant (Apple blue·MSFT cyan 등) 금지.

| 요소 | 색상 |
|---|---|
| body bg | `#0f1419` (다크 베이스) |
| body text | `#e6e6e6` |
| h1 (회사명) | `#4ec9b0` (민트 그린) + border-bottom `#2d3748` |
| h2 (대주제) | `#76b9c4` (라이트 블루) + border-left `#76b9c4` |
| h3·h4 (중·소주제) | `#c5a572` (베이지) |
| strong | `#f0b070` (오렌지) |
| 폰트 | 'Pretendard' (한글 우선) |
| max-width | 1280px |

전체 CSS template + 색상 의미는 메모리 `feedback_company_overview_html_design_standard.md` 참조.

### B. 변경 대상 (디자인 비표준 상태)

| 종목 | 현재 비표준 패턴 | 변경 필요 |
|---|---|---|
| AAPL | bg `#0e1117` + h1·h2 Apple blue `#007AFF` | 표준 적용 |
| MSFT | bg `#0e1117` + h1·h2 MSFT cyan `#00A4EF` | 표준 적용 |
| AMZN | (확인 필요) | 표준 적용 |
| GOOGL | (확인 필요) | 표준 적용 |
| META | (확인 필요) | 표준 적용 |
| TSLA | (확인 필요) | 표준 적용 |
| NVDA | ✅ 본 세션에서 표준 적용 완료 (반도체 겸함) |

전력 인프라 종목 (HE, 효성중공업)은 확인 결과 **이미 표준 적용 완료**. 나머지 ABB·GEV·SU·HD현대일렉트릭·LS일렉트릭는 다른 세션이 작성한 상태이므로 검증 + 비표준이면 재생성 필요.

### C. 발동 문구 — 빅테크 세션

```
company-overview/_RETROFIT_HANDOFF.md 섹션 8 읽고
AAPL·AMZN·GOOGL·META·MSFT·TSLA 6개 .html을 삼성전자 표준 dark theme으로 재생성해줘.
.md는 그대로 유지. .html companion만 표준 CSS로 교체.

표준 CSS는 메모리 feedback_company_overview_html_design_standard.md에 저장됨 (자동 로드).
batch 스크립트 sample: outputs/batch_html_samsung_standard.py 패턴 따라 재사용.
```

### D. 발동 문구 — 전력 인프라 세션

```
company-overview/_RETROFIT_HANDOFF.md 섹션 8 읽고
ABB·GEV·SU·HD현대일렉트릭·LS일렉트릭 5개 .html을 삼성전자 표준 dark theme으로 검증·재생성해줘.
(HE, 효성중공업은 이미 표준 적용 완료라 skip)
.md는 그대로 유지. .html companion만 표준 CSS로 교체.

표준 CSS는 메모리 feedback_company_overview_html_design_standard.md에 저장됨 (자동 로드).
```

### E. 검증 방법 (재생성 후 확인)

각 종목 .html 첫 1KB에서 CSS 확인:
```bash
head -c 1000 {종목}_기업개요.html | grep -E "background|color"
# 기대: background: #0f1419; color: #e6e6e6;
# 기대: h1 color: #4ec9b0; h2 color: #76b9c4;
```

비표준 색상 (`#0e1117`, `#007AFF`, `#00A4EF`) 발견 시 재생성 필요.
