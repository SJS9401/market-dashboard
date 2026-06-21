---
ticker: "META"
company_name: Meta Platforms, Inc.
country: US
theme_keyword: 에이전트AI
parent_industry: 빅테크 (수요 측, 자체 인프라 only)
role: macro_layer_component
trend_revenue_share: 20                # AI 직접 노출 (AI 광고 ARR + Reality Labs AI + Llama)
ai_capex_FY26: 100                    # CY26 ~$100B (FY25 $75B → +33%) — 빅테크 4사 중 가장 작음
ai_ad_arr_FY25: 30                    # AI 광고 ARR $30B (Value Optimization + Partnership ads, 2x YoY)
last_updated: 2026-06-21
auto_references:
  - 반도체_산업기초.md (2026-05-18)
  - 에이전트AI_테마분석.md (v4, 2026-05-26)
  - META_기업개요.md (v1.0, 2026-05-19)
  - 2026-Q1_META_리뷰.md (Q1 2026, 2026-04-29 발표)
  - 2026-Q2_META_팔로업.md (Q2 2026 예정)
  - 엔비디아_에이전트AI_기업분석.md (NVIDIA monopoly + AMD MI450 위협)
  - AMD_에이전트AI_기업분석.md (★ AMD MI450 6GW Meta lead customer)
  - 마이크로소프트·구글·아마존_에이전트AI_기업분석.md (빅테크 peer)
analyst_reports_attached:
  - META Q1 2026 IR Press Release
  - Mark Zuckerberg commentary
notes:
  - Meta 회계연도 = calendar year. Q1 2026 = 2026.01~03 (4/29 발표)
  - 본 분석 frame은 MSFT·Google·AWS와 가장 다른 angle — ★ Cloud 사업 없음 (자체 인프라만, 외부 판매 X) + ★ 광고 99% 사업 + ★ Llama open source (OpenAI/Anthropic 폐쇄 정반대) + ★ AMD MI450 6GW mega deal (AMD 최대 단일 고객)
  - Meta = ★ AMD thesis 단독 driver (AMD MI450 6GW + 6th Gen EPYC lead customer)
---

# Meta Platforms 기업 분석 — 에이전트AI 테마 (★ 빅테크 frame — Cloud X + Llama open + AMD MI450)

> **본 분석 frame (★ MSFT·Google·AWS와 가장 다른 빅테크 angle)**: Meta는 본 테마의 **고객 (수요 측, 자체 인프라 only)**. ★ **Cloud 사업 없음** = MSFT/Google/AWS와 본질적 차이. 광고 99%+ 사업 + AI 광고 ARR + Reality Labs 별도 베팅. **★ 차별 strategic angle**: (a) ★ **Llama open source** — OpenAI/Anthropic 폐쇄 정반대 (b) ★ **AMD MI450 6GW mega deal (2025-10)** — Meta가 AMD 최대 단일 hyperscaler 고객 + 6th Gen EPYC lead customer (c) ★ **MTIA (Meta Training and Inference Accelerator) Broadcom 위탁** — Google TPU와 같은 Broadcom 위탁 모델 (d) ★ **Reality Labs** (VR/AR/Meta AI 글래스) — 본 테마 외 별도 베팅 (FY25 적자 -$17.7B) (e) ★ **AI 광고 ARR $30B** (Value Optimization $20B + Partnership ads $10B, 2x YoY) = ★ AI = 광고 efficiency monetization. **★ Q1 2026 + DAP 3.56B (글로벌 인구 44%) + FY25 매출 $219.4B (+34%) + CapEx FY26E ~$100B + Reality Labs 누적 적자 $72B**.

> **CapEx·매출 단위 기준**: USD billion (Meta 회계연도 = calendar year). Q1 2026 = 2026.01~03. ★ Meta는 Cloud 매출 disclosure 없음 (자체 인프라만, 외부 판매 X) → ★ AI 사업부 = "AI 광고 ARR" 중심으로 측정.

---

## Executive Summary (5줄)

1. **위치**: 글로벌 #1 광고 플랫폼 (Family of Apps 99%) + ★ **DAP 3.56B (글로벌 인구 44%)** + ★ **Llama open source (오픈소스 AI Foundation 유일 빅테크)** + ★ **Reality Labs (Quest VR + Ray-Ban Meta AI 글래스)** 별도 베팅. ★ **Cloud 사업 없음** (자체 인프라만 — MSFT/Google/AWS와 본질 차이).
2. **AI 사업부**: ★ **AI 광고 ARR $30B (Value Optimization $20B + Partnership ads $10B, 2x YoY)** + Llama 4 (오픈소스) + Meta Superintelligence Labs (2025 설립) + Meta AI 챗봇 + AI 글래스 (Ray-Ban Meta). ★ **AI = 광고 efficiency monetization 중심** (Cloud 매출 없음).
3. **★ Meta 차별 strategic angle (빅테크 4사 중 가장 다름)**:
   - **★ Cloud 사업 없음** — 자체 인프라만, 외부 판매 X = MSFT/Google/AWS와 본질 차이
   - **★ AMD MI450 6GW mega deal (2025-10)** — Meta가 AMD 최대 단일 hyperscaler 고객 + ★ 6th Gen EPYC lead customer = ★ **AMD thesis 단독 driver**
   - **★ Llama open source** — OpenAI/Anthropic 폐쇄 정반대 strategy
   - **★ MTIA Broadcom 위탁** — Google TPU와 같은 Broadcom 위탁 모델 = Broadcom 추가 driver
   - **★ Reality Labs** — VR/AR/Meta AI 글래스 별도 베팅 (FY25 적자 -$17.7B)
4. **CapEx**: FY25 $75B → ★ **FY26E ~$100B+** (Zuckerberg 가이던스). ★ **빅테크 4사 중 가장 작음** (MSFT $190B / Google $100B / AWS $195B 대비). 단 Meta는 ★ Cloud 외부 판매 없이 100% 자체 사용 = ★ CapEx efficiency 다른 의미.
5. **종합 (macro layer)**: <span class="star">★★★ AI 수요 측 #4 (Cloud 없음) + ★ AMD·Llama·Broadcom 단독 driver + Reality Labs 별도 베팅</span>. (a) Reality Labs 적자 누적 $72B (b) Llama 4 monetization risk (open source 매출 X) (c) AI 광고 ROI 검증 risk. 단 ★ AMD MI450 6GW = ★ **NVIDIA 의존도 분산 가장 적극적 빅테크**.

---

# 항목 1. 입력 정리 + Meta 위치

## 1-1. 산업·테마 컨텍스트

- **반도체 산업기초**: Meta는 수요 측 driver — 단 ★ Cloud 사업 없음 = 자체 인프라만 = ★ **AMD/MTIA 자체 chip 가장 적극적 빅테크**
- **에이전트AI 테마 v4**: Meta는 수요 driver + ★ **Llama open source = AI Foundation 오픈소스 유일** + AMD MI450 = NVIDIA 위협 #1
- **NVIDIA 기업분석**: ★ **Meta 6GW MI450 = NVIDIA monopoly 위협 catalyst 중 #1 (AMD MI400)** — Meta가 NVIDIA 의존도 분산 가장 적극적
- **AMD 기업분석**: ★ **Meta 6GW MI450 + 6th Gen EPYC lead customer = AMD thesis 단독 driver**
- **MSFT/Google/AWS 기업분석 (peer)**: MSFT OpenAI + Google Gemini+Anthropic + AWS Anthropic+OpenAI vs ★ **Meta Llama open source** = AI Foundation 4가지 strategy 양상

## 1-2. Meta 위치 (수요 측 + Cloud X + AMD·Llama 단독 driver)

| Segment | 글로벌 위치 | 비고 |
|---|---|---|
| **광고 플랫폼 (FoA)** | **글로벌 #1** | Family of Apps 99% 매출 |
| **DAP (일일 활성 사용자)** | **3.56B (글로벌 인구 44%)** | Q1 2026 |
| **★ AI Foundation 전략** | **★ Llama open source (유일 빅테크)** | OpenAI/Anthropic 폐쇄 정반대 |
| **Llama 시리즈** | **★ Llama 4 (2025)** + Meta Superintelligence Labs | open source 표준 |
| **★ AI 광고 ARR** | **★ $30B (Value Opt $20B + Partnership $10B, 2x YoY)** | AI = 광고 efficiency |
| **★ AMD MI450 6GW mega deal** | **★ AMD 최대 단일 hyperscaler 고객** | 2025-10 발표, AMD thesis 단독 driver |
| **★ 6th Gen EPYC lead customer** | **★ AMD 6세대 EPYC lead** | Meta 단일 |
| **★ MTIA (자체 ASIC)** | **Broadcom 위탁** (Google TPU와 같은 모델) | Broadcom 추가 driver |
| **★ Cloud 사업** | **★ 없음 (자체 인프라만)** | MSFT/Google/AWS와 본질 차이 |
| **Reality Labs (VR/AR)** | 글로벌 #1 VR (Quest) + Ray-Ban Meta 글래스 | 별도 베팅 (FY25 적자 -$17.7B) |
| **CY26 CapEx** | **~$100B+** | 빅테크 4사 중 가장 작음 |
| **시총** | **~$1.5T** | M7 멤버 |

→ **★ Meta = 빅테크 4사 중 가장 다른 angle** (Cloud X + Llama open + AMD MI450 단독 + Reality Labs 베팅).

## 1-3. 사업부 구성 (Q1 2026 + FY25)

| Segment | Q1 2026 매출 ($M) | YoY | 본 테마 연결 | 비중 |
|---|---|---|---|---|
| **★ Family of Apps (광고 99%)** | ~$45B | +16% | ★ AI 광고 ARR + Llama AI 통합 | **99.1%** |
| Advertising | ~$44B | +16% | ★ AI Value Optimization $20B + Partnership $10B | 98.4% |
| Family of Apps Other | $885M | **+74%** | WhatsApp business + Threads + AI subs | 0.7% |
| **Reality Labs (VR/AR + AI 글래스)** | **$402M** | **-2%** | Quest + Ray-Ban Meta AI 글래스 | **0.9%** |
| **Total** | ~$45.4B | +15% | | 100% |

### 본 테마 직접 매출 노출
- **Family of Apps 99% × ~20%** (AI 광고 ARR $30B 중 매출 14% 기여 + Llama 인프라 + Meta AI 챗봇)
- **Reality Labs 1% × ~100%** (Meta AI 글래스 + Quest AI)
- **순 본 테마 직접 노출 = 약 20%** (빅테크 4사 중 가장 작음, Cloud 사업 없으므로)
- **★ AI 광고 ARR $30B** = 매출 비중 14% (Value Optimization $20B + Partnership ads $10B, 2x YoY)
- **★ Meta는 AI = 광고 efficiency monetization 중심** (다른 빅테크는 AI = Cloud 매출)

---

## ★ 2-0. 에이전트AI 테마 logical flow — 왜 Meta가 부각받는가 (수요 측 + AMD·Llama 단독 driver)

> **정성적 인과 사슬** (테마 v4 → Meta 위치 — 수요 측 + AMD·Llama·Broadcom 단독 driver + Cloud X)

### 1단계: 에이전트 AI = 데이터·연산·메모리 폭증
- 에이전트 1건 = chat 1턴 대비 **토큰 20-30x**
- ★ **Mark Zuckerberg Q1 2026**: *"AI is the most exciting opportunity I've worked on — Llama open source + Meta AI + AI glasses + Reality Labs full-stack"*

### 2단계: AI 인프라 layer별 분담 — Meta는 어디 위치?

| Layer | 9·10개사 (공급) | **Meta (수요 측 + 자체 인프라 only)** |
|---|---|---|
| Hot (HBM) | SK·삼성·Micron | ★ AMD MI450 HBM4 + NVIDIA GPU HBM (Meta 자체 인프라) |
| Warm (DRAM·SSD) | 메모리 3사 + SNDK·Solidigm | Meta 자체 DC DRAM·eSSD 발주 (Cloud 외부 판매 X) |
| Warm-Cold (eSSD·HBF) | SNDK | Meta 자체 vector DB·체크포인트 |
| Cold (HDD nearline) | WDC·Seagate | Meta 자체 cold storage (Llama 학습 데이터셋) |
| Compute (CPU) | Intel·AMD·ARM | ★ **EPYC (★ 6th Gen Meta lead) + Xeon legacy + (자체 ARM CPU 없음)** |
| **★ Compute (GPU·AI)** | NVIDIA·AMD·ASIC | **★ AMD MI450 6GW (최대 단일) + NVIDIA GPU + MTIA 자체 (Broadcom 위탁)** |
| IP layer | ARM + NVIDIA | ★ Llama open source = OpenAI/Anthropic 폐쇄 정반대 |

→ **Meta 위치: ★ Cloud 없는 자체 인프라 + AMD MI450 6GW (NVIDIA 의존도 분산 가장 적극) + Llama open + MTIA + Reality Labs**

### 3단계: 왜 Meta가 본 테마에서 부각받는가? — 5가지 본질적 이유

1. **★ AMD MI450 6GW mega deal (2025-10)** = Meta가 AMD 최대 단일 hyperscaler 고객 → ★ **AMD thesis 단독 driver** + NVIDIA 의존도 분산 가장 적극
2. **★ Llama open source = AI Foundation 오픈소스 유일 빅테크** → OpenAI/Anthropic 폐쇄 정반대 strategy
3. **★ AI 광고 ARR $30B (2x YoY)** = ★ AI = 광고 efficiency monetization 중심 → 다른 빅테크 (Cloud 매출) 와 차원이 다른 driver
4. **★ MTIA Broadcom 위탁** = Google TPU와 같은 Broadcom 위탁 모델 → ★ Broadcom 추가 thesis driver
5. **★ Reality Labs (VR/AR + Meta AI 글래스)** = 본 테마 외 별도 베팅이지만 ★ Llama AI 통합으로 본 테마 일부 연결

### 4단계: 왜 Meta가 부각? — AMD·Llama·Broadcom 단독 driver

- **★ 6GW MI450 = ★ AMD 최대 단일 mega deal** (OpenAI 6GW + Meta 6GW = AMD 12GW 중 절반)
- **★ Llama 4 (2025) + Meta Superintelligence Labs**: open source AI Foundation 표준 (Hugging Face·기타 AI 스타트업 대다수 Llama base)
- **★ Ray-Ban Meta 글래스 + Llama 통합**: 차세대 AI 디바이스 entry point
- **★ AI 광고 Value Optimization $20B + Partnership $10B = 광고 efficiency revolution**
- ★ **Zuckerberg "AI는 가장 흥미로운 기회"** = founder-led 베팅 강도

### 5단계: 본 분석 frame 결론

**본 테마 수요 측 #4 (Cloud X) + ★ AMD·Llama·Broadcom 단독 driver + Reality Labs 별도 베팅**. AI ARR (광고 efficiency) ~$30B (MSFT $37B / Google $30B+ / AWS $25B+ 다음 #4). CY26 CapEx ~$100B = ★ 빅테크 4사 중 가장 작음 (Cloud 없으므로). ★ **AMD MI450 6GW = AMD thesis 단독 driver + NVIDIA monopoly 위협 catalyst #1**. **통합 모드 macro layer에서 AMD·Llama·Broadcom evidence + AI 광고 monetization 단독 case**.

---

# 항목 2. AI 사업부 + CAPEX + 10·11개사 발주 mapping — ★ 핵심

## 2-1. AI 사업부 분석 (Meta = AI 광고 + Llama + Reality Labs + AI 글래스)

### ★ AI 광고 ARR $30B (FY25, 2x YoY)
- **Value Optimization ads ARR $20B** — Meta Advantage+ AI 자동 캠페인 최적화
- **Partnership ads ARR $10B** — 광고주 측 AI 통합
- **AI = 광고 efficiency monetization 중심** (Cloud 매출 없음)
- ★ Meta 광고 사업의 ★ **structural moat** = 3.56B DAP × AI 광고 효율 = 다른 광고주가 불가

### Llama (오픈소스 AI Foundation)
- **Llama 1 (2023.02) → Llama 2 (2023.07) → Llama 3 (2024.04) → Llama 4 (2025)**
- ★ **open source = OpenAI/Anthropic 폐쇄형 정반대**
- ★ Hugging Face·AI 스타트업 대다수 Llama base = open source 표준
- ★ Meta Superintelligence Labs (2025 설립) = AGI 베팅

### Meta AI (챗봇 + Reality Labs 통합)
- Meta AI 챗봇 — WhatsApp·Messenger·Instagram·Facebook 통합
- ★ Ray-Ban Meta 글래스 + Llama AI 통합 = 차세대 AI 디바이스 entry point
- Quest 4 VR + Meta AI 통합

### ★ AMD MI450 6GW mega deal (2025-10)
- ★ **Meta가 AMD 최대 단일 hyperscaler 고객**
- AMD 12GW MI450 deal 중 6GW = Meta 단일
- ★ ★ NVIDIA 의존도 분산 가장 적극적 빅테크
- 2H 2026 ramp 예정

### ★ 6th Gen EPYC lead customer (2026-Q1)
- ★ Meta = AMD 6세대 EPYC lead customer
- AMD EPYC 점유 24% → 27% (+3.3%p YoY) 가속의 ★ 핵심 catalyst

### ★ MTIA (자체 ASIC) — Broadcom 위탁
- Meta Training and Inference Accelerator
- ★ Broadcom 위탁 (Google TPU와 같은 모델)
- ★ Broadcom 추가 thesis driver

## 2-2. CAPEX trajectory 분해 (★ 빅테크 4사 중 가장 작음)

| 분기/연 | CapEx ($B) | YoY | 비고 |
|---|---|---|---|
| FY22 | 31.4 | — | 메타버스 베팅 정점 |
| FY23 | 27.3 | -13% | Year of Efficiency |
| FY24 | 39.2 | +44% | AI Llama + Reality Labs 가속 |
| FY25 | 75.0 | +91% | ★ AI 슈퍼사이클 |
| **Q1 2026** | **$19.0B** | — | annualized ~$76B+ |
| **★ FY26E (Zuckerberg)** | **~$100B+** | **+33%** | Llama 5 + AMD MI450 ramp + Reality Labs |

### CapEx 구성
- ★ **Cloud 외부 판매 없이 100% 자체 사용** (MSFT/Google/AWS와 본질 차이)
- 2/3 short-lived (★ AMD MI450 + NVIDIA GPU + MTIA + EPYC), 1/3 long-lived (DC + 전력)
- **★ AMD MI450 비중 본격화 (2H 2026~)**: NVIDIA 의존도 분산 가속

### MSFT·Google·AWS 대비 CapEx 비교
- MSFT $190B / Google $100B / AWS $195B / **★ Meta $100B (가장 작음)**
- 단 Meta는 ★ Cloud 외부 판매 X = 100% 자체 사용 = ★ CapEx efficiency 다른 의미
- ★ Meta AI 광고 ARR $30B vs CapEx $100B = ARR/CapEx 비율 30%

## 2-3. ★ 10·11개사 thesis와 직접 connection mapping (Meta 특별 angle)

### 발주 mapping (Meta → 10·11개사)

| 종목 | Meta 발주 형태 | 정량 추정 | 본 테마 driver 영향 |
|---|---|---|---|
| **NVIDIA (Blackwell·Rubin)** | Meta 자체 DC GPU (NVIDIA 우선) | **~$20-25B/년 (CY26)** ★ MSFT $30-40B의 60-70% | NVIDIA DC 매출 ~10-12% |
| **★ AMD (MI450 6GW + 6th Gen EPYC)** | **★ AMD 최대 단일 hyperscaler 고객** | **★ AMD MI 매출 +★ 비중 큼 (예상 $5B+/년 2027~)** | **★ AMD thesis 단독 driver** + NVIDIA 의존 분산 |
| **★ Broadcom (MTIA 위탁)** | **★ MTIA 자체 chip 설계·생산 위탁** | Google TPU와 별도 | ★ Broadcom 추가 thesis driver |
| SK하이닉스 (HBM) | NVIDIA GPU HBM + ★ AMD MI450 HBM4 + MTIA HBM | 간접 + 직접 | SK HBM driver (★ AMD MI450 driver 핵심) |
| 삼성전자 (HBM AMD 우선 + DRAM) | ★ AMD MI455X Samsung preferred HBM4 + Meta DRAM | ★ 삼성 HBM4 AMD driver | ★ 삼성 HBM4 AMD MoU driver 일부 |
| Micron (HBM·DDR5) | NVIDIA GPU + AMD HBM 일부 + DRAM | 간접 + 직접 | Micron driver |
| **★ AMD EPYC (6th Gen)** | **★ Meta 6세대 EPYC lead customer** | EPYC 점유 24%→27% 가속 driver | ★ AMD EPYC thesis 단독 driver |
| Intel (Xeon) | 자체 DC server CPU legacy (★ 잠식 중) | Xeon legacy | Intel legacy + 잠식 가속 |
| **★ ARM** | 자체 ARM CPU 없음 (MSFT Cobalt·Google Axion·AWS Graviton과 다름) | ARM royalty 작음 | ARM driver 약함 (빅테크 4사 중 가장 약) |
| SanDisk (eSSD) | Meta DC storage tier | direct enterprise SSD | SNDK NBM 일부 |
| WDC (HDD nearline) | Meta cold storage (Llama 학습 데이터셋) | direct (글로벌 #3-4) | WDC nearline driver |
| Seagate (HDD nearline) | Meta cold storage | direct | STX nearline driver |
| **★ NVIDIA monopoly 위협** | **★ AMD MI450 6GW = NVIDIA 위협 #1** | NVIDIA 80% → 75-78% 위협 | ★ NVIDIA 4대 위협 #1 |

→ **★ Meta 차별 특징**:
- ★ **AMD 단독 driver** (MI450 6GW + 6th Gen EPYC lead = 빅테크 4사 중 AMD 가장 적극적)
- ★ **NVIDIA 발주 작음** ($20-25B vs MSFT/AWS $30-40B) — AMD 의존도 분산
- ★ **MTIA Broadcom 위탁** = Broadcom 추가 driver
- ★ **자체 ARM CPU 없음** = ARM driver 약함 (빅테크 4사 중 가장 약)
- ★ **Llama open source** = AI Foundation 다른 strategy

## 2-4. ★ AI Foundation strategy (Llama open source = 빅테크 4사 중 유일)

| 빅테크 | AI Foundation | 차별점 |
|---|---|---|
| MSFT | OpenAI 독점 ($13B+) | 폐쇄형, 49% economic interest |
| Google | Gemini 자체 + Anthropic $3B | 폐쇄형 자체 + 투자 |
| AWS | Anthropic $8B (최대) + OpenAI 2GW | 폐쇄형 양면 투자 |
| **★ Meta** | **★ Llama open source (유일)** | **★ open source 표준 strategy** |

→ ★ **Meta는 AI Foundation 완전히 다른 strategy** = open source로 ecosystem 확장. ★ Llama가 Hugging Face·AI 스타트업 대다수 base가 됨으로써 ★ **AI 생태계 영향력 = 폐쇄형 모델 매출보다 더 큰 가치**.

---

# 항목 3. 재무 분석

## 3-1. 실적 추이 — 12년 매출·OPM·CapEx (AI 광고 + 메타버스 베팅 사이클)

| FY | 매출 ($B) | YoY | OPM | CapEx ($B) | Reality Labs 적자 | 사이클 |
|---|---|---|---|---|---|---|
| FY14 | 12.47 | — | 40.0% | 1.83 | n/a | WhatsApp $19B 인수 |
| FY18 | 55.84 | +37% | 44.6% | 13.92 | n/a | Cambridge Analytica 쇼크 |
| FY21 | 117.93 | +37% | 39.6% | 19.24 | -$10.2B | 광고 슈퍼사이클 + Meta 사명 변경 |
| FY22 | 116.61 | -1% | **24.8%** | 31.43 | -$13.7B | ★ 3차 압축 저점 (메타버스 + 광고 위축) |
| FY23 | 134.90 | +16% | 34.7% | 27.27 | -$16.1B | Year of Efficiency (21K layoff) |
| FY24 | 164.50 | +22% | 42.2% | 39.23 | -$17.7B | AI 광고 monetization 시작 |
| **FY25** | **~219.4** | **+34%** | **~46.5%** | **~75.0** | **-$17.7B** | **★ 3차 정점 (AI 광고 ARR $30B + Muse Spark)** |
| **Q1 2026** | $45.4B | +15% | — | $19.0B | n/a | Q1 2026 |
| **★ FY26E** | ~$260B (+18%) | — | — | **~$100B+** | — | Llama 5 + AMD MI450 + RL |

## 3-2. AI PQC 분해 (Meta = AI 광고 + Reality Labs)

| 차원 | AI 광고 (Family of Apps) | Reality Labs | Llama (open source) |
|---|---|---|---|
| **P (단가)** | CPM·CPC 안정 | Quest $300-500, Ray-Ban Meta $300 | 매출 X (open source) |
| **Q (출하)** | DAP 3.56B + AI 광고 ARR $30B | Quest+RB Meta 출하 | Llama 다운로드 무료 |
| **C (원가)** | AI 인프라 (AMD MI450 + NVIDIA + MTIA) | 하드웨어 BOM 손실 | 학습 비용 (자체 흡수) |
| **매출** | $215B+ FY25 광고 | $1.6B FY25 (적자) | 매출 X |
| **마진** | ★ OPM 50%+ (FoA 단독) | ★ -$17.7B 적자 | ★ open source = 매출 X |

## 3-3. 재무 건전성 + 자본 환원

- **부채 매우 안정** (현금 $80B+ vs 부채 $30B)
- **OCF Q1 2026 $32.2B / FCF $13.2B** (연환산 OCF $130B+)
- ★ **2024 첫 배당 시작** (3월)
- 자사주 매입 FY25 ~$50B+ → Q1 2026 일시 중단 (★ CapEx 우선 시그널)
- ★ **AI CapEx 우선** = NVDA·MSFT·Google·AWS와 동일 패턴
- ★ **Reality Labs 누적 적자 $72B (2019-2025)** = Zuckerberg founder-led 베팅

## 3-4. 수익성 트렌드

- **OPM 추이**: FY17 49.7% (정점) → FY22 24.8% (메타버스 베팅 저점) → FY25 46.5% (회복 + AI 광고)
- **★ FoA 단독 OPM 50%+** (Reality Labs 적자 제외 normalized 시 55%+)
- **★ 12년 사이클 진폭 24.9%pt** = 빅테크 4사 중 가장 큼 (메타버스 베팅 변동성)
- ★ **AI 광고 monetization으로 OPM 회복 trajectory** (FY22 25% → FY25 46.5%)

---

# 항목 4. 성장성 분석

## 4-1. 과거 성장률

| 기간 | 매출 CAGR |
|---|---|
| 3년 (FY22→FY25) | **+24%** (★ 빅테크 4사 #1) |
| 5년 (FY20→FY25) | +21% |
| 12년 (FY13→FY25) | **+30%** (★ 빅테크 4사 #1) |

→ ★ **Meta 매출 CAGR = 빅테크 4사 #1** (MSFT +12% / Google +12% / AMZN +12% / Meta +24% 3년).

## 4-2. 향후 성장 가시성

| 차원 | 전망 | 근거 |
|---|---|---|
| **P 전망** | CPM·CPC 안정, Quest·RB Meta 가격 안정 | AI 광고 효율 향상 |
| **Q 전망** | ★ DAP 3.56B → 3.7B+, AI 광고 ARR $50B+ 가능 | Llama 5 + AMD MI450 ramp |
| **C 전망** | ★ AI CapEx 폭증 ($100B+) but 자체 인프라 효율 | AMD MI450 + MTIA 효율 |
| **→ 매출 성장** | FY26 ~$260B (+18%) / FY27 ~$300B (+15%) | AI 광고 + Llama + Reality Labs |
| **→ 마진** | OPM 45-48% (Reality Labs 적자 흡수) | FoA OPM 50%+ |

### 성장 지속성 구조적 근거 + 저해 risk
**구조적 +**:
- ★ AI 광고 ARR $30B 2x YoY (Value Opt + Partnership)
- ★ DAP 3.56B (글로벌 인구 44%)
- ★ AMD MI450 6GW = NVIDIA 의존 분산
- ★ Llama open source = ecosystem 확장
- ★ Reality Labs (장기 베팅) + Ray-Ban Meta AI 글래스

**저해 risk**:
- ★ Reality Labs 누적 적자 $72B (FY25 -$17.7B 진행)
- ★ Llama open source = monetization 직접 매출 X
- AI 광고 ROI 검증 risk (Value Opt $20B 실제 efficiency 입증 필요)
- AMD MI450 ramp risk (2H 2026)
- Antitrust risk (FTC 분리 명령 가능성)

## 4-3. 빅테크 4사 비교 (★ macro layer baseline)

| 빅테크 | 매출 CAGR (3년) | AI ARR | CY26 CapEx | Cloud 매출 | strategic angle |
|---|---|---|---|---|---|
| MSFT | +12.4% | $37B (+123%) | $190B | Azure $95B | OpenAI 독점 + Maia + Cobalt |
| Google | +12% | ~$30B+ | $100B | GCP $80B | TPU + Anthropic + Broadcom |
| AWS | +12% (AWS +28%) | ~$25B+ | $195B (#1) | $137B (#1) | Anthropic + OpenAI + Trainium + Graviton |
| **★ Meta** | **★ +24% (#1)** | **★ $30B (광고 ARR)** | **~$100B (가장 작음)** | **★ 없음 (자체만)** | **★ Llama open + AMD MI450 6GW + MTIA + Reality Labs (가장 다른 angle)** |

→ ★ **Meta = 빅테크 4사 중 가장 다른 angle** (Cloud X + Llama open + AMD 단독 + Reality Labs).

---

# 항목 5. 통합 모드 입력용 Fact 정리

| 항목 | 정리 |
|---|---|
| **★ CY26 CapEx** | **~$100B+ (FY25 $75B → +33%)** — 빅테크 4사 중 가장 작음 |
| **★ AI 광고 ARR (FY25)** | **★ $30B (Value Opt $20B + Partnership $10B, 2x YoY)** |
| **DAP** | **3.56B (글로벌 인구 44%)** Q1 2026 |
| **★ AMD MI450 6GW mega deal** | **★ AMD 최대 단일 hyperscaler 고객 (2025-10)** |
| **★ 6th Gen EPYC lead customer** | **★ AMD 6세대 EPYC lead (2026-Q1)** |
| **★ Llama open source** | **★ Llama 4 (2025) + Meta Superintelligence Labs** |
| **★ MTIA (Broadcom 위탁)** | Google TPU와 같은 모델 |
| **★ Cloud 사업** | **★ 없음 (자체 인프라만, 외부 판매 X)** |
| Reality Labs | Quest VR + Ray-Ban Meta AI 글래스, FY25 적자 -$17.7B (누적 $72B) |
| FY25 매출 | $219.4B (+34%) |
| FY25 OPM | ~46.5% (12년 최고 권역) |
| NVIDIA 발주 추정 | $20-25B/년 (MSFT/AWS의 60-70%) |
| 시총 | ~$1.5T (2026-06) |
| **★ NVIDIA monopoly 위협 catalyst** | **★ AMD MI450 6GW = NVIDIA 위협 #1** |
| **★ AMD thesis 단독 driver** | **★ MI450 + 6th Gen EPYC lead 모두 Meta** |
| **★ Broadcom 추가 driver** | MTIA 위탁 (Google과 함께) |

---

# 항목 6. 구조적 트리거 모니터링

## 상방 트리거

- ★ **AMD MI450 6GW ramp 본격화** (2H 2026) — NVIDIA 의존도 분산 가속
- ★ AI 광고 ARR $50B+ 도달 (Q4 2026)
- ★ Llama 5 출시 + open source 영향력 확대
- ★ Ray-Ban Meta 글래스 100M+ 출하 (FY27)
- ★ Reality Labs 적자 -$15B 이하 축소 (효율화)
- ★ AMD 6th Gen EPYC + MI450 동시 ramp
- CapEx FY27 가이드 $120B+

## 하방 트리거

- ★ Reality Labs 적자 -$20B 초과 (FY26)
- ★ AMD MI450 yield/ramp 지연
- AI 광고 ARR 둔화 (Value Opt $20B 효율 검증 실패)
- DAP 3.6B 미달 (성장 둔화)
- Antitrust (FTC 분리 명령) 진전

## 모니터링 캘린더

- **Q2 2026 실적** (2026-07-30 예정): AI 광고 ARR + CapEx + Reality Labs
- **Meta Connect 2026** (9월): Llama 5 + Quest 5 + Ray-Ban Meta 발표
- **★ AMD MI450 ramp 본격화** (2H 2026)
- **★ AMD Q3 FY26 실적**: Meta MI450 6GW deal 정량 진행

---

# 종합 판단 (macro layer component)

## 매트릭스

| 차원 | 평가 | 근거 |
|---|---|---|
| **AI 수요 측 #4 (Cloud X)** | ★★ | 광고 ARR $30B, Cloud 매출 없음 |
| **★ AMD·Llama·Broadcom 단독 driver** | ★★★ | AMD MI450 + 6th Gen + MTIA + Llama open |
| **AI 사업부 강도** | ★★★ | AI 광고 ARR $30B + Llama 4 + Meta AI 글래스 |
| **재무 건전성** | ★★ | OPM 46.5%, OCF $130B+ (Reality Labs 적자) |
| **★ Macro layer 가치** | ★★★ | AMD 단독 driver + AI 광고 monetization 단독 case + NVIDIA 위협 #1 evidence |

## 핵심 투자 포인트 3

1. **★ AMD MI450 6GW mega deal + 6th Gen EPYC lead customer = AMD thesis 단독 driver**: Meta = AMD 최대 단일 hyperscaler 고객 (12GW MI450 deal 중 6GW). NVIDIA 의존도 분산 가장 적극적 빅테크. ★ **NVIDIA monopoly 위협 catalyst #1 evidence**.
2. **★ AI 광고 ARR $30B (2x YoY) + Llama open source + DAP 3.56B = ★ 광고 AI monetization 단독 case**: MSFT/Google/AWS는 Cloud 매출 중심 vs Meta는 광고 efficiency 중심. ★ Llama open source = AI 생태계 영향력 (Hugging Face·AI 스타트업 대다수 Llama base).
3. **★ MTIA (Broadcom 위탁) + Reality Labs (별도 베팅)**: Google TPU와 같은 Broadcom 위탁 = ★ Broadcom 추가 driver. ★ Ray-Ban Meta 글래스 + Llama AI = 차세대 AI 디바이스 entry point.

## 핵심 리스크 3

1. **★ Reality Labs 누적 적자 $72B + FY25 -$17.7B 지속**: Zuckerberg founder-led 베팅. 흑전 시점 미명. AI 글래스 + Quest VR ROI 검증 risk.
2. **★ Llama open source = 매출 직접 X**: AI Foundation 매출은 OpenAI ($MSFT 49% interest) / Anthropic ($AWS·GOOGL 투자 평가차익) 대비 직접 매출 없음. monetization 간접 (광고 효율).
3. **AMD MI450 ramp risk (2H 2026)**: 6GW deal 양산 안정성. yield issue 또는 NVIDIA Rubin 우위 유지 시 AMD 대안 thesis 약화.

→ **종합 (macro layer)**: <span class="star">★★★ 빅테크 4사 중 가장 다른 angle (Cloud X + AMD 단독 + Llama open) + AI 광고 monetization 단독 case</span>. **통합 모드 macro layer에서 ★ AMD thesis 단독 driver + ★ NVIDIA monopoly 위협 catalyst #1 evidence + Broadcom 추가 driver + Llama open source 영향력 핵심 component**.

---

# 향후 관찰 포인트

1. **Q2 2026 실적** (2026-07-30): AI 광고 ARR $35B+ + CapEx $25B+ + Reality Labs
2. **★ AMD MI450 6GW ramp 본격화** (2H 2026)
3. **Llama 5 출시 + Meta Superintelligence Labs 진행**
4. **★ Ray-Ban Meta 글래스 출하 가속 (Llama 통합)**
5. **CapEx FY26 $100B+ 페이스 검증 + FY27 가이드**
6. **Reality Labs 적자 trajectory** (효율화 vs 베팅 확대)
7. **★ AMD Q3 FY26: Meta MI450 deal 정량 진행 disclosure**
8. **FTC Antitrust 진전**

---

## 부록: v1 changelog

**v1 (2026-06-21)**: 최초 작성 — 빅테크 frame (Meta 차별 angle: Cloud X + Llama open + AMD MI450 단독 + Reality Labs)
- MSFT·Google·AWS와 가장 다른 angle: ★ Cloud 사업 없음 (자체 인프라만) + Llama open source + AMD MI450 6GW mega deal + MTIA Broadcom 위탁
- Q1 2026 매출 $45B + AI 광고 ARR $30B + DAP 3.56B + AMD lead customer 반영
- AMD thesis 단독 driver (MI450 + 6th Gen EPYC) + NVIDIA 위협 #1 evidence + Broadcom 추가 driver + Llama open source 영향력 narrative
