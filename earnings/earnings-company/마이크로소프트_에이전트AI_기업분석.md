---
ticker: "MSFT"
company_name: Microsoft Corporation
country: US
theme_keyword: 에이전트AI
parent_industry: 빅테크 (수요 측)
role: macro_layer_component   # 9개사·NVIDIA와 다름 — 본 분석은 수요 측 macro layer single component
trend_revenue_share: 50                # AI 직접 노출 (Azure AI + Copilot + AI Foundry)
ai_capex_FY26: 190                    # CY26 ~$190B (component pricing $25B 포함)
ai_arr_Q3FY26: 37                     # AI Annual Revenue Run-rate $37B (+123% YoY CC)
last_updated: 2026-06-21
auto_references:
  - 반도체_산업기초.md (2026-05-18)
  - 에이전트AI_테마분석.md (v4, 2026-05-26)
  - MSFT_기업개요.md (v1.0, 2026-05-19)
  - 2026-Q1_MSFT_리뷰.md (Q3 FY26, 2026-04-29 발표)
  - 2026-Q2_MSFT_팔로업.md (Q4 FY26 예정)
  - 엔비디아_에이전트AI_기업분석.md (NVIDIA → MSFT GPU 발주 mapping)
analyst_reports_attached:
  - MSFT Q3 FY26 Press Release + Earnings Slides + 10-Q + Transcript (IR 원본 7종)
  - MSFT Q3 FY26 Outlook (Amy Hood CFO commentary)
notes:
  - Microsoft 회계연도 = 7월~6월. FY26 = 2025.07~2026.06. Q3 FY26 = 2026.01~03 (calendar 2026-Q1)
  - 본 분석 frame은 9개사·NVIDIA와 다름 — 빅테크는 본 테마의 "고객" (수요 측). AI 사업부 (Azure AI + Copilot + Maia) + CAPEX trajectory + 10개사 발주 mapping이 본질
  - 통합 모드 macro layer의 single 종목 component — 4사 (MSFT·Google·AWS·Meta) 통합 시 CAPEX baseline + AI 매출 trajectory 합산
---

# Microsoft 기업 분석 — 에이전트AI 테마 (★ 빅테크 frame, 수요 측)

> **본 분석 frame (★ 9개사·NVIDIA와 다름)**: Microsoft는 본 테마의 **고객 (수요 측)**. 9개사·NVIDIA가 공급 측 (반도체)이라면 MSFT는 **CAPEX 발주 + AI 매출 driver**. 본 분석 frame은 (a) **AI 사업부 분석** (Azure AI + M365 Copilot + GitHub Copilot + AI Foundry) (b) **CAPEX trajectory 분해** (CY26 $190B) (c) **10개사 thesis와 직접 connection mapping** (NVIDIA Blackwell·Rubin 발주 + SK·삼성·Micron HBM·DDR5·eSSD + WDC·STX HDD nearline + Intel Foundry 18A Maia ASIC + ARM Cobalt CPU). **통합 모드 macro layer의 single 종목 component**. **★ Q3 FY26 매출 $82.9B (+18% YoY) + AI ARR $37B (+123% YoY) + RPO $627B (+99% YoY) + CY26 CapEx ~$190B + "remain constrained at least through 2026"** = AI 인프라 사이클 정점 미도래 가장 강한 시그널.

> **CapEx·매출 단위 기준**: 모든 매출·CapEx는 USD billion (Microsoft 회계연도 = 7월~6월). FY26 = 2025.07~2026.06. AI ARR (Annual Revenue Run-rate)은 분기 매출 × 4 + 일부 추정. Constant Currency (CC) 기준 별도 표기.

---

## Executive Summary (5줄)

1. **위치**: 글로벌 Cloud #2 (Azure, AWS 다음) + AI Foundation 파트너십 #1 (OpenAI $13B+) + M365 Copilot 좌석 #1. ★ **Q3 FY26 매출 $82.9B (+18% YoY) record + AI ARR $37B (+123% YoY)** + RPO $627B (+99% YoY) = **매출 가시성 2-3년 sector best**. CY26 CapEx ~$190B (FY25 $65B 대비 +192%, 단일 분기 $40B+).
2. **AI 사업부 구성**: Azure AI (Intelligent Cloud $34.7B, +30% YoY) + M365 Copilot 20M+ 좌석 (Accenture 740K 최대 단일 win) + GitHub Copilot (6/1 usage-based 전환) + AI Foundry (OpenAI + Anthropic + 5K open source 5K). **★ AI 사업부 매출 비중 ~50%** (본 테마 직접 노출).
3. **10개사 thesis driver**: NVIDIA Blackwell 발주 최대 hyperscaler 1위 + SK·삼성·Micron HBM3E·HBM4 발주 + Maia ASIC (Intel Foundry 18A) + Cobalt CPU (ARM Neoverse) + WDC·STX HDD nearline + ★ "remain constrained at least through 2026" = NVIDIA·메모리·HDD 모두 sold out driver.
4. **CapEx trajectory**: FY24 $44.5B → FY25 $65B → **CY26 ~$190B** (단일 분기 $40B+). 2/3 short-lived (GPU·CPU, 5-6년 monetization), 1/3 long-lived (15+ years). ★ "FY27 double-digit growth" preliminary outlook + "second half 2026 acceleration" 시사.
5. **종합 (macro layer component)**: <span class="star">★★★ AI 인프라 수요 측 needle-mover</span>. NVIDIA·9개사 thesis 모두의 #1 driver. (a) **Microsoft Cloud GPM 5분기 연속 하락** (69% → 66% → 가이드 64%) — AI 인프라 비용 흡수 risk (b) **OpenAI 의존도** (Foundry 다각화 진행 중) (c) **소비자 BU 약세** (Windows·Xbox·Search). 단기 thesis 강고, 장기 CapEx 사이클 정점 검증 필요.

---

# 항목 1. 입력 정리 + Microsoft 위치

## 1-1. 산업·테마 컨텍스트

- **반도체 산업기초**: MSFT는 수요 측 needle-mover — 공급 측 9개사·NVIDIA가 제공하는 반도체의 #1 발주처
- **에이전트AI 테마 v4**: 17 segment 중 MSFT는 **수요 driver** (AI Datacenter CapEx + Sovereign AI 일부 + Industrial AI 일부). 본 테마 종목 (NVIDIA·SK·HBM 등)의 매출 trajectory anchor
- **NVIDIA 기업분석** (2026-06-21): NVIDIA 본 테마 needle-mover의 #1 고객. ★ MSFT 단일 hyperscaler가 NVIDIA GPU 매출의 ~15-20% 추정 ($30-40B/년)
- **10개사 thesis와의 관계**:
  - **메모리 3사 (SK·삼성·Micron)**: HBM3E·HBM4 발주, DDR5 server, eSSD 직접 발주
  - **HDD (WDC·STX)**: cold storage nearline 직접 발주 (Azure exabyte data store)
  - **Intel·Intel Foundry**: Xeon (legacy) + ★ Intel 18A Maia ASIC 위탁 (turnaround 핵심)
  - **AMD**: EPYC server CPU + MI300/350 alternative 일부
  - **ARM**: Cobalt CPU (ARM Neoverse 기반) — Intel Xeon 잠식의 일부
  - **NVIDIA**: Blackwell·Rubin GPU 최대 발주 (전체 4-5 hyperscaler 중 #1-2)

## 1-2. Microsoft 위치 (수요 측 needle-mover)

| Segment | 글로벌 위치 | 비고 |
|---|---|---|
| **AI Cloud (Azure AI)** | **글로벌 #2** (AWS 다음) | Q3 FY26 Azure +40% YoY, AI Services +13pp contribution |
| **★ AI ARR (Annual Run-rate)** | **$37B Q3 FY26 (+123% YoY)** | OpenAI + Azure AI + Copilot 종합 |
| **AI Foundation 파트너십** | **#1 OpenAI 독점적 파트너** ($13B+ 투자, 49% economic interest) | + Anthropic 추가 (다각화) |
| **AI 좌석 (M365 Copilot)** | **20M+ 좌석 #1** | Accenture 740K (Copilot 사상 최대 단일 win) |
| **AI 개발자 (GitHub Copilot)** | **#1 글로벌 코드 AI** | 6/1 usage-based pricing 전환 |
| **★ CY26 CapEx** | **~$190B** | GOOGL FY26 $180-190B 동일 수준 |
| **★ RPO (Remaining Performance Obligation)** | **$627B (+99% YoY)** | 매출 가시성 2-3년 sector best |
| **자체 ASIC (Maia)** | **Intel Foundry 18A, Iowa·Arizona DC live** | DC 절반 이상 deployed |
| **자체 ARM CPU (Cobalt)** | **ARM Neoverse 기반, 양산 본격화** | Intel Xeon 잠식 일부 |

→ **단일 빅테크로 본 테마 가장 광범위 수요 driver** — Azure AI + Copilot + Maia + Cobalt + OpenAI 파트너십.

## 1-3. 사업부 구성 (Q3 FY26, FY25 비교)

| Segment | Q3 FY26 매출 | YoY | 본 테마 연결 | 비중 |
|---|---|---|---|---|
| **Intelligent Cloud (★ Azure)** | **$34.68B** | **+30% YoY (+28% CC)** | ★ 본 테마 직접 (Azure AI Services) | **42%** |
| **Productivity & Business Processes** | **$35.01B** | **+17%** | ★ M365 Copilot 직접 + 일부 LinkedIn AI | **42%** |
| **More Personal Computing** | **$13.19B** | **-1%** | 본 테마 미미 (Windows·Xbox·Search) | **16%** |
| **Total** | **$82.89B** | **+18%** | | 100% |

### 본 테마 직접 매출 노출
- **Intelligent Cloud 42% × ~80%** (Azure AI Services + Server)
- **Productivity & BP 42% × ~30%** (M365 Copilot + Foundry + Dynamics AI)
- **More Personal Computing 16% × ~5%** (Search·Copilot Web)
- **순 본 테마 직접 노출 = 약 50%** (9개사·NVIDIA보다 작음, 빅테크 종합 사업 특성)
- **★ Microsoft Cloud $54.5B (+29% YoY, +25% CC) = 매출 비중 66%** (Azure + Office 365 Commercial + LinkedIn + Dynamics 365 통합)
- **★ AI ARR $37B (+123% YoY)** = 매출 비중 18% (전 분기 ARR, Q3 매출 × 4 ~ $14B 단순환산보다 큰 이유는 OpenAI 매출 + non-MSFT cloud 일부 포함)

---

## ★ 2-0. 에이전트AI 테마 logical flow — 왜 Microsoft가 부각받는가 (수요 측)

> **정성적 인과 사슬** (테마 v4 narrative → MSFT 위치 매핑 — 수요 측 driver)

### 1단계: 에이전트 AI = 데이터·연산·메모리 폭증의 본질
- 에이전트 1건 = chat 1턴 대비 **토큰 20-30x** (Stanford/NVIDIA 실측, 테마 v4)
- 각 추론 단계·도구 호출·검색·메모리 갱신 = **연산 + 메모리 + 스토리지 + IP 모든 layer 부하 폭증**
- agent는 stateful → 과거 trace·long-context 보존 필요 = secular 누적
- ★ **MSFT Satya Q3 FY26**: *"We're at the start of an agentic computing era — every application, every workflow must be re-architected for AI agents"*

### 2단계: AI 인프라 layer별 분담 — MSFT는 어디 위치? (수요 측)

| Layer | 9·10개사 (공급 측) | **MSFT (수요 측 driver)** |
|---|---|---|
| **Hot (HBM)** | SK·삼성·Micron | **MSFT HBM 발주 가속 (Blackwell·Rubin GPU 채택)** |
| **Warm (DRAM·SSD)** | 메모리 3사 + SNDK·Solidigm | **MSFT Azure DRAM·eSSD 최대 발주** |
| **Warm-Cold (eSSD·HBF)** | SNDK | **MSFT Azure Vector DB·체크포인트 발주** |
| **Cold (HDD nearline)** | WDC·Seagate | **★ MSFT Azure exabyte data store 최대 발주** (Azure storage tier) |
| **Compute (CPU)** | Intel·AMD·ARM 라이선시 | **MSFT Cobalt CPU (ARM Neoverse 기반) 자체 + EPYC + Xeon 혼합** |
| **Compute (GPU·AI)** | NVIDIA·AMD·hyperscaler ASIC | **★ MSFT Blackwell·Rubin GPU 최대 발주 + Maia ASIC (Intel Foundry 18A) + AMD MI300/350 일부** |
| **IP layer** | ARM Holdings + NVIDIA | **MSFT는 ARM IP 라이선시 (Cobalt) + Windows on ARM 협력 (NVIDIA N1/N1X)** |

→ **MSFT 위치: 본 테마 7개 layer 모두에 수요 측 driver. 9·10개사 thesis 모두의 #1 직접 고객 (또는 #1-2)**

### 3단계: 왜 MSFT가 본 테마에서 수요 측 needle-mover인가? — 4가지 본질적 이유

1. **★ AI ARR $37B (+123% YoY)** = OpenAI + Azure AI + Copilot 종합 → 빅테크 4사 중 AI ARR 단연 #1 정량 입증
2. **★ CY26 CapEx ~$190B** = AI 인프라 발주 사상 최대 → 9·10개사 thesis 모두에 직접 driver (NVIDIA·SK·HBM·HDD 매출 가시성)
3. **★ RPO $627B (+99% YoY) = 매출 가시성 2-3년** → 빅테크 4사 중 가장 명확한 commitment + OpenAI multi-year deal 인식
4. **★ "remain constrained at least through 2026"** (Amy Hood CFO) → 공급 제약이 천장이지 수요 둔화가 아님 = AI 인프라 사이클 정점 미도래

### 4단계: 왜 MSFT가 부각? — Azure + Copilot + OpenAI + Maia 통합 strategy

- **★ OpenAI 독점적 파트너십** ($13B+ 투자, 49% economic interest) — Anthropic 추가로 다각화 진행 (Foundry)
- **★ M365 Copilot 20M+ 좌석** (Accenture 740K = Copilot 사상 최대 단일 win) — AI 수요 driver
- **★ Azure +40% YoY (+39% CC) 3분기 연속 가속** — capacity-constrained 상태로 수요 압도
- **★ Maia ASIC (Intel Foundry 18A) Iowa·Arizona DC live + Cobalt CPU (ARM Neoverse) 양산** — NVIDIA 의존도 분산 시그널
- **★ AI Foundry multi-model strategy** — OpenAI + Anthropic + 5K open source = 고객 선택권 차별화

### 5단계: 본 분석 frame 결론 (수요 측 macro layer component)

**본 테마 수요 측 needle-mover + 9·10개사 thesis 모두의 #1 driver**. AI 사업부 매출 ~50%, AI ARR $37B (+123% YoY) = 빅테크 4사 #1. CY26 CapEx $190B = 9·10개사 매출 가시성 anchor. **★ "constrained through 2026" + RPO $627B = AI 인프라 사이클 정점 미도래의 가장 강한 시그널**. 단 ★ Microsoft Cloud GPM 5분기 연속 하락 = AI 인프라 비용 흡수 risk + OpenAI 의존도 + 소비자 BU 약세 3대 risk. **통합 모드 macro layer의 single 종목 component** — 4사 (MSFT·Google·AWS·Meta) 통합 시 CAPEX baseline + AI 매출 trajectory 합산.

---

# 항목 2. AI 사업부 + CAPEX trajectory + 10개사 발주 mapping — ★ 핵심

## 2-1. AI 사업부 분석 (Azure AI + Copilot + Foundry)

### Azure AI (Intelligent Cloud 내, $34.7B Q3 FY26)
- **Azure +40% YoY (+39% CC) 3분기 연속 가속** — capacity-constrained 상태
- **Azure AI Services**: AI 워크로드 +13pp contribution (Azure 성장 +40% 중 13pp가 AI)
- **고객 구성**: 10K+ Foundry 고객 (multi-model), 5K open source 사용, 300+ 고객 1T+ tokens 처리
- **★ Q4 FY26 가이드 Azure +39~40% CC** — sustainable 가속

### M365 Copilot (Productivity & BP 내)
- **20M+ 좌석 (Q3 FY26)** — 분기 신규 +250% YoY 사상 최대
- **Accenture 740K (Copilot 사상 최대 단일 win)** + Bayer·J&J·Mercedes·Roche 90K+ 각각
- ARPU growth = M365 Copilot driven (E5와 함께)
- **★ Q4 FY26 25M+ 좌석 도달 가능성**

### GitHub Copilot
- **6/1 usage-based pricing 전환** (단기 GPM 압박)
- 개발자 시장 #1, 경쟁 Cursor·Codeium 대비 enterprise 우위

### AI Foundry (multi-model platform)
- **OpenAI + Anthropic 양립** (OpenAI 독점 → 다각화 진행)
- 10K+ 고객 multi-model 사용
- **★ 시그널**: OpenAI 의존도 분산 + 고객 선택권 차별화

### ★ AI ARR $37B Q3 FY26 (+123% YoY)
- ★ **CEO 직접 공식 disclosure** (Satya Nadella, Q3 FY26 2026-04-29)
- OpenAI 매출 + Azure AI Services + Copilot 종합
- ★ **빅테크 4사 중 AI ARR 단연 #1**

## 2-2. CAPEX trajectory 분해 (★ macro layer 핵심)

### 분기 + 연간 CapEx 추이

| 분기/연 | CapEx ($B) | YoY | 비고 |
|---|---|---|---|
| FY24 (연) | **44.5** | — | AI 본격 진입 |
| FY25 (연) | **65.0** | **+46%** | AI 슈퍼사이클 진입 |
| Q1 FY26 | 34.9 | +75% | AI 가속 본격화 |
| Q2 FY26 | 37.5 | +66% | OpenAI multi-year deal |
| **Q3 FY26** | **31.9** | **+49%** | finance lease timing (sequential decline) |
| **Q4 FY26 (G)** | **>$40B** | — | 재가속 + component pricing $5B |
| **★ CY26 (연)** | **~$190B** | **+192% vs FY25** | **★ AI 인프라 발주 사상 최대** |
| **FY27 (preliminary)** | "double-digit growth" | — | preliminary, 정량 가이드 Q1 FY27 (10월) |

### CapEx 구성 분해
- **2/3 short-lived assets (5-6년 monetization)**: GPU·CPU (NVIDIA Blackwell·Rubin + Maia + Cobalt + EPYC)
- **1/3 long-lived assets (15+ years)**: 데이터센터 부지·건물·전력 인프라·냉각

### ★ 핵심 시그널
- ★ **"remain constrained at least through 2026"** (Amy Hood CFO) — 공급 제약이 천장
- ★ **"second half calendar 2026 acceleration"** (CFO) — Q4 FY26·Q1 FY27 추가 가속 가능
- **2H CY26 (Q1+Q2 FY27) 분기당 ~$60B 페이스 필요** (CY26 $190B의 25% = ~$48B/quarter baseline)

## 2-3. ★ 10개사 thesis와 직접 connection mapping (본 분석 frame의 본질)

### 발주 mapping (MSFT → 10개사)

| 10개사 종목 | MSFT 발주 형태 | 정량 추정 | 본 테마 driver 영향 |
|---|---|---|---|
| **NVIDIA (Blackwell·Rubin)** | DC GPU 직접 발주 #1-2 hyperscaler | **~$30-40B/년 (CY26)** | NVIDIA DC 매출 ~15-20% 비중 |
| **SK하이닉스 (HBM3E·HBM4)** | NVIDIA GPU 통한 간접 + Maia·Cobalt 직접 | 간접 + 직접 일부 | SK HBM3E·HBM4 majority driver |
| **삼성전자 (HBM4 AMD + DRAM)** | AMD MI400 일부 + 일반 DRAM 직접 | 간접 + 직접 | 삼성 DDR5 server CAPA #1 driver |
| **Micron (HBM + DDR5)** | NVIDIA GPU 통한 간접 + 미국 본토 직접 | 간접 + 미국 본토 우선 | Micron HBM 21% 가속 driver |
| **AMD (EPYC + MI300/MI400)** | EPYC server CPU + MI300 일부 | 일부 (NVIDIA 우선) | AMD EPYC 점유 24% → 27% driver |
| **Intel (Xeon + ★ Foundry 18A Maia)** | Xeon legacy + ★ **Maia ASIC 18A 양산 위탁** | ★ Foundry 18A 첫 외부 대형 고객 | Intel Foundry turnaround 핵심 leg |
| **ARM (Cobalt CPU)** | ★ **자체 Cobalt CPU = ARM Neoverse 기반** | ARM royalty 직접 | ARM 데이터센터 royalty 2x YoY driver |
| **SanDisk (eSSD)** | Azure storage tier nearline SSD | direct enterprise SSD | SNDK $42B NBM 5년 backlog 일부 |
| **WDC (HDD nearline)** | ★ Azure exabyte data store 최대 발주 | Azure cold storage tier | WDC nearline 52% #1 sold out driver |
| **Seagate (HDD nearline)** | ★ Azure cold storage 5 CSP qualified on Mozaic 3+ | FY27 build-to-order 일부 | STX nearline ~40% #2 driver |

→ **MSFT 단일 빅테크가 10개사 thesis 모두에 driver — 9·10개사 어느 누구도 이런 위치 없음** (수요 측 needle-mover)

### MSFT 자체 chip strategy (NVIDIA 의존도 분산)

| 자체 chip | 협력사 | 진행 단계 | 본 테마 영향 |
|---|---|---|---|
| **Maia 100/200 (AI 가속기)** | Intel Foundry 18A | ★ Iowa·Arizona DC live, DC 절반 이상 deployed | Intel Foundry 18A 첫 외부 대형 고객 = Intel turnaround driver |
| **Cobalt CPU (ARM Neoverse)** | TSMC | 양산 본격화 | ARM 데이터센터 royalty driver + Intel Xeon 잠식 |
| **★ 시그널**: NVIDIA 의존도 점진 분산 | — | 5년 trajectory | NVIDIA monopoly 위협 catalyst 중 #2 |

## 2-4. AI Foundry multi-model strategy (OpenAI 의존도 분산)

| Model | MSFT 위치 | 매출 contribution |
|---|---|---|
| **OpenAI (GPT 시리즈)** | ★ 독점 파트너 (2019 $1B + 2023 $10B + 2025 추가) → 다각화 진행 | OpenAI 매출 일부 + Azure GPU 매출 |
| **Anthropic (Claude)** | Foundry 추가 (다각화 시그널) | 신규 + 점진 |
| **MSFT 자체 (Phi-3·Phi-4)** | small language model strategy | 점진 |
| **Open source (Llama·Mistral·Qwen)** | 5K Foundry 고객 사용 | 점진 |

→ **★ OpenAI 의존도 분산 진행** = MSFT thesis risk hedging

---

# 항목 3. 재무 분석

## 3-1. 실적 추이 — 12년 매출·OPM·CapEx (AI 슈퍼사이클 변곡점)

| FY | 매출 ($B) | YoY | OPM | CapEx ($B) | 사이클 |
|---|---|---|---|---|---|
| FY14 | 86.83 | — | 32.0% | 10.9 | Satya CEO 취임 |
| FY15 | 93.58 | +8% | 19.4% | 5.9 | Nokia 손상 (일회성) |
| FY18 | 110.36 | +14% | 31.8% | 11.6 | 1차 점프 (Office 365 + Azure +91%) |
| FY21 | 168.09 | +18% | 41.6% | 20.6 | Cloud 슈퍼사이클 진입 |
| FY23 | 211.92 | +7% | 41.8% | 28.1 | ChatGPT/OpenAI 파트너십 |
| FY24 | 245.12 | +16% | 44.6% | 44.5 | ★ AI Copilot launch (2024-04) |
| **FY25** | **281.70** | **+15%** | **46.3%** | **65.0** | **★ AI 슈퍼사이클 정점 OPM** |
| **Q3 FY26 (분기)** | **82.89** | **+18%** | **46.3%** | **31.9** | **★ AI ARR $37B record** |
| **Q4 FY26 (G)** | **86.7~87.8** | **+13~15%** | **~45.5%** | **>$40** | acceleration 시작 |
| **CY26 (calendar)** | — | — | — | **~$190B** | **★ CapEx 사상 최대** |

## 3-2. AI 사업부 PQC 분해 (Azure vs M365 Copilot vs Foundry)

| 차원 | Azure AI Services | M365 Copilot | AI Foundry | 비고 |
|---|---|---|---|---|
| **P (단가)** | 컴퓨트 기반 (token·hour) | $30/seat/월 | API 기반 | enterprise pricing |
| **Q (출하)** | 폭증 (capacity-constrained) | **20M+ 좌석 (+250% YoY 신규)** | 10K+ 고객 | Copilot driver |
| **C (원가)** | NVIDIA GPU + Maia + datacenter | GPU + OpenAI 매출 share | OpenAI + Anthropic API 비용 | GPU·전력 |
| **매출** | Azure +40% (AI +13pp) | $30/seat × 20M = $600M/월 = $7.2B+/년 | Foundry usage 기반 | — |
| **마진 (GPM)** | Microsoft Cloud GPM 66% (5분기 연속 ↓) | 60%+ (P&BP segment) | GPU 비용 압박 | ★ GPM 하락 진행 |

## 3-3. 재무 건전성 + 자본 환원

- **부채비율**: 매우 안정 (현금 $80B+ vs 부채 ~$45B)
- **OCF/FCF**: Q3 FY26 OCF $46.74B / FCF $15.8B (★ CapEx 폭증으로 FCF -22% YoY)
- **★ 자본 환원 우선순위 변화**: FCF 폭증에도 CapEx 우선 → 자사주 매입·배당 페이스 안정
- **배당**: 분기 $0.83 (2026 기준)
- **자사주 매입**: FY25 ~$23B (NVDA 대비 작음)
- **★ FCF margin 압박**: AI CapEx 폭증으로 단기 FCF margin 하락. 단 RPO $627B = 2-3년 매출 가시성으로 buffer

## 3-4. 수익성 트렌드

- **GPM 추이**: Microsoft Cloud GPM **5분기 연속 하락** (Q3 FY25 69% → Q3 FY26 66% → Q4 가이드 64%)
- **OPM 추이**: FY25 46.3% (12년 최고) → Q3 FY26 46.3% 유지 → Q4 가이드 ~45.5%
- **★ 마진 압박 동인**: AI 인프라 투자 + GitHub Copilot usage-based 전환 + GPU·전력 cost
- **★ Maia + Cobalt 양산 확대 = Cloud GPM 변곡 동인 가능** (NVIDIA 의존도 분산 효과)

---

# 항목 4. 성장성 분석

## 4-1. 과거 성장률 (CAGR)

| 기간 | 매출 CAGR | OP CAGR | EPS CAGR |
|---|---|---|---|
| 3년 (FY22→FY25) | +12.4% | +16% | +25% |
| 5년 (FY20→FY25) | +14.5% | +20% | +30% |
| 12년 (FY13→FY25) | +11.3% | — | — |

→ **빅테크 안정 secular 성장**. 9개사 (NVIDIA +100%, AMD +35%) 대비 작지만 **AI ARR $37B (+123%) = AI 사업부 단독으로는 NVIDIA·AMD에 필적**.

## 4-2. 향후 성장 가시성 — 미래 PQC 전망

| 차원 | 전망 | 근거 | 6 카테고리 |
|---|---|---|---|
| **P 전망** | Azure compute pricing 안정, Copilot $30/seat 유지 | Azure capacity-constrained | (A) 안정 P |
| **Q 전망** | ★ Azure +40% CC 지속, Copilot 25M+ 좌석 | "second half 2026 acceleration" | (A)+(D) 폭증 |
| **C 전망** | ★ Microsoft Cloud GPM 5분기 연속 하락 → Q4 64% | AI 인프라 비용 흡수 + GitHub usage-based | 마진 압박 진행 |
| **→ 매출 성장** | **FY26 ~$330B (+17%) / FY27 ~$370B (+12%)** | RPO $627B 2-3년 가시성 | ★ secular |
| **→ 마진 지속** | OPM 45-47% 박스 유지 (operating leverage) | Microsoft Cloud GPM 64% 안정 후 회복 가능 | Maia ASIC 효과 |

### RPO + AI ARR 가시성
- **★ Commercial RPO $627B (+99% YoY)** — Q2 FY26 $625B (OpenAI deal 인식) → Q3 안정
- ★ **CFO**: "25% will be recognized in next 12 months, up 39% YoY" = 향후 12개월 인식분 약 **$157B 확보**
- **★ AI ARR $37B (+123% YoY)** = 단순 환산 시 분기 매출 ~$9.25B AI 직접 매출

### 성장 지속성 구조적 근거 + 저해 risk
**구조적 +**:
- ★ AI ARR $37B (+123% YoY) — AI 수익화 정량 입증
- ★ M365 Copilot 20M+ 좌석 — AI 수요 driver
- ★ RPO $627B 2-3년 가시성
- ★ CY26 CapEx $190B = 9·10개사 thesis 모두의 driver
- ★ "remain constrained at least through 2026" = 수요 압도

**저해 risk**:
- Microsoft Cloud GPM 5분기 연속 하락 (AI 인프라 비용)
- OpenAI 의존도 (Foundry 다각화 진행)
- 소비자 BU 약세 (Windows·Xbox·Search -1% YoY)
- 신규 ASIC (Maia) ramp risk (NVIDIA 대체 단기 어려움)

## 4-3. 빅테크 4사 비교 (★ 통합 모드 macro layer baseline)

| 빅테크 | 매출 CAGR (3년) | AI ARR | CY26 CapEx | 핵심 strategic angle |
|---|---|---|---|---|
| **MSFT** | +12.4% | **★ $37B (+123%)** | **~$190B** | OpenAI 독점 + Copilot 20M + Maia + Cobalt |
| **Google (Alphabet)** | +12% | ~$30B+ (추정) | $180-190B | TPU 6세대 + Gemini + GCP + Anthropic 투자 $3B |
| **AWS (Amazon)** | +10% | ~$25B+ (Anthropic Claude) | $195B | Trainium 2 + Inferentia + Graviton + Anthropic $11B deal |
| **Meta** | +20% | $20B+ (Llama + AI infra OPEX) | $135B | Llama + MTIA + ★ AMD MI450 6GW deal + 자체 인프라 |

→ ★ **MSFT가 AI ARR + CapEx 모두 빅테크 4사 #1**

---

# 항목 5. 통합 모드 입력용 Fact 정리 (macro layer single 종목 component)

| 항목 | 정리 |
|---|---|
| **CY26 CapEx** | **~$190B (FY25 $65B 대비 +192%)**, 단일 분기 $40B+ |
| **★ AI ARR (Q3 FY26)** | **$37B (+123% YoY CC)** — 빅테크 4사 #1 |
| **★ RPO** | **$627B (+99% YoY)**, 25% = $157B 향후 12개월 인식 |
| **Azure 성장** | **+40% YoY (+39% CC) 3분기 연속 가속** — capacity-constrained |
| **M365 Copilot 좌석** | **20M+ (+250% YoY 신규)** — Accenture 740K 최대 단일 |
| **AI Foundry 고객** | 10K+ multi-model, 5K open source, 300+ 1T+ tokens |
| **OpenAI 파트너십** | $13B+ (2019 $1B + 2023 $10B + 2025 추가), 49% economic interest. Anthropic 추가 (다각화) |
| **★ 자체 chip Maia 200 (Intel Foundry 18A)** | ★ Iowa·Arizona DC live, DC 절반 이상 deployed = Intel Foundry 18A 첫 외부 대형 고객 |
| **★ 자체 chip Cobalt CPU (ARM Neoverse)** | TSMC 양산 본격화 |
| **NVIDIA 발주 추정** | $30-40B/년 (NVIDIA DC 매출 15-20% 비중) |
| **HBM·HDD 발주** | SK·삼성·Micron HBM (NVIDIA GPU 통한 간접) + WDC·STX HDD nearline 직접 |
| **Microsoft Cloud GPM** | **5분기 연속 하락** (69% → 66% → Q4 가이드 64%) — AI 인프라 비용 |
| **시총** | ~$3.7T (2026-06 기준) |

---

# 항목 6. 구조적 트리거 모니터링

## 상방 트리거

- ★ **Azure +41%+ CC 4분기 연속 가속** (Q4 FY26 검증)
- ★ **CY26 CapEx $190B 페이스 유지** + FY27 정량 가이드 (Q1 FY27, 10월 말 예정)
- ★ **AI ARR $50B+ 도달** (Q4 FY26 예상)
- ★ **M365 Copilot 25M+ 좌석** (Q4 FY26)
- **Maia 200 + Cobalt CPU 양산 확대** = Cloud GPM 변곡 시그널
- **Anthropic 협력 deepening** (OpenAI 의존도 분산 가속)

## 하방 트리거

- Azure +37% 이하 둔화 (가속 사이클 종료)
- Microsoft Cloud GPM 62% 이하 하락 (FY27 OpMargin 위협)
- CY26 CapEx 가이던스 cut (NVIDIA·메모리·HDD thesis 모두 위협)
- OpenAI 파트너십 exclusivity 변경 (multiple 재평가)
- 소비자 BU (Windows·Xbox·Search) 지속 약화

## 모니터링 캘린더

- **Q4 FY26 실적** (2026-07-30 예정): Azure 가속 + CapEx + AI ARR + Copilot 좌석
- **Microsoft Build 2026** (5월): Maia 200 + Cobalt + Copilot 신기능
- **Q1 FY27 실적** (2026-10-29 예정): FY27 CapEx 정량 가이드
- **OpenAI structuring update** (2025 비영리 → 영리 전환 진행 중)

---

# 종합 판단 (macro layer component)

## 매트릭스

| 차원 | 평가 | 근거 |
|---|---|---|
| **AI 수요 측 needle-mover** | ★★★ | AI ARR $37B + CapEx $190B + RPO $627B 모두 빅테크 #1 |
| **10개사 thesis driver** | ★★★ | NVIDIA·SK·HBM·HDD·Intel·ARM 모두 #1 발주처 |
| **AI 사업부 강도** | ★★★ | Azure +40% 3분기 가속 + Copilot 20M+ + Foundry multi-model |
| **재무 건전성** | ★★★ | OPM 46.3%, RPO 2-3년 가시성 (단 GPM 5분기 하락) |
| **★ Macro layer single component 가치** | ★★★ | 4사 합산 시 anchor |

## 핵심 투자 포인트 3 (수요 측 driver 관점)

1. **★ AI 수요 측 needle-mover**: AI ARR $37B (+123%) + CY26 CapEx $190B + RPO $627B (+99%) = 빅테크 4사 #1. 9·10개사 thesis 모두의 driver (NVIDIA·SK·HBM·HDD·Intel·ARM).
2. **★ "Remain constrained at least through 2026"** (Amy Hood CFO) + **"Second half 2026 acceleration"** = AI 인프라 사이클 정점 미도래 가장 강한 시그널. RPO $627B = 매출 가시성 2-3년 sector best.
3. **★ Azure + Copilot + OpenAI + Maia 통합 strategy**: Azure +40% YoY 3분기 연속 가속 + M365 Copilot 20M+ 좌석 (Accenture 740K) + OpenAI 독점 + AI Foundry multi-model (Anthropic 추가) + Maia ASIC (Intel Foundry 18A) + Cobalt CPU (ARM Neoverse) = NVIDIA 의존도 분산 + 다각화 trifecta.

## 핵심 리스크 3

1. **Microsoft Cloud GPM 5분기 연속 하락** (69% → 66% → Q4 가이드 64%): AI 인프라 비용 흡수 risk + GitHub Copilot 6/1 usage-based pricing 전환. FY27 OpMargin 위협 가능.
2. **OpenAI 의존도** (49% economic interest): Foundry 다각화 진행이지만 단기 의존도 risk. OpenAI 파트너십 exclusivity 변경 시 multiple 재평가.
3. **소비자 BU 약세** (Windows·Xbox·Search -1% YoY 3분기 연속): 메모리 가격 + Windows 10 EOL 기저효과. 본 테마와 무관이지만 전체 성장 drag.

→ **종합 (macro layer)**: <span class="star">★★★ AI 수요 측 needle-mover + 9·10개사 thesis 모두의 #1 driver</span>. **통합 모드 macro layer single 종목 component**로 4사 통합 시 CapEx baseline + AI ARR trajectory + RPO 매출 가시성 anchor 역할.

---

# 향후 관찰 포인트

1. **Q4 FY26 실적 (2026-07-30)**: Azure +41%+ 가속 + CapEx $40B+ + AI ARR $50B+ 도달 여부
2. **CY26 CapEx $190B 페이스 검증** (분기당 ~$48B baseline)
3. **FY27 CapEx 정량 가이드** (Q1 FY27, 2026-10-29 예정) — "double-digit growth" 정량화
4. **Microsoft Cloud GPM 변곡** (5분기 연속 하락 멈출지) — Maia + Cobalt 양산 효과
5. **Maia 200 + Cobalt CPU 양산 확대** (NVIDIA 의존도 분산 가속)
6. **AI Foundry Anthropic 협력 deepening** (OpenAI 의존도 분산)
7. **M365 Copilot 25M+ 좌석 + Mega-deal 추가** (Accenture 740K 다음)
8. **GitHub Copilot 6/1 usage-based 전환 영향** (Cloud GPM 추가 압박)

---

## 부록: v1 changelog

**v1 (2026-06-21)**: 최초 작성 — 빅테크 frame (수요 측, macro layer single 종목 component)
- 9개사·NVIDIA와 다른 frame: AI 사업부 분석 + CAPEX trajectory + 10개사 thesis connection mapping
- ★ Q3 FY26 record + AI ARR $37B + RPO $627B + CY26 CapEx $190B 반영
- 10개사 발주 mapping 표 (NVIDIA·SK·삼성·Micron·AMD·Intel·ARM·SNDK·WDC·STX 모두 #1 발주)
- Maia + Cobalt 자체 chip strategy + AI Foundry multi-model 다각화 narrative
