---
theme_keyword: 에이전트AI
parent_trend: AI
parent_industry: 반도체
cross_ref_industry: 전력 인프라
sibling_themes: [HBM, 온디바이스AI, 추론최적화, AI데이터센터전력]
status: active
sunset_date: null
sunset_reason: null
bottleneck_category: A+D hybrid — 구조적 메가 병목 (A) + 동반 확대 (D)
active_companies: 미정 — 1차 분석 단계
sunset_companies: []
last_updated: 2026-05-26 (v4)
last_theme_review_date: null
narrative_shift_log:
  - {date: 2024-Q4, event: "Anthropic Claude 3.5 Computer Use 공개 — 에이전트 진입 신호탄"}
  - {date: 2025-Q1, event: "OpenAI Operator·Manus AI 출시 — 에이전트 narrative 시장 확산"}
  - {date: 2025-H2, event: "에이전트 작업 1건 = chat 대비 토큰 20-30x 실측 확인 (Stanford·NVIDIA)"}
  - {date: 2025-Q3, event: "NAND +65% MoM, DDR5 +50% YTD — 레거시 메모리 병목 narrative 부상"}
  - {date: 2025-Q4, event: "Big Tech 2026 capex $700B 합의"}
  - {date: 2026-Q2, event: "★ NVIDIA Kyber Ultra 660kW/rack 발표 (GB200 NVL72 130kW의 5x) — 48V→800V DC 전환 물리적 강제"}
  - {date: 2026-Q2, event: "★ SemiAnalysis '800VDC Revolution Part 1' 발행 (2026-05-26) — HVDC Power Rack·SST narrative 본격화. OCP Diablo 400 표준 형성"}
---

# 에이전트AI 테마 분석 (v4)

> **본 테마의 분석 frame**: 에이전트AI는 narrative-driven 키워드. 그 narrative가 가져오는 충격(토큰 N배 폭증)이 **추론 인프라**에 집중되고, 추론 인프라는 **반도체 + 전력** 두 축. HBM은 이미 시장이 반영했고 **신규 병목은 레거시 메모리·광통신·CPU·CoWoS**로 이동.

---

## 표기 컨벤션

| 표기 | 풀이 (전체 분류명) |
|---|---|
| **(A) 구조적 메가 병목** | 공급 제한 + 수요 급증. ASP 강한 상승 + Q 점진. 다년간 지속 |
| **(B) 수요 견인** | 공급 적당 + 수요 폭증. 새 capa 가동 시 완화 |
| **(C) 사이클 반등** | 일시 공급 축소 + 수요 일정. 공급 회복 시 정상화 |
| **(D) 동반 확대** | 공급 확대 + 수요 폭증. 신규 시장 형성기. ASP 안정 + Q 폭증 |
| **(E) 점진적 가격 상승** | 공급 제한 + 수요 일정 |
| **(F) 공급 과잉** | 공급 과잉 + 수요 일정/감소 |
| **(G) 구조조정** | 공급 축소 + 수요 감소 |

> 본 .md 본문에서 카테고리는 항상 전체 분류명 병기 (예: "(A) 구조적 메가 병목").

---

## Executive Summary

1. **에이전트AI** = LLM이 multi-step reasoning + tool calls + 컨텍스트 유지로 자율 작업 실행 (Claude Computer Use, OpenAI Operator, Cursor, Devin, Manus).
2. **수요 충격**: 에이전트 1건 = chat 대비 토큰 **20-30배** (코딩 1000배). 컨텍스트 스노볼링·tool overhead·재시도.
3. **병목 = 추론 인프라 두 축**: ① 반도체(HBM·**레거시 메모리·광통신·CPU**·추론 GPU·CoWoS·후공정) ② 전력(데이터센터 전력·UHV 변압기·SMR·**가스터빈**·액랭). HBM은 합의 반영, 신규 알파는 DDR5·eSSD·800G/1.6T·서버 CPU·가스터빈·SMR 부품(두산).
4. 병목 분류: **(A) 구조적 메가 병목 + (D) 동반 확대 hybrid**.
5. **글로벌 트렌드 관통 + Moat 기업** (한국/글로벌 통합 view): SK하이닉스(HBM #1·DDR5 #2·eSSD #2), 한미반도체(TC본더 #1), 효성중공업(미국 765kV UHV #1), **두산에너빌리티 (SMR forging 글로벌 5사 중 하나)**, 오이솔루션(1.6T·ITLA 국산화) 등.

---

## 1-pager 요약 표

| 단계 | 핵심 결론 |
|---|---|
| **Step 0. 산업기초 참조** | ✓ 반도체_산업기초.md (2026-05-18) / ✓ 전력 인프라_산업기초.md (2026-05-18) — 둘 다 **(A) 구조적 메가 병목** |
| **Step 1. 정의·트렌드** | AI 메가 트렌드 안의 에이전트 narrative. 형제자매: HBM·온디바이스AI·추론최적화·AI데이터센터전력 |
| **Step 2. 병목 역추적** | 에이전트 = 토큰 20-30x → 추론 인프라 동시 병목 → 병목 파생형 |
| **Step 3. 병목 인뎁스 (★)** | 반도체: HBM(이미 반영) + **레거시 메모리·광통신·CPU·CoWoS(신규)** / 전력: 데이터센터 전력·변압기 128주·**가스터빈 3사 capa 25-35% 확대**·SMR 22 GW |
| **Step 4. 통합 Moat view** | segment별 글로벌 강자 1-5위에 한국 다수. SMR은 4 layer (본체·사업자·부품·EPC)로 확장 → **두산 forging 글로벌 5사 중 1, 현대건설 EPC** |
| **Step 5. 17 Segment TAM 시간축** | 각 segment P/Q 4분기 + 연간(2026·2027) + 변동 근거. **★ v4: 800VDC 전환 (HVDC Power Rack·SST·SSCB) 신규 segment 추가**. 한국 접근 TAM **$216-262B+** (SMR 부품·EPC + 800VDC DC switchgear 포함) |
| **Step 6. 주도 섹터** | ★★★ — 17 segment 중 **10 segment 한국 글로벌 Top 5** (SMR 부품 + 800VDC LS ELECTRIC 추가), 5 segment Top 2 |

---

# Step 0. 산업 기초 분석 자동 참조

| 참조 | 상태 | 활용 |
|---|---|---|
| `반도체_산업기초.md` | ✓ 2026-05-18 | 반도체 측 직접 기반 ((A) 구조적 메가 병목) |
| `전력 인프라_산업기초.md` | ✓ 2026-05-18 | 전력 측 직접 기반 ((A) 구조적 메가 병목) — 변압기 4년·GSU 144주 |

---

# Step 1. 테마 키워드 정의 + 상위 트렌드

## 1-1. 정의

| 요소 | 단순 chat | 에이전트AI |
|---|---|---|
| 입출력 구조 | 1 요청 → 1 응답 | 지시 → multi-step plan → tool call → ... → 자체 종료 |
| 도구 사용 | ❌ | ✓ (브라우저·코드·API·DB) |
| 평균 turn | 1 | 10~100+ (코딩 1000+) |

**시장 대표**: Anthropic Claude Computer Use, OpenAI Operator·Agents Platform, Cursor·Cline·Devin·Manus·Replit·Salesforce Einstein·ServiceNow·Microsoft Copilot Studio.

## 1-2. 상위 트렌드 — AI 슈퍼사이클 2단

| 단계 | 시기 | 특징 |
|---|---|---|
| 1단 (학습) | 2022–2024 | LLM 학습용 GPU·HBM 폭발 |
| **2단 (에이전트+추론)** ★ | 2024– | 토큰 폭증, 추론 capa·전력 인프라 동시 병목 + **레거시 메모리·광통신·CPU 신규 병목** |

> **시장 view**: "AI capex 무게중심이 학습→추론으로 이동 + 추론 부담 자체가 N배 폭증". 1단은 칩 쇼티지, 2단은 **칩 + 전력 + 메모리/네트워크/CPU 동시 쇼티지**.

## 1-3. 형제자매 테마

| 형제자매 | 관계 |
|---|---|
| **HBM** | 본 테마의 반도체 측 1단 병목. 이미 시장 합의 반영 |
| **온디바이스AI** | 추론을 단말기로 분산 (Apple·Qualcomm) |
| **추론최적화** | NVIDIA Dynamo·vLLM·FP4·KV cache offload. **본 테마의 신규 병목(레거시 메모리)을 만드는 원인** |
| **AI데이터센터전력** | 본 테마의 전력 측 병목 |

---

# Step 2. 상위 산업 병목 역추적

## 2-1. 에이전트 = N배 토큰 폭증의 본질

| 항목 | 단순 chat | 에이전트 (단순) | 에이전트 (코딩) |
|---|---|---|---|
| 입력 토큰 / 작업 | ~500-2,000 | ~10K-50K | ~100K-1M |
| 출력 토큰 / 작업 | ~200-2,000 | ~5K-20K | ~50K-500K |
| 평균 turn 수 | 1 | 5-30 | 30-300 |
| 토큰 폭증 배수 vs chat | 1x | **20-30x** | **500-1,000x** |

**3대 메커니즘**:

(1) **컨텍스트 스노볼링** — n step → O(n²) 누적. 30 step = 900배. → **HBM + KV cache offload용 DDR5·eSSD 부담**

(2) **Tool call overhead** — 도구 결과 모두 컨텍스트 포함. → **CPU 전처리 + 광통신 throughput 부담**

(3) **재시도·재계획·자기 평가** — 추가 50-200%

## 2-2. 본 테마 = 병목 파생형

| 인프라 축 | 산업기초 4+5 결론 | 에이전트 충격 후 |
|---|---|---|
| 반도체 | (A) 구조적 메가 병목 | **(A) 강화 + 병목 확산** — HBM에서 레거시 메모리·광통신·CPU·CoWoS로 |
| 전력 | (A) 구조적 메가 병목 (변압기·UHV) | **(A) 격화** — 미국 본토 capa 부족 + 가스터빈 capa 부족 노출 |

---

# Step 3. 테마 밸류체인 + 병목 구간 인뎁스 ★

> 절대 요약 X. 두 축 풍부한 밀도. 반도체 측 = HBM 비중 축소 + 4 신규 병목 중심.

## 3-1. 전체 밸류체인 4 layer

| Layer | 역할 | 대표 플레이어 | 본 분석 깊이 |
|---|---|---|---|
| (1) 모델·SW | LLM·에이전트 framework | Anthropic·OpenAI·Google·Meta·xAI / LangChain·MCP·Agent SDK | narrative driver — 깊이 X |
| (2) Agentic SaaS | 응용 | Cursor·Devin·Manus·Salesforce·ServiceNow·Replit·Copilot Studio | narrative driver — 깊이 X |
| (3) **반도체 인프라** | 추론 capa | 7개 sub-layer | ★ 인뎁스 |
| (4) **전력 인프라** | 데이터센터 전력 | 8개 sub-layer | ★ 인뎁스 |

## 3-2. [반도체 인프라 측] 병목 구간 인뎁스

### 3-2-1. HBM — 이미 시장 반영한 1단 병목 (축소)

| 항목 | 상세 |
|---|---|
| 점유 (2025 Q3) | SK 53%, 삼성 35%, Micron 11% |
| TAM | $35B (2025) → $100B (2028E), CAGR 40% |
| narrative 단계 | **이미 합의 반영** |

> 새 알파는 다음 4개 신규 병목.

### 3-2-2. 레거시 메모리 (DDR5 server + eSSD) — KV cache offload ★

**메커니즘**: 에이전트 토큰 폭증 → KV cache 폭발 → HBM 부족 → **NVIDIA Dynamo·vLLM이 KV cache를 DDR5·eSSD로 offload** → DDR5·eSSD "추론 active 메모리"로 격상.

**DDR5 server**:
| 정량 | 수치 |
|---|---|
| Samsung 32GB DDR5 (2025-09) | $149 → $239 (+60% 단월) |
| DRAM YTD (2025) | +50% |
| Q4 2025 추가 | +30% |
| 2026 1H 추가 | +20% |
| HBM의 wafer 소비 (DRAM 대비) | 3x per GB → 일반 DRAM squeeze |
| AI의 2026 DRAM 생산 소비 | 20%+ |
| SK하이닉스 capa | 2026까지 sold out |

**병목 카테고리**: **(A) 구조적 메가 병목**

**eSSD**:
| 정량 | 수치 |
|---|---|
| NAND 가격 (2025-01) | +65% MoM |
| eSSD Top 5 매출 (Q3) | $6.54B |
| eSSD Top 5 매출 (Q4 QoQ) | +50% |
| Samsung 점유 | 32.3% |
| SK Group | 30.2% (Q4 +75% QoQ) |
| Solidigm 122TB eSSD | KV cache offload·VectorDB tuning 용도 |

**병목 카테고리**: **(A) 구조적 메가 병목 → (D) 동반 확대** (신규 수요 + 공급 확대)

### 3-2-3. 광통신 — AI 클러스터 통신 병목 ★

**메커니즘**: NVIDIA GB200 NVL72 (72 GPU NVLink) → rack을 InfiniBand/Ethernet으로 → 수만 GPU 클러스터 → **광통신 throughput이 성능 결정**

| 항목 | 수치 |
|---|---|
| Datacom optical (2025) | $16B+ (+60% YoY) |
| 800G 모듈 shipment | +60% YoY |
| 1.6T 본격 양산 | 2026 (100만개 미만, NVIDIA·hyperscaler 한정) |
| Innolight 2024 매출 | $3.3B (+123%) |
| Innolight NVIDIA 800G 점유 | 50%+ |
| Lumentum 200G/lane EML 점유 | 50-60% (1.6T 핵심) |

**병목 카테고리**: **(A) 구조적 메가 병목** — EML/DSP 1-2사 과점

### 3-2-4. CPU (서버) ★

**메커니즘**: AI 서버 = GPU 8장 + host CPU 2장. 에이전트는 tool call·컨텍스트 관리 부담 비례 증가. Grace·GB200처럼 ARM CPU와 GPU 직접 결합도 표준화.

| 점유 (Q4 2025) | 수치 |
|---|---|
| Intel Xeon | **71%** (역대 최저) |
| AMD EPYC | **28.8%** (역대 최고, 5th Gen Q4 server 매출 50%+) |
| ARM (NVIDIA Grace·Ampere·AWS Graviton) | 13-15% |
| 2026 view | AMD 1위 가능 |

**한국 직접 노출**: ❌ (삼성 파운드리 일부 노드 위탁 간접)
**병목 카테고리**: **(B) 수요 견인 → (A) 구조적 메가 병목 진입** (AMD·ARM 공급 확대 단기 (B), 첨단 노드 wafer 제약으로 점진 (A)화)

### 3-2-5. 추론 GPU + ASIC

| 기업 | 제품 | 점유 (2025) | Moat |
|---|---|---|---|
| **NVIDIA** | Blackwell B100/B200/B300, Rubin (2026) | 추론 80%+ | CUDA 17년 |
| AMD | MI300X·MI350·MI400 | 5-10% | NVIDIA 외 유일 |
| Broadcom 디자인 ASIC | TPU·MTIA | hyperscaler 30%+ | Google·Meta |

**Blackwell 효율**: Hopper 대비 token cost 15x↓, throughput/MW 10x. Rubin (2026) 추가 10x. **Jevons 우세** (token cost 90% 감소에도 NVIDIA 매출 폭증)

### 3-2-6. CoWoS·첨단 패키징

| 항목 | 수치 |
|---|---|
| TSMC CoWoS 점유 | 85% (2025), 2026E 75% |
| CoWoS capa | 38K → 75K → **130K** wafer/월 (2024 말 → 2025 → 2026E) |

**한국 후공정 장비**: 한미반도체(TC본더 #1), 이오테크닉스, HPSP
**병목 카테고리**: **(A) 구조적 메가 병목**

### 3-2-7. 첨단 노드 wafer (TSMC N3/N2)

TSMC 3·2nm 90%+. Apple > NVIDIA > AMD > Broadcom > QCOM 알로케이션. Intel 18A Fab 52 양산. 삼성 2nm 시도.
**병목 카테고리**: **(A) 구조적 메가 병목**

## 3-3. [전력 인프라 측] 병목 구간 인뎁스

### 3-3-1. AI rack 전력 폭증

| 구분 | 전력 |
|---|---|
| 일반 데이터센터 rack | 15-25 kW |
| **GB200 NVL72 rack** | **~130 kW** (5-10x) |
| AI 데이터센터 단지 | 100-500 MW |
| hyperscaler 신규 캠퍼스 | 1-2 GW |

### 3-3-2. 글로벌 데이터센터 전력 수요 (IEA)

| 2024 | 2025 | 2030E | 2035E |
|---|---|---|---|
| 460 TWh | 485 TWh | **950 TWh (x2)** | 1,193 TWh |

미국 +240 TWh (+130%), 전력 증가의 ~50% 차지.

### 3-3-3. 변압기 병목 — Lead time 128주 ★

| 항목 | 수치 |
|---|---|
| 표준 변압기 lead time | 128주 (~2.5년) |
| GSU 변압기 | 144주 (~2.8년) |
| Hitachi Energy 대기 | 30개월+ |
| 공급 부족 | 2025 100% → 2030 <10% (2027-28까지 relief 없음) |

**병목 카테고리**: **(A) 구조적 메가 병목**

### 3-3-4. 가스 터빈 — 신규 부각 ★

원자력 2030+까지 못 들어옴 + 재생E 24/7 부족 → 단기 (2025-30) AI 데이터센터 전력 backbone은 천연가스.

| 거래 | 규모 |
|---|---|
| GE Vernova 1Q25 신규 주문 | 7 GW |
| GE-Crusoe AI | LM2500XPRESS 29기 |
| Chevron-GE | 4 GW (2027) |
| Siemens Energy YTD | 14 GW (60% 데이터센터) |
| Mitsubishi 1Q25 | 7 GW |
| 3사 capa 확대 | 2026부터 연 25-35% |

**병목 카테고리**: **(A) 구조적 메가 병목**

### 3-3-5. SMR — 2030+ 동반 확대 ★

| 거래 | 규모 | 시점 |
|---|---|---|
| Amazon-Talen Susquehanna | 1.92 GW PPA | 2042까지 |
| Amazon-Energy Northwest | 4 SMR, 320-960 MW | 2030+ |
| Microsoft-Constellation (TMI) | 837 MW | 2028 restart |
| Google-Kairos Power | 500 MW fleet | 2030+ |
| **Big Tech 합산** | **$10B+, 22 GW** | 첫 commercial 2030 |

**SMR 밸류체인 4 layer** (★ v3 확장):
1. **SMR 본체 개발사** — NuScale·Kairos·X-Energy·TerraPower·Holtec·Rolls-Royce SMR
2. **사업자/유틸리티** — Constellation·Talen·Vistra·Exelon
3. **SMR 부품 OEM (forging·압력용기·증기발생기)** — **두산에너빌리티**·Japan Steel Works·Sheffield Forgemasters
4. **EPC 시공** — Bechtel·Fluor·Worley·**현대건설**

**병목 카테고리**: **(D) 동반 확대** — 신규 시장 형성기

### 3-3-6. 액랭

| 항목 | 수치 |
|---|---|
| 시장 | $5.52B (2025) → $18.79B (2031), CAGR **22.65%** |
| Direct-to-chip 점유 | 42.85% |
| Vertiv | 11.3% (1위) |

**병목 카테고리**: **(D) 동반 확대**

### 3-3-7. UPS·스위치기어·HVDC·케이블

| 부문 | 글로벌 강자 (한국 포함) |
|---|---|
| UPS | Eaton, Schneider, Vertiv |
| 스위치기어·GIS | ABB, Siemens, Schneider, **LS ELECTRIC** |
| HVDC | Hitachi, Siemens, GE Vernova, ABB, **효성·HD현대일렉트릭** |
| 케이블 | Prysmian, Nexans, NKT, **LS·LS전선·대한전선** |

### 3-3-8. 800V DC 전환 — Rack 내부 전력 architecture 혁명 ★ 신규 (SemiAnalysis 2026-05-26 기반)

**왜 신규 부각인가**: NVIDIA Kyber Ultra **660kW/rack** (GB200 NVL72 130kW의 5x) → 기존 48V DC 분배는 물리법칙상 불가 (1MW 랙 = 구리 부스바 200kg, 11,111A). **800V DC 전환**이 물리적 강제. NVIDIA monopolar 800V reference 자체 규격화, Google·Meta·MSFT·AMZN 공동 **OCP Diablo 400 표준** (2025-05 v0.5.2).

**4 phase 전환 로드맵**:

| Phase | 시기 | 핵심 변화 | 신규 BoM |
|---|---|---|---|
| **1. White Space Retrofit** | 2026말~2027초 | 기존 415V AC 유지, **HVDC Power Rack (사이드카)**이 row 레벨 415V AC → 800V DC 정류 | Power Rack ($500K/MW, 기존 $40k의 10x) |
| **2. 800VDC-Native Compute** | 2027/2028 | NVIDIA Kyber rack부터 AC fallback 불가, on-blade 800V→50V 강압, UPS double conversion 제거 | Battery Rack ($200K/MW, BBU+supercap만) |
| **3. Centralized Rectifier** | 2028말/2029 | Grey space에 MW급 LV 정류기, AC PDU 사라짐, DC busway + **SSCB (SiC/GaN solid-state breaker)** | DC busway, SSCB |
| **4. SST (Solid State Transformer)** | >2029 | MV(13.8-45kV) → 800V DC 직접 변환, **무게 40x↓·부피 14x↓·효율 97%+** | SST ($1.0-1.5M/MW), Wolfspeed 10kV SiC MOSFET |

**핵심 정량**:
- 전류 14.8x 감소 → I²R 손실 **219x 감소** (48V 대비 278x)
- 시설 레벨 전력 **5% 절감** = 1GW 부하 기준 **연속 50MW** 절감
- 효율 경로: Baseline 82.0% → Phase 1 83.7% → Phase 2 86.5% → Phase 3 86.9% → Phase 4 87.4%

**시장 규모**:
- 사이드카 (HVDC Power Rack) TAM: 2028년 **~$11B** 정점 후 감소
- SST TAM: 2030년 **~$13B**
- 2030년 800VDC 누적 capacity **~39GW**
- SST 스타트업에 12개월 **$320M+** 자본 유입 (2025.3~2026.3)

**병목 카테고리**: **(D) 동반 확대** — 신규 시장 형성기, 2027/2028 Kyber 인플렉션이 트리거



| 단계 | Lead time |
|---|---|
| NVIDIA GPU 발주 | 6개월 |
| 부지 선정 | 12개월 |
| 전력 인입 신청 | 12-24개월 |
| **변압기 발주→납품 ★** | **24-36개월** (최대 bottleneck) |
| 발전 capa (PPA·SMR·가스터빈) | 24-60개월 |
| 데이터센터 건설 + 액랭 + UPS | 18-24개월 (병렬) |
| **전체 from-scratch** | **3-5년** |

## 3-4. 본 테마 병목 카테고리 분류 결론

> ★ 모든 카테고리 풀이 일괄 적용 (피드백 #5)

| Sub-segment | 카테고리 | 핵심 근거 |
|---|---|---|
| HBM | **(A) 구조적 메가 병목** | CR3 95%+, 단 이미 시장 반영 |
| 레거시 DRAM (DDR5 server) | **(A) 구조적 메가 병목** | HBM 우선 생산 squeeze + AI 추론. P +50% YTD |
| eSSD (NAND) | **(A) 구조적 메가 병목 → (D) 동반 확대** | KV cache offload 신규 수요 + 공급 확대 |
| 광통신 (800G/1.6T·EML) | **(A) 구조적 메가 병목** | EML/DSP 1-2사 과점 |
| CPU (server) | **(B) 수요 견인 → (A) 구조적 메가 병목 진입** | AMD·ARM 공급 확대, 첨단 노드 wafer 제약 |
| 추론 GPU·ASIC | **(A) 구조적 메가 병목** | NVIDIA 80%+, 첨단 노드 한정 |
| CoWoS·첨단 패키징 | **(A) 구조적 메가 병목** | TSMC 85%, 2026 capa 확대해도 부족 |
| 첨단 노드 wafer | **(A) 구조적 메가 병목** | TSMC 3/2nm 90%+ |
| 변압기·UHV | **(A) 구조적 메가 병목** | lead time 128주 |
| 가스터빈 | **(A) 구조적 메가 병목** | 3사 과점, lead time 2-3년 |
| 스위치기어·HVDC·케이블 | **(A) 구조적 메가 병목** | 글로벌 capa 부족 |
| UPS | **(B) 수요 견인** | 공급 적당 |
| SMR | **(D) 동반 확대** | 신규 시장 형성, 2030+ |
| 액랭 | **(D) 동반 확대** | 신규 시장, CAGR 22%+ |
| **★ 800VDC 전환 (HVDC Power Rack·SST·SSCB)** | **(D) 동반 확대** | NVIDIA Kyber Ultra 660kW가 물리적 강제. 사이드카 TAM $11B (2028), SST $13B (2030) |

**전체 결론**: **(A) 구조적 메가 병목 + (D) 동반 확대 hybrid**

---

# Step 4. Moat 기업 — Segment별 글로벌 통합 view ★

> 글로벌·한국 분할 X. 한국 기업도 글로벌 점유율 기준 평가. 🇰🇷 = 한국.

## 4-1. 반도체 인프라

### HBM
| # | 기업 | 국적 | 점유 (Q3 2025) | Moat |
|---|---|---|---|---|
| 1 | **SK하이닉스** | 🇰🇷 | 53% | HBM3E·HBM4 NVIDIA 단독 |
| 2 | **삼성전자** | 🇰🇷 | 35% | HBM3E 12단 추격 |
| 3 | Micron | 🇺🇸 | 11% | 미국 본토 |

### 레거시 DRAM (DDR5 server)
| # | 기업 | 국적 | 점유 | Moat |
|---|---|---|---|---|
| 1 | **삼성전자** | 🇰🇷 | ~42% | DRAM 종합 1위 |
| 2 | **SK하이닉스** | 🇰🇷 | ~33% | capa 2026까지 sold out |
| 3 | Micron | 🇺🇸 | ~24% | 추격 |

### eSSD
| # | 기업 | 국적 | 점유 (Q4) | Moat |
|---|---|---|---|---|
| 1 | **삼성전자** | 🇰🇷 | 32.3% | 서버 SSD 50% |
| 2 | **SK Group (SK하이닉스 + Solidigm)** | 🇰🇷 | 30.2% | 122TB eSSD, Q4 +75% QoQ |
| 3 | Kioxia | 🇯🇵 | ~15% | NAND 전문 |
| 4 | WD/SanDisk | 🇺🇸 | ~13% | NAND |
| 5 | Micron | 🇺🇸 | ~10% | SLC SSD 개발 |

### 광통신 트랜시버 (800G/1.6T)
| # | 기업 | 국적 | 점유 | Moat |
|---|---|---|---|---|
| 1 | Innolight | 🇨🇳 | NVIDIA 800G 50%+ | 시장 1위, 1.6T 우위 |
| 2 | Eoptolink | 🇨🇳 | 두 자릿수 | 데이터센터 |
| 3 | Coherent | 🇺🇸 | 두 자릿수 | DSP+EML |
| 4 | **오이솔루션** | 🇰🇷 | 한국 1위 + 일부 글로벌 | 1.6T OSFP·ITLA 국산화 |

### 광통신 핵심 부품 (EML laser·DSP)
| # | 기업 | 국적 | 점유 | Moat |
|---|---|---|---|---|
| 1 | Lumentum | 🇺🇸 | EML 50-60% | 1.6T 핵심 (200G/lane) |
| 2 | Coherent | 🇺🇸 | EML+DSP | 종합 |
| 3 | Broadcom | 🇺🇸 | DSP+Tomahawk | ASIC 통합 |
| 4 | Marvell | 🇺🇸 | DSP·SerDes | ASIC 협력 |

### 서버 CPU
| # | 기업 | 국적 | 점유 (Q4 2025) | Moat |
|---|---|---|---|---|
| 1 | Intel | 🇺🇸 | 71% | Xeon 6·18A 회복 시도 |
| 2 | AMD | 🇺🇸 | 28.8% | EPYC 5th Gen |
| 3 | ARM (NVIDIA Grace·Ampere·AWS Graviton) | 🇺🇸 | 13-15% | Grace Blackwell |

### 추론 GPU·ASIC
| # | 기업 | 국적 | 점유 | Moat |
|---|---|---|---|---|
| 1 | **NVIDIA** | 🇺🇸 | 추론 80%+ | CUDA·NVLink·Dynamo |
| 2 | AMD | 🇺🇸 | 5-10% | MI300X·MI350·MI400 |
| 3 | Broadcom ASIC | 🇺🇸 | hyperscaler 30%+ | Google·Meta |

### CoWoS·첨단 패키징 + 첨단 노드 wafer
| # | 기업 | 국적 | 점유 | Moat |
|---|---|---|---|---|
| 1 | **TSMC** | 🇹🇼 | CoWoS 85% / 3·2nm 90%+ | EUV+CoWoS+R&D |
| 2 | **삼성전자** | 🇰🇷 | 파운드리 #2 (7%) | 추격 |
| 3 | Intel Foundry | 🇺🇸 | 18A Fab 52 양산 | 본토 |

### 후공정 장비
| # | 기업 | 국적 | 점유 | Moat |
|---|---|---|---|---|
| 1 | **한미반도체** | 🇰🇷 | TC본더 글로벌 1위 | HBM 12·16-stack 핵심 |
| 2 | KLA | 🇺🇸 | 검사 1위 | 첨단 노드 |
| 3 | Camtek | 🇮🇱 | 검사 | HBM |
| 4 | **이오테크닉스** | 🇰🇷 | 레이저 강자 | HBM 후공정 |
| 5 | **HPSP** | 🇰🇷 | 고압수소 어닐링 단독 | 첨단 노드 |

### 전공정 장비
| # | 기업 | 국적 | 점유 | Moat |
|---|---|---|---|---|
| 1 | ASML | 🇪🇺(NL) | EUV 100% | 노광 절대 독점 |
| 2 | Applied Materials | 🇺🇸 | 증착·식각 1위 | 종합 |
| 3 | Lam Research | 🇺🇸 | 식각·증착 | 메모리 강자 |
| 4 | Tokyo Electron | 🇯🇵 | 코터·디벨로퍼 단독 | EUV 종속 |
| 5 | KLA | 🇺🇸 | 검사 1위 | 첨단 노드 |

## 4-2. 전력 인프라

### UHV 변압기 (북미)
| # | 기업 | 국적 | 점유/특기 | Moat |
|---|---|---|---|---|
| 1 | Hitachi Energy | 🇯🇵/🇨🇭 | 글로벌 1위 | lead time 30개월+ |
| 2 | GE Vernova | 🇺🇸 | 미국 본토 strongest | 본토+IRA |
| 3 | Siemens Energy | 🇪🇺(DE) | 유럽·글로벌 | 종합 |
| 4 | **효성중공업** | 🇰🇷 | 미국 765kV 1위, capa 2배 | UHV·POSCO GOES |
| 5 | **HD현대일렉트릭** | 🇰🇷 | 미국 M/S 15-20% | UHV+회전기기 |

### 스위치기어·GIS
| # | 기업 | 국적 | 점유 | Moat |
|---|---|---|---|---|
| 1 | Schneider Electric | 🇪🇺(FR) | 1위 | 종합 |
| 2 | Eaton | 🇺🇸 | 1-2위 | UPS+스위치기어 |
| 3 | ABB | 🇪🇺(CH) | 메이저 | 산업·전력 |
| 4 | Siemens | 🇪🇺(DE) | 메이저 | 종합 |
| 5 | **LS ELECTRIC** | 🇰🇷 | 국내 1위, 글로벌 7-8위 + ★ **DC 분야 선도** | 스위치기어+UHV + **UL 인증 1500V DC MCCB 최초 데이터센터용** (ABB Emax 2와 나란히, SemiAnalysis 2026-05-26) |

### ★ 800VDC 전환 — HVDC Power Rack · SST · SSCB · DC busway (v4 신규)
| # | 기업 | 국적 | 역할 | Moat |
|---|---|---|---|---|
| 1 | **NVIDIA** | 🇺🇸 | spec 자체 정의 | 800V monopolar reference, Vera Rubin·Kyber·Kyber Ultra 660kW |
| 2 | **Delta** | 🇹🇼 | Power Rack BoM 1위 | 110kW PSU shelf, 80kW BBU, 2.4MW In-Row CDU |
| 3 | **DG Matrix** | 🇺🇸 (ABB-backed) | SST 선도 스타트업 | NVIDIA MGX 유일 SST, Infineon SiC, Q2 2026 UL |
| 4 | **ABB** | 🇪🇺 (CH) | Incumbent | Emax 2 1500V DC, SACE Infinitus solid-state (NVIDIA 협업) |
| 5 | **Eaton** | 🇺🇸 | Incumbent | Resilient Power Systems 2025-08 인수 |
| 6 | **Wolfspeed** | 🇺🇸 | 핵심 반도체 | 10kV SiC MOSFET 2026-03 상용화, MV 정류 게이트키퍼 |
| 7 | Infineon | 🇪🇺 (DE) | 핵심 반도체 | BBU 4kW PPC → 12kW @ 99.5%, SST용 SiC |
| 8 | TE Connectivity | 🇺🇸 | busbar | Power Rack 표준 busbar |
| 9 | Amperesand·Heron Power·Novos Power | 🇺🇸 | SST 스타트업 | 12개월 $320M+ 자본 유입 |
| 10 | **LS ELECTRIC** | 🇰🇷 | ★ **한국 선도** | **UL 인증 1500V DC MCCB 최초 데이터센터용**, DistribuTECH 2026 DC 전력장비 전시 |
| 11 | Hyperscaler 공저 | 🇺🇸 | 표준화 | Google·Meta·MSFT·AMZN **OCP Diablo 400** (2025-05 v0.5.2) |

> **800VDC 차세대 architecture**의 한국 직접 노출: **LS ELECTRIC만 본문 명시** (SemiAnalysis 2026-05-26). DC MCCB·DC busway·SSCB 분야 초기 진입 권리 확보. 효성·HD현대일렉은 본 segment 직접 노출 미공식.

### HVDC 송전
| # | 기업 | 국적 | 점유 | Moat |
|---|---|---|---|---|
| 1 | Hitachi Energy | 🇯🇵/🇨🇭 | 1위 | HVDC+변압기 |
| 2 | Siemens Energy | 🇪🇺(DE) | 1-2위 | 종합 |
| 3 | GE Vernova | 🇺🇸 | 메이저 | 본토 |
| 4 | ABB | 🇪🇺(CH) | 메이저 | 종합 |
| 5 | **효성·HD현대일렉** | 🇰🇷 | 한국+일부 해외 | UHV+HVDC 통합 |

### 가스 터빈
| # | 기업 | 국적 | 점유 | Moat |
|---|---|---|---|---|
| 1 | GE Vernova | 🇺🇸 | 1-2위 (3사 capa 2/3) | Crusoe·Chevron |
| 2 | Siemens Energy | 🇪🇺(DE) | 1-2위, 14 GW YTD | 60% 데이터센터 |
| 3 | Mitsubishi Power | 🇯🇵 | 3위, 1Q25 7 GW | capa 2배 |

### 케이블 (초고압·해상풍력)
| # | 기업 | 국적 | 점유 | Moat |
|---|---|---|---|---|
| 1 | Prysmian | 🇪🇺(IT) | 1위 | 종합 |
| 2 | Nexans | 🇪🇺(FR) | 1-2위 | 해상 |
| 3 | NKT | 🇪🇺(DK) | 해상 강자 | HVDC |
| 4 | **LS·LS전선** | 🇰🇷 | 글로벌 4-5위 | 초고압·해상풍력 |
| 5 | **대한전선** | 🇰🇷 | 한국+미국·중동 | 초고압 |

### 액랭
| # | 기업 | 국적 | 점유 | Moat |
|---|---|---|---|---|
| 1 | Vertiv | 🇺🇸 | 11.3% | DC 인프라 통합 |
| 2 | Schneider | 🇪🇺(FR) | 11% | Motivair 인수 |
| 3 | Rittal·Stulz·Boyd 등 | 🇪🇺·🇺🇸 | 합 13% | specialty |

### SMR ★ 4 layer (피드백 #9 — 두산·현대건설 포함)

#### Layer 1. SMR 본체 개발사
| # | 기업 | 국적 | 점유 | Moat |
|---|---|---|---|---|
| 1 | NuScale | 🇺🇸 | NRC 인허가 선두 | SMR 선두 |
| 2 | Kairos Power | 🇺🇸 | Google 500 MW PPA | molten salt |
| 3 | X-Energy | 🇺🇸 | Amazon 협력 | TRISO 연료 |
| 4 | TerraPower (Bill Gates) | 🇺🇸 | Natrium | sodium 냉각 |
| 5 | Holtec | 🇺🇸 | SMR-300, 폴란드 | small footprint |
| 6 | Rolls-Royce SMR | 🇬🇧 | 영국 정부 지원 | 유럽 시장 |

#### Layer 2. 사업자·유틸리티 (PPA 직접 수혜)
| # | 기업 | 국적 | Moat |
|---|---|---|---|
| 1 | Constellation | 🇺🇸 | MSFT TMI 837 MW restart |
| 2 | Talen Energy | 🇺🇸 | AWS Susquehanna 1.92 GW |
| 3 | Vistra | 🇺🇸 | 기존 원전 + SMR 통합 |
| 4 | Energy Northwest | 🇺🇸 | Amazon X-Energy 협력 |

#### Layer 3. SMR 부품 OEM (forging·압력용기·증기발생기) ★ 신규
| # | 기업 | 국적 | 점유 | Moat |
|---|---|---|---|---|
| 1 | **두산에너빌리티** | 🇰🇷 | **글로벌 5-6사 중 1** | **NuScale Power Module 핵심 forging 단독 공급, X-Energy 협력 (2024)**. 모든 SMR 양산이 forging capa에 의존 |
| 2 | Japan Steel Works (JSW) | 🇯🇵 | 글로벌 메이저 | 원자로 압력용기 |
| 3 | Sheffield Forgemasters | 🇬🇧 | 영국 메이저 | Rolls-Royce SMR 협력 |
| 4 | China First Heavy Industries | 🇨🇳 | 중국 내수 | 중국 SMR 부품 |
| 5 | Mitsubishi Heavy Industries (MHI) | 🇯🇵 | 일본 메이저 | 일본 SMR 부품 |

#### Layer 4. EPC 시공
| # | 기업 | 국적 | 점유 | Moat |
|---|---|---|---|---|
| 1 | Bechtel | 🇺🇸 | 글로벌 1위 EPC | NuScale·X-Energy 협력 |
| 2 | Fluor | 🇺🇸 | NuScale 주요 EPC | NuScale 지분 보유 |
| 3 | Worley | 🇦🇺 | 글로벌 메이저 | engineering services |
| 4 | **현대건설** | 🇰🇷 | 한국 + 글로벌 진출 | **Holtec SMR-300 협력 (한·미·폴란드), 한국 차세대 원전 시공** |
| 5 | 삼성E&A·대우건설·DL이앤씨 등 | 🇰🇷 | 한국 시장 | 한국 SMR 진입 시 EPC 후보 |

## 4-3. 다음 [기업 분석 모드] 우선 권장

| 우선 | 기업 | Segment 글로벌 위치 | 분석 가치 |
|---|---|---|---|
| 1 | **SK하이닉스** | HBM #1 + DDR5 #2 + eSSD #2 (3 segment Top 2) | 메모리 종합 Moat |
| 2 | **한미반도체** | TC본더 글로벌 #1 | 단일 segment 1위 |
| 3 | **삼성전자** | DRAM #1 + eSSD #1 + HBM #2 + 파운드리 #2 (4 segment Top 2) | multi-axis |
| 4 | **효성중공업** | UHV 변압기 미국 #1 + HVDC | 미국 1위 |
| 5 | **HD현대일렉트릭** | UHV 미국 15-20% + 회전기기 | 변압기+발전 |
| 6 | **LS ELECTRIC** ★ v4 강화 | 스위치기어 글로벌 7-8 + **★ DC 분야 한국 선도 (UL 1500V DC MCCB 최초)** | 스위치기어+UHV + **800VDC 전환 직접 노출** |
| 7 | **오이솔루션** | 1.6T·ITLA 국산화 | 광통신 단일 |
| 8 | **두산에너빌리티** ★ 신규 | **SMR forging 글로벌 5사 중 1** | NuScale·X-Energy 부품 단독 |
| 9 | **현대건설** ★ 신규 | SMR EPC Holtec 협력 | 한·미·폴란드 SMR 진입 |
| 10 | NVIDIA·TSMC·Hitachi Energy·Innolight·GE Vernova | 글로벌 1-2위 | 별도 분석 |

---

# Step 5. 시장 규모 — 16 Segment TAM 시간축 PQ ★

> **★ v3 신구조** (피드백 #7·#8): 각 segment 별 **P 분기 (2Q25E~1Q26E) + P 연간 (2026E·2027E) + Q 분기 + Q 연간 + 변동 근거** 분리. 컴팩트 표기.

## 5-1. 반도체 8 Segment

| # | Segment | TAM (2025→2028E) | **P 4Q (2Q25E~1Q26E)** | **P 2Y (2026·2027)** | **Q 4Q** | **Q 2Y** | **근거 (P / Q)** | 글로벌 1-5위 |
|---|---|---|---|---|---|---|---|---|
| 1 | HBM | $35B → $100B (CAGR 40%) | +5·+3·+2·0% | +8·0% | +10·10·8·8% | +40·30% | **P**: HBM4 mix↑·신규 capa로 둔화 / **Q**: NVIDIA Rubin·hyperscaler allocation | SK·삼성·Micron |
| 2 | 레거시 DRAM (DDR5) | $60B → $120B+ (25%+) | +30·20·15·10% | +30·0% | +5·5·5·5% | +25·15% | **P**: HBM squeeze·재고 정상화 / **Q**: AI 서버 + KV cache offload | 삼성·SK·Micron |
| 3 | eSSD | $25-30B → $60B+ (30%+) | +20·15·10·8% | +25·10% | +15·20·20·25% | +50·40% | **P**: NAND 사이클 + AI premium / **Q**: KV cache offload·VectorDB·체크포인트 | 삼성·SK Group·Kioxia·WD·Micron |
| 4 | 추론 GPU·ASIC | $100B → $250B+ (30%+) | +5·+3·+3·+3% | +5·+3% | +20·25·25·20% | +35·25% | **P**: Blackwell→Rubin 노드 transition / **Q**: hyperscaler capex $700B·에이전트 추론 | NVIDIA·AMD·Broadcom ASIC |
| 5 | 광통신 (트랜시버) | $16B → $35B+ (30%+) | +3·+5·+8·+10% | +15·+8% | +20·25·30·35% | +60·40% | **P**: 1.6T mix↑·EML 부족 / **Q**: 800G shipment +60%·1.6T 본격 2026 | Innolight·Eoptolink·Coherent·Lumentum·오이솔루션 |
| 6 | 서버 CPU | $25-30B → $50B+ (15-20%) | +5·+5·+5·+5% | +10·+8% | +10·12·12·15% | +25·20% | **P**: AMD EPYC premium·ARM share↑ / **Q**: AI 서버 1대당 CPU 2장·ARM 확장 | Intel·AMD·ARM |
| 7 | CoWoS·첨단 패키징 | $5-7B → $15-20B+ (30%+) | +5·+5·+5·+5% | +10·+5% | +25·25·25·25% | +60·40% | **P**: TSMC 가격·capa 부족 premium / **Q**: capa 75K→130K wafer/월 | TSMC·Amkor·Intel·삼성 진입 — 한미·이오 (장비) |
| 8 | 첨단 노드 wafer | $50B+ → $100B+ (25%+) | +3·+3·+5·+5% | +12·+10% | +10·15·15·15% | +30·25% | **P**: 노드 transition (3→2nm) +10-15% / **Q**: Apple·NVIDIA·AMD 동시 수요 | TSMC·삼성·Intel |

## 5-2. 전력 8 Segment

| # | Segment | TAM | **P 4Q (2Q25E~1Q26E)** | **P 2Y (2026·2027)** | **Q 4Q** | **Q 2Y** | **근거 (P / Q)** | 글로벌 1-5위 |
|---|---|---|---|---|---|---|---|---|
| 1 | 변압기 (UHV+일반) | $40B → $80B+ (12-15%) | +8·+8·+5·+5% | +15·+10% | +8·8·10·10% | +25·20% | **P**: GOES 강판·인력·lead time 128주 / **Q**: 한국 3사 capa 2배 확대 (2027-28부터) | Hitachi·GE·Siemens·효성·HD현대일렉 |
| 2 | 스위치기어·GIS | $50B+ → $80B+ (8-12%) | +3·+3·+3·+3% | +5·+3% | +8·10·10·12% | +18·15% | **P**: 안정 / **Q**: 데이터센터 + 그리드 노후화 교체 | Schneider·Eaton·ABB·Siemens·LS ELECTRIC |
| 3 | HVDC | $15B+ → $40B+ (20%+) | +5·+5·+8·+8% | +12·+10% | +15·18·20·22% | +30·25% | **P**: 대규모 프로젝트 단가↑ / **Q**: 재생E 통합·해상풍력 | Hitachi·Siemens·GE·ABB·효성·HD |
| 4 | 케이블 (초고압·해상) | $30B+ → $50B+ (12-15%) | +5·+5·+5·+8% | +10·+8% | +10·12·15·15% | +25·20% | **P**: 동·알루미늄 + 해상풍력 premium / **Q**: 해상풍력 + DC 인입 | Prysmian·Nexans·NKT·LS·LS전선·대한전선 |
| 5 | UPS+ESS | $15+$20B → $30+$50B (15%·25%) | +2·+2·+2·+3% (UPS) / +5·+5·+5·+5% (ESS) | +5·+3% / +10·+8% | +12·15·15·15% (UPS) / +20·25·25·25% (ESS) | +20·15% / +50·35% | **P**: 안정 (UPS), ESS 배터리 가격↓·시스템 premium / **Q**: DC + 재생E 통합 | Schneider·Eaton·Vertiv (UPS) / LG·Samsung·CATL (ESS) |
| 6 | 액랭 | $5.52B → $18.79B (22.65%) | +2·+2·+3·+3% | +5·+5% | +25·30·30·30% | +60·50% | **P**: 안정·CAGR premium / **Q**: GB200 130 kW rack 필수, hyperscaler 전환 가속 | Vertiv·Schneider·Rittal·Stulz·Boyd |
| 7 | 가스 터빈 | $50B → $80B+ (10-15%) | +8·+8·+5·+5% | +15·+10% | +15·18·20·22% | +30·25% | **P**: 3사 과점·premium / **Q**: GE 7+Siemens 14+Mitsubishi 7 = 28 GW (1Q25)·capa 25-35%↑ | GE·Siemens·Mitsubishi |
| 8 | **원자력+SMR** (★ 4 layer 통합) | $10B+ commit → $30B+ (2035) | n/a (PPA 기반) | n/a | (개발사) 본격 매출 2028+ / (부품) **두산 즉시 매출 +20%/yr** / (EPC) 단계별 | (부품·EPC) +25·20% | **P**: PPA 고정 / **Q**: 22 GW 개발 중, Big Tech $10B+. **부품 (두산) Q는 2025-27부터 가시화** | (본체) NuScale·Kairos·X-Energy·TerraPower·Holtec·Rolls-Royce / (사업자) Constellation·Talen·Vistra / (부품) **두산에너빌리티**·JSW·Sheffield / (EPC) Bechtel·Fluor·**현대건설** |
| **9** | **★ 800VDC 전환 (HVDC Power Rack·SST·SSCB·DC busway)** | **사이드카 $11B (2028) / SST $13B (2030)** | (D) 동반 확대 | Power Rack ASP $500K/MW (기존 AC $40k의 10x), SST $1-1.5M/MW | n/a | 2030 39GW 누적 | **P**: 신규 architecture premium / **Q**: 2027/2028 Kyber 인플렉션부터 본격, NEC 2029 부분/2032 완전 | NVIDIA·Delta·DG Matrix·ABB·Eaton·Wolfspeed·Infineon·TE Connectivity / **LS ELECTRIC (한국 선도, UL 1500V DC MCCB 최초)** |

## 5-3. 한국 접근 가능 TAM 합산 (2028E)

| Segment | 한국 접근 TAM | 주요 한국 점유 |
|---|---|---|
| HBM | $50-60B | SK·삼성 합 88% |
| 레거시 DRAM | $90B+ | 삼성·SK 합 75% |
| eSSD | $35-40B | 삼성·SK Group 합 62% |
| 광통신 (한국 일부) | $1-2B | 오이솔루션 |
| 후공정 장비 | $5-8B | 한미·이오·HPSP |
| 변압기 (북미 수출) | $12-16B | 효성·HD·LS·제룡 합 15-20% |
| 스위치기어 | $5-8B | LS ELECTRIC |
| HVDC | $2-4B | 효성·HD |
| 케이블 | $5-7B | LS·대한 |
| ESS | $5-7B | LG에너지·삼성SDI 일부 |
| **SMR forging** | **$3-5B** | **두산에너빌리티 (글로벌 5사 중 1)** |
| **SMR EPC** | **$2-4B** | **현대건설·삼성E&A** |
| **★ 800VDC DC switchgear/MCCB (v4 신규)** | **$1-2B** | **LS ELECTRIC (UL 1500V DC MCCB 최초, 한국 유일 본문 명시)** |
| **합계** | **$216-262B+** | 한국 실제 점유 **$96-117B+** (글로벌 TAM의 10-15%) |

---

# Step 6. 산업 유형 + 주도 섹터 가능성

| 항목 | 결론 |
|---|---|
| 산업 유형 | **메가 트렌드** (AI 슈퍼사이클 2단) |
| 단계 | 초기-중기 (2024-25 narrative → 2026-2030+ Q 폭발) |
| 글로벌 트렌드 관통 + 한국 Moat | ★★★ — 17 segment 중 **10 segment 한국 글로벌 Top 5** (SMR 부품 + 800VDC LS ELECTRIC 추가), 5 segment Top 2 |
| **주도 섹터 가능성** | **★★★ 매우 높음** |

---

# Step 7. 리스크 팩터

| 리스크 | 확률 | 임팩트 | 시그널 |
|---|---|---|---|
| 에이전트 narrative 약화 | 25% | 매우 큼 | Anthropic·OpenAI ARR 정체 |
| AI capex 변곡점 | 25% | 큼 (12-18개월 침체) | hyperscaler capex 가이던스 하향 |
| 추론 효율 급격 개선 | 50% (진행) | 양면 (Jevons vs reset) | 2027-28 확인 |
| 메모리 가격 하락 reset | 20% | 큼 | DRAM YoY 둔화 |
| 미·중 디커플링 강화 | 30% | 중 | 추가 수출규제 |
| 광통신 CPO 빠른 채택 | 30% | 중 | NVIDIA CPO 전환 |
| 변압기·가스터빈 capa 글로벌 경쟁 | 15% | 중 (5-7년 후) | 인도·동남아 진입 |
| 원자력 정치 risk (SMR 인허가) | 20% | 중 | NRC·정부 지연 |
| 에이전트 안전성 사고 | 30% | 중-큼 | 대규모 사고 |

---

# Step 8. 트래킹 지표

## 수요 측 (에이전트 채택)
- Anthropic·OpenAI API 매출 (분기), Cursor·Devin·Manus ARR, Token consumption per agent (Stanford), GitHub Copilot·Cursor 활성 사용자

## 반도체 측
- NVIDIA 데이터센터 segment, NVIDIA Blackwell allocation, TSMC CoWoS capa expansion, HBM 가격 (TrendForce), **DDR5 server 가격 (DRAMeXchange) ★**, **eSSD Top 5 분기 매출 (TrendForce) ★**, **800G/1.6T 트랜시버 shipment (Cignal AI) ★**, **서버 CPU 점유 (Mercury Research) ★**, HBM4 양산, 삼성 HBM3E 12단 NVIDIA 인증

## 전력 측
- 변압기 lead time (Powermag·Nikkei), 한국 변압기 3사 분기 수주, 3사 수주잔고, **가스터빈 3사 분기 신규 주문 (GE·Siemens·Mitsubishi) ★**, SMR 신규 PPA (Constellation·Talen·Vistra·Kairos), **두산에너빌리티 SMR 부품 수주 ★**, **현대건설 Holtec 협력 진행 ★**, IEA 데이터센터 전력, hyperscaler 분기 capex
