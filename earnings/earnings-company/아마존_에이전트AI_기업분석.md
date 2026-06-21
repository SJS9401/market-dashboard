---
ticker: "AMZN"
company_name: Amazon.com, Inc. (AWS 포함)
country: US
theme_keyword: 에이전트AI
parent_industry: 빅테크 (수요 측, AWS-driven)
role: macro_layer_component
trend_revenue_share: 25                # AI 직접 노출 (AWS 18% + Anthropic + 광고 일부 + Alexa AI)
ai_capex_FY26: 195                    # CY26 ~$195B (TTM Q1 2026 $147B → 가속, 빅테크 #1)
aws_growth_Q1_2026: 28                # AWS +28% YoY (15분기 최고)
last_updated: 2026-06-21
auto_references:
  - 반도체_산업기초.md (2026-05-18)
  - 에이전트AI_테마분석.md (v4, 2026-05-26)
  - AMZN_기업개요.md (v1.2, 2026-05-19)
  - 2026-Q1_AMZN_리뷰.md (Q1 2026, 2026-04-29 발표)
  - 2026-Q2_AMZN_팔로업.md (Q2 2026 예정)
  - 엔비디아_에이전트AI_기업분석.md (NVIDIA monopoly + Trainium 위협)
  - 마이크로소프트_에이전트AI_기업분석.md (빅테크 peer)
  - 구글_에이전트AI_기업분석.md (빅테크 peer + Anthropic 양면 투자)
analyst_reports_attached:
  - AMZN Q1 2026 IR Earnings Release + Supplemental Financial Information
  - Andy Jassy commentary
notes:
  - Amazon 회계연도 = calendar year. Q1 2026 = 2026.01~03 (4/29 발표)
  - 본 분석 frame은 MSFT·Google과 동일 빅테크 frame. 단 ★ Amazon 전체 multi-segment (Stores + AWS + Ads) 중 AWS만 본 테마 직접. AWS는 Cloud 절대 #1 ($137B TTM Q1 2026)
  - 핵심 차별: ★ Cloud 절대 #1 + Anthropic $8B (Google 양면 투자) + ★ OpenAI 2GW Trainium 계약 신규 (MSFT 독점 깨는 evidence) + Graviton (가장 성숙한 ARM 자체)
---

# Amazon (AWS 포함) 기업 분석 — 에이전트AI 테마 (★ 빅테크 frame, 수요 측)

> **본 분석 frame (★ MSFT·Google과 동일 빅테크 frame, 차별점은 Cloud 절대 #1 + Anthropic·OpenAI 다축)**: Amazon은 본 테마의 **고객 (수요 측, AWS-driven)**. ★ **AWS = 글로벌 Cloud 절대 #1 ($137B TTM vs Azure $95B vs GCP $80B)**. MSFT (OpenAI 독점)·Google (TPU + Anthropic)과 차별: (a) ★ **Cloud 절대 #1 매출** = 9·10개사 thesis 수요 측 driver 단연 최대 (b) ★ **Anthropic 누적 $8B 투자 (Google과 양면 투자자)** — Claude 학습 Trainium (c) ★ **OpenAI 2GW Trainium 계약 (Q1 2026 신규)** — ★ MSFT-OpenAI 독점 깨는 evidence (d) ★ **Graviton (자체 ARM CPU)** = MSFT Cobalt·Google Axion보다 trajectory 길음, 가장 성숙 (e) ★ **Trainium 2 + Inferentia 2 양산** + Anthropic·OpenAI Foundation 양면 사용. **★ Q1 2026 AWS +28% YoY (15분기 최고) + CapEx TTM $147B (+67% YoY 빅테크 #1) + Anthropic 평가이익 $16.8B (Q1 일회성) + AWS TTM OPM 35.2%**.

> **CapEx·매출 단위 기준**: USD billion (Amazon 회계연도 = calendar year). Q1 2026 = 2026.01~03. AWS는 별도 segment disclosure (AWS TTM Q1 2026 $137.05B / OPM 35.2%).

---

## Executive Summary (5줄)

1. **위치**: ★ **AWS = 글로벌 Cloud 절대 #1** ($137B TTM, Azure $95B / GCP $80B 압도) + 전 세계 최대 e-commerce + 광고 (TTM $70B+, Google·Meta 다음 #3). ★ **Q1 2026 매출 $181.5B (+17%) + AWS +28% (15분기 최고 가속) + Anthropic 평가차익 $16.8B (Q1 일회성) + OpenAI 2GW Trainium deal (신규)**.
2. **AI 사업부 구성**: AWS (AI infrastructure + Bedrock + SageMaker + Q + Nova) + ★ Anthropic Claude (★ $8B 투자, Claude 학습 Trainium) + ★ OpenAI 2GW Trainium (Q1 2026 신규 deal) + Amazon Nova (자체 모델) + Alexa AI (Echo 디바이스 통합).
3. **★ AWS 차별 strategic angle**:
   - **★ Cloud 절대 #1 매출** ($137B vs Azure $95B / GCP $80B) — 9·10개사 thesis 수요 측 driver 단연 최대
   - **★ Anthropic $8B + OpenAI 2GW** = AI Foundation 양면 (MSFT 독점·Google 단일 대비 가장 다축)
   - **★ Trainium 2 + Inferentia 2 자체 ASIC** — Anthropic Claude 학습 + OpenAI 2GW 신규 (vs NVIDIA 우위 시작)
   - **★ Graviton (자체 ARM CPU) = MSFT Cobalt·Google Axion 대비 trajectory 길음**, 가장 성숙
   - Trainium 백로그 $225B+ (NVIDIA 4대 위협 catalyst 중 #3 — Google TPU 다음)
4. **CapEx trajectory**: ★ **CapEx TTM $147B (+67% YoY 빅테크 #1)**. ★ FY26 ~$195B (가이던스, MSFT $190B + Google $100B 위). 단 AWS TTM OPM 35.2% (전년 37.5% -2.3%pt = AI 인프라 비용 흡수 진행).
5. **종합 (macro layer)**: <span class="star">★★★ AI 수요 측 #1-2 (Cloud 절대 #1 + CapEx 빅테크 #1)</span>. (a) AWS OPM 압박 (35.2% → 30%대 가능성) (b) Trainium 2 yield/ramp risk (c) e-commerce 사업 cycle (인프라 CapEx 부담). 단 ★ Anthropic·OpenAI 양면 + Graviton + Trainium = MSFT-OpenAI 독점 깨는 가장 강한 evidence.

---

# 항목 1. 입력 정리 + AWS·Amazon 위치

## 1-1. 산업·테마 컨텍스트

- **반도체 산업기초**: AMZN(AWS)은 수요 측 driver — ★ **Cloud 절대 #1**이라 9·10개사 thesis 수요 측 driver 단연 최대
- **에이전트AI 테마 v4**: AWS는 수요 driver + ★ **Trainium 2 + Inferentia 2 자체 ASIC으로 NVIDIA 위협 + Anthropic Claude 학습 deal**
- **NVIDIA 기업분석**: AWS Trainium = NVIDIA monopoly 4대 위협 catalyst 중 #3 (Google TPU 다음)
- **MSFT 기업분석 (peer)**: MSFT OpenAI 독점 vs ★ **AWS Anthropic ($8B) + OpenAI 2GW (Q1 2026 신규)** = MSFT 독점 깨는 evidence
- **Google 기업분석 (peer)**: Google Anthropic $3B vs ★ **AWS Anthropic $8B (2.7x)** = Anthropic 최대 투자자

## 1-2. AWS·Amazon 위치 (Cloud 절대 #1 + 다축 AI Foundation)

| Segment | 글로벌 위치 | 비고 |
|---|---|---|
| **★ AWS (Cloud)** | **★ 글로벌 절대 #1** | ★ $137B TTM Q1 2026 (Azure $95B / GCP $80B 압도) |
| **★ AWS 성장** | **★ Q1 2026 +28% YoY (15분기 최고)** | 5분기 연속 가속 |
| **★ AI Foundation 투자 (Anthropic)** | **★ $8B 누적 (Google $3B 대비 2.7x)** | Claude 학습 = Trainium |
| **★ OpenAI 2GW Trainium 계약** | **★ Q1 2026 신규 deal** | ★ MSFT 독점 깨는 evidence |
| **★ Trainium 2 + Inferentia 2** | **자체 ASIC, GA (2024)** | Anthropic Claude + OpenAI 학습 |
| **★ Graviton (ARM Neoverse)** | **★ 가장 성숙한 자체 ARM CPU** | AWS 인스턴스 50%+ ARM |
| **Amazon Nova (자체 모델)** | 자체 multimodal | Bedrock 통합 |
| **CY26 CapEx (TTM)** | **★ $147B (+67% YoY 빅테크 #1)** | FY26 가이던스 ~$195B |
| e-commerce | 글로벌 #1 | Stores 79% 매출 비중 |
| 광고 (Advertising) | ★ 글로벌 #3 (Google·Meta 다음) | TTM $70B+ |
| Alexa·Echo | 글로벌 #1 voice assistant | AI 통합 가속 |

→ **★ AWS 단일로 본 테마 수요 측 driver 단연 최대 (Cloud 매출·CapEx 빅테크 #1)**.

## 1-3. 사업부 구성 (Q1 2026)

| Segment | Q1 2026 매출 | YoY | 본 테마 연결 | 비중 |
|---|---|---|---|---|
| **★ AWS** | **$29.27B (annualized ~$117B)** | **★ +28% YoY (15분기 최고)** | ★ 본 테마 직접 (AI infra + Bedrock + Trainium) | **16%** (TTM 18%) |
| North America Stores | ~$93B | +12% | 부분 (광고 + Alexa AI) | 51% |
| International Stores | ~$36B | +10% | 부분 | 20% |
| Advertising (별도 분리, 추정) | ~$15B | +20% | 부분 (AI 광고 타겟팅) | 8% |
| Other (Subs·Physical·Devices) | ~$8B | — | Alexa·Echo + Devices | 5% |
| **Total** | **~$181.5B** | **+17%** | | 100% |

### 본 테마 직접 매출 노출
- **AWS 16% × 100%** (Cloud + AI infra 모두 본 테마)
- **Stores·Ads 79% × ~10%** (광고 AI 타겟팅 + Alexa AI)
- **순 본 테마 직접 노출 = 약 25%** (MSFT 50% / Google 35% 대비 작음, e-commerce 비중 큼)
- **★ AWS TTM $137B (+23% YoY)** = ★ Cloud 절대 #1 매출
- **★ AWS OP 비중 ~60%** (매출 18% 대비 3.3x leverage) = AWS가 P&L driver

---

## ★ 2-0. 에이전트AI 테마 logical flow — 왜 AWS가 부각받는가 (수요 측 + Cloud 절대 #1)

> **정성적 인과 사슬** (테마 v4 → AWS 위치 — 수요 측 + Cloud 절대 #1 + Foundation 다축)

### 1단계: 에이전트 AI = 데이터·연산·메모리 폭증
- 에이전트 1건 = chat 1턴 대비 **토큰 20-30x**
- ★ **Andy Jassy Q1 2026**: *"AI represents the largest opportunity I've seen since cloud — we're investing in capacity and Trainium for the next decade"*

### 2단계: AI 인프라 layer별 분담 — AWS는 어디 위치?

| Layer | 9·10개사 (공급) | **AWS (수요 측 + Cloud 절대 #1)** |
|---|---|---|
| Hot (HBM) | SK·삼성·Micron | ★ AWS Trainium에 HBM 직접 발주 + AWS-hosted NVIDIA GPU HBM |
| Warm (DRAM·SSD) | 메모리 3사 + SNDK·Solidigm | ★ AWS 글로벌 #1 Cloud DRAM·eSSD 최대 발주 (단일 빅테크 #1) |
| Warm-Cold (eSSD·HBF) | SNDK | AWS S3·Glacier Vector DB |
| Cold (HDD nearline) | WDC·Seagate | ★ AWS S3 Glacier exabyte data store 최대 (글로벌 #1) |
| Compute (CPU) | Intel·AMD·ARM | **★ Graviton ARM (가장 성숙한 자체) + EPYC + Xeon** |
| **★ Compute (GPU·AI)** | NVIDIA·AMD·ASIC | **★ Trainium 2 + Inferentia 2 자체 + NVIDIA GPU (AWS-hosted 최대) + AMD MI300 일부** |
| IP layer | ARM + NVIDIA | ★ ARM Neoverse 라이선시 (Graviton) + AI Foundation 다축 |

→ **AWS 위치: ★ Cloud 절대 #1 + Foundation 다축 (Anthropic·OpenAI·Nova) + Trainium·Graviton 자체 = 빅테크 #1 수요 측 driver**

### 3단계: 왜 AWS가 본 테마에서 부각받는가? — 5가지 본질적 이유

1. **★ Cloud 절대 #1 매출 ($137B TTM)** = MSFT Azure ($95B) · Google GCP ($80B) 압도 → 9·10개사 thesis 수요 측 driver 단연 최대
2. **★ AWS +28% YoY (15분기 최고 가속)** = MSFT Azure +40% / Google GCP +63% 동기화 사이클이지만 절대 매출 base가 압도적
3. **★ Anthropic 누적 $8B + OpenAI 2GW Trainium deal (Q1 2026 신규)** = AI Foundation 양면 다축 (MSFT 독점·Google 단일 대비)
4. **★ Trainium 2 + Inferentia 2 자체 ASIC** = NVIDIA monopoly 4대 위협 catalyst 중 #3 (Anthropic Claude 학습 + OpenAI 2GW 사용)
5. **★ Graviton ARM CPU (가장 성숙)** = MSFT Cobalt·Google Axion 대비 trajectory 길음, AWS 인스턴스 50%+ ARM

### 4단계: 왜 AWS가 부각? — Cloud 절대 #1 + AI Foundation 양면 + 자체 ASIC

- **★ AWS Cloud 매출 $137B = MSFT·Google 합과 동급** ($95B + $80B = $175B)
- **★ Anthropic $8B (Google $3B의 2.7x) + OpenAI 2GW Trainium 신규**: AI Foundation 양면 + MSFT-OpenAI 독점 깨는 evidence
- **★ Trainium 2 + Inferentia 2 + Graviton 풀스택 자체 ASIC**: NVIDIA 의존도 분산 중간 수준
- **★ CapEx TTM $147B (+67% YoY 빅테크 #1)** = AI 인프라 사이클 정점 미도래 정량
- **★ Anthropic 평가이익 $16.8B (Q1 일회성)** = NVIDIA의 Equity 평가차익 $15.9B와 동급 = AI ecosystem 투자자 검증

### 5단계: 본 분석 frame 결론

**본 테마 수요 측 #1-2 + ★ Cloud 절대 #1 + AI Foundation 양면 다축**. AI ARR 추정 ~$25B+ (MSFT $37B / Google $30B+ 다음 #3). CY26 CapEx ~$195B = ★ 빅테크 #1. ★ **OpenAI 2GW Trainium 계약 (Q1 2026 신규) = MSFT-OpenAI 독점 깨는 가장 강한 evidence**. **통합 모드 macro layer에서 Cloud 절대 #1 매출 baseline + AI Foundation 다축 evidence**.

---

# 항목 2. AI 사업부 + CAPEX + 10·11개사 발주 mapping — ★ 핵심

## 2-1. AI 사업부 분석 (AWS + Bedrock + Trainium + Graviton)

### AWS — Cloud 절대 #1 ($137B TTM Q1 2026)
- ★ **AWS +28% YoY (Q1 2026, 15분기 최고 가속)** — 5분기 연속 가속
- AWS TTM OPM 35.2% (전년 37.5% -2.3%pt = AI 인프라 비용 흡수)
- **고객**: 글로벌 enterprise 전 영역. ★ **Anthropic (Claude 학습)** + **OpenAI (2GW Trainium)** + Apple·Netflix·NASDAQ·기타

### Anthropic 파트너십 ($8B 누적 투자)
- 2023 $4B 1차 + 2024 $4B 2차 = **누적 $8B (Google $3B 대비 2.7x)**
- Anthropic Claude 학습 = ★ **Trainium 사용** (NVIDIA GPU 대신)
- Q1 2026 Anthropic 평가차익 $16.8B (일회성, OCI 반영)

### ★ OpenAI 2GW Trainium 계약 (Q1 2026 신규)
- ★ **MSFT 독점 깨는 evidence** — OpenAI가 AWS Trainium도 사용 시작
- MSFT-OpenAI 49% economic interest 유지하면서 인프라 다각화
- AWS 입장에서는 ★ **MSFT 독점 깨는 가장 강한 시그널**

### ★ Trainium 2 + Inferentia 2 자체 ASIC
- ★ **Trainium 2 GA (2024)** — Anthropic Claude 학습 + 신규 OpenAI 2GW
- Inferentia 2 — 추론 가속
- ★ **Trainium 백로그 $225B+** (테마 v4 reference)
- ★ NVIDIA monopoly 4대 위협 catalyst 중 #3 (Google TPU 다음)

### ★ Graviton (자체 ARM CPU)
- **가장 성숙한 자체 ARM CPU** (MSFT Cobalt·Google Axion 대비 trajectory 길음)
- AWS 인스턴스 50%+ ARM 사용
- ARM Neoverse 기반 = ARM royalty driver

### Amazon Nova (자체 multimodal 모델)
- Bedrock 통합 — AI Foundation 다각화

### Bedrock (AI Platform)
- Anthropic Claude + Amazon Nova + Meta Llama + Mistral + Cohere + AI21
- ★ MSFT Foundry와 유사한 multi-model 전략

## 2-2. CAPEX trajectory 분해 (★ macro layer 핵심)

| 분기/연 | CapEx ($B) | YoY | 비고 |
|---|---|---|---|
| FY22 | 63.6 | — | 팬데믹 capex 후 |
| FY23 | 52.7 | -17% | Year of Efficiency |
| FY24 | 77.7 | +47% | AWS AI 진입 |
| FY25 | 105.0 | +35% | AI 슈퍼사이클 |
| **TTM Q1 2026** | **$147.30B** | **★ +67% YoY** | ★ **빅테크 #1** |
| **★ CY26 (가이던스)** | **~$195B** | **+30%** | MSFT $190B + Google $100B 위 |

### CapEx 구성
- **AWS-driven CapEx** (e-commerce fulfillment보다 AWS 데이터센터 비중 큼)
- 2/3 short-lived (NVIDIA GPU + Trainium·Inferentia + Graviton + EPYC)
- 1/3 long-lived (DC + 전력)
- **★ NVIDIA GPU 발주 매우 큼** (AWS-hosted NVIDIA 인스턴스 압도적 #1)

### MSFT·Google 대비 CapEx 비교
- MSFT $190B / Google $100B / **★ AWS $195B (빅테크 #1)** / Meta $135B
- AWS는 ★ **Cloud 절대 #1 매출 base + AI 인프라 폭증** 양면 = CapEx 규모 최대

## 2-3. ★ 10·11개사 thesis와 직접 connection mapping (AWS 특별 angle)

### 발주 mapping (AWS → 10·11개사)

| 종목 | AWS 발주 형태 | 정량 추정 | 본 테마 driver 영향 |
|---|---|---|---|
| **★ NVIDIA (Blackwell·Rubin)** | ★ AWS-hosted NVIDIA 인스턴스 #1 hyperscaler | **~$30-40B/년** ★ MSFT 동급 | NVIDIA DC 매출 ~15-20% (MSFT 동급) |
| **★ Anthropic (Claude)** | **★ $8B 투자 + Trainium 학습** | Anthropic 최대 투자자 | Anthropic Claude → AWS Trainium |
| **★ OpenAI (Q1 2026 신규)** | **★ 2GW Trainium 계약** | OpenAI MSFT 외 신규 deal | MSFT 독점 깨는 evidence |
| ★ Broadcom (Trainium 위탁?) | ★ Trainium 일부 설계 위탁 가능성 | Google TPU $30%과 별도 | 추가 Broadcom 매출 driver |
| SK하이닉스 (HBM) | Trainium·Inferentia HBM + AWS-hosted NVIDIA HBM | 간접 + 직접 | SK HBM driver |
| 삼성전자 (HBM·DRAM) | Trainium HBM + AWS DRAM | 간접 + 직접 | 삼성 DRAM driver |
| Micron (HBM·DDR5) | Trainium HBM + AWS DRAM | 간접 + 직접 | Micron driver |
| **AMD (EPYC + MI300)** | EPYC AWS 인스턴스 + MI300 일부 | EPYC + MI300 | AMD EPYC + MI300 driver |
| Intel (Xeon) | AWS server CPU 일부 (점진 잠식) | Xeon legacy | Intel legacy |
| **★ ARM (Graviton)** | **★ Graviton = 가장 성숙한 자체 ARM CPU** | AWS 인스턴스 50%+ ARM | **★ ARM DC royalty 최대 driver** |
| SanDisk (eSSD) | AWS S3 storage tier | direct | SNDK NBM 일부 |
| **★ WDC (HDD nearline)** | **★ AWS S3 Glacier exabyte data store 최대** | AWS Cloud #1 | WDC nearline 절대 driver |
| **★ Seagate (HDD nearline)** | **★ AWS S3 cold storage** | Mozaic 3+ qualified 5 CSP 일부 | STX nearline driver |
| **★ NVIDIA monopoly 위협** | **★ Trainium = NVIDIA alt #3** | NVIDIA 80% → 점진 위협 | NVIDIA 4대 위협 #3 |

→ **AWS 특별 특징**:
- ★ **NVIDIA 발주가 MSFT와 동급 (~$30-40B/년)** — AWS-hosted NVIDIA 인스턴스 글로벌 #1
- ★ **Anthropic $8B 최대 투자자** + ★ **OpenAI 2GW 신규 deal** = AI Foundation 양면
- ★ **Graviton ARM CPU 가장 성숙** = ARM royalty 최대 driver
- ★ **WDC·STX HDD nearline 최대 발주** (S3 Glacier 글로벌 #1)
- ★ **Trainium = NVIDIA 위협 catalyst #3** (Google TPU 다음)

## 2-4. ★ AI Foundation 양면 strategy (vs MSFT OpenAI 독점 + Google Anthropic+Gemini)

| Model | AWS 위치 | 차별점 |
|---|---|---|
| **★ Anthropic (Claude)** | ★ **$8B 최대 투자자 (Google $3B의 2.7x)** | Claude 학습 = ★ Trainium |
| **★ OpenAI (2GW Trainium)** | ★ **Q1 2026 신규 deal** | ★ MSFT 독점 깨는 evidence |
| Amazon Nova (자체) | multimodal foundation | Bedrock 통합 |
| Llama·Mistral·Cohere·AI21 | Bedrock multi-model | open source 다축 |

→ **★ AWS AI Foundation 차별**:
- MSFT = OpenAI 독점 ($13B+, 49%) → exclusivity risk
- Google = Anthropic $3B + Gemini 자체 + 다축
- ★ **AWS = Anthropic $8B (최대) + OpenAI 2GW (신규) + Nova + Bedrock multi-model = AI Foundation 양면 + 다축**
- ★ **OpenAI도 AWS Trainium 사용 = MSFT-OpenAI 독점 본질적 weakening evidence**

---

# 항목 3. 재무 분석

## 3-1. 실적 추이 — 12년 매출·OPM·CapEx (multi-segment + AI 슈퍼사이클)

| FY | 매출 ($B) | YoY | OPM | CapEx ($B) | AWS 매출 ($B) | 사이클 |
|---|---|---|---|---|---|---|
| FY14 | 89.0 | — | 0.2% | — | n/a | 12년 OPM 최저 |
| FY18 | 232.9 | +31% | 5.3% | — | ~$25B | AWS 가속 + 광고 본격 |
| FY20 | 386.1 | +38% | 5.9% | — | ~$45B | COVID 정점 |
| FY22 | 514.0 | +9% | 2.4% | 63.6 | ~$80B | 2차 압축 저점 (순손실) |
| FY23 | 574.8 | +12% | 6.4% | 52.7 | ~$91B | Year of Efficiency |
| FY24 | 638.0 | +11% | 10.8% | 77.7 | ~$108B | AWS +19% YoY |
| **FY25** | **716.9** | **+12%** | **11.2%** | **105.0** | **$128.7B** | **★ AWS +28% 슈퍼사이클** |
| **Q1 2026 (분기)** | **$181.5B** | **+17%** | — | **$36B 분기** | **$29.27B (+28%)** | ★ AWS 15분기 최고 |
| **★ CY26 (E)** | — | — | — | **~$195B** | **~$160B+** | ★ 빅테크 #1 |

## 3-2. AWS PQC 분해

| 차원 | AWS Compute (NVIDIA + Trainium) | AWS Storage (S3 + Glacier) | AWS Database·Bedrock |
|---|---|---|---|
| **P (단가)** | GPU·CPU hour | $/GB/월 | API·token |
| **Q (출하)** | ★ +28% YoY 폭증 | exabyte 폭증 | Bedrock 사용량 폭증 |
| **C (원가)** | NVIDIA + Trainium + DC | HDD·SSD + DC | GPU + Foundation 라이선스 |
| **매출** | AWS의 60%+ | AWS의 20% | AWS의 10%+ |
| **마진** | ★ AWS OPM 35.2% (전년 37.5% -2.3%pt) | 안정 ~40% | Bedrock 빠른 성장 |

## 3-3. 재무 건전성 + 자본 환원

- **부채 안정** (현금 $100B+ vs 부채 $130B = AWS DC + Stores 인프라 부채)
- **OCF FY25 ~$130B** / FCF ~$15B (★ CapEx 폭증으로 -95% YoY)
- ★ **TTM FCF $1.2B (Q1 2026)** = ★ "첫 자본 시험기 진입" (기업개요 commentary)
- **배당 미시작** (NVDA·MSFT·Google 대비) — CapEx 우선
- **자사주 매입**: 거의 없음
- ★ **AWS-driven CapEx 우선** = 자본 환원 후순위

## 3-4. 수익성 트렌드

- **OPM 추이**: FY14 0.2% (최저) → FY20 5.9% (COVID) → FY22 2.4% (압축) → FY25 11.2% (★ AWS 35% leverage)
- **AWS OPM**: FY24 36.5% → FY25 37%+ → Q1 2026 35.2% (-2.3%pt = ★ AI 인프라 비용 흡수)
- **★ AWS OP 비중 ~60%** (매출 18% 대비 3.3x leverage) = AWS가 P&L driver
- ★ **AWS OPM 압박 trajectory**: AI CapEx 폭증으로 35% → 30%대 가능성

---

# 항목 4. 성장성 분석

## 4-1. 과거 성장률

| 기간 | 매출 CAGR | AWS CAGR |
|---|---|---|
| 3년 (FY22→FY25) | +12% | +17% |
| 5년 (FY20→FY25) | +13% | +25%+ |
| 12년 (FY13→FY25) | +19.5% | +28.6% (FY15 disclosure 이후 11년) |

→ AWS만 보면 +28.6% CAGR 11년 = 빅테크 #1 단일 segment 성장률.

## 4-2. 향후 성장 가시성

| 차원 | 전망 | 근거 |
|---|---|---|
| P 전망 | AWS compute 안정, Bedrock 가속 | Trainium 효율성 |
| Q 전망 | ★ AWS +28% → +25%+ 지속 가능 | Anthropic + OpenAI 2GW deal |
| C 전망 | ★ AWS OPM 35% → 30%대 압박 가능 | AI 인프라 비용 흡수 |
| **→ 매출 성장** | FY26 ~$800B (+12%) / FY27 ~$880B (+10%) | AWS + 광고 + Stores |
| **→ AWS 성장** | FY26 ~$160B+ (+25%) / FY27 ~$190B+ (+18%) | 가속 + 신규 deal |
| → 마진 | OPM 10-12% 박스 + AWS OPM 압박 | Trainium 효율성 만회 |

### 성장 지속성 구조적 근거 + 저해 risk
**구조적 +**:
- ★ AWS +28% (15분기 최고) + 가속 지속 가능
- ★ Anthropic $8B + OpenAI 2GW = AI Foundation 양면
- ★ Trainium·Graviton 자체 ASIC = NVIDIA 의존도 분산
- ★ AWS Cloud 절대 #1 매출 base
- ★ CapEx TTM $147B = AI 인프라 사이클 정점 미도래

**저해 risk**:
- ★ AWS OPM 35% → 30%대 압박 (AI CapEx 흡수)
- ★ Trainium 2 yield/ramp risk
- e-commerce 사업 cycle (인프라 CapEx 부담)
- TTM FCF -95% YoY = ★ 첫 자본 시험기

## 4-3. 빅테크 4사 비교 (★ macro layer baseline)

| 빅테크 | 매출 CAGR (3년) | AI ARR | CY26 CapEx | Cloud 매출 | strategic angle |
|---|---|---|---|---|---|
| MSFT | +12.4% | $37B (+123%) | $190B | Azure $95B | OpenAI 독점 + Maia + Cobalt |
| Google | +12% | ~$30B+ | $100B | GCP $80B | TPU + Anthropic + Broadcom |
| **AWS** | **+12% (AWS +28%)** | **~$25B+** | **★ $195B (#1)** | **★ $137B (#1 절대)** | **★ Anthropic $8B + OpenAI 2GW + Trainium + Graviton (Cloud 절대 #1)** |
| Meta | +20% | $20B+ | $135B | 자체 인프라 | Llama + MTIA + AMD MI450 6GW |

→ ★ **AWS는 Cloud 매출 절대 #1 + CapEx 빅테크 #1 + AI Foundation 양면 다축**.

---

# 항목 5. 통합 모드 입력용 Fact 정리

| 항목 | 정리 |
|---|---|
| **★ CY26 CapEx** | **★ ~$195B (TTM Q1 2026 $147B, 빅테크 #1)** |
| **★ AWS 매출** | **★ TTM $137.05B (+23% YoY) — Cloud 절대 #1** (Azure $95B / GCP $80B 압도) |
| **★ AWS 성장** | **★ Q1 2026 +28% YoY (15분기 최고)** — 5분기 연속 가속 |
| **AI ARR 추정** | ~$25B+ (MSFT $37B / Google $30B+ 다음 #3) |
| **★ Anthropic 누적 투자** | **★ $8B (Google $3B의 2.7x) — Anthropic 최대 투자자** |
| **★ OpenAI 2GW Trainium 계약** | **★ Q1 2026 신규 — MSFT 독점 깨는 evidence** |
| **★ Anthropic 평가차익** | **★ Q1 2026 $16.8B 일회성** (NVDA Equity 평가차익 $15.9B 동급) |
| **★ Trainium 2 + Inferentia 2** | ★ GA (2024), Anthropic Claude + OpenAI 학습 |
| **★ Graviton ARM CPU** | **★ 가장 성숙한 자체 ARM (AWS 인스턴스 50%+)** |
| **AWS TTM OPM** | 35.2% (전년 37.5% -2.3%pt = AI 인프라 비용) |
| NVIDIA 발주 추정 | $30-40B/년 (MSFT 동급, AWS-hosted NVIDIA #1) |
| HBM·HDD 발주 | Trainium HBM + AWS S3 Glacier (★ 글로벌 #1) |
| 시총 | ~$2.3T (2026-06) |
| **★ NVIDIA monopoly 위협 catalyst** | **★ Trainium = NVIDIA alt #3** (Google TPU 다음) |

---

# 항목 6. 구조적 트리거 모니터링

## 상방 트리거

- ★ AWS +30%+ YoY 가속 (Q2 2026)
- ★ CY26 CapEx $195B 페이스 유지 + FY27 가이드
- ★ **Trainium 2 ramp 본격화** + Trainium 3 발표
- ★ Anthropic Claude → AWS Trainium 사용 확대
- ★ **OpenAI Trainium deal 2GW → 추가 GW 확장**
- ★ Bedrock 매출 disclosure 시작 (현재 미공개)
- Graviton 인스턴스 60%+ AWS 점유

## 하방 트리거

- AWS +25% 이하 둔화
- ★ AWS OPM 30% 이하 (AI CapEx 흡수 한계)
- ★ Trainium 2 yield issue
- TTM FCF 음수 진입 (CapEx 페이스)
- Anthropic·OpenAI 파트너십 변경

## 모니터링 캘린더

- **Q2 2026 실적** (2026-07-31 예정): AWS 가속 + Trainium + CapEx
- **AWS re:Invent 2026** (12월): Trainium 3 + Graviton 5 + Bedrock 신기능
- Anthropic Claude 추가 deal
- OpenAI Trainium deal 확장

---

# 종합 판단 (macro layer component)

## 매트릭스

| 차원 | 평가 | 근거 |
|---|---|---|
| **AI 수요 측 #1-2** | ★★★ | Cloud 절대 #1 + CapEx 빅테크 #1 |
| **★ Foundation 다축** | ★★★ | Anthropic $8B (최대) + OpenAI 2GW (신규) |
| **AI 사업부 강도** | ★★★ | AWS +28% 15분기 최고 + Trainium·Graviton 자체 |
| **재무 건전성** | ★★ | AWS OPM 35% (압박), TTM FCF 시험기 |
| **★ Macro layer 가치** | ★★★ | Cloud 절대 #1 baseline + MSFT-OpenAI 독점 깨는 evidence |

## 핵심 투자 포인트 3

1. **★ Cloud 절대 #1 + CapEx 빅테크 #1**: AWS $137B TTM (Azure $95B / GCP $80B 압도) + CY26 CapEx $195B = AI 인프라 수요 측 단연 #1. AWS +28% (15분기 최고 가속) + AWS OP 비중 ~60% = P&L driver.
2. **★ Anthropic $8B + OpenAI 2GW Trainium (신규) = AI Foundation 양면 다축**: Anthropic 최대 투자자 (Google $3B의 2.7x) + ★ OpenAI 2GW Trainium 신규 deal = **★ MSFT-OpenAI 독점 깨는 가장 강한 evidence**. NVDA Equity 평가차익과 동급 $16.8B Anthropic 평가차익.
3. **★ Trainium 2 + Graviton 자체 ASIC**: NVIDIA monopoly 4대 위협 catalyst 중 #3 + Graviton 가장 성숙한 ARM 자체 (AWS 인스턴스 50%+). NVIDIA 의존도 분산 + ARM royalty 최대 driver.

## 핵심 리스크 3

1. **AWS OPM 35% → 30%대 압박**: 전년 37.5% → Q1 2026 35.2% -2.3%pt. AI CapEx 폭증 흡수 진행. AI 인프라 비용 흡수 한계 시 AWS OPM 30%대 가능.
2. **Trainium 2 yield/ramp risk**: 자체 ASIC 양산 안정성 + Anthropic·OpenAI 학습 deployment 안정성. Trainium 3 출시 전 단기 risk.
3. **TTM FCF $1.2B (-95% YoY) = 첫 자본 시험기**: CapEx 폭증 ($147B TTM)로 FCF 압박. CapEx 정점 통과 시점 불확실 + 자사주·배당 후순위 = 자본 환원 thesis 약함.

→ **종합 (macro layer)**: <span class="star">★★★ AI 수요 측 #1-2 + Cloud 절대 #1 + AI Foundation 양면 다축</span>. **통합 모드 macro layer에서 Cloud 절대 #1 baseline + MSFT-OpenAI 독점 깨는 가장 강한 evidence + Trainium NVIDIA 위협 catalyst + Graviton ARM driver 핵심 component**.

---

# 향후 관찰 포인트

1. **Q2 2026 실적** (2026-07-31): AWS +30%+ 가속 + CapEx $40B+ + Trainium ramp
2. **OpenAI Trainium deal 2GW → 확장** (MSFT 독점 본격 weakening 시그널)
3. **Trainium 3 발표** (AWS re:Invent 2026, 12월)
4. **CY26 CapEx $195B 페이스 검증 + FY27 가이드**
5. **AWS OPM 30% 진입 여부** (AI CapEx 흡수 한계)
6. **Anthropic Claude 4.0·5.0 출시 + AWS Trainium 사용 확대**
7. **Bedrock 매출 disclosure 시작** (현재 미공개)
8. **TTM FCF 회복 trajectory** (자본 시험기 통과)

---

## 부록: v1 changelog

**v1 (2026-06-21)**: 최초 작성 — 빅테크 frame (AWS 차별 angle: Cloud 절대 #1 + Anthropic·OpenAI 양면 + Trainium·Graviton)
- MSFT·Google과 동일 빅테크 frame이지만 ★ Cloud 절대 #1 매출 + Anthropic 최대 투자자 + OpenAI 2GW Trainium 신규 + Graviton 가장 성숙한 ARM 자체 차별 narrative
- Q1 2026 AWS +28% (15분기 최고) + Anthropic 평가차익 $16.8B + OpenAI 2GW Trainium 신규 deal 반영
- MSFT-OpenAI 독점 깨는 가장 강한 evidence로 OpenAI 2GW Trainium 강조
- Trainium = NVIDIA monopoly 4대 위협 catalyst 중 #3 (Google TPU 다음) 매핑
