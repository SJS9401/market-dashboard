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
active_companies:
  dominant:    # 현재 테마 패권 보유 (Moat 4.0+, 점유 #1-2 또는 기술 리더)
    - {ticker: "NVDA", name: "NVIDIA", country: US, moat: 4.8, theme_relevance: high}
    - {ticker: "000660", name: "SK하이닉스", country: KR, moat: 4.4, theme_relevance: high}
    - {ticker: "005930", name: "삼성전자", country: KR, moat: 4.3, theme_relevance: high}
    - {ticker: "ARM", name: "ARM Holdings", country: UK_JP, moat: 4.1, theme_relevance: high}
    - {ticker: "STX", name: "Seagate", country: US, moat: 4.1, theme_relevance: high}
    - {ticker: "WDC", name: "Western Digital", country: US, moat: 4.0, theme_relevance: high}
    - {ticker: "SNDK", name: "SanDisk", country: US, moat: 4.0, theme_relevance: high}
    - {ticker: "MU", name: "Micron", country: US, moat: 4.0, theme_relevance: high}
  challenger:  # 패권 도전 중 (Moat 3.8-4.0, 빠른 성장)
    - {ticker: "AMD", name: "AMD", country: US, moat: 3.8, theme_relevance: high}
    - {ticker: "INTC", name: "Intel", country: US, moat: 2.8, theme_relevance: high}
  macro_layer:  # 수요 측 빅테크 (4사, CapEx + AI ARR baseline)
    - {ticker: "MSFT", name: "Microsoft", country: US, role: macro_demand, ai_arr_FY26: "$37B", capex_CY26: "$190B"}
    - {ticker: "GOOGL", name: "Google (Alphabet)", country: US, role: macro_demand, ai_arr_FY26: "$30B+", capex_CY26: "$100B"}
    - {ticker: "AMZN", name: "Amazon (AWS)", country: US, role: macro_demand, ai_arr_FY26: "$25B+", capex_CY26: "$195B"}
    - {ticker: "META", name: "Meta", country: US, role: macro_demand, ai_arr_FY26: "$30B", capex_CY26: "$100B"}
sunset_companies: []
last_updated: 2026-07-27 (v5.1 — 한국 Neocloud/AI Factory segment 신설 + SF AI Summit 패키지 반영)
last_theme_review_date: null
narrative_shift_log:
  - {date: 2024-Q4, event: "Anthropic Claude 3.5 Computer Use 공개 — 에이전트 진입 신호탄"}
  - {date: 2025-Q1, event: "OpenAI Operator·Manus AI 출시 — 에이전트 narrative 시장 확산"}
  - {date: 2025-H2, event: "에이전트 작업 1건 = chat 대비 토큰 20-30x 실측 확인 (Stanford·NVIDIA)"}
  - {date: 2025-Q3, event: "NAND +65% MoM, DDR5 +50% YTD — 레거시 메모리 병목 narrative 부상"}
  - {date: 2025-Q4, event: "Big Tech 2026 capex $700B 합의"}
  - {date: 2026-Q2, event: "★ NVIDIA Kyber Ultra 660kW/rack 발표 (GB200 NVL72 130kW의 5x) — 48V→800V DC 전환 물리적 강제"}
  - {date: 2026-Q2, event: "★ SemiAnalysis '800VDC Revolution Part 1' 발행 (2026-05-26) — HVDC Power Rack·SST narrative 본격화. OCP Diablo 400 표준 형성"}
  - {date: 2026-Q1, event: "★ AWS OpenAI 2GW Trainium 신규 deal — MSFT-OpenAI 독점 깨는 evidence"}
  - {date: 2026-Q1, event: "★ NVIDIA 자본 정책 게임 체인저 (배당 25배 + $80B buyback) — secular + 자본환원 hybrid 진입"}
  - {date: 2026-Q1, event: "★ 4사 macro layer 합산 CapEx $585B (FY25 $258B 대비 +127%) — AI 인프라 사이클 정점 미도래 정량 시그널"}
  - {date: 2026-Q1, event: "★ Meta MI450 6GW + 6th Gen EPYC lead = AMD thesis 단독 driver"}
  - {date: 2026-Q2, event: "★ v5 (2026-06-21): 14개사 기업 분석 통합본 작성 — 반도체 10 + 빅테크 4 + Terminal 시나리오 3년/5년 dual horizon"}
  - {date: 2026-Q2, event: "★ 네이버+NVIDIA 기가와트급 AI Factory 발표 (2026-06-08) — 'Asian CoreWeave' narrative 형성"}
  - {date: 2026-Q3, event: "★ SF AI Summit 한국 sovereign AI 패키지 (2026-07-24~25): NVIDIA $1B Naver 투자 + Brookfield $9B + SK LTA 5년 $750B + 삼성-Broadcom $200B + NVIDIA-SK Group 2GW DC"}
  - {date: 2026-Q3, event: "★ v5.1 (2026-07-27): #18 segment 신설 — 한국 Neocloud/AI Factory (sovereign AI), 카테고리 (D). 한국 접근 TAM $226-277B+ 상향. NAVER 기업분석 클라우드 세션 핸드오프"}
---

# 에이전트AI 테마 분석 (v4)

> **본 테마의 분석 frame**: 에이전트AI는 스토리(narrative)-driven 키워드. 그 narrative가 가져오는 충격(토큰 N배 폭증)이 **추론 인프라**에 집중되고, 추론 인프라는 **반도체 + 전력** 두 축. HBM은 이미 시장이 반영했고 **신규 병목은 레거시 메모리·광통신·CPU·CoWoS**로 이동.

> **점유율·CAPA 표기 기준**: 본 분석(테마/기업 분석 공통)의 모든 % 점유율은 **매출 기준** (TrendForce·Counterpoint·Astute Group 등 메모리 시장 분석 표준 metric). **CAPA는 wafer 기준** (산업 통계, K wafer/월). bit 출하 기준 점유는 분기 변동성이 커서 본 분석에서는 다루지 않음.

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
| **Step 1. 정의·트렌드** | AI 메가 트렌드 안의 에이전트 스토리(narrative). 형제자매: HBM·온디바이스AI·추론최적화·AI데이터센터전력 |
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
| 입출력 구조 | 1 요청 → 1 응답 | 지시 → multi-step plan → 도구 호출(tool call) → ... → 자체 종료 |
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
| (1) 모델·SW | LLM·에이전트 framework | Anthropic·OpenAI·Google·Meta·xAI / LangChain·MCP·Agent SDK | 스토리(narrative) driver — 깊이 X |
| (2) Agentic SaaS | 응용 | Cursor·Devin·Manus·Salesforce·ServiceNow·Replit·Copilot Studio | 스토리(narrative) driver — 깊이 X |
| (3) **반도체 인프라** | 추론 capa | 7개 sub-layer | ★ 인뎁스 |
| (4) **전력 인프라** | 데이터센터 전력 | 8개 sub-layer | ★ 인뎁스 |

## 3-2. [반도체 인프라 측] 병목 구간 인뎁스

### 3-2-1. HBM — 이미 시장 반영한 1단 병목 (축소)

| 항목 | 상세 |
|---|---|
| 점유 (2025 Q3) | SK 53%, 삼성 35%, Micron 11% |
| TAM | $35B (2025) → $100B (2028E), CAGR 40% |
| 스토리(narrative) 단계 | **이미 합의 반영** |

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
| SK하이닉스 capa | 2026까지 공급 매진 |

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
| 800G 모듈 출하 | +60% YoY |
| 1.6T 본격 양산 | 2026 (100만개 미만, NVIDIA·하이퍼스케일러 한정) |
| Innolight 2024 매출 | $3.3B (+123%) |
| Innolight NVIDIA 800G 점유 | 50%+ |
| Lumentum 200G/lane EML 점유 | 50-60% (1.6T 핵심) |

**병목 카테고리**: **(A) 구조적 메가 병목** — EML/DSP 1-2사 과점

### 3-2-4. CPU (서버) ★

**메커니즘**: AI 서버 = GPU 8장 + host CPU 2장. 에이전트는 도구 호출(tool call)·컨텍스트 관리 부담 비례 증가. Grace·GB200처럼 ARM CPU와 GPU 직접 결합도 표준화.

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
| Broadcom 디자인 ASIC | TPU·MTIA | 하이퍼스케일러 30%+ | Google·Meta |

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
| 하이퍼스케일러 신규 캠퍼스 | 1-2 GW |

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
| 2 | **SK하이닉스** | 🇰🇷 | ~33% | capa 2026까지 공급 매진 |
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
| 3 | Broadcom ASIC | 🇺🇸 | 하이퍼스케일러 30%+ | Google·Meta |

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
| 1 | HBM | $35B → $100B (CAGR 40%) | +5·+3·+2·0% | +8·0% | +10·10·8·8% | +40·30% | **P**: HBM4 mix↑·신규 capa로 둔화 / **Q**: NVIDIA Rubin·하이퍼스케일러 allocation | SK·삼성·Micron |
| 2 | 레거시 DRAM (DDR5) | $60B → $120B+ (25%+) | +30·20·15·10% | +30·0% | +5·5·5·5% | +25·15% | **P**: HBM squeeze·재고 정상화 / **Q**: AI 서버 + KV cache offload | 삼성·SK·Micron |
| 3 | eSSD | $25-30B → $60B+ (30%+) | +20·15·10·8% | +25·10% | +15·20·20·25% | +50·40% | **P**: NAND 사이클 + AI 프리미엄 / **Q**: KV cache offload·VectorDB·체크포인트 | 삼성·SK Group·Kioxia·WD·Micron |
| 4 | 추론 GPU·ASIC | $100B → $250B+ (30%+) | +5·+3·+3·+3% | +5·+3% | +20·25·25·20% | +35·25% | **P**: Blackwell→Rubin 노드 transition / **Q**: 하이퍼스케일러 capex $700B·에이전트 추론 | NVIDIA·AMD·Broadcom ASIC |
| 5 | 광통신 (트랜시버) | $16B → $35B+ (30%+) | +3·+5·+8·+10% | +15·+8% | +20·25·30·35% | +60·40% | **P**: 1.6T mix↑·EML 부족 / **Q**: 800G 출하 +60%·1.6T 본격 2026 | Innolight·Eoptolink·Coherent·Lumentum·오이솔루션 |
| 6 | 서버 CPU | $25-30B → $50B+ (15-20%) | +5·+5·+5·+5% | +10·+8% | +10·12·12·15% | +25·20% | **P**: AMD EPYC 프리미엄·ARM share↑ / **Q**: AI 서버 1대당 CPU 2장·ARM 확장 | Intel·AMD·ARM |
| 7 | CoWoS·첨단 패키징 | $5-7B → $15-20B+ (30%+) | +5·+5·+5·+5% | +10·+5% | +25·25·25·25% | +60·40% | **P**: TSMC 가격·capa 부족 프리미엄 / **Q**: capa 75K→130K wafer/월 | TSMC·Amkor·Intel·삼성 진입 — 한미·이오 (장비) |
| 8 | 첨단 노드 wafer | $50B+ → $100B+ (25%+) | +3·+3·+5·+5% | +12·+10% | +10·15·15·15% | +30·25% | **P**: 노드 transition (3→2nm) +10-15% / **Q**: Apple·NVIDIA·AMD 동시 수요 | TSMC·삼성·Intel |

## 5-2. 전력 8 Segment

| # | Segment | TAM | **P 4Q (2Q25E~1Q26E)** | **P 2Y (2026·2027)** | **Q 4Q** | **Q 2Y** | **근거 (P / Q)** | 글로벌 1-5위 |
|---|---|---|---|---|---|---|---|---|
| 1 | 변압기 (UHV+일반) | $40B → $80B+ (12-15%) | +8·+8·+5·+5% | +15·+10% | +8·8·10·10% | +25·20% | **P**: GOES 강판·인력·lead time 128주 / **Q**: 한국 3사 capa 2배 확대 (2027-28부터) | Hitachi·GE·Siemens·효성·HD현대일렉 |
| 2 | 스위치기어·GIS | $50B+ → $80B+ (8-12%) | +3·+3·+3·+3% | +5·+3% | +8·10·10·12% | +18·15% | **P**: 안정 / **Q**: 데이터센터 + 그리드 노후화 교체 | Schneider·Eaton·ABB·Siemens·LS ELECTRIC |
| 3 | HVDC | $15B+ → $40B+ (20%+) | +5·+5·+8·+8% | +12·+10% | +15·18·20·22% | +30·25% | **P**: 대규모 프로젝트 단가↑ / **Q**: 재생E 통합·해상풍력 | Hitachi·Siemens·GE·ABB·효성·HD |
| 4 | 케이블 (초고압·해상) | $30B+ → $50B+ (12-15%) | +5·+5·+5·+8% | +10·+8% | +10·12·15·15% | +25·20% | **P**: 동·알루미늄 + 해상풍력 프리미엄 / **Q**: 해상풍력 + DC 인입 | Prysmian·Nexans·NKT·LS·LS전선·대한전선 |
| 5 | UPS+ESS | $15+$20B → $30+$50B (15%·25%) | +2·+2·+2·+3% (UPS) / +5·+5·+5·+5% (ESS) | +5·+3% / +10·+8% | +12·15·15·15% (UPS) / +20·25·25·25% (ESS) | +20·15% / +50·35% | **P**: 안정 (UPS), ESS 배터리 가격↓·시스템 프리미엄 / **Q**: DC + 재생E 통합 | Schneider·Eaton·Vertiv (UPS) / LG·Samsung·CATL (ESS) |
| 6 | 액랭 | $5.52B → $18.79B (22.65%) | +2·+2·+3·+3% | +5·+5% | +25·30·30·30% | +60·50% | **P**: 안정·CAGR 프리미엄 / **Q**: GB200 130 kW rack 필수, 하이퍼스케일러 전환 가속 | Vertiv·Schneider·Rittal·Stulz·Boyd |
| 7 | 가스 터빈 | $50B → $80B+ (10-15%) | +8·+8·+5·+5% | +15·+10% | +15·18·20·22% | +30·25% | **P**: 3사 과점·프리미엄 / **Q**: GE 7+Siemens 14+Mitsubishi 7 = 28 GW (1Q25)·capa 25-35%↑ | GE·Siemens·Mitsubishi |
| 8 | **원자력+SMR** (★ 4 layer 통합) | $10B+ commit → $30B+ (2035) | n/a (PPA 기반) | n/a | (개발사) 본격 매출 2028+ / (부품) **두산 즉시 매출 +20%/yr** / (EPC) 단계별 | (부품·EPC) +25·20% | **P**: PPA 고정 / **Q**: 22 GW 개발 중, Big Tech $10B+. **부품 (두산) Q는 2025-27부터 가시화** | (본체) NuScale·Kairos·X-Energy·TerraPower·Holtec·Rolls-Royce / (사업자) Constellation·Talen·Vistra / (부품) **두산에너빌리티**·JSW·Sheffield / (EPC) Bechtel·Fluor·**현대건설** |
| **9** | **★ 800VDC 전환 (HVDC Power Rack·SST·SSCB·DC busway)** | **사이드카 $11B (2028) / SST $13B (2030)** | (D) 동반 확대 | Power Rack ASP $500K/MW (기존 AC $40k의 10x), SST $1-1.5M/MW | n/a | 2030 39GW 누적 | **P**: 신규 architecture 프리미엄 / **Q**: 2027/2028 Kyber 인플렉션부터 본격, NEC 2029 부분/2032 완전 | NVIDIA·Delta·DG Matrix·ABB·Eaton·Wolfspeed·Infineon·TE Connectivity / **LS ELECTRIC (한국 선도, UL 1500V DC MCCB 최초)** |

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
| 글로벌 트렌드 관통 + 한국 Moat | ★★★ — 17 segment 중 10 segment 한국 글로벌 Top 5 |
| **주도 섹터 가능성** | **★★★ 매우 높음** |

---

# Step 7. 리스크 팩터

| 리스크 | 확률 | 임팩트 | 시그널 |
|---|---|---|---|
| 에이전트 narrative 약화 | 25% | 매우 큼 | Anthropic·OpenAI ARR 정체 |
| AI capex 변곡점 | 25% | 큼 (12-18개월) | 하이퍼스케일러 capex 가이던스 하향 |
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
- Anthropic·OpenAI API 매출, Cursor·Devin·Manus ARR, Token consumption per agent

## 반도체 측
- NVIDIA 데이터센터, Blackwell allocation, TSMC CoWoS capa, HBM 가격, DDR5 server, eSSD Top 5, 800G/1.6T 트랜시버, 서버 CPU 점유, HBM4 양산

## 전력 측
- 변압기 lead time, 한국 변압기 3사 분기 수주, 가스터빈 3사 주문, SMR PPA, 두산 SMR 부품, 현대건설 Holtec, IEA 데이터센터 전력, 하이퍼스케일러 분기 capex

## ★ 자본공급자 측 (credit cycle — v5 추가, 2026-06-21, 이그전 '자본공급자' 프레임 기반)

> **프레임**: Capex 사이클의 진짜 변곡점은 빅테크의 자발적 축소가 아니라 **자본공급자 (채권시장)의 변심**. "이 회사에 계속 돈을 빌려줘도 괜찮을까?"라는 의심이 시작되는 순간이 사이클 종료 시그널. 본 테마 Step 7 "AI capex 변곡점 (25%)" 리스크의 선행 지표 세트.

- **★ 오라클 5Y CDS 프리미엄** (LSEG) — 반도체 ETF (SOXX)와 동행성 확인. 사실상 AI credit cycle의 실시간 지표. 200bp+ 고착 시 경계
- **Neocloud 채권 스프레드** (CoreWeave·Lambda·Nebius 등) — 한계 차입자의 조달 여건. 첫 default가 심리 전환점 (2000년 텔레콤 채권 붕괴 유사 패턴)
- **Hyperscaler 채권 발행 규모** (BIS) — 2024 ~$0 → 2025 $105B → 2026e $175B+. 매출 대비 capex 47%+ 도달로 외부 조달 의존 가속
- **Hyperscaler 합산 FCF** (Bloomberg 전망) — 2027 합산 마이너스 전망 → 2028 개선. 개선 시점 앞당김/지연이 핵심
- **OpenAI ARR 추정치** (간접: MSFT OpenAI 매출 인식·Azure AI contribution) — 오라클 RPO의 counterparty risk 본질
- **circular financing 문제화 강도** — NVIDIA→OpenAI→오라클→NVIDIA 순환 구조에 대한 회계·규제·언론 조명

---

# ★ Step 9. 통합본 (v5 — 2026-06-21)

> **본 통합본 frame**: 14개사 기업 분석 (반도체 10 + 빅테크 4) 완료 후 통합. **수요 측 빅테크 4사 (MSFT·Google·AWS·Meta) macro layer**를 baseline, **공급 측 반도체 10개사 thesis**를 cross-validation. **3년 (peak) / 5년 (normalize) dual horizon Terminal 시나리오**. ★ peak 시점은 사전 가정 X — 4사 macro 분석 결과로 도출.

> **분석된 14개사**: 반도체 10 = SK·삼성·Micron·ARM·STX·SNDK·WDC·AMD·Intel·NVIDIA / 빅테크 4 = MSFT·Google·AWS·Meta

---

## 9-1. 통합 narrative — 4사 macro 신호 수렴

**1단계: 산업 기초 (반도체·전력 — 사이클·secular 양면)**
- 반도체: 메모리 4-5년 단주기 + 매크로 7-10년 장주기 중첩. CR3 95%+ + EUV 양산 한정
- 전력: 변압기 lead time 128주 + ★ AI DC 폭증으로 신규 segment (800VDC)
- 본 테마 = 사이클 정점 + secular AI 진입 양면 hybrid

**2단계: 에이전트 AI 테마 narrative**
- 에이전트 1건 = chat 1턴 대비 **토큰 20-30x** → 추론 인프라 폭증
- 17 segment 병목 ((A) 구조적 메가 병목 + (D) 동반 확대 hybrid)
- 한국 접근 가능 TAM 2028E $216-262B+

**3단계: ★ 수요 측 4사 macro layer (v5 신규)**
- ★ **빅테크 4사 CY26 CapEx 합산 ~$585B** (FY25 $258B 대비 +127%)
- ★ **빅테크 4사 AI ARR 합산 ~$122B (2x YoY)**: MSFT $37B + Google $30B+ + AWS $25B+ + Meta $30B
- ★ **AI Foundation 4가지 strategy**:
  - MSFT = OpenAI 독점 + Maia + Cobalt
  - Google = Gemini + Anthropic + ★ TPU (Broadcom) + Axion
  - AWS = ★ Anthropic $8B 최대 + ★ OpenAI 2GW Trainium 신규 + Graviton
  - Meta = ★ Llama open + ★ AMD MI450 6GW + MTIA + RL
- ★ **4사 commentary 수렴**: "constrained through 2026" (MSFT) / "compute constrained" (Google) / "largest opportunity" (AWS) / "most exciting" (Meta) = ★ AI 인프라 사이클 정점 미도래

**4단계: ★ 공급 측 14개사 thesis cross-validation**

| layer | 종목 | Moat | 4사 macro 신호 evidence |
|---|---|---|---|
| Hot (HBM) | SK하이닉스 | **4.4** | 4사 NVIDIA Blackwell·Rubin 발주 → SK HBM3E·HBM4 majority |
| Hot (HBM) | 삼성전자 | 4.3 | ★ Meta 6GW MI450 = 삼성 HBM4 preferred MoU (2026.03) |
| Hot+Warm | Micron | 4.0 | ★ MSFT/AWS 미국 본토 + 1Q26 HBM4 진입 |
| Compute (GPU) | **NVIDIA** | **4.8** | 4사 모두 NVIDIA #1 발주 (MSFT·AWS $30-40B/년) |
| Compute (GPU) | AMD | 3.8 | ★ Meta 6GW + OpenAI 6GW = 12GW MI450 mega deal |
| Compute (CPU) | Intel | 2.8 | ★ MSFT Maia (Intel Foundry 18A 첫 외부 대형) |
| IP | ARM | 4.1 | ★ Cobalt·Axion·Graviton 모두 ARM = DC royalty 2x YoY |
| Warm-Cold | SanDisk | 4.0 | 4사 eSSD + KV cache offload |
| Cold (HDD) | WDC | 4.0 | ★ AWS S3 #1 + MSFT Azure exabyte = nearline 52% sold out |
| Cold (HDD) | Seagate | 4.1 | ★ 5 CSP qualified on Mozaic 3+ |

**5단계: ★ NVIDIA monopoly 4대 위협 catalyst — 빅테크 macro evidence**

| 위협 | 단기 (2-3년) | 장기 (5년+) | 4사 evidence |
|---|---|---|---|
| **#1 AMD MI400** | 4%→18% | NVIDIA 70-75% jam | ★ Meta 6GW + OpenAI 6GW = 12GW |
| **#2 Hyperscaler ASIC** | -3-5%pt | -8-10%pt | TPU + MTIA + Trainium + Maia = $225B+ |
| **#3 CUDA 대체** | dominance | 일부 잠식 | ROCm + Triton + Mojo |
| **#4 중국 통제** | $0 | upside | H20 $0 (Q1 FY27) |

→ ★ **단기 2-3년 thesis 강고, 장기 5년+ monopoly 점진 약화 가능**

---

## 9-2. Terminal 밸류 시나리오 — 3년 Peak / 5년 Normalize

### 9-2-1. 4사 CapEx trajectory + peak/normalize 도출

| 연도 | MSFT | Google | AWS | Meta | **4사 합** | YoY |
|---|---|---|---|---|---|---|
| FY23 | 28.1 | 32.3 | 52.7 | 27.3 | 140.4 | — |
| FY24 | 44.5 | 52.5 | 77.7 | 39.2 | 213.9 | +52% |
| FY25 | 65 | 75 | 105 | 75 | **320** | +50% |
| **CY26E** | **190** | **100** | **195** | **100** | **★ 585** | **+83%** |
| CY27E | 220 | 125 | 240 | 120 | 705 | +20% |
| **CY28E (peak)** | 240 | 145 | 270 | 130 | **★ 785** | +11% |
| CY29E | 255 | 160 | 285 | 130 | 830 | +6% |
| **CY30E (normalize)** | 260 | 165 | 290 | 130 | **★ 845** | +2% |

**★ Peak 시점**: 2027 H2 ~ 2028 H1

**★ Normalize 시나리오 (2030)**:
- 낙관 -5% (메가 트렌드 영구) = $745B
- 중립 -15% (secular 강함) = $670B
- 비관 -30% (메모리 사이클) = $550B

### 9-2-2. 3년 Peak (2028) — 14개사 정점 leverage

| 종목 | Moat | Peak thesis | Peak 매출 |
|---|---|---|---|
| **NVIDIA** | 4.8 | Vera Rubin + Kyber rack 정점 | FY28 ~$420B (+30%) |
| **SK하이닉스** | 4.4 | HBM3E + HBM4 majority + DDR5 정점 | 130-150조원 |
| **삼성전자** | 4.3 | ★ HBM4 AMD driver + 메모리 CAPA #1 | DS $200B+ |
| **AMD** | 3.8 | ★ MI450 6GW + 12GW + EPYC 30%+ | $80B+ |
| **ARM** | 4.1 | ★ 4사 ARM CPU + ARMv9 2x rate | $7-8B |
| **Seagate** | 4.1 | ★ Mozaic 4·5 + FY27 build-to-order | $15B+ |
| **WDC** | 4.0 | nearline 52% + 분사 + EPMR 가속 | $15B+ |
| **SanDisk** | 4.0 | NAND 정점 + HBF + $42B NBM | $20B+ |
| **Micron** | 4.0 | HBM 21% + 미국 본토 | $50B+ |
| **Intel** | 2.8 | ★ Foundry 18A turnaround | $80-90B |
| **MSFT** | macro | AI ARR $75B+, Copilot 50M+ | $400B+ |
| **Google** | macro | GCP +40%+, Gemini 600M+, TPU 7 | $600B+ |
| **AWS** | macro | AWS $230B+, Trainium 3 | 전체 $1T+ |
| **Meta** | macro | AI 광고 $80B+, Llama 6, MI450 ramp | $350B+ |

### 9-2-3. 5년 Normalize (2030) — 14개사 secular survivor

| 종목 | 낙관 | 중립 | 비관 | secular buffer |
|---|---|---|---|---|
| NVIDIA | monopoly 80% | 75% | 70% | ★★★ CUDA 20년 |
| SK하이닉스 | HBM #1 53%+ | majority 50% | HBM4E dual | ★★★ |
| 삼성전자 | HBM4 AMD + 메모리 #1 | 메모리 #1 (HBM #2) | HBM3E 후발 실패 | ★★ |
| AMD | AI 가속기 25-30% | 20% | NVIDIA Rubin Ultra 회복 | ★★ |
| ARM | DC 30%+, AGI 본격 | DC 25% | 라이선시 자기잠식 | ★★★ royalty 영구 |
| WDC+STX | Mozaic 5/6 + EPMR | 안정 | SSD 일부 잠식 | ★★★ GB당 5-10x |
| SanDisk | HBF + 차세대 | NAND 보통 | 침체 -50% | ★★ |
| Micron | HBM 25%+ + 본토 영구 | HBM 21% | HBM 후발 실패 | ★★ |
| Intel | Foundry 18A + 14A | 회복 초기 | TSMC 압도 | ★ |
| MSFT | AI ARR $100B+ | $80B | exclusivity weakening | ★★★ |
| Google | GCP +30% + TPU 8 | +20% | DOJ Search 분리 | ★★★ |
| AWS | AWS +25% | +20% | OPM 30% 진입 | ★★★ Cloud #1 |
| Meta | AI 광고 $150B+ | $100B | RL -$30B+ | ★★ |

---

## 9-3. ★ Long-run multiple anchor

| 종목 | PER | EV/EBITDA | EV/Sales | 근거 |
|---|---|---|---|---|
| **NVIDIA** | 22x | 18x | 10x | secular monopoly + GPM 75%. 위협 -5x |
| **SK하이닉스** | 8x | 5x | 2.5x | 메모리 사이클 평균 + HBM +2x |
| **삼성전자** | 10x | 6x | 2.5x | DRAM+파운드리 multi discount |
| **AMD** | 30x | 20x | 8x | NVIDIA 대안 + Lisa Su track |
| **ARM** | 40x | 30x | 20x | chipless IP + royalty 영구 |
| **Seagate** | 15x | 10x | 3x | HDD pure + HAMR + 자본환원 |
| **WDC** | 12x | 8x | 2.5x | HDD #1 + 분사 premium |
| **SanDisk** | 10x | 6x | 2x | NAND pure 진폭 큼 |
| **Micron** | 10x | 6x | 2.5x | HBM 후발 + 미국 본토 |
| **Intel** | 15x | 8x | 2x | Foundry 18A turnaround |
| **MSFT** | 30x | 22x | 9x | secular Apple-like |
| **Google** | 22x | 15x | 6x | secular + DOJ -3-5x |
| **AWS** | 35x | 20x | 3.5x | Cloud #1 + Foundation 양면 |
| **Meta** | 25x | 18x | 8x | 광고+Llama+AMD, RL -5x |

---

## 9-4. ★ Terminal 시총 시나리오별 결과

### 3년 Peak (2028) 성장 배수

| 종목 | 현재 시총 | Peak OP | PER | 3년 시총 | **배수** |
|---|---|---|---|---|---|
| NVIDIA | $5.7T | $280B+ | 22x | $6.2T | 1.09x |
| **SK하이닉스** | 200조 | 70-80조 | 8x | 560-640조 | **★ 3.0x** |
| **삼성전자** | 500조 | 120-130조 | 10x | 1,200-1,300조 | **★ 2.5x** |
| **AMD** | $290B | $25B+ | 30x | $750B | **★ 2.6x** |
| ARM | $200B | $4B+ | 40x | $160B | 0.8x |
| Seagate | $50B | $3-4B | 15x | $45-60B | 1.05x |
| WDC | $25B | $2.5-3B | 12x | $30-36B | 1.3x |
| **SanDisk** | $25B | $5B+ | 10x | $50B | **★ 2.0x** |
| Micron | $130B | $20B+ | 10x | $200B | 1.5x |
| **Intel** | $90B | $10-15B | 15x | $150-225B | **★ 2.1x** |
| MSFT | $3.7T | $150B+ | 30x | $4.5T | 1.22x |
| Google | $2.2T | $130B+ | 22x | $2.9T | 1.32x |
| AWS | $2.3T | 전체 $90B | 35x | $3.2T | 1.39x |
| **Meta** | $1.5T | $130B+ | 25x | $3.3T | **★ 2.2x** |

### 5년 Normalize (2030) 시나리오별 배수

| 종목 | 5년 낙관 | 5년 중립 | 5년 비관 |
|---|---|---|---|
| NVIDIA | 0.96x | 0.79x | 0.61x |
| **SK하이닉스** | ★ 2.4x | 1.75x | 1.25x |
| **삼성전자** | ★ 2.2x | 1.7x | 1.2x |
| **AMD** | ★ 2.3x | 1.7x | 1.2x |
| ARM | 1.0x | 0.8x | 0.6x |
| Seagate | 1.04x | 0.84x | 0.6x |
| WDC | 1.36x | 1.04x | 0.72x |
| SanDisk | 1.2x | 0.8x | 0.48x |
| Micron | 1.4x | 1.0x | 0.69x |
| **Intel** | ★ 2.0x | 1.3x | 0.67x |
| MSFT | 1.38x | 1.08x | 0.81x |
| Google | 1.45x | 1.14x | 0.82x |
| AWS | 1.52x | 1.17x | 0.87x |
| **Meta** | ★ 2.5x | 1.87x | 1.2x |

### 시나리오별 BT 핵심 결론

**★ 3년 Peak 최대 leverage (2.0x+)**: SK 3.0x · AMD 2.6x · 삼성 2.5x · Meta 2.2x · Intel 2.1x · SanDisk 2.0x

**★ 5년 Normalize secular survivor 낙관 (2.0x+)**: Meta 2.5x · SK 2.4x · AMD 2.3x · 삼성 2.2x · Intel 2.0x

**★ 비관 시나리오 살아남는 종목 (1.2x+)**: 삼성·SK·AMD·Meta 1.2x+ / 빅테크 (0.8x+ 안정)

**★ Terminal 한계 종목**: NVIDIA 3년 1.09x = 가격 반영, 5년 비관 0.61x = monopoly 위협 본격화 risk. ARM 3년 0.8x · 5년 1.0x = royalty 영구지만 valuation 한계

---

## 9-5. 메타데이터 갱신 (v5 dominant/challenger/macro_layer 분기)

- **dominant (8)**: NVIDIA, SK, 삼성, ARM, Seagate, WDC, SanDisk, Micron (Moat 4.0+)
- **challenger (2)**: AMD, Intel (Moat 3.8-2.8, 빠른 성장 또는 turnaround)
- **macro_layer (4)**: MSFT, Google, AWS, Meta (수요 측 baseline)

(상세는 file frontmatter active_companies)

---

## 9-6. 워치리스트 자동 등록

### T1 반도체 (10개사)
```
NVIDIA (NVDA, industry=반도체|AI 인프라)
SK하이닉스 (industry=반도체|메모리)
삼성전자 (industry=반도체|메모리|파운드리)
ARM (ARM, industry=반도체|IP)
Seagate (STX, industry=반도체|스토리지)
Micron (MU, industry=반도체|메모리)
SanDisk (SNDK, industry=반도체|메모리)
WDC (WDC, industry=반도체|스토리지)
AMD (AMD, industry=반도체|AI 인프라)
Intel (INTC, industry=반도체|AI 인프라|파운드리)
```

### T1 미국 빅테크 (4개사, macro layer)
```
Microsoft (MSFT, industry=빅테크|클라우드|AI)
Google (GOOGL, industry=빅테크|클라우드|AI 광고|자율주행)
Amazon (AMZN, industry=빅테크|클라우드|소비재|AI)
Meta (META, industry=빅테크|광고|AI|VR/AR)
```

### 한국 주도주 후보 워치리스트

| 우선 | 종목 | T분류 | 본 테마 thesis |
|---|---|---|---|
| 1 | SK하이닉스 | T1 메모리 | HBM 정점 + DDR5 + eSSD |
| 2 | 삼성전자 | T1 메모리·파운드리 | HBM4 AMD MoU + CAPA #1 |
| 3 | 한미반도체 | T2 반도체 후공정 | TC본더 글로벌 #1 |
| 4 | 효성중공업 | T1 전력 | UHV 변압기 미국 #1 |
| 5 | HD현대일렉트릭 | T1 전력 | UHV 미국 15-20% |
| 6 | LS ELECTRIC | T1 전력 | 스위치기어 + 800VDC 한국 선도 |
| 7 | 오이솔루션 | T2 광통신 | 1.6T·ITLA 국산화 |
| 8 | 두산에너빌리티 | T1 SMR | SMR forging 5사 중 1 |
| 9 | 현대건설 | T1 SMR | SMR EPC Holtec 협력 |

---

# Step 9 통합본 — 핵심 결론 종합

## A. valuation thesis 결론

**3년 Peak (2028)**: ★ SK 3.0x / AMD 2.6x / 삼성 2.5x / Meta 2.2x / Intel 2.1x / SanDisk 2.0x = 6 종목 정점 leverage

**5년 Normalize (2030)** 낙관: Meta 2.5x / SK 2.4x / AMD 2.3x / 삼성 2.2x / Intel 2.0x = 5 종목 secular survivor

## B. 한국 주도주 결론

**★ 1순위: SK하이닉스 + 삼성전자** — HBM 정점 + 메모리 CAPA + HBM4 AMD MoU + NVIDIA 단독

## C. 미국 주도주 결론

**★ 1순위: AMD + Meta** — NVIDIA 대안 #1 (AMD) + AMD 단독 driver (Meta). ★ Meta·OpenAI 12GW MI450 핵심 catalyst

**★ 2순위: NVIDIA** — 본 테마 needle-mover지만 단기 1.09x = 가격 반영. long-term holdings로 monopoly 지속

## D. ★ 4사 macro layer 핵심 시그널 (분기 트래킹)

- 4사 CY26 CapEx 합산 $585B + peak 2027 H2 ~ 2028 H1 = secular 정점 미도래
- AI ARR 합산 $122B (2x YoY)
- "constrained through 2026" 4사 commentary 수렴
- NVIDIA Q1 FY27 record + 9분기 연속 컨센 beat

## E. ★ NVIDIA monopoly 위협 catalyst (5년 risk)

| 위협 | 점유 영향 | macro evidence |
|---|---|---|
| #1 AMD MI400 | 80% → 70-75% | Meta 6GW + OpenAI 6GW = 12GW |
| #2 Hyperscaler ASIC | -8-10%pt | TPU+MTIA+Trainium+Maia = $225B+ |
| #3 CUDA 대체 | 일부 잠식 | ROCm·Triton·Mojo (장기) |
| #4 중국 통제 | upside | H20 $0 |

---

## v5 changelog

**v5 (2026-06-21)**: Step 9 통합본 append
- 14개사 기업 분석 완료 (반도체 10 + 빅테크 4)
- 4사 macro layer baseline + peak/normalize 도출 (peak 2027 H2 ~ 2028 H1)
- 3년 peak / 5년 normalize dual horizon Terminal 시나리오
- 14개사별 Long-run multiple anchor + Terminal 시총 시나리오별
- 한국: SK·삼성 / 미국: AMD·Meta
- ★ NVIDIA monopoly 4대 위협 catalyst macro evidence
- 메타데이터: active_companies dominant 8 / challenger 2 / macro_layer 4
- 워치리스트: 반도체 10 + 빅테크 4 + 한국 주도주 9

---

# ★ v5.1 add-on (2026-07-27) — 한국 Neocloud/AI Factory segment 신설

> **trigger**: "네이버 = 한국의 코어위브" narrative + 2026-07-24~25 SF AI Summit (이재명 대통령 주재, NVIDIA·OpenAI·Anthropic·Broadcom + 삼성·SK 총수 참석) 한국 sovereign AI 패키지 일괄 발표. 본 세션 (반도체/에이전트AI)은 **테마 연결성 검증**을 담당, NAVER 기업 심층 분석은 **클라우드 세션 핸드오프** (분업 결정 2026-07-27).

## A. narrative 형성 timeline

| 시점 | 이벤트 | 의미 |
|---|---|---|
| **2026-06-08** | ★ 1차 형성 — NAVER + NVIDIA 기가와트급 AI Factory 계획 (GAK 세종, DSX platform, 55MW 시작). 언론 "Asian CoreWeave" 표현 시작 | narrative 탄생 |
| **2026-07-24~25** | ★ 2차 폭발 — SF AI Summit에서 **NVIDIA $1B 직접 투자 (신주 204,500원) + Brookfield 최대 $9B (exclusive capital partner, nonbinding) + 55MW → 200MW 3배 확대 (2028) + 장기 1GW** 발표. "AI 인프라 매출 20조원" 목표 | narrative 정점 |
| **2026-07-25 (동일 주간)** | ★ 한국 sovereign AI 패키지 동시 발표: **SK-NVIDIA·미국 CSP 5년 $750B 메모리 LTA** + **삼성-Broadcom 5년 $200B 메모리/파운드리 수주** + **NVIDIA-SK Group 2GW+ AI DC** (SKT GW급 AI cloud + SK하이닉스 메모리 공동개발 + 두산·LG deal, DSX platform) | 한국 = sovereign AI 국가 단위 진입 |
| **2026-07-27** | NAVER 주가 +10% | 시장 반영 시작 |

Roadmap: 55MW (1H 2027 가동) → 100MW (2027 후반) → 200MW (2028) → 1GW (장기).

## B. segment 신설 — ★ #18 한국 Neocloud/AI Factory (sovereign AI)

| 항목 | 내용 |
|---|---|
| **병목 카테고리** | **(D) 동반 확대** — 신규 시장 형성기. ASP 안정 (GPU cloud 시세 연동) + Q 폭증 (55MW → 1GW). 향후 (B) 수요 견인 전환 가능 |
| **밸류체인 위치** | 수요 측 신규 layer — 미국 hyperscaler 4사와 별개의 **국가 단위 AI 인프라 발주 주체** 등장 |
| **글로벌 peer** | CoreWeave (미국 #1 Neocloud, NVIDIA 투자 + $225B급 백로그 생태계), Lambda, Nebius. ★ NVIDIA의 Naver $1B = CoreWeave 투자와 동일 playbook |
| **한국 플레이어** | **NAVER (GAK 세종, #1)** + SK Group (SKT GW급, 2GW+) + 삼성SDS·KT클라우드 (후보) |
| **자본 구조** | ★ Brookfield $9B = 외부 인프라 펀드 조달 — **이그전 '자본공급자' 프레임의 한국 첫 사례** (Step 8 credit cycle 트래킹 지표 직결). nonbinding term sheet = 구속력 낮음 주의 |
| **TAM (한국 접근)** | 인프라 투자 $10B+ (NAVER 단독) + SK 2GW+ 별도. NAVER 매출 목표 20조원 (~$15B). ★ **한국 접근 TAM 표에 +$10-15B 추가** (기존 $216-262B → **$226-277B+**) |

## C. 14개사 thesis 영향 매핑

| 종목 | 영향 | 방향 |
|---|---|---|
| **NVIDIA** | ACIE (Sovereign AI) segment 한국 확장 검증 — $1B 투자 + DSX platform 표준 수출. ★ Neocloud playbook (CoreWeave → Naver) 반복 = ACIE 다각화 thesis 강화 | ★ + |
| **SK하이닉스** | ★ 이중 수혜 — (1) 5년 $750B LTA (연 250조, 예상 매출의 50-60%) (2) NVIDIA-SK Group 2GW DC의 HBM·DDR5·eSSD 국내 발주 경로 신설 | ★★ + |
| **삼성전자** | 삼성-Broadcom $200B (메모리/파운드리) — HBM4 + 파운드리 다각화 검증. 단 Naver·SK DC 직접 수혜는 SK 대비 낮음 | + |
| **전력 인프라 (LS ELECTRIC·효성·HD현대일렉·두산)** | ★ GAK 세종 200MW→1GW + SK 2GW+ = **한국 본토 변압기·스위치기어·액랭·800VDC 직접 수요 신설**. 특히 DSX platform = NVIDIA 800VDC reference → LS ELECTRIC DC MCCB 직결. 두산은 SK Group deal에 직접 포함 | ★★ + |
| **AMD·Intel·ARM·Micron·HDD** | 간접 — 한국 DC는 NVIDIA DSX 중심이라 AMD 진입 제한적. HDD는 cold storage 수요 시차 수혜 | 중립~약+ |
| **빅테크 4사 (macro)** | 수요 주체 다변화 — 미국 4사 외 **국가 단위 발주자** 등장 = capex 사이클의 지역 분산 = 자본공급자 리스크 일부 완화 (수요 base 다변화) | + |

## D. 리스크 (신설 segment 고유)

1. **Brookfield $9B nonbinding** — 구속력 낮음. 자본공급자 프레임상 금리·credit 환경 악화 시 첫 철회 후보
2. **NAVER 실행력** — CoreWeave 대비 GPU cloud 운영 경험 부족 (ClusterMAX 평가 "Unavailable Tier" 참고)
3. **수익성 미검증** — 매출 20조 목표 vs CoreWeave도 아직 적자. Neocloud 모델 자체가 자본집약 + 낮은 마진
4. **한국 전력망 제약** — 1GW급 DC의 계통 연결·전력 확보가 실제 병목 가능

## E. 클라우드 세션 핸드오프 노트

- **본 세션 완료분**: narrative timeline + segment 신설 + thesis 영향 매핑 (본 문서)
- **클라우드 세션 요청분**: NAVER 기업 심층 분석 — 사업부 구조 (검색·커머스·핀테크·클라우드 mix), AI Factory 사업부의 전체 밸류에이션 비중, "코어위브 멀티플 정당성" 판단 (pure-play CoreWeave vs mixed NAVER 차이), 신주 발행 (204,500원) 희석 효과
- **cross-ref**: 본 문서 v5.1 + 클라우드_산업기초.md

## v5.1 changelog

**v5.1 (2026-07-27)**: 한국 Neocloud/AI Factory segment 신설 add-on
- 네이버 "한국의 코어위브" narrative timeline (6/8 형성 → 7/24-25 정점)
- ★ #18 segment 신설: 한국 Neocloud/AI Factory (sovereign AI), 카테고리 (D)
- 한국 접근 TAM $216-262B → $226-277B+ 상향
- 14개사 thesis 영향: SK·전력 ★★+ / NVIDIA·삼성 + / AMD·HDD 중립
- SF AI Summit 패키지 (SK LTA $750B + 삼성-Broadcom $200B + SK Group 2GW) 반영
- NAVER 기업분석 → 클라우드 세션 핸드오프

# Step 6. 산업 유형 + 주도 섹터 가능성

| 항목 | 결론 |
|---|---|
| 산업 유형 | **메가 트렌드** (AI 슈퍼사이클 2단) |
| 단계 | 초기-중기 (2024-25 narrative → 2026-2030+ Q 폭발) |
| 글로벌 트렌드 관통 + 한국 Moat | ★★★ — 17 segment 중 10 segment 한국 글로벌 Top 5 |
| **주도 섹터 가능성** | **★★★ 매우 높음** |

---

# Step 7. 리스크 팩터

| 리스크 | 확률 | 임팩트 | 시그널 |
|---|---|---|---|
| 에이전트 narrative 약화 | 25% | 매우 큼 | Anthropic·OpenAI ARR 정체 |
| AI capex 변곡점 | 25% | 큼 (12-18개월) | 하이퍼스케일러 capex 가이던스 하향 |
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
- Anthropic·OpenAI API 매출, Cursor·Devin·Manus ARR, Token consumption per agent

## 반도체 측
- NVIDIA 데이터센터, Blackwell allocation, TSMC CoWoS capa, HBM 가격, DDR5 server 가격, eSSD Top 5, 800G/1.6T 트랜시버, 서버 CPU 점유, HBM4 양산, 삼성 HBM3E 12단 NVIDIA 인증

## 전력 측
- 변압기 lead time, 한국 변압기 3사 분기 수주, 가스터빈 3사 주문, SMR PPA, 두산 SMR 부품, 현대건설 Holtec, IEA 데이터센터 전력, 하이퍼스케일러 분기 capex

---

# ★ Step 9. 통합본 (v5 — 2026-06-21)

> **본 통합본 frame**: 14개사 기업 분석 (반도체 10 + 빅테크 4) 완료 후 통합. **수요 측 빅테크 4사 (MSFT·Google·AWS·Meta) macro layer**를 baseline, **공급 측 반도체 10개사 thesis**를 cross-validation. **3년 (peak) / 5년 (normalize) dual horizon Terminal 시나리오**. ★ peak 시점은 사전 가정 X — 4사 macro 분석 결과로 도출.

> **분석된 14개사**: 반도체 10 = SK·삼성·Micron·ARM·STX·SNDK·WDC·AMD·Intel·NVIDIA / 빅테크 4 = MSFT·Google·AWS·Meta

---

## 9-1. 통합 narrative (산업기초 → 14개사 thesis flow)

**1단계: 산업 기초 (반도체·전력 — 사이클·secular 양면)**
- 반도체: 메모리 4-5년 단주기 + 매크로 7-10년 장주기 중첩. CR3 95%+ 과점 + EUV 양산 한정 = 진입 장벽 영구. ★ 본 테마는 사이클 정점 + secular AI 진입 양면 hybrid
- 전력: 변압기·가스터빈 lead time 128주 = 공급 절제 누적. ★ AI DC 전력 폭증으로 신규 segment (800VDC) 등장

**2단계: 에이전트 AI 테마 narrative**
- 에이전트 1건 = chat 1턴 대비 **토큰 20-30x** → 추론 인프라 폭증
- 17 segment 병목 (반도체 8 + 전력 9)
- (A) 구조적 메가 병목 + (D) 동반 확대 hybrid
- 한국 접근 가능 TAM 2028E $216-262B+

**3단계: ★ 수요 측 4사 macro layer (v5 신규)**
- ★ **빅테크 4사 CY26 CapEx 합산 ~$585B** (FY25 $258B 대비 +127%)
- ★ **빅테크 4사 AI ARR 합산 ~$122B (2x YoY)**
- ★ **AI Foundation 4가지 strategy 양상**:
  - MSFT = OpenAI 독점 + Maia + Cobalt
  - Google = Gemini + Anthropic + ★ TPU (Broadcom) + Axion
  - AWS = ★ Anthropic $8B + ★ OpenAI 2GW Trainium + Graviton
  - Meta = ★ Llama open + ★ AMD MI450 6GW + MTIA + RL
- ★ **4사 공통 commentary 수렴**: "constrained through 2026" (MSFT) / "compute constrained" (Google) / "largest opportunity" (AWS) / "most exciting" (Meta)
- → ★ **AI 인프라 사이클 정점 미도래 가장 강한 정량 시그널**

**4단계: ★ 공급 측 14개사 thesis cross-validation**

| layer | 종목 | Moat | 4사 macro 신호 evidence |
|---|---|---|---|
| Hot (HBM) | SK하이닉스 | **4.4** | 4사 모두 NVIDIA Blackwell·Rubin 발주 → SK HBM3E·HBM4 majority |
| Hot (HBM) | 삼성전자 | 4.3 | ★ Meta 6GW MI450 = 삼성 HBM4 preferred (2026.03 MoU) |
| Hot+Warm | Micron | 4.0 | ★ MSFT/AWS 미국 본토 supplier + 1Q26 HBM4 진입 |
| Compute (GPU) | **NVIDIA** | **4.8** | 4사 모두 NVIDIA #1 발주 (MSFT·AWS $30-40B/년) |
| Compute (GPU) | AMD | 3.8 | ★ Meta 6GW + OpenAI 6GW = 12GW MI450 mega deal |
| Compute (CPU) | Intel | 2.8 | ★ MSFT Maia (Intel Foundry 18A 첫 외부 대형) = turnaround leg |
| IP | ARM | 4.1 | ★ Cobalt·Axion·Graviton 모두 ARM = DC royalty 2x YoY |
| Warm-Cold | SanDisk | 4.0 | 4사 데이터센터 eSSD + KV cache offload 직접 발주 |
| Cold (HDD) | WDC | 4.0 | ★ AWS S3 Glacier #1 + MSFT Azure exabyte = nearline 52% sold out |
| Cold (HDD) | Seagate | 4.1 | ★ 5 CSP qualified on Mozaic 3+ |

**5단계: ★ NVIDIA monopoly 4대 위협 catalyst — 빅테크 macro evidence**

| 위협 | 단기 (2-3년) | 장기 (5년+) | 4사 evidence |
|---|---|---|---|
| **#1 AMD MI400** | 4%→18% | NVIDIA 70-75% jam | ★ Meta 6GW + OpenAI 6GW = 12GW |
| **#2 하이퍼스케일러 ASIC** | -3-5%pt | -8-10%pt | Google TPU + Meta MTIA + AWS Trainium + MSFT Maia = $225B+ |
| **#3 CUDA 대체** | dominance 유지 | 일부 잠식 | ROCm + Triton + Mojo |
| **#4 중국 통제** | $0 baseline | upside | H20 $0 (Q1 FY27) |

→ ★ **단기 2-3년 thesis 강고, 장기 5년+ monopoly 점진 약화 가능**

---

## 9-2. Terminal 밸류 시나리오 — 3년 (peak) / 5년 (normalize)

### 9-2-1. 4사 CapEx trajectory + peak/normalize 도출

| 연도 | MSFT | Google | AWS | Meta | **4사 합** | YoY |
|---|---|---|---|---|---|---|
| FY23 | 28.1 | 32.3 | 52.7 | 27.3 | 140.4 | — |
| FY24 | 44.5 | 52.5 | 77.7 | 39.2 | 213.9 | +52% |
| FY25 | 65 | 75 | 105 | 75 | **320** | +50% |
| **CY26E** | **190** | **100** | **195** | **100** | **★ 585** | **+83%** |
| CY27E | 220 | 125 | 240 | 120 | 705 | +20% |
| **CY28E (peak)** | 240 | 145 | 270 | 130 | **★ 785** | +11% |
| CY29E | 255 | 160 | 285 | 130 | 830 | +6% |
| **CY30E (normalize)** | 260 | 165 | 290 | 130 | **★ 845** | +2% |

**★ Peak 시점**: 2027 H2 ~ 2028 H1 (4사 평균 CapEx +11% 둔화 진입 시그널)

**★ Normalize 시나리오 (2030)**:
- 낙관 -5% (메가 트렌드 영구) = $745B
- 중립 -15% (secular 강함) = $670B
- 비관 -30% (메모리 사이클) = $550B

### 9-2-2. 3년 Peak (2028) — 14개사 정점 leverage

| 종목 | Moat | Peak thesis | Peak OPM/GPM | Peak 매출 |
|---|---|---|---|---|
| **NVIDIA** | 4.8 | Vera Rubin + Kyber rack 정점 | GPM 73-75% | FY28 ~$420B (+30%) |
| **SK하이닉스** | 4.4 | HBM3E + HBM4 majority + DDR5 정점 | OPM 60%+ | 130-150조원 |
| **삼성전자** | 4.3 | ★ HBM4 AMD MI455X driver + 메모리 CAPA #1 | DS OPM 50%+ | DS $200B+ |
| **AMD** | 3.8 | ★ MI450 6GW + 12GW + EPYC 30%+ | OPM 25-30% | $80B+ |
| **ARM** | 4.1 | ★ 4사 모두 ARM CPU + AGI + ARMv9 2x rate | OPM 50%+ | $7-8B (FY28) |
| **Seagate** | 4.1 | ★ HAMR Mozaic 4·5 + FY27 build-to-order | GPM 50%+ | $15B+ |
| **WDC** | 4.0 | nearline 52% + 분사 + UltraSMR/EPMR 가속 | GPM 50%+ | $15B+ |
| **SanDisk** | 4.0 | NAND 정점 + HBF + $42B NBM | OPM 70%+ | $20B+ |
| **Micron** | 4.0 | HBM 21% + 미국 본토 premium | OPM 50%+ | $50B+ |
| **Intel** | 2.8 | ★ Foundry 18A turnaround (MSFT Maia·DoD·AMZN) | OPM 10-15% | $80-90B |
| **MSFT** | macro | AI ARR $75B+, Azure +35%+, Copilot 50M+ | OPM 47-50% | $400B+ |
| **Google** | macro | GCP +40%+, Gemini 600M+, TPU 7 정점 | OPM 35%+ | $600B+ |
| **AWS** | macro | AWS $230B+ (+30%), Trainium 3, Anthropic+OpenAI | AWS OPM 35%+ | $1T+ |
| **Meta** | macro | AI 광고 ARR $80B+, Llama 6, AMD MI450 본격 | OPM 48%+ | $350B+ |

### 9-2-3. 5년 Normalize (2030) — 14개사 secular survivor

| 종목 | 낙관 thesis | 중립 thesis | 비관 thesis | secular buffer |
|---|---|---|---|---|
| NVIDIA | monopoly 80% | 75% (alt 침투) | 70% (MI500 경쟁) | ★★★ CUDA 20년 |
| SK하이닉스 | HBM #1 53%+ | majority 50% | HBM4E dual sourcing | ★★★ HBM4E |
| 삼성전자 | HBM4 AMD + 메모리 #1 | 메모리 #1 (HBM #2) | HBM3E 후발 만회 실패 | ★★ DRAM CAPA |
| AMD | AI 가속기 25-30% | 20% | NVIDIA Rubin Ultra 회복 | ★★ NVIDIA 대안 |
| ARM | DC 30%+, AGI 본격 | DC 25% | 라이선시 자기잠식 | ★★★ royalty 영구 |
| WDC+STX | Mozaic 5/6 + EPMR 정점 | 안정 | SSD 일부 잠식 | ★★★ GB당 5-10x |
| SanDisk | HBF + NAND 차세대 | NAND 보통 | 침체 -50% | ★★ 진폭 ±61pt |
| Micron | HBM 25%+ + 본토 영구 | HBM 21% | HBM 후발 실패 | ★★ 본토 secular |
| Intel | Foundry 18A + 14A | 회복 초기 | TSMC 압도 | ★ Foundry turnaround |
| MSFT | AI ARR $100B+, OpenAI 분산 | $80B + 갱신 | exclusivity weakening | ★★★ Azure+Copilot |
| Google | GCP +30% + TPU 8 | +20% + TPU 7 | DOJ Search 분리 | ★★★ TPU+Gemini+Anthropic |
| AWS | AWS +25% + Trainium 3 | +20% 안정 | OPM 30% 진입 | ★★★ Cloud #1 |
| Meta | AI 광고 $150B+ + RB 100M+ | $100B + Llama | RL -$30B+ + Llama 약화 | ★★ 광고 단독 |

---

## 9-3. ★ Long-run multiple anchor (14개사)

| 종목 | PER | EV/EBITDA | EV/Sales | 근거 |
|---|---|---|---|---|
| **NVIDIA** | 22x | 18x | 10x | secular monopoly + GPM 75% + 자본환원. monopoly 위협 -5x |
| **SK하이닉스** | 8x | 5x | 2.5x | 메모리 사이클 평균 + HBM premium +2x |
| **삼성전자** | 10x | 6x | 2.5x | DRAM+파운드리 multi discount |
| **AMD** | 30x | 20x | 8x | NVIDIA 대안 + Lisa Su track |
| **ARM** | 40x | 30x | 20x | chipless IP + royalty 영구, PEG 0.6x |
| **Seagate** | 15x | 10x | 3x | HDD pure + HAMR + 자본환원 |
| **WDC** | 12x | 8x | 2.5x | HDD #1 + 분사 premium |
| **SanDisk** | 10x | 6x | 2x | NAND pure 사이클 진폭 큼 |
| **Micron** | 10x | 6x | 2.5x | HBM 후발 + 미국 본토 |
| **Intel** | 15x | 8x | 2x | Foundry 18A turnaround anchor |
| **MSFT** | 30x | 22x | 9x | secular compounder Apple-like |
| **Google** | 22x | 15x | 6x | secular + DOJ -3-5x |
| **AWS** | 35x | 20x | 3.5x | Cloud 절대 #1 + Foundation 양면 |
| **Meta** | 25x | 18x | 8x | 광고+Llama+AMD, RL 적자 -5x |

---

## 9-4. ★ Terminal 시총 시나리오별 결과

### 3년 Peak (2028) 성장 배수

| 종목 | 현재 시총 | Peak OP (2028E) | PER | **3년 시총** | **배수** |
|---|---|---|---|---|---|
| NVIDIA | $5.7T | $280B+ | 22x | $6.2T | 1.09x |
| **SK하이닉스** | 200조 | 70-80조 | 8x | 560-640조 | **★ 3.0x** |
| **삼성전자** | 500조 | 120-130조 | 10x | 1,200-1,300조 | **★ 2.5x** |
| **AMD** | $290B | $25B+ | 30x | $750B | **★ 2.6x** |
| ARM | $200B | $4B+ | 40x | $160B | 0.8x |
| Seagate | $50B | $3-4B | 15x | $45-60B | 1.05x |
| WDC | $25B | $2.5-3B | 12x | $30-36B | 1.3x |
| **SanDisk** | $25B | $5B+ | 10x | $50B | **★ 2.0x** |
| Micron | $130B | $20B+ | 10x | $200B | 1.5x |
| **Intel** | $90B | $10-15B | 15x | $150-225B | **★ 2.1x** |
| MSFT | $3.7T | $150B+ | 30x | $4.5T | 1.22x |
| Google | $2.2T | $130B+ | 22x | $2.9T | 1.32x |
| AWS | $2.3T | 전체 $90B | 35x | $3.2T | 1.39x |
| **Meta** | $1.5T | $130B+ | 25x | $3.3T | **★ 2.2x** |

### 5년 Normalize (2030) 시나리오별

| 종목 | 5년 낙관 | 5년 중립 | 5년 비관 |
|---|---|---|---|
| NVIDIA | 0.96x | 0.79x | 0.61x |
| **SK하이닉스** | ★ 2.4x | 1.75x | 1.25x |
| **삼성전자** | ★ 2.2x | 1.7x | 1.2x |
| **AMD** | ★ 2.3x | 1.7x | 1.2x |
| ARM | 1.0x | 0.8x | 0.6x |
| Seagate | 1.04x | 0.84x | 0.6x |
| WDC | 1.36x | 1.04x | 0.72x |
| SanDisk | 1.2x | 0.8x | 0.48x |
| Micron | 1.4x | 1.0x | 0.69x |
| **Intel** | ★ 2.0x | 1.3x | 0.67x |
| MSFT | 1.38x | 1.08x | 0.81x |
| Google | 1.45x | 1.14x | 0.82x |
| AWS | 1.52x | 1.17x | 0.87x |
| **Meta** | ★ 2.5x | 1.87x | 1.2x |

### 시나리오별 BT 핵심 결론

**★ 3년 Peak 최대 leverage (2.0x+)**:
- SK하이닉스 3.0x · AMD 2.6x · 삼성 2.5x · Meta 2.2x · Intel 2.1x · SanDisk 2.0x

**★ 5년 Normalize secular survivor (낙관 2.0x+)**:
- Meta 2.5x · SK 2.4x · AMD 2.3x · 삼성 2.2x · Intel 2.0x

**★ 비관 시나리오 살아남는 종목 (1.2x+)**:
- 삼성 1.2x · SK 1.25x · AMD 1.2x · Meta 1.2x · 빅테크 (0.8x+ 안정)

**★ Terminal 한계 종목**:
- NVIDIA: 3년 1.09x = 이미 가격 반영. 5년 비관 0.61x = monopoly 위협 본격화 risk
- ARM: 3년 0.8x · 5년 1.0x = royalty 영구이지만 valuation 한계

---

## 9-5. 메타데이터 갱신 (v5 active_companies dominant/challenger/macro_layer 분기)

> ★ v5 — 14개사 분석 완료 후 active_companies 분기:
> - **dominant (8)**: NVIDIA, SK, 삼성, ARM, Seagate, WDC, SanDisk, Micron (Moat 4.0+, 점유 Top 2 또는 기술 리더)
> - **challenger (2)**: AMD, Intel (Moat 3.8-2.8, 빠른 성장 또는 turnaround)
> - **macro_layer (4)**: MSFT, Google, AWS, Meta (수요 측 baseline)

### narrative_shift_log v5 추가

- 2026-Q1: ★ AWS OpenAI 2GW Trainium 신규 = MSFT-OpenAI 독점 깨는 evidence
- 2026-Q1: ★ NVIDIA 자본 정책 게임 체인저 (배당 25배 + $80B buyback)
- 2026-Q1: ★ 4사 macro CapEx 합산 $585B (+127% vs FY25) = 사이클 정점 미도래
- 2026-Q1: ★ Meta MI450 6GW + 6th Gen EPYC lead = AMD thesis 단독 driver
- 2026-Q2: ★ NVIDIA Q1 FY27 record + 9분기 연속 컨센 beat
- 2026-Q2: ★ v5 14개사 통합본 + 3년/5년 Terminal 시나리오

---

## 9-6. 워치리스트 자동 등록

### T1 반도체 (10개사)

```
NVIDIA (NVDA, industry=반도체|AI 인프라)
SK하이닉스 (industry=반도체|메모리)
삼성전자 (industry=반도체|메모리|파운드리)
ARM (ARM, industry=반도체|IP)
Seagate (STX, industry=반도체|스토리지)
Micron (MU, industry=반도체|메모리)
SanDisk (SNDK, industry=반도체|메모리)
WDC (WDC, industry=반도체|스토리지)
AMD (AMD, industry=반도체|AI 인프라)
Intel (INTC, industry=반도체|AI 인프라|파운드리)
```

### T1 미국 빅테크 (4개사, macro layer)

```
Microsoft (MSFT, industry=빅테크|클라우드|AI)
Google (GOOGL, industry=빅테크|클라우드|AI 광고|자율주행)
Amazon (AMZN, industry=빅테크|클라우드|소비재|AI)
Meta (META, industry=빅테크|광고|AI|VR/AR)
```

### 한국 주도주 후보 워치리스트 (산업기초 + 본 테마 후보)

| 우선 | 종목 | T분류 | 본 테마 thesis |
|---|---|---|---|
| 1 | SK하이닉스 | T1 메모리 | HBM 정점 + DDR5 + eSSD |
| 2 | 삼성전자 | T1 메모리·파운드리 | HBM4 AMD MoU + CAPA #1 + Tesla 22조 |
| 3 | 한미반도체 | T2 반도체 후공정 | TC본더 글로벌 #1 |
| 4 | 효성중공업 | T1 전력 | UHV 변압기 미국 #1 |
| 5 | HD현대일렉트릭 | T1 전력 | UHV 미국 15-20% |
| 6 | LS ELECTRIC | T1 전력 | 스위치기어 + 800VDC 한국 선도 |
| 7 | 오이솔루션 | T2 광통신 | 1.6T·ITLA 국산화 |
| 8 | 두산에너빌리티 | T1 SMR | SMR forging 5사 중 1 |
| 9 | 현대건설 | T1 SMR | SMR EPC Holtec 협력 |

---

# Step 9 통합본 — 핵심 결론 종합

## A. valuation thesis 결론 (3년 vs 5년)

**3년 Peak (2028)**: ★ SK하이닉스 3.0x / AMD 2.6x / 삼성 2.5x / Meta 2.2x / Intel 2.1x / SanDisk 2.0x = 정점 leverage 6 종목

**5년 Normalize (2030)** 낙관: Meta 2.5x / SK 2.4x / AMD 2.3x / 삼성 2.2x / Intel 2.0x = secular survivor 5 종목

## B. 한국 주도주 결론

**★ 1순위: SK하이닉스 + 삼성전자** — HBM 정점 + 메모리 CAPA + HBM4 AMD MoU (삼성) + NVIDIA 단독 (SK)

## C. 미국 주도주 결론

**★ 1순위: AMD + Meta** — NVIDIA 대안 #1 (AMD) + AMD 단독 driver (Meta) 양강. ★ Meta·OpenAI 12GW MI450 핵심 catalyst

**★ 2순위: NVIDIA** — 본 테마 needle-mover지만 단기 1.09x = 이미 가격 반영. long-term holdings로 monopoly 지속 가능성

## D. ★ 4사 macro layer 핵심 시그널 (분기 트래킹)

- 4사 CY26 CapEx 합산 $585B + peak 시점 2027 H2 ~ 2028 H1 = secular 정점 미도래
- AI ARR 합산 $122B (2x YoY)
- "constrained through 2026" 4사 commentary 수렴
- NVIDIA Q1 FY27 record + 9분기 연속 컨센 beat

## E. ★ NVIDIA monopoly 위협 catalyst (5년 risk)

| 위협 | 5년+ 점유 영향 | macro evidence |
|---|---|---|
| #1 AMD MI400 | 80% → 70-75% | Meta 6GW + OpenAI 6GW = 12GW |
| #2 하이퍼스케일러 ASIC | -8-10%pt | TPU+MTIA+Trainium+Maia = $225B+ |
| #3 CUDA 대체 | 일부 잠식 | ROCm·Triton·Mojo (장기) |
| #4 중국 통제 | upside | H20 $0 baseline |

---

## v5 changelog

**v5 (2026-06-21)**: Step 9 통합본 append
- 14개사 기업 분석 완료 (반도체 10 + 빅테크 4)
- 4사 macro layer baseline + peak/normalize 도출 (peak 2027 H2 ~ 2028 H1)
- 3년 peak (2028) / 5년 normalize (2030) dual horizon Terminal 시나리오
- 14개사별 Long-run multiple anchor + Terminal 시총 시나리오별
- 한국 주도주: SK·삼성 / 미국 주도주: AMD·Meta
- ★ NVIDIA monopoly 4대 위협 catalyst macro evidence
- 메타데이터: active_companies dominant 8 / challenger 2 / macro_layer 4
- 워치리스트 자동 등록: 반도체 10 + 빅테크 4 + 한국 주도주 9
 Step 6. 산업 유형 + 주도 섹터 가능성

| 항목 | 결론 |
|---|---|
| 산업 유형 | **메가 트렌드** (AI 슈퍼사이클 2단) |
| 단계 | 초기-중기 (2024-25 스토리(narrative) → 2026-2030+ Q 폭발) |
| 글로벌 트렌드 관통 + 한국 Moat | ★★★ — 17 segment 중 **10 segment 한국 글로벌 Top 5** (SMR 부품 + 800VDC LS ELECTRIC 추가), 5 segment Top 2 |
| **주도 섹터 가능성** | **★★★ 매우 높음** |

---

# Step 7. 리스크 팩터

| 리스크 | 확률 | 임팩트 | 시그널 |
|---|---|---|---|
| 에이전트 스토리(narrative) 약화 | 25% | 매우 큼 | Anthropic·OpenAI ARR 정체 |
| AI capex 변곡점 | 25% | 큼 (12-18개월 침체) | 하이퍼스케일러 capex 가이던스 하향 |
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
- NVIDIA 데이터센터 segment, NVIDIA Blackwell allocation, TSMC CoWoS capa expansion, HBM 가격 (TrendForce), **DDR5 server 가격 (DRAMeXchange) ★**, **eSSD Top 5 분기 매출 (TrendForce) ★**, **800G/1.6T 트랜시버 출하 (Cignal AI) ★**, **서버 CPU 점유 (Mercury Research) ★**, HBM4 양산, 삼성 HBM3E 12단 NVIDIA 인증

## 전력 측
- 변압기 lead time (Powermag·Nikkei), 한국 변압기 3사 분기 수주, 3사 수주잔고, **가스터빈 3사 분기 신규 주문 (GE·Siemens·Mitsubishi) ★**, SMR 신규 PPA (Constellation·Talen·Vistra·Kairos), **두산에너빌리티 SMR 부품 수주 ★**, **현대건설 Holtec 협력 진행 ★**, IEA 데이터센터 전력, 하이퍼스케일러 분기 capex

---

# Step 9. 통합본 (v4 → v5 add-on, 2026-06-21)

> **본 통합본 frame**: 14개사 기업 분석 (반도체 10 + 빅테크 4) 완료 후 통합. **수요 측 빅테크 4사 (MSFT·Google·AWS·Meta) macro layer**를 baseline으로, **공급 측 반도체 10개사 thesis**를 cross-validation. **3년 (peak) / 5년 (normalize) dual horizon Terminal 시나리오**.

> **본 분석 frame 핵심**: peak 시점은 사전 가정 X — ★ 빅테크 4사 macro 분석 결과로 도출. 사이클 위치 axis (3년 = peak·근접 가시성 / 5년 = normalize 후 정상 trajectory). 4사 CapEx 합산 + AI ARR 합산 → peak/normalize 시점·깊이 도출 → 14개사 thesis 시나리오별 검증.

> **분석된 14개사 reference**:
> - **반도체 10개사**: SK하이닉스, 삼성전자, Micron, ARM, Seagate, SanDisk, WDC, AMD, Intel, NVIDIA
> - **빅테크 4사 (macro layer)**: MSFT, Google, AWS, Meta

---

## 9-1. 통합 narrative (산업기초 → 14개사 thesis flow)

### 1단계: 산업 기초 (반도체·전력 인프라 = 사이클 산업이지만 본 테마는 사이클·secular 양면)

- **반도체 산업기초** (v1, 2026-05-18): 메모리 4-5년 단주기 + 매크로 7-10년 장주기 중첩. CR3 95%+ 과점 + EUV 양산 한정 = 진입 장벽 영구. ★ **본 테마는 사이클 정점 + secular AI 진입 양면 hybrid**
- **전력 인프라 산업기초** (v1, 2026-05-18): 변압기·가스터빈 lead time 128주 = 공급 절제 누적. ★ AI DC 전력 폭증으로 신규 segment (800VDC) 등장

### 2단계: 에이전트 AI 테마 narrative (v4 1차 분석 종합)

- **에이전트 1건 = chat 1턴 대비 토큰 20-30x** (Stanford·NVIDIA 실측) → 추론 인프라 폭증
- **17 segment 병목**: 반도체 8 (HBM·DDR5·eSSD·GPU·광통신·CPU·CoWoS·wafer) + 전력 9 (변압기·스위치기어·HVDC·케이블·UPS·액랭·가스터빈·SMR·★ 800VDC) + 한국 핵심 비중 (10 segment 글로벌 Top 5)
- **병목 카테고리**: **(A) 구조적 메가 병목 + (D) 동반 확대 hybrid**
- **한국 접근 가능 TAM 2028E $216-262B+**

### 3단계: ★ 수요 측 4사 macro layer (★ v5 신규)

- ★ **빅테크 4사 CY26 CapEx 합산 ~$585B (FY25 $258B 대비 +127%)**: MSFT $190B + Google $100B + AWS $195B + Meta $100B
- ★ **빅테크 4사 AI ARR 합산 ~$122B (2x YoY)**: MSFT $37B (+123%) + Google $30B+ + AWS $25B+ + Meta $30B
- ★ **AI Foundation 4가지 strategy 양상**:
  - MSFT = OpenAI 독점 ($13B+) + Maia (Intel Foundry 18A) + Cobalt
  - Google = Gemini 자체 + Anthropic $3B + ★ TPU (Broadcom 위탁) + Axion
  - AWS = ★ Anthropic $8B (최대) + ★ OpenAI 2GW Trainium (신규) + Graviton (가장 성숙)
  - Meta = ★ Llama open source (유일) + ★ AMD MI450 6GW (AMD 최대 단일) + MTIA (Broadcom)
- ★ **공통 시그널** (4사 모두 동일 commentary 수렴):
  - MSFT (Amy Hood): *"remain constrained at least through 2026"*
  - Google (Sundar): *"compute constrained"*
  - AWS (Andy Jassy): *"AI represents the largest opportunity since cloud"*
  - Meta (Zuckerberg): *"AI is the most exciting opportunity I've worked on"*
- → ★ **AI 인프라 사이클 정점 미도래의 가장 강한 정량 시그널**

### 4단계: ★ 공급 측 14개사 thesis cross-validation (반도체 10 + NVIDIA)

> 빅테크 4사 macro 신호 → 반도체 10개사·NVIDIA thesis 검증. ★ Moat 4.8 (NVIDIA) → SK 4.4 → 삼성 4.3 → ARM 4.1 → STX 4.1 → Micron/SNDK/WDC 4.0 → AMD 3.8 → Intel 2.8.

| layer | 종목 | Moat | 본 테마 수요 driver evidence (4사 macro 신호) |
|---|---|---|---|
| **Hot (HBM)** | SK하이닉스 | **4.4** | 4사 모두 NVIDIA Blackwell·Rubin 발주 → SK HBM3E·HBM4 majority driver |
| **Hot (HBM)** | 삼성전자 | 4.3 | ★ Meta 6GW MI450 = AMD MI455X Samsung preferred HBM4 (2026.03 MoU) driver |
| **Hot+Warm** | Micron | 4.0 | ★ MSFT/AWS 미국 본토 supplier 신뢰 + 1Q26 HBM4 양산 진입 |
| **Compute (GPU)** | **NVIDIA** | **4.8** | 4사 모두 NVIDIA #1 발주 ($30-40B/년 MSFT·AWS, $20-25B Meta, $5-10B Google) |
| **Compute (GPU)** | AMD | 3.8 | ★ Meta MI450 6GW (단독) + OpenAI 6GW + AWS MI300 일부 = 12GW MI450 mega deal |
| **Compute (CPU)** | Intel | 2.8 | ★ MSFT Maia ASIC (Intel Foundry 18A 첫 외부 대형) = Foundry turnaround leg |
| **IP layer** | ARM | 4.1 | ★ 4사 모두 ARM Neoverse 자체 CPU (Cobalt·Axion·Graviton — Meta만 없음) = ARM DC royalty 2x YoY driver |
| **Warm-Cold** | SanDisk | 4.0 | 4사 데이터센터 eSSD + KV cache offload 직접 발주 |
| **Cold (HDD)** | WDC | 4.0 | ★ AWS S3 Glacier 글로벌 #1 + MSFT Azure exabyte 발주 = nearline 52% sold out driver |
| **Cold (HDD)** | Seagate | 4.1 | ★ 5 CSP qualified on Mozaic 3+ = AWS·MSFT·Google·Meta·Oracle = HAMR 양산 선행 |

### 5단계: ★ NVIDIA monopoly 4대 위협 catalyst — 빅테크 4사 macro evidence

| 위협 | 단기 (2-3년) | 장기 (5년+) | 4사 evidence |
|---|---|---|---|
| **#1 AMD MI400** | 점유 4%→18% (2026E) | 점유 70-75% NVIDIA jam 가능 | ★ Meta 6GW + OpenAI 6GW = 12GW mega deal |
| **#2 하이퍼스케일러 ASIC** | -3-5%pt | -8-10%pt | ★ Google TPU (가장 성숙) + Meta MTIA + AWS Trainium + MSFT Maia 합 $225B+ 백로그 |
| **#3 CUDA 대체** | dominance 유지 | 일부 잠식 | ROCm + OpenAI Triton + Mojo (장기) |
| **#4 중국 통제** | $0 baseline | upside optionality | H20 $0 (Q1 FY27) → 재개 시 분기 $4-5B upside |

→ ★ **단기 2-3년 thesis 강고, 장기 5년+ monopoly 점진 약화 가능**

---

## 9-2. Terminal 밸류 시나리오 — 3년 (peak) / 5년 (normalize) dual horizon

### 9-2-1. ★ 4사 macro layer baseline — peak 시점·normalize 깊이 도출

#### 4사 CapEx 합산 trajectory

| 연도 | MSFT | Google | AWS | Meta | **4사 합** | YoY | 비고 |
|---|---|---|---|---|---|---|---|
| FY23 | 28.1 | 32.3 | 52.7 | 27.3 | 140.4 | — | AI 진입 시작 |
| FY24 | 44.5 | 52.5 | 77.7 | 39.2 | 213.9 | +52% | ★ AI Copilot/Llama/Gemini launch |
| FY25 | 65.0 | 75.0 | 105.0 | 75.0 | **320.0** | **+50%** | ★ AI 슈퍼사이클 본격 |
| **CY26E** | **190** | **100** | **195** | **100** | **★ ~585B** | **+83%** | ★ Hyperscaler $640B 컨센과 일치 (4사 합 91%) |
| **CY27E** | **220** | **125** | **240** | **120** | **★ ~705B** | **+20%** | 가속 둔화이지만 +20% 성장 지속 |
| **CY28E** | **240** | **145** | **270** | **130** | **★ ~785B** | **+11%** | **★ peak 도달 가능성 (4사 평균 +11% = 둔화 진입 시그널)** |
| CY29E | 255 | 160 | 285 | 130 | ~830B | +6% | normalize 진입 시작 |
| CY30E | 260 | 165 | 290 | 130 | ~845B | +2% | normalize 안정화 |

#### ★ Peak 시점 도출 (4사 macro 신호 기반)

| 신호 | 시점 | 의미 |
|---|---|---|
| **★ "remain constrained through 2026"** (MSFT Amy Hood) | 2026 전체 | 공급 제약 천장 = 수요 압도 |
| **★ "second half 2026 acceleration"** (MSFT) | 2H 2026 | 가속 지속 |
| **★ AWS +28% (15분기 최고)** | Q1 2026 | 5분기 연속 가속 |
| **★ Google GCP +63% (11분기 만 가속)** | Q1 2026 | 가속 진입 |
| **★ MSFT RPO $627B (+99% YoY) = 2-3년 가시성** | Q1 2026 | 매출 가시성 2-3년 sector best |
| **★ AWS OpenAI 2GW Trainium 신규** | Q1 2026 | 추가 수요 driver |
| **CY26 CapEx 가이던스 4사 모두 +20-30% upside** | 2026 | peak 도달 미명 |
| **NVIDIA Q1 FY27 매출 +85% YoY record + 9분기 연속 컨센 beat** | Q1 FY27 | secular 정점 미도래 |

→ ★ **Peak 시점: 2027 H2 ~ 2028 H1 (3년 시점)** — 4사 평균 CapEx 성장률 +11% 둔화 진입 시점

#### ★ Normalize 시나리오 (5년 시점, 2030)

| 시나리오 | normalize 깊이 (peak 대비) | 4사 합 CapEx (2030) | 사이클 평균 vs 메가 트렌드 비교 |
|---|---|---|---|
| **★ 낙관** | -5% (메가 트렌드 영구 base) | ~$745B (vs peak $785B) | AI agent + edge AI + 신규 industrial AI 영구 수요 |
| **★ 중립** | -15% (secular base 강함) | ~$670B | 사이클 진폭 작음, AI 인프라 base 영구 |
| **★ 비관** | -30% (메모리 사이클 패턴) | ~$550B | 메모리 사이클 (FY22 → FY23 -37%) 패턴 적용 |

### 9-2-2. ★ 3년 시점 (peak, 2028) — 14개사 정점 leverage 시나리오

| 종목 | Moat | 3년 시점 (peak) thesis | P 시나리오 | Q 시나리오 | 정점 OPM/GPM | 매출 trajectory |
|---|---|---|---|---|---|---|
| **NVIDIA** | 4.8 | ★ Vera Rubin + Kyber rack 양산 정점 | (A) ASP step-up (Blackwell 대비 +50%) | DC 출하 +50% YoY | GPM 73-75% 유지 | FY28 ~$420B (+30% YoY) |
| **SK하이닉스** | 4.4 | HBM3E + HBM4 majority + DDR5 정점 | (A) ASP 강한 상승 | HBM CAPA 매진 | OPM 60%+ | $130-150조원 (+30%) |
| **삼성전자** | 4.3 | ★ HBM4 AMD MI455X driver + 메모리 절대 CAPA #1 | (A) HBM premium | DRAM·HBM 전 segment 폭증 | DS OPM 50%+ | DS $200B+ |
| **AMD** | 3.8 | ★ MI450 6GW + 12GW total deal + EPYC 점유 30%+ | (D) 안정 ASP + Q 폭증 | AI 가속기 점유 25-30% | OPM 25-30% | $80B+ (CY28) |
| **ARM** | 4.1 | ★ 4사 모두 ARM CPU + AGI CPU + ARMv9 royalty rate 2x | (E) 점진 상승 | royalty volume +40% | OPM 50%+ | $7-8B (FY28) |
| **Seagate** | 4.1 | ★ HAMR Mozaic 4·5 + FY27 build-to-order | (A) ASP 안정 | Exabyte +47% 지속 | GPM 50%+ | $15B+ (FY28) |
| **WDC** | 4.0 | nearline 52% + 분사 + UltraSMR/EPMR 가속 | (A) ASP 안정 | exabyte +30% | GPM 50%+ | $15B+ (FY28) |
| **SanDisk** | 4.0 | NAND 정점 + HBF 양산 + $42B NBM | (A) ASP 정점 +200%+ | NAND 폭증 | OPM 70%+ | $20B+ (FY28) |
| **Micron** | 4.0 | HBM 21% 가속 + DDR5 #3 + 미국 본토 premium | (A) HBM·DDR5 ASP 강상승 | 점진 | OPM 50%+ | $50B+ (FY28) |
| **AMD** (중복 정리) | — | — | — | — | — | — |
| **Intel** | 2.8 | ★ Foundry 18A turnaround (MSFT Maia + Microsoft·Amazon·DoD 확보) | (C) Xeon 정상화 + Foundry 성장 | Foundry 점진 ramp | OPM 회복 10-15% | $80-90B (CY28) |
| **MSFT** | macro | AI ARR $75B+, Azure +35%+ 지속, M365 Copilot 50M+ | (A) Azure 안정 P | AI ARR 가속 | OPM 47-50% | $400B+ (FY28) |
| **Google** | macro | GCP +40%+, Gemini App 600M+, TPU 7세대 양산 정점 | (A) 안정 | GCP 폭증 | OPM 35%+ | $600B+ (FY28) |
| **AWS** | macro | AWS $230B+ (+30%), Trainium 3, Anthropic +OpenAI 양면 | (A) 안정 | Cloud #1 폭증 | AWS OPM 35%+ | $1T+ (CY28 전체) |
| **Meta** | macro | AI 광고 ARR $80B+, Llama 6, AMD MI450 ramp 본격 | (A) 광고 efficiency | DAP 3.8B | OPM 48%+ | $350B+ (CY28) |

### 9-2-3. ★ 5년 시점 (normalize, 2030) — 14개사 secular 생존 시나리오

> **5년 시점 핵심 질문**: Peak (2028) 후 normalize 시점에 **누가 살아남고 누가 점유 잃는지** = secular thesis 본질.

| 종목 | 5년 시점 thesis (낙관) | 5년 시점 thesis (중립) | 5년 시점 thesis (비관) | secular buffer 강도 |
|---|---|---|---|---|
| **NVIDIA** | monopoly 유지 80% | 점유 75% (AMD/ASIC 침투) | 점유 70% + AMD MI500/Rubin Ultra 경쟁 | ★★★ (CUDA lock-in 20년) |
| **SK하이닉스** | HBM #1 유지 53%+ | HBM majority 50% | HBM4E dual sourcing 본격 | ★★★ (HBM4E + 차세대 packaging) |
| **삼성전자** | HBM4 AMD majority + 메모리 #1 | 메모리 #1 유지 (HBM #2) | HBM3E 후발 만회 실패 | ★★ (DRAM CAPA + 파운드리) |
| **NVIDIA Grace + ARM** | ARM DC 30%+, AGI CPU 본격 매출 | ARM DC 25% | ARM 라이선시 자기잠식 | ★★★ (royalty 모델 영구) |
| **AMD** | AI 가속기 25-30% 유지 | AI 가속기 20% | NVIDIA Rubin Ultra 우위 회복 | ★★ (NVIDIA 대안 #1 차별화) |
| **WDC + STX (HDD 양강)** | Mozaic 5/6 + EPMR 차세대 정점 | nearline 사이클 안정 | SSD 일부 잠식 (장기) | ★★★ (HDD vs SSD 가격 5-10x 영구) |
| **SanDisk** | HBF 양산 + NAND 차세대 | NAND 사이클 보통 | NAND 사이클 침체 (-50% 매출) | ★★ (NAND 단일사업 진폭 ±61pt) |
| **Micron** | HBM 25%+ + 미국 본토 영구 premium | HBM 21% 유지 | HBM 후발 가속 실패 | ★★ (미국 본토 secular 영구) |
| **Intel** | Foundry 18A 양산 + 14A 진입 | Foundry trough → 회복 초기 | TSMC 압도, Intel 18A 양산 실패 | ★ (Foundry 18A turnaround) |
| **MSFT** | AI ARR $100B+ + OpenAI 의존 분산 | AI ARR $80B + OpenAI 갱신 | OpenAI exclusivity weakening | ★★★ (Azure + Copilot + Maia) |
| **Google** | GCP +30% 지속 + TPU 8세대 | GCP +20% + TPU 7세대 안정 | DOJ Search 분리 명령 진전 | ★★★ (TPU + Gemini + Anthropic + Broadcom) |
| **AWS** | AWS +25%+ 지속 + Trainium 3 + Anthropic Claude 5 | AWS +20% + 안정 | AWS OPM 30% 진입 (마진 압박) | ★★★ (Cloud 절대 #1) |
| **Meta** | AI 광고 ARR $150B+ + RB Meta 100M+ | AI 광고 ARR $100B + Llama 영향력 | Reality Labs 적자 -$30B+ + Llama 약화 | ★★ (광고 monetization 단독) |

---

## 9-3. ★ 멀티플 적정성 — Long-run anchor

> **본 모드 frame**: 단기 forward P/E·EV/EBITDA·EV/Sales는 다루지 않음 (분기 실적 분석 영역). ★ **산업 성숙기 Long-run anchor 멀티플 1개씩 결정**.

### 9-3-1. 14개사 Long-run anchor 멀티플 결정 논거

| 종목 | Long-run PER anchor | EV/EBITDA anchor | EV/Sales anchor | 근거 (산업 성숙기 평균 + 글로벌 peer + ROE·ROIC) |
|---|---|---|---|---|
| **NVIDIA** | **22x** | **18x** | **10x** | secular monopoly + GPM 75% + FCF margin 32% + 자본 환원 게임 체인저. Apple-like compounder transition. 단 monopoly 위협 catalyst -5x discount |
| **SK하이닉스** | **8x** | **5x** | **2.5x** | 메모리 사이클 정점 평균 (P/E 6-12x range). HBM premium +2x. AI secular base +1x |
| **삼성전자** | **10x** | **6x** | **2.5x** | DRAM #1 + 파운드리 #2 + HBM4 AMD MoU. 사이클 평균 12x. multi-segment discount |
| **AMD** | **30x** | **20x** | **8x** | NVIDIA 대안 + Lisa Su turnaround track record. 성장 secular premium. 단 사이클 risk -5x |
| **ARM** | **40x** | **30x** | **20x** | chipless IP + royalty model 영구. PEG ratio 0.6x. CSS·ARMv9 driver. 단 AGI CPU 라이선시 경쟁 -5x |
| **Seagate** | **15x** | **10x** | **3x** | HDD pure-play + HAMR 선두 + 자본 환원 king. sustainable 사이클 정점 |
| **WDC** | **12x** | **8x** | **2.5x** | HDD #1 + 분사 1년차. sustainable 사이클이지만 분사 premium 약간 |
| **SanDisk** | **10x** | **6x** | **2x** | NAND pure-play 정점. 사이클 진폭 큼 (±61pt). 보수적 anchor |
| **Micron** | **10x** | **6x** | **2.5x** | HBM 후발 + 미국 본토 premium. SK 대비 약간 우위 anchor |
| **Intel** | **15x** | **8x** | **2x** | Foundry 18A turnaround anchor. 회복 시점 기준. 실패 시 5x risk |
| **MSFT** | **30x** | **22x** | **9x** | secular compounder + AI ARR + RPO + Cloud #2 + 자본 환원. Apple-like |
| **Google** | **22x** | **15x** | **6x** | secular compounder. 단 DOJ Antitrust -3-5x discount + AI Overviews monetization risk |
| **AWS (Amazon)** | **35x** | **20x** | **3.5x** | Cloud 절대 #1 + Foundation 양면 + Trainium. multi-segment SOTP (Stores + AWS + Ads) |
| **Meta** | **25x** | **18x** | **8x** | 광고 #1 + Llama + AMD 단독 + DAP 3.56B. Reality Labs 적자 -5x discount |

### 9-3-2. 멀티플 anchor 종합 결론

**메모리 사이클 종목 (SK·삼성·Micron·SanDisk)**: Long-run PER 8-10x = 사이클 정점 평균. HBM secular premium +1-2x로 보정.

**HDD 사이클 종목 (WDC·STX)**: PER 12-15x = HDD pure-play + 자본 환원 base.

**Compute secular 종목 (NVIDIA·AMD·ARM·Intel)**: PER 22-40x = secular growth premium. ARM 가장 높음 (royalty model), Intel 가장 낮음 (turnaround).

**빅테크 macro layer (MSFT·Google·AWS·Meta)**: PER 22-35x = secular compounder. AWS Cloud #1으로 가장 높음, Google DOJ로 가장 낮음.

---

## 9-4. ★ Terminal 시총 시나리오별 결과 (14개사)

> ★ **현재 시총 대비 성장 배수**가 핵심 결론. 종목별 (Terminal 영업이익 × 멀티플 = Terminal 시총).

### 9-4-1. 3년 시점 (peak, 2028) — Terminal 시총

| 종목 | 현재 시총 ($T·조원) | Peak OP (2028E) | Long-run PER | **3년 Terminal 시총** | **현재 대비 배수** |
|---|---|---|---|---|---|
| **NVIDIA** | $5.7T | $280B+ (FY28) | 22x | **$6.2T** | **1.09x** (제한적, monopoly 위협 catalyst 일부 반영됨) |
| **SK하이닉스** | 200조원 (~$140B) | 70-80조원 | 8x | **560-640조원** (~$400-460B) | **2.8-3.2x** ★ 메모리 사이클 정점 |
| **삼성전자** | 500조원 (~$350B) | DS 90-100조원 + 모바일 30조 = 120-130조원 | 10x | **1,200-1,300조원** (~$840-910B) | **2.4-2.6x** ★ 메모리 + 파운드리 + HBM4 AMD |
| **AMD** | $290B | $25B+ (CY28) | 30x | **$750B** | **2.6x** ★ Meta·OpenAI 12GW + EPYC 가속 |
| **ARM** | $200B | $4B+ (FY28) | 40x | **$160B** | **0.8x** (이미 가격 반영, 단 royalty rate +) |
| **Seagate** | $50B | $3-4B (FY28) | 15x | **$45-60B** | **0.9-1.2x** (현재 가격 적정 — HAMR premium 일부) |
| **WDC** | $25B | $2.5-3B (FY28) | 12x | **$30-36B** | **1.2-1.4x** (분사 1년차 가격 반영 부족) |
| **SanDisk** | $25B | $5B+ peak (FY28) | 10x | **$50B** | **2.0x** ★ NAND 사이클 + HBF |
| **Micron** | $130B | $20B+ (FY28) | 10x | **$200B** | **1.5x** ★ HBM 가속 |
| **Intel** | $90B | $10-15B (Foundry 회복 시) | 15x | **$150-225B** | **1.7-2.5x** ★ Turnaround 성공 시 |
| **MSFT** | $3.7T | $150B+ (FY28) | 30x | **$4.5T** | **1.22x** secular compounder |
| **Google** | $2.2T | $130B+ (FY28) | 22x | **$2.9T** | **1.32x** AI 광고 + Cloud + TPU |
| **AWS** | $2.3T | AWS $60B + 전체 $90B (CY28) | 35x | **$3.2T** | **1.39x** Cloud 절대 #1 |
| **Meta** | $1.5T | $130B+ (CY28) | 25x | **$3.3T** | **2.2x** ★ AI 광고 ARR 폭증 |

### 9-4-2. 5년 시점 (normalize, 2030) — Terminal 시총

| 종목 | 5년 시점 Normalize OP (낙관) | Long-run PER | 5년 낙관 시총 | 5년 중립 시총 | 5년 비관 시총 |
|---|---|---|---|---|---|
| **NVIDIA** | $250B | 22x | $5.5T | $4.5T | $3.5T |
| **SK하이닉스** | 60조원 | 8x | 480조원 | 350조원 | 250조원 |
| **삼성전자** | 110조원 | 10x | 1,100조원 | 850조원 | 600조원 |
| **AMD** | $22B | 30x | $660B | $500B | $350B |
| **ARM** | $5B | 40x | $200B | $160B | $120B |
| **Seagate** | $3.5B | 15x | $52B | $42B | $30B |
| **WDC** | $2.8B | 12x | $34B | $26B | $18B |
| **SanDisk** | $3B (normalize) | 10x | $30B | $20B | $12B |
| **Micron** | $18B | 10x | $180B | $130B | $90B |
| **Intel** | $12B | 15x | $180B | $120B | $60B (Foundry 실패) |
| **MSFT** | $170B | 30x | **$5.1T** | $4.0T | $3.0T |
| **Google** | $145B | 22x | **$3.2T** | $2.5T | $1.8T (DOJ 진전) |
| **AWS** | $100B (전체) | 35x | **$3.5T** | $2.7T | $2.0T |
| **Meta** | $150B+ (AI 광고 정점) | 25x | **$3.75T** | $2.8T | $1.8T (RL 실패) |

### 9-4-3. 시나리오별 성장 배수 종합

| 종목 | 3년 Peak 배수 | 5년 낙관 배수 | 5년 중립 배수 | 5년 비관 배수 |
|---|---|---|---|---|
| **NVIDIA** | 1.09x | 0.96x | 0.79x | 0.61x |
| **SK하이닉스** | **3.0x ★** | 2.4x | 1.75x | 1.25x |
| **삼성전자** | **2.5x ★** | 2.2x | 1.7x | 1.2x |
| **AMD** | **2.6x ★** | **2.3x ★** | 1.7x | 1.2x |
| **ARM** | 0.8x | 1.0x | 0.8x | 0.6x |
| **Seagate** | 1.05x | 1.04x | 0.84x | 0.6x |
| **WDC** | 1.3x | 1.36x | 1.04x | 0.72x |
| **SanDisk** | **2.0x ★** | 1.2x | 0.8x | 0.48x (사이클 침체) |
| **Micron** | **1.5x** | 1.4x | 1.0x | 0.69x |
| **Intel** | **2.1x ★★** | **2.0x ★★** | 1.3x | 0.67x |
| **MSFT** | 1.22x | 1.38x | 1.08x | 0.81x |
| **Google** | 1.32x | 1.45x | 1.14x | 0.82x |
| **AWS** | 1.39x | 1.52x | 1.17x | 0.87x |
| **Meta** | **2.2x ★** | **2.5x ★★** | 1.87x | 1.2x |

### 9-4-4. 시나리오별 BT 핵심 결론

#### ★ 3년 (peak, 2028) 최대 leverage 종목 (성장 배수 2.0x+)
- **SK하이닉스 3.0x** (HBM 정점 + HBM4 majority)
- **AMD 2.6x** (Meta·OpenAI 12GW + EPYC 가속)
- **삼성전자 2.5x** (HBM4 AMD + 메모리 절대 CAPA)
- **Meta 2.2x** (AI 광고 ARR + AMD 단독 + Llama)
- **Intel 2.1x** (Foundry 18A turnaround 성공 시)
- **SanDisk 2.0x** (NAND 사이클 정점)

#### ★ 5년 (normalize) secular survivor — 낙관 시나리오 2.0x+
- **Meta 2.5x** (AI 광고 ARR $150B+ + Reality Labs 흑전 가능성)
- **SK하이닉스 2.4x** (HBM3E·HBM4 dominance 유지)
- **AMD 2.3x** (NVIDIA 대안 #1 영구)
- **삼성전자 2.2x** (HBM4 AMD majority + 메모리 #1)
- **Intel 2.0x** (Foundry 18A → 14A 양산 성공)

#### ★ 비관 시나리오에서 살아남는 종목 (배수 1.0x+)
- **삼성전자 1.2x** (메모리 + 파운드리 buffer)
- **SK하이닉스 1.25x** (HBM secular base)
- **AMD 1.2x** (NVIDIA 대안 위치 영구)
- **Meta 1.2x** (광고 monetization 영구)
- **MSFT 0.81x / Google 0.82x / AWS 0.87x** (빅테크 안정성)

#### ★ Terminal 시나리오에서 한계 종목
- **NVIDIA**: 단기 (3년) 1.09x = 이미 가격 반영. 장기 (5년) 비관 시 0.61x = ★ monopoly 위협 4대 catalyst 본격화 risk
- **ARM**: 단기 0.8x = 이미 가격 반영, 단 5년 1.0x로 안정. royalty 모델 영구이지만 valuation 한계

#### ★ 종합 — 한국 주도주 후보 최상위
**SK하이닉스 + 삼성전자**: 메모리 3사 + HBM 정점 + 한국 주도주 후보 최상. 3년 Peak 2.5-3.0x.

#### ★ 미국 주도주 후보 최상위
**AMD + Meta**: NVIDIA 대안 #1 (AMD) + AMD 단독 driver (Meta) = ★ AMD·Meta 단독 driver 양면 양강 + AI 광고 monetization.

---

## 9-5. 메타데이터 갱신 (v5 active_companies dominant/challenger 분기)

> ★ v5 (2026-06-21) — 14개사 분석 완료 후 active_companies를 dominant/challenger 분기. **dominant = 현재 테마 패권 보유 (Moat 4.3+ 또는 점유 #1)**, **challenger = 패권 도전 중 (Moat 3.8-4.2 또는 빠른 성장)**.

### dominant (현재 패권 8개사)

| 종목 | 국가 | Moat | 패권 근거 |
|---|---|---|---|
| NVIDIA | 🇺🇸 | 4.8 | AI DC GPU 80%+ + CUDA + Networking |
| SK하이닉스 | 🇰🇷 | 4.4 | HBM 53%+ + NVIDIA 단독공급 |
| 삼성전자 | 🇰🇷 | 4.3 | DRAM 42% + HBM4 AMD MoU + 메모리 CAPA #1 |
| ARM | 🇬🇧/🇯🇵 | 4.1 | 모바일 99% + DC IP 광범위 + N1/N1X |
| Seagate | 🇺🇸 | 4.1 | HDD #1 (45%) + HAMR 양산 선행 |
| WDC | 🇺🇸 | 4.0 | nearline 52% + 2026 sold out |
| SanDisk | 🇺🇸 | 4.0 | NAND + HBF + $42B NBM |
| Micron | 🇺🇸 | 4.0 | HBM 21% + 미국 본토 premium + 1Q26 HBM4 |

### challenger (패권 도전 2개사)

| 종목 | 국가 | Moat | 도전 근거 |
|---|---|---|---|
| AMD | 🇺🇸 | 3.8 | NVIDIA 대안 #1 (4%→18%) + Meta·OpenAI 12GW |
| Intel | 🇺🇸 | 2.8 | Foundry 18A turnaround (MSFT Maia·DoD·Amazon 확보) |

### macro layer (빅테크 4사 — 수요 측, 워치리스트 mixed)

| 종목 | 국가 | role | 수요 측 evidence |
|---|---|---|---|
| MSFT | 🇺🇸 | macro #1 | AI ARR $37B + RPO $627B + CY26 CapEx $190B |
| Google | 🇺🇸 | macro #2 (NVIDIA 의존 최저) | GCP +63% + TPU + Anthropic + Broadcom |
| AWS (Amazon) | 🇺🇸 | macro #3 (Cloud 절대 #1) | AWS $137B + Trainium + Graviton + OpenAI 2GW |
| Meta | 🇺🇸 | macro #4 (AMD 단독 driver) | AI 광고 ARR $30B + AMD MI450 6GW + Llama open |

### narrative_shift_log 추가 (v5)

```yaml
- {date: 2026-Q1, event: "★ AWS OpenAI 2GW Trainium 신규 deal — MSFT-OpenAI 독점 깨는 evidence"}
- {date: 2026-Q1, event: "★ NVIDIA 자본 정책 게임 체인저 (배당 25배 + $80B buyback) — secular + 자본환원 hybrid 진입"}
- {date: 2026-Q1, event: "★ 4사 macro layer 합산 CapEx $585B (FY25 $258B 대비 +127%) — AI 인프라 사이클 정점 미도래 정량 시그널"}
- {date: 2026-Q1, event: "★ Meta MI450 6GW + 6th Gen EPYC lead = AMD thesis 단독 driver"}
- {date: 2026-Q2, event: "★ NVIDIA Q1 FY27 record + 9분기 연속 컨센 beat — secular 정점 미도래 검증"}
```

### bottleneck_category 확정

| Sub-category | 분류 | 적용 종목 |
|---|---|---|
| (A) 구조적 메가 병목 | HBM·CoWoS·첨단노드·UHV 변압기 등 | NVIDIA·SK·삼성·Micron·TSMC·효성·HD현대일렉 |
| (A) + (D) hybrid | 본 테마 전체 — 14개사 + 산업 17 segment | 전체 |

---

## 9-6. 워치리스트 자동 등록 (14개사)

> `feedback_watchlist_auto_add.md` 룰 적용. **반도체 (T1)** + **미국 빅테크 (T1)** 섹터에 자동 추가.

### T1 반도체 (10개사)

```
NVIDIA (NVDA, industry=반도체|AI 인프라)
SK하이닉스 (industry=반도체|메모리)
삼성전자 (industry=반도체|메모리|파운드리)
ARM (ARM, industry=반도체|IP)
Seagate (STX, industry=반도체|스토리지)
Micron (MU, industry=반도체|메모리)
SanDisk (SNDK, industry=반도체|메모리)
WDC (WDC, industry=반도체|스토리지)
AMD (AMD, industry=반도체|AI 인프라)
Intel (INTC, industry=반도체|AI 인프라|파운드리)
```

### T1 미국 빅테크 (4개사, macro layer)

```
Microsoft (MSFT, industry=빅테크|클라우드|AI)
Google (GOOGL, industry=빅테크|클라우드|AI 광고|자율주행)
Amazon (AMZN, industry=빅테크|클라우드|소비재|AI)
Meta (META, industry=빅테크|광고|AI|VR/AR)
```

### 한국 주도주 후보 워치리스트 매핑

| 우선순위 | 종목 | T분류 | 본 테마 thesis |
|---|---|---|---|
| **1** | SK하이닉스 | T1 메모리 | HBM 정점 + DDR5 + eSSD 3 segment Top 2 |
| **2** | 삼성전자 | T1 메모리·파운드리 | HBM4 AMD MoU + 메모리 CAPA #1 + 파운드리 #2 + Tesla 22조 |
| **3** | 한미반도체 | T2 반도체 후공정 | TC본더 글로벌 #1 (★ 신규 본 테마 매핑) |
| **4** | 효성중공업 | T1 전력 | UHV 변압기 미국 #1 |
| **5** | HD현대일렉트릭 | T1 전력 | UHV 미국 15-20% |
| **6** | LS ELECTRIC | T1 전력 | 스위치기어 + ★ 800VDC 한국 선도 |
| **7** | 오이솔루션 | T2 광통신 | 1.6T·ITLA 국산화 |
| **8** | 두산에너빌리티 | T1 SMR | SMR forging 글로벌 5사 중 1 |
| **9** | 현대건설 | T1 SMR | SMR EPC Holtec 협력 |

---

# Step 9 통합본 — 핵심 결론 종합

## A. 본 테마 valuation thesis (3년 vs 5년)

**3년 (peak, 2028)**: ★ SK하이닉스 3.0x / AMD 2.6x / 삼성전자 2.5x / Meta 2.2x / Intel 2.1x / SanDisk 2.0x = 정점 leverage 6 종목.

**5년 (normalize, 2030)**: 낙관 시나리오에서 Meta 2.5x / SK 2.4x / AMD 2.3x / 삼성 2.2x / Intel 2.0x = secular survivor 5 종목. 비관 시나리오에서도 1.2x+ 살아남는 종목 = 삼성·SK·AMD·Meta.

## B. 한국 주도주 결론

**★ 1순위: SK하이닉스 + 삼성전자** = HBM 정점 + 메모리 CAPA + HBM4 AMD MoU (삼성) + NVIDIA 단독공급 (SK).

## C. 미국 주도주 결론

**★ 1순위: AMD + Meta** = NVIDIA 대안 #1 (AMD) + AMD 단독 driver (Meta) 양강. ★ Meta·OpenAI 12GW MI450 mega deal 핵심 catalyst.

**★ 2순위: NVIDIA** = 본 테마 needle-mover지만 ★ 단기 (3년) 1.09x = 이미 가격 반영. 단 long-term holdings로 monopoly 지속 가능성.

## D. ★ 4사 macro layer 핵심 시그널 (분기 트래킹)

- **★ 4사 CY26 CapEx 합산 $585B** + ★ peak 시점 **2027 H2 ~ 2028 H1** = secular 정점 미도래
- **★ AI ARR 합산 $122B (2x YoY)** = AI monetization 정량 입증
- **★ "constrained through 2026" 4사 commentary 수렴** = 공급 제약 천장
- **★ NVIDIA Q1 FY27 record + 9분기 연속 컨센 beat** = secular 정점 미도래 검증

## E. ★ NVIDIA monopoly 위협 catalyst (5년 risk)

| 위협 | 5년+ NVIDIA 점유 영향 | macro evidence |
|---|---|---|
| #1 AMD MI400 | 80% → 70-75% | ★ Meta 6GW + OpenAI 6GW = 12GW (2025-10·2026-Q1) |
| #2 하이퍼스케일러 ASIC | -8-10%pt | ★ Google TPU + Meta MTIA + AWS Trainium + MSFT Maia 합 $225B+ |
| #3 CUDA 대체 | 일부 잠식 | ROCm·Triton·Mojo (장기) |
| #4 중국 통제 | upside optionality | H20 $0 baseline |

---

## v5 changelog

**v5 (2026-06-21)**: Step 9 통합본 append
- 14개사 기업 분석 완료 (반도체 10 + 빅테크 4)
- 4사 macro layer baseline + peak/normalize 도출
- 3년 peak (2028) / 5년 normalize (2030) dual horizon Terminal 시나리오
- 14개사별 Long-run multiple anchor + Terminal 시총 시나리오별
- 한국 주도주 결론 (SK·삼성), 미국 주도주 결론 (AMD·Meta)
- ★ NVIDIA monopoly 4대 위협 catalyst macro evidence 정리
- 메타데이터: active_companies dominant 8 / challenger 2 / macro layer 4 분기
- 워치리스트 자동 등록: 반도체 10개사 + 빅테크 4개사 + 한국 주도주 9개사



