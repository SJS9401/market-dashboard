---
ticker: "GOOGL"
company_name: Alphabet Inc.
country: US
theme_keyword: 에이전트AI
parent_industry: 빅테크 (수요 측)
role: macro_layer_component
trend_revenue_share: 35                # AI 직접 노출 (GCP + AI Solutions + Gemini App + AI Overviews)
ai_capex_FY26: 100                    # CY26 ~$100B (Q1 2026 $22B annualized $88B+ + 가속)
gcp_growth_Q1_2026: 63                # +63% YoY (11분기 만의 가속)
last_updated: 2026-06-21
auto_references:
  - 반도체_산업기초.md (2026-05-18)
  - 에이전트AI_테마분석.md (v4, 2026-05-26)
  - GOOGL_기업개요.md (v1.0, 2026-05-19)
  - 2026-Q1_GOOGL_리뷰.md (Q1 2026, 2026-04-29 발표)
  - 2026-Q2_GOOGL_팔로업.md (Q2 2026 예정)
  - 엔비디아_에이전트AI_기업분석.md (NVIDIA monopoly + TPU 위협 매핑)
  - 마이크로소프트_에이전트AI_기업분석.md (빅테크 peer)
analyst_reports_attached:
  - Alphabet Q1 2026 IR Press Release + Earnings Call Transcript
  - Sundar Pichai commentary
notes:
  - Alphabet 회계연도 = calendar year (1월~12월). Q1 2026 = 2026.01~03 (4/29 발표)
  - 본 분석 frame은 MSFT와 유사한 빅테크 frame (수요 측, macro layer component). 단 차별점은 ★ TPU 6세대 (Trillium) 자체 양산 성공 + Broadcom 위탁 + Anthropic $3B 투자 (OpenAI 대비)
  - Google이 ★ NVIDIA 의존도 가장 낮은 hyperscaler (TPU 자체 chip 6세대 가장 성숙)
---

# Google (Alphabet) 기업 분석 — 에이전트AI 테마 (★ 빅테크 frame, 수요 측)

> **본 분석 frame (★ MSFT 동일 빅테크 frame, 차별점은 TPU·Anthropic)**: Google은 본 테마의 **고객 (수요 측)** + ★ **TPU 6세대 (Trillium) 자체 양산 성공 = NVIDIA monopoly의 가장 강력한 alternative**. MSFT (OpenAI 독점 + Maia)와 차별: (a) **★ TPU 6세대 (Trillium) + 7세대 (Ironwood) 자체 양산** — Google 6년 자체 칩 trajectory의 정점 (b) **★ Broadcom 위탁 생산 (Broadcom 전체 매출의 ~30% 추정)** (c) **★ Anthropic $3B+ 투자 (vs MSFT-OpenAI)** — AI Foundation 양강 구도 (d) **★ Gemini 자체 모델 + DeepMind** = OpenAI 의존 없는 AI Foundation (e) **★ Axion ARM CPU + GCP** = NVIDIA 의존도 최저 빅테크. **★ Q1 2026 GCP $20.03B (+63% YoY) 11분기 만의 가속 + Backlog "nearly all-time high" + CY26 CapEx ~$100B + Gemini App 350M+ paid subscriptions**.

> **CapEx·매출 단위 기준**: USD billion (Alphabet 회계연도 = calendar year). Q1 2026 = 2026.01~03. AI ARR 직접 disclosure 미공개 → AI 사업부 매출 합산 추정 (GCP + AI Solutions + Gemini App + AI Overviews monetization).

---

## Executive Summary (5줄)

1. **위치**: 글로벌 Search 광고 #1 (90%+ 점유) + 글로벌 Cloud #3 (AWS·Azure 다음, 단 ★ 성장률 #1 +63%) + AI Foundation 자체 #2 (Gemini, OpenAI·Anthropic과 동급) + ★ **TPU 6세대 (Trillium) + 7세대 (Ironwood) 자체 양산 = hyperscaler ASIC 가장 성숙**. ★ Gemini App **350M+ paid subscriptions**.
2. **AI 사업부 구성**: Google Cloud (GCP) $20.03B Q1 2026 (+63% YoY 11분기 만의 가속) + Gemini App 350M+ paid subs + AI Overviews +19% YoY + Vertex AI + Workspace AI. ★ **AI ARR 추정 ~$30B+ (Q1 2026 annualized)** — MSFT $37B 다음 #2.
3. **★ Google의 차별 strategic angle**:
   - **★ TPU Trillium (v6) + Ironwood (v7)** = NVIDIA monopoly의 가장 강력한 alternative (Anthropic Claude 학습에 일부 사용)
   - **★ Broadcom 위탁 생산** — Broadcom 매출의 ~30% 추정 (Google 단일 deal)
   - **★ Anthropic $3B+ 투자** (vs MSFT-OpenAI) — AI Foundation 양강 구도
   - **★ Axion ARM CPU + Gemini 자체** = NVIDIA·OpenAI 의존도 최저 빅테크
4. **CapEx trajectory**: FY24 $52.5B → FY25 $75B → ★ **CY26 ~$100B+ (Q1 2026 $22B annualized $88B+ 추가 가속)**. MSFT $190B 대비 작지만 Google은 ★ **TPU 자체 chip + Broadcom 위탁으로 CapEx 효율성 우위**.
5. **종합 (macro layer)**: <span class="star">★★★ AI 수요 측 #2 + NVIDIA 의존도 최저 빅테크</span>. Broadcom thesis driver 단독 + Anthropic Foundation 양강. (a) Search 광고 vs AI Overviews monetization risk (b) DOJ antitrust (Search 분리 명령 항소심) (c) Network 광고 정체 -4%.

---

# 항목 1. 입력 정리 + Google 위치

## 1-1. 산업·테마 컨텍스트

- **반도체 산업기초**: Google은 수요 측 driver — 단 ★ TPU 자체 chip으로 NVIDIA 의존도 낮은 유일 빅테크
- **에이전트AI 테마 v4**: 17 segment 중 Google은 수요 driver + ★ **TPU Trillium·Ironwood 양산 성공으로 NVIDIA AI 가속기 segment에 위협 catalyst 제공**
- **NVIDIA 기업분석**: Google TPU는 NVIDIA monopoly 4대 위협 catalyst 중 #2 (Google TPU 6세대 가장 성숙)
- **MSFT 기업분석 (peer)**: MSFT는 OpenAI 독점 + Maia (Intel 18A) vs Google은 ★ TPU Trillium (Broadcom 위탁) + Gemini 자체 + Anthropic 투자 = 두 빅테크 strategic angle 정반대

## 1-2. Google의 위치 (수요 측 + TPU 자체 chip)

| Segment | 글로벌 위치 | 비고 |
|---|---|---|
| **Search 광고** | **글로벌 #1 (90%+)** | Q1 2026 +11% YoY (AI Overviews +19%) |
| **AI Cloud (GCP)** | **글로벌 #3 (AWS·Azure 다음)** | Q1 2026 GCP $20.03B (+63% YoY) — **11분기 만의 가속** |
| **★ AI Foundation (Gemini)** | **자체 #2 (OpenAI·Anthropic 동급)** | Gemini Pro·Ultra·Flash·Nano 다중 tier |
| **★ AI Foundation 투자 (Anthropic)** | **$3B+ 누적** | OpenAI ($13B MSFT) 다음 #2 투자 |
| **★ Gemini App** | **350M+ paid subscriptions** | M365 Copilot (MSFT 20M+) 대비 17x |
| **★ TPU (Trillium v6 + Ironwood v7)** | **★ hyperscaler ASIC 가장 성숙** | NVIDIA AI 가속기 점유 위협 #1 |
| **★ Broadcom 위탁 생산** | **★ Broadcom 매출 ~30% 추정** | Google 단일 deal |
| **★ Axion ARM CPU** | **자체 ARM Neoverse 양산** | Intel Xeon 잠식 |
| **CY26 CapEx** | **~$100B+** | MSFT $190B 대비 작지만 TPU 효율성 |
| **YouTube** | **글로벌 #1 동영상** | Q1 2026 +16% YoY |
| **Waymo (자율주행)** | Other Bets 단독 | 본 테마 외 (자율주행 별도) |

→ **단일 빅테크로 ★ NVIDIA 의존도 가장 낮은 hyperscaler** (TPU 6세대 + Anthropic + Gemini 자체).

## 1-3. 사업부 구성 (Q1 2026)

| Segment | Q1 2026 매출 | YoY | 본 테마 연결 | 비중 |
|---|---|---|---|---|
| **Google Services** | ~$77B | **+11%** | 부분 (AI Overviews + Gemini App + Workspace AI) | **78%** |
| Search + Other | ~$50B | +11% | ★ AI Overviews +19% | 51% |
| YouTube ads | ~$10B | +16% | YouTube AI features | 10% |
| Network ads | ~$7B | -4% | 정체 | 7% |
| Subscriptions (YouTube Premium·Google One) | ~$10B | +20%+ | Google One 350M+ subs | 10% |
| **Google Cloud (GCP + Workspace + AI Solutions)** | **$20.03B** | **★ +63% (11분기 만의 가속)** | ★ 본 테마 직접 (GCP + AI Solutions) | **20%** |
| Other Bets (Waymo) | ~$0.6B | — | 자율주행 (본 테마 외) | 0.6% |
| **Total** | **~$99B** | **+15%** | | 100% |

### 본 테마 직접 매출 노출
- **Google Cloud 20% × ~70%** (GCP AI Solutions + AI infrastructure, Workspace 일부)
- **Google Services 78% × ~20%** (AI Overviews + Gemini App + Workspace AI + Subscriptions AI)
- **순 본 테마 직접 노출 = 약 35%** (MSFT ~50% 대비 작음, 광고 사업 비중 큼)
- **★ Google Cloud $20B (+63% YoY)** = ★ AI 사업부 직접 driver
- **★ Backlog "nearly all-time high"** (Q1 2026 회사 코멘트) = 매출 가시성 추가

---

## ★ 2-0. 에이전트AI 테마 logical flow — 왜 Google이 부각받는가 (수요 측 + 자체 chip)

> **정성적 인과 사슬** (테마 v4 → Google 위치 — 수요 측 + NVIDIA 의존도 최저)

### 1단계: 에이전트 AI = 데이터·연산·메모리 폭증
- 에이전트 1건 = chat 1턴 대비 **토큰 20-30x**
- ★ **Sundar Pichai Q1 2026**: *"We're in a unique position with full-stack AI — TPU + Gemini + GCP + DeepMind 4-layer integration"*

### 2단계: AI 인프라 layer별 분담 — Google은 어디 위치?

| Layer | 9·10개사 (공급) | **Google (수요 측 + 자체 chip)** |
|---|---|---|
| Hot (HBM) | SK·삼성·Micron | **Google TPU에 HBM3E·HBM4 직접 발주** (Broadcom 통한 발주) |
| Warm (DRAM·SSD) | 메모리 3사 + SNDK·Solidigm | GCP DRAM·eSSD 직접 발주 |
| Warm-Cold (eSSD·HBF) | SNDK | GCP Vector DB·체크포인트 |
| Cold (HDD nearline) | WDC·Seagate | GCP cold storage 직접 발주 |
| Compute (CPU) | Intel·AMD·ARM 라이선시 | **★ Axion ARM CPU (자체) + EPYC + Xeon 혼합** |
| **★ Compute (GPU·AI)** | NVIDIA·AMD·ASIC | **★ TPU Trillium·Ironwood 자체 (NVIDIA 의존도 최저) + NVIDIA 일부 (GCP 고객용)** |
| **★ IP layer** | ARM + NVIDIA | **★ ARM Neoverse 라이선시 (Axion) + Gemini 자체 모델 (CUDA 의존 X)** |

→ **Google 위치: ★ NVIDIA 의존도 가장 낮은 빅테크 — TPU 자체 6세대 + Axion 자체 ARM + Gemini 자체 모델 풀스택**

### 3단계: 왜 Google이 본 테마에서 부각받는가? — 4가지 본질적 이유

1. **★ TPU 6세대 (Trillium) + 7세대 (Ironwood) 자체 양산** — Google 2016 TPU v1 → 10년 trajectory 정점. **hyperscaler ASIC 가장 성숙** = NVIDIA AI 가속기 점유 위협 #1
2. **★ GCP +63% YoY Q1 2026 (11분기 만의 가속)** + Backlog "nearly all-time high" = AWS·Azure 추격 가속화
3. **★ Anthropic $3B+ 투자 + Gemini 자체 모델** = OpenAI 의존 없는 AI Foundation 다축
4. **★ Broadcom 위탁 생산** — Broadcom 매출의 ~30% Google 단일 deal = ★ Broadcom thesis driver 단독

### 4단계: 왜 Google이 부각? — NVIDIA 의존도 최저 + TPU·Gemini·Anthropic 풀스택

- **★ TPU full trajectory** (v1 2016 → v7 Ironwood 2026): hyperscaler ASIC 6년 누적, AlphaGo·AlphaFold·Gemini 학습 모두 TPU
- **★ Anthropic 투자 $3B+** = Claude 사용처 GCP (NVIDIA GPU 대신 TPU 일부)
- **★ Gemini App 350M+ paid subscriptions** = MSFT M365 Copilot 20M+ 대비 **17x 규모**
- **★ DeepMind 자체 R&D** — AlphaFold·AlphaGo·Gemini 핵심
- **★ Sundar "compute constrained"** = Azure CFO와 동일 시그널 (수요 압도)

### 5단계: 본 분석 frame 결론 (수요 측 + 자체 chip + NVIDIA 의존도 최저)

**본 테마 수요 측 #2 + ★ NVIDIA monopoly 위협 catalyst 가장 강한 hyperscaler**. AI ARR 추정 ~$30B+ (MSFT $37B 다음 #2). CY26 CapEx ~$100B (MSFT $190B 대비 작지만 TPU 효율성 우위). **★ TPU + Gemini + Anthropic + Axion 풀스택 strategy** = NVIDIA·OpenAI·Intel 의존도 최저. **★ Broadcom 단독 thesis driver** (Broadcom 매출 ~30% Google). **통합 모드 macro layer에서 NVIDIA 위협 evidence의 핵심 component**.

---

# 항목 2. AI 사업부 + CAPEX + 10·11개사 발주 mapping — ★ 핵심

## 2-1. AI 사업부 분석 (GCP + Gemini + TPU)

### Google Cloud (GCP) — $20.03B Q1 2026 (+63% YoY)
- **★ 11분기 만의 가속** (Q1 2024 +29% 저점 → Q1 2026 +63%)
- AI Solutions segment 가속 (Anthropic + AI 스타트업 GCP 사용)
- ★ Backlog "nearly all-time high" (Sundar Q1 2026)
- Vertex AI + Gemini API + BigQuery + AI infrastructure
- 고객: Spotify, Snap, Wayfair, McDonald's, Walmart, PayPal, **★ Anthropic**

### Gemini (AI Foundation 자체)
- **Gemini App 350M+ paid subscriptions** (Q1 2026)
- Gemini Pro·Ultra·Flash·Nano 다중 tier
- AI Overviews +19% YoY (Search 직접 monetization)
- DeepMind 자체 R&D

### ★ TPU (Trillium v6 + Ironwood v7) — NVIDIA alternative #1
- **TPU 진화**: v1 (2016) → v2/v3/v4/v5 → v6 (Trillium 2024) → ★ v7 (Ironwood 2026)
- Google 자체 학습 (Gemini) + Anthropic 학습 (Claude)
- ★ **NVIDIA monopoly 4대 위협 catalyst 중 #2** (Google TPU 가장 성숙한 ASIC)

### Axion CPU (ARM Neoverse)
- Google 자체 ARM CPU (MSFT Cobalt와 동일 strategy)
- Intel Xeon 잠식의 일부

## 2-2. CAPEX trajectory 분해

| 분기/연 | CapEx ($B) | YoY | 비고 |
|---|---|---|---|
| FY22 | 31.5 | — | ChatGPT 쇼크 후 시작 |
| FY23 | 32.3 | +2% | Year of Efficiency |
| FY24 | 52.5 | +63% | ★ Gemini + AI Overviews launch |
| FY25 | 75.0 | +43% | AI 슈퍼사이클 진입 |
| **Q1 2026** | **~$22B** | **+40%+** | annualized ~$88B+ |
| **★ CY26 (가이던스)** | **~$100B+** | **+33%** | TPU + DC 확장 + Backlog 매출 |

### CapEx 구성
- **TPU 자체 양산 비중 큼** (NVIDIA GPU 발주 대비 낮음)
- **2/3 short-lived (TPU·Axion·EPYC GPU)**, 1/3 long-lived (DC·전력)
- ★ **CapEx 효율성**: TPU 자체 chip = NVIDIA GPU ($25-30K/unit) 대비 cost per FLOP 낮음

### MSFT 대비 CapEx 비교
- MSFT CY26 $190B vs Google CY26 ~$100B = MSFT 1.9x 큼
- 단 Google ★ TPU 효율성 = 실질 AI compute capacity는 격차 작음 가능성
- **★ Google의 CapEx 작은 이유 = NVIDIA GPU 발주 적음 + TPU 자체 양산**

## 2-3. ★ 10·11개사 thesis와 직접 connection mapping (Google 특별 angle)

### 발주 mapping (Google → 10·11개사)

| 종목 | Google 발주 형태 | 정량 추정 | 본 테마 driver 영향 |
|---|---|---|---|
| **NVIDIA (Blackwell·Rubin)** | GCP 고객용 일부 (자체 TPU 우선) | **~$5-10B/년 (CY26)** ★ MSFT $30-40B의 1/3-1/6 | NVIDIA DC 매출 ~3-5% (MSFT 대비 작음) |
| **★ Broadcom (TPU 위탁)** | **★ TPU 자체 chip 설계·생산 위탁** | **★ Broadcom 매출 ~30% 추정** | **★ Broadcom 단독 thesis driver** (Google deal) |
| SK하이닉스 (HBM) | TPU에 HBM 직접 + 일반 DRAM | TPU HBM 발주 (Broadcom 통한 간접) | SK HBM driver (NVIDIA + Google) |
| 삼성전자 (HBM·DRAM) | TPU HBM + GCP DRAM | 간접 + 직접 | 삼성 DRAM CAPA #1 driver |
| Micron (HBM·DDR5) | TPU HBM + GCP DRAM | 간접 + 직접 | Micron driver |
| **AMD (EPYC + MI300)** | GCP server CPU + 일부 MI300 | EPYC 일부 | AMD EPYC 점유 driver |
| **Intel (Xeon)** | GCP server CPU 일부 (잠식 중) | Xeon legacy | Intel Xeon legacy 매출 |
| **★ ARM (Axion CPU + TPU)** | **★ 자체 Axion + TPU 모두 ARM 기반** | ARM royalty 직접 | **★ ARM DC royalty 2x driver** |
| SanDisk (eSSD) | GCP storage tier | direct | SNDK NBM 일부 |
| WDC (HDD nearline) | GCP cold storage 직접 | Azure 다음 #2-3 hyperscaler | WDC nearline driver |
| Seagate (HDD nearline) | GCP cold storage | Mozaic 3+ qualified 5 CSP 일부 | STX nearline driver |
| **★ NVIDIA monopoly 위협** | **★ TPU = NVIDIA alternative 가장 성숙** | NVIDIA 80% → 75-78% 위협 | **★ NVIDIA 4대 위협 #2 (catalyst)** |

→ **Google 차별 특징**:
- ★ **NVIDIA 발주가 빅테크 중 가장 작음** (TPU 자체 우선)
- ★ **Broadcom 단독 driver** (TPU 위탁)
- ★ **ARM royalty driver** (Axion + TPU 모두 ARM)
- ★ **NVIDIA monopoly 위협 catalyst의 가장 강한 source**

## 2-4. ★ AI Foundation 다축 strategy (vs MSFT OpenAI 독점)

| Model | Google 위치 | 차별점 |
|---|---|---|
| **★ Gemini (자체)** | ★ Pro·Ultra·Flash·Nano 다중 tier, **350M+ paid subs** | OpenAI 의존 없음 |
| **★ Anthropic (Claude)** | ★ $3B+ 투자 (2023~), Anthropic GCP 사용 | Claude 사용처 = TPU |
| Llama·Mistral·Qwen | GCP에 open source 호스팅 | multi-model 옵션 |

→ **★ Google의 AI Foundation 차별점**:
- MSFT는 OpenAI 독점 ($13B+, 49% economic interest) → exclusivity 변경 risk
- ★ Google은 ★ 자체 Gemini + Anthropic 투자 + open source 다축 = **OpenAI 의존도 0**
- ★ Anthropic + Google = MSFT-OpenAI 양강 구도

---

# 항목 3. 재무 분석

## 3-1. 실적 추이 — 12년 매출·OPM·CapEx (AI 슈퍼사이클 변곡점)

| FY | 매출 ($B) | YoY | OPM | CapEx ($B) | 사이클 |
|---|---|---|---|---|---|
| FY14 | 66.0 | — | 25.0% | 11.0 | baseline |
| FY18 | 136.8 | +23% | 20.1% | 25.1 | EU 벌금 저점 |
| FY21 | 257.6 | +41% | 30.6% | 24.6 | 1차 정점 (COVID 광고) |
| FY22 | 282.8 | +10% | 26.5% | 31.5 | ChatGPT 쇼크 (압축) |
| FY23 | 307.4 | +9% | 27.4% | 32.3 | Year of Efficiency |
| FY24 | 350.0 | +14% | 32.1% | 52.5 | ★ Gemini + AI Overviews launch |
| **FY25** | **402.8** | **+15%** | **~33%** | **75.0** | **★ TPU + Gemini 슈퍼사이클** |
| **Q1 2026 (분기)** | **~99** | **+15%** | — | **~22** | **★ GCP +63% 11분기 만 가속** |
| **CY26 (E)** | — | — | — | **~$100B+** | **★ TPU + DC 확장** |

## 3-2. AI 사업부 PQC 분해

| 차원 | GCP (AI infra) | Gemini App | AI Overviews | 비고 |
|---|---|---|---|---|
| **P (단가)** | 컴퓨트·token 기반 | $20/월 (Pro·Ultra) | 광고 클릭 | enterprise |
| **Q (출하)** | ★ +63% YoY 가속 | 350M+ paid subs | Search 통합 | Cloud 폭증 |
| **C (원가)** | ★ TPU 효율성 (NVIDIA GPU 대비 cost 낮음) | TPU + DC | Search 인프라 | NVIDIA 대비 우위 |
| **매출 (Q1 2026)** | $20.03B (+63%) | ~$5B+ 추정 | Search +19% AI Overviews | — |
| **마진** | Cloud OPM 점진 회복 (FY25 ~14%, FY24 8% 대비) | — | Search OPM 안정 (~50%) | TPU 효율 |

## 3-3. 재무 건전성 + 자본 환원

- **부채 매우 안정** (현금 $100B+ vs 부채 $30B)
- **OCF FY25 $147.5B (사상 최대)** / FCF $72.5B (CapEx 폭증으로 정체)
- ★ **2024 첫 배당 시작** + 20:1 액면분할
- 자사주 매입: Q1 2026 $0 (★ 일시 중단 — CapEx 우선 시그널)
- ★ **AI CapEx 우선** = NVIDIA·MSFT와 동일 패턴

## 3-4. 수익성 트렌드

- **OPM 추이**: FY18 20.1% (EU 벌금 저점) → FY21 30.6% (정점) → FY22 26.5% (압축) → FY25 ~33% (회복 + AI 슈퍼사이클)
- **Google Cloud OPM**: FY24 8% → FY25 ~14% (★ 흑자 전환 + 확대)
- **Search OPM**: 안정 50%+ (AI Overviews monetization로 +) 
- **★ Cloud OPM 회복 trajectory** = AI 사업부 수익화 정량 입증

---

# 항목 4. 성장성 분석

## 4-1. 과거 성장률

| 기간 | 매출 CAGR |
|---|---|
| 3년 (FY22→FY25) | +12% |
| 5년 (FY20→FY25) | +17% |
| 12년 (FY13→FY25) | +18% |

→ MSFT +12.4% 대비 약간 우위. AI 슈퍼사이클 진입 후 GCP +63% 가속으로 추가 가속 가능.

## 4-2. 향후 성장 가시성

| 차원 | 전망 | 근거 |
|---|---|---|
| **P 전망** | GCP compute 안정, Gemini $20/월 유지 | TPU 효율성 |
| **Q 전망** | ★ GCP +63% → +50%+ 지속 가능 | Backlog "nearly all-time high" |
| **C 전망** | ★ TPU 효율성으로 NVIDIA 의존 빅테크 대비 우위 | CapEx 효율 |
| **→ 매출 성장** | FY26 ~$460B (+15%) / FY27 ~$520B (+13%) | GCP 가속 + Search AI monetization |
| **→ 마진** | OPM 33-35% 박스 + Cloud OPM 15%+ | Cloud 흑자 확대 |

### 성장 지속성 구조적 근거 + 저해 risk
**구조적 +**:
- ★ GCP +63% (11분기 만의 가속)
- ★ Gemini App 350M+ paid subs
- ★ TPU 효율성 (NVIDIA GPU 의존도 최저)
- ★ Anthropic + Gemini 다축
- ★ Backlog "nearly all-time high"

**저해 risk**:
- ★ **DOJ Antitrust** (Search 분리 명령 항소심) — multiple cap risk
- ★ Search 광고 vs AI Overviews monetization 전환 risk
- Network ads -4% YoY 정체
- AI CapEx 폭증으로 FCF 압박

## 4-3. 빅테크 4사 비교 (★ macro layer baseline)

| 빅테크 | 매출 CAGR (3년) | AI ARR | CY26 CapEx | strategic angle |
|---|---|---|---|---|
| MSFT | +12.4% | $37B (+123%) | $190B | OpenAI 독점 + Maia + Cobalt |
| **Google** | **+12%** | **~$30B+ 추정** | **~$100B** | **★ TPU + Gemini + Anthropic + Broadcom + Axion (NVIDIA 의존도 최저)** |
| AWS | +10% | ~$25B+ | $195B | Trainium 2 + Anthropic $11B + Graviton |
| Meta | +20% | $20B+ | $135B | Llama + MTIA + AMD MI450 6GW |

→ Google CapEx 작지만 ★ **TPU 효율성 + NVIDIA 의존도 최저** = 다른 strategic angle.

---

# 항목 5. 통합 모드 입력용 Fact 정리

| 항목 | 정리 |
|---|---|
| **★ CY26 CapEx** | **~$100B+ (Q1 2026 $22B, annualized $88B+)** |
| **★ AI ARR 추정** | **~$30B+ (MSFT $37B 다음 #2)** — Gemini App + GCP AI + Vertex |
| **★ GCP 성장** | **+63% YoY (Q1 2026)** — 11분기 만의 가속 |
| **★ Backlog** | **"nearly all-time high"** (Sundar Q1 2026) |
| Gemini App | **350M+ paid subscriptions** |
| AI Foundation | Gemini (자체) + ★ **Anthropic $3B+ 투자** + open source 다축 |
| **★ TPU 자체 chip** | **★ Trillium (v6) + Ironwood (v7), Broadcom 위탁** |
| **★ Broadcom 단독 deal** | **★ Broadcom 매출 ~30% Google deal** |
| Axion CPU (ARM Neoverse) | 자체 ARM chip, TSMC 양산 |
| NVIDIA 발주 추정 | $5-10B/년 (MSFT $30-40B의 1/3-1/6) — ★ NVIDIA 의존도 최저 |
| HBM·HDD 발주 | TPU에 HBM 직접 + GCP cold storage |
| Cloud OPM | FY24 8% → FY25 ~14% (흑자 확대) |
| 시총 | ~$2.2T (2026-06) |
| **★ NVIDIA monopoly 위협 catalyst** | **★ TPU 6세대 = NVIDIA alternative 가장 성숙** |

---

# 항목 6. 구조적 트리거 모니터링

## 상방 트리거

- ★ GCP +65%+ YoY 가속 지속 (Q2 2026)
- ★ CY26 CapEx $100B+ 페이스 유지 + FY27 가이드 상향
- ★ **TPU 7세대 Ironwood 본격 양산** (2026 H2)
- ★ Anthropic Claude 추가 사용처 확대 (GCP)
- ★ Gemini App 500M+ paid subs (Q4 2026)
- Cloud OPM 18%+ 도달

## 하방 트리거

- ★ **DOJ Antitrust 판결** (Search 분리 명령) — 분리 strucutre 변경 risk
- GCP +50% 이하 둔화
- AI Overviews monetization risk (Search 광고 cannibalization)
- TPU 7세대 yield issue
- AI CapEx 가이던스 cut

## 모니터링 캘린더

- **Q2 2026 실적** (2026-07-22 예정): GCP 가속 + CapEx + Gemini subs
- **Google Cloud Next 2026** (4월): TPU + Gemini 발표
- **DOJ 판결 진행** (Search 분리 명령 항소심)
- **Anthropic 추가 deal 발표**

---

# 종합 판단 (macro layer component)

## 매트릭스

| 차원 | 평가 | 근거 |
|---|---|---|
| **AI 수요 측 #2** | ★★★ | AI ARR ~$30B+, GCP +63% 가속 |
| **★ NVIDIA 의존도 최저** | ★★★ | TPU 자체 chip + Gemini 자체 + Anthropic |
| **AI 사업부 강도** | ★★★ | GCP 11분기 만의 가속 + Gemini 350M+ paid |
| **재무 건전성** | ★★★ | OCF $147B, OPM 33%, Cloud 흑자 확대 |
| **★ Macro layer 가치** | ★★★ | TPU = NVIDIA monopoly 위협 evidence + Broadcom thesis driver |

## 핵심 투자 포인트 3

1. **★ NVIDIA 의존도 가장 낮은 hyperscaler + TPU 6세대 자체 양산**: Google 2016 TPU v1 → 2026 Trillium·Ironwood 10년 trajectory. NVIDIA monopoly 4대 위협 catalyst 중 #2. ★ Broadcom 매출 ~30% Google deal = Broadcom thesis driver 단독.
2. **★ GCP +63% YoY (11분기 만의 가속) + Backlog "nearly all-time high"**: Q1 2026 $20B, AWS·Azure 추격 가속. Cloud OPM 흑자 확대 (FY24 8% → FY25 14%) = AI 사업부 수익화 정량 입증.
3. **★ Gemini App 350M+ paid subscriptions + Anthropic $3B+ 투자 + Gemini 자체**: MSFT-OpenAI 양강 구도. OpenAI 의존 없는 AI Foundation 다축. ★ Anthropic Claude 사용처 = GCP TPU.

## 핵심 리스크 3

1. **★ DOJ Antitrust (Search 분리 명령)**: 항소심 진행 중. 분리 strucutre 변경 시 multiple cap risk + Search 광고 model 변경 가능.
2. **Search 광고 vs AI Overviews monetization 전환 risk**: AI Overviews +19% YoY이지만 ★ Search 광고 cannibalization risk (전환 시 매출 영향 불확실).
3. **Network ads -4% YoY 정체 + AI CapEx 폭증 FCF 압박**: Q1 2026 자사주 매입 $0 = CapEx 우선 시그널, FCF margin 압박.

→ **종합 (macro layer)**: <span class="star">★★★ AI 수요 측 #2 + ★ NVIDIA 의존도 최저 빅테크 + Broadcom thesis 단독 driver</span>. **통합 모드 macro layer에서 NVIDIA 위협 evidence + TPU·Broadcom·Anthropic 풀스택 alternative narrative의 핵심 component**.

---

# 향후 관찰 포인트

1. **Q2 2026 실적** (2026-07-22): GCP +65%+ 가속 + Gemini paid subs 400M+ + Backlog 증가
2. **TPU 7세대 Ironwood 본격 양산** (2026 H2) — Broadcom 매출 driver
3. **DOJ Search 분리 명령 판결** (항소심)
4. **CY26 CapEx $100B+ 페이스 검증** + FY27 가이드
5. **Anthropic 추가 GCP 사용 deal**
6. **Cloud OPM 18%+ 도달 시점**
7. **AI Overviews → Search 광고 monetization 전환 trajectory**
8. **Gemini Pro 3·Ultra 출시 + multimodal 가속**

---

## 부록: v1 changelog

**v1 (2026-06-21)**: 최초 작성 — 빅테크 frame (Google 차별 angle: TPU·Anthropic·NVIDIA 의존도 최저)
- MSFT와 동일 빅테크 frame이지만 ★ TPU + Gemini + Anthropic + Broadcom + Axion 차별 narrative 강조
- Q1 2026 GCP +63% (11분기 만의 가속) + Gemini 350M+ subs + Backlog "all-time high" 반영
- NVIDIA monopoly 4대 위협 catalyst 중 #2 (TPU 가장 성숙한 ASIC) 매핑
- Broadcom 매출 ~30% Google 단독 deal = Broadcom thesis driver 강조
