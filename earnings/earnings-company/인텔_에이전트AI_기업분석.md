---
ticker: "INTC"
company_name: 인텔 (Intel Corporation)
country: US
theme_keyword: 에이전트AI
parent_industry: 반도체
cross_ref_industry: 전력 인프라
moat_strength: 2.8              # 본 테마 segment 가중 평균 — 메모리 3사 4.0+ 대비 낮음
moat_by_segment:
  x86_server_CPU: 3.0           # 점유 65%→54.9% 가속 잠식 (Q1 2026)
  x86_client_CPU: 3.0           # 점유 75% 안정, NVIDIA+ARM N1/N1X 신규 위협 (★ 2026-06-01)
  AI_가속기_Gaudi: 1.5          # 점유 ~0%, NVIDIA 96% 압도
  Intel_Foundry_18A: 4.0        # ★ Microsoft Maia 3 외부 고객 확정 + DoD + Amazon (긍정 narrative)
  미국_본토_지정학: 4.5         # CHIPS Act $7.86B 확정, Ohio·AZ·NM fab
  Mobileye_ADAS: 4.0            # 79.9% 자회사 (자율주행, 본 테마 별도)
trend_revenue_share: 30         # CCG 일부 + DCAI 100% + Foundry 일부 — 본 테마 직접 노출 약 30%
last_updated: 2026-06-02
auto_references:
  - 반도체_산업기초.md (2026-05-18)
  - 전력 인프라_산업기초.md (2026-05-18)
  - 에이전트AI_테마분석.md (v4, 2026-05-26)
  - INTC_기업개요.md (v4.9, 2026-05-18 — SEC 10-K 16개·10-Q 46개 기반)
analyst_reports_attached:
  - Intel Q1 2026 8-K (2026-04-23 발표)
  - NVIDIA GTC Taipei 2026 keynote (2026-06-01, Jensen Huang)
  - Microsoft Maia 3 "Griffin" Foundry 발표 (2026-01)
notes:
  - 인텔은 미국 기업, **회계연도 12월 마지막 토요일 종료** (FY25 = 2024-12-29~2025-12-27)
  - 본 분석 frame: 메모리 3사(SK·삼성·Micron) 사이클 정점 수혜와 정반대 — **구조적 침체 + Turnaround 종목**
---

# 인텔(INTC) 기업 분석 — 에이전트AI 테마

> **본 분석 frame**: 에이전트AI 테마 분석(v4)의 17 segment 중 **인텔은 본 테마 핵심 segment에서 점유율 가속 잠식 진행 중 + Intel Foundry 18A 첫 외부 대형 고객 확보로 한 줄기 positive narrative**. **메모리 3사(SK 4.4 / 삼성 4.3 / Micron 4.0)와 정반대 케이스 — 본 테마 직접 수혜자가 아닌 Turnaround 종목**. SK = HBM 집중 / 삼성 = 분산 + 차세대 / Micron = 후발 + 미국 지정학 / **Intel = x86 잠식 위협 + Foundry catch-up**가 핵심 narrative.

> **점유율·CAPA 표기 기준**: 본 분석의 모든 % 점유율은 **매출 기준** (TrendForce·Counterpoint·IDC·Mercury Research). **CAPA는 wafer 기준** (산업 통계, K wafer/월). bit shipment 기준 점유는 분기 변동성이 커서 본 분석에서 다루지 않음.

---

## Executive Summary (5줄)

1. **위치**: x86 CPU 글로벌 #1이지만 **DC server CPU 점유 1년 만에 64.4%→54.9% (-9.5%p)** (Q1 2026 IDC), AMD 24.1%→27.4%·**ARM 11.5%→17.7% (+6.2%p)**. AI 가속기 점유 ~0% (NVIDIA 96% 압도). **★ 2026-06-01 NVIDIA Jensen Huang Computex/GTC Taipei keynote에서 NVIDIA + Microsoft "N1/N1X" Arm-based PC 칩 발표 = client CPU 추가 위협**. Intel Foundry 18A 양산 시작 + Microsoft Maia 3 "Griffin" 첫 외부 대형 고객 확정 (★ 2026-01) — 유일한 positive narrative.
2. **해자 종합 (segment 가중)**: <strong>2.8 / 5.0</strong> (메모리 3사 4.0+ 대비 1.5p 낮음) — Intel Foundry 18A 4.0 / 미국 본토 지정학 4.5 / Mobileye 4.0이 buoyant, x86 server·client 3.0 / **AI 가속기 1.5 (사실상 부재)** 추격형 mix. 메모리 3사 가중 평균보다 명확히 낮음.
3. **재무 (구조적 침체 + Turnaround 초기)**: **FY25 매출 $52.85B (-0.5% YoY) / OP $0.26B / OPM 0.5% / NPM 15.3%** (2018 정점 $79B 대비 -33%, 12년 매출 CAGR **-0.46% 마이너스**). **Q1 2026 매출 $13.6B (+7% YoY) / GAAP EPS $(0.73) / Non-GAAP EPS $0.29** (restructuring $2.1B 차지). **DCAI +22% YoY ($5.1B) 가장 빠른 segment**, Intel Foundry +16% ($5.4B), CCG +1% ($7.7B). **신용등급 A2 / BBB+ / BBB+** (2024-10 동반 하향, 메모리 3사 회복 흐름과 반대).
4. **미래**: **★ Intel Foundry는 14A 외부 고객 확보 성패에 회사 전체 운명**. 18A는 Microsoft Maia 3 (Griffin) + Amazon Xeon 6 + DoD ($3B) 확보. NVIDIA·Broadcom 테스트 단계 (미확정). x86 client CPU는 NVIDIA+MSFT N1/N1X 협력으로 추가 위협. **Turnaround 성공 시 PBR 1.0 → 1.5~2.0 복원**, 실패 시 Foundry 분사·매각·매물화 시나리오.
5. **종합 판단**: <span class="star">★ Turnaround risk-reward 종목 (메모리 3사 같은 주도주 X)</span>. 본 테마 직접 수혜 측면에서는 후발·역방향. **(a) DC CPU 점유율 지속 잠식, (b) NVIDIA+ARM 협력 확대, (c) AI 가속기 완전 부재** 3대 구조적 risk. 단 **(1) Intel Foundry 18A Microsoft 확보 + 14A 외부 고객 ramp, (2) NVIDIA $5B 지분 인수 시너지, (3) Lip-Bu Tan CEO Turnaround**가 positive optionality.

---

# 항목 1. 입력 정리 + 기업 포지셔닝

## 1-1. 산업·테마 컨텍스트

- **반도체 산업기초** (v1, 2026-05-18): (A) 구조적 메가 병목 → 단, **인텔은 병목 수혜자가 아닌 병목으로 잠식당하는 측**
- **에이전트AI 테마 v4** (2026-05-26): 17 segment 중 CPU·Foundry segment 관련 위치
  - CPU 병목 = NVIDIA Grace + ARM Neoverse (Cobalt·Axion·Graviton) + AMD EPYC가 leader
  - Foundry 병목 = TSMC가 압도, Intel 18A는 후발 추격
- **한국 접근 가능 TAM (2028E)**: $216-262B+ (인텔은 미국이라 한국 TAM 무관)
- **Intel의 본 테마 frame**: 메모리 3사 사이클 정점 수혜와 정반대 — **본 테마 위협 + Foundry Turnaround 종목**

## 1-2. 인텔의 위치 (테마 v4 Moat 후보 — segment별)

| Segment | 글로벌 점유 (2025-2026) | 순위 | 비고 |
|---|---|---|---|
| **x86 server CPU (Xeon)** | **64.4% → 54.9% (Q1 2026, -9.5%p YoY)** | **#1** | AMD EPYC 27.4% / ARM 17.7%, 가속 잠식 |
| **x86 client CPU (PC, Core)** | **~75%** | **#1** | AMD Ryzen ~22% / ARM ~3% (Qualcomm + 신규 NVIDIA N1/N1X 위협) |
| **AI 가속기 (Gaudi 3)** | **~0%** | **n/a** | NVIDIA 96% / AMD 4% — Habana 인수에도 매출 매우 미미 |
| **Intel Foundry (제3자 매출)** | **<1%** | **#4-5** | TSMC ~60% 압도. 단 18A 외부 고객 확보 진행 (★ Microsoft Maia 3 Griffin 확정) |
| **★ 미국 본토 첨단 공정 (18A·14A)** | **유일 (TSMC AZ 외)** | **#1** | CHIPS Act $7.86B 확정, Ohio·Arizona·NM fab |
| **★ Mobileye (자율주행 ADAS)** | **79.9% 자회사** | — | ADAS Tier 1, 본 에이전트AI 테마와 별도 (자율주행 트렌드) |
| **신규 위협 (2026-06-01 ★)** | **NVIDIA + MSFT "N1/N1X" Arm-based PC 칩** | — | Computex/GTC Taipei keynote 발표, "new era of PC" |
| **HBM/메모리** | **0%** (2018 매각) | n/a | 본 테마 핵심 병목에서 완전 부재 |

→ **본 테마 핵심 segment (CPU·AI 가속기)에서 모두 후발 + 점유 잠식 진행**, 단 **Intel Foundry 18A는 첫 외부 대형 고객 확보로 catch-up 가능성**.

## 1-3. 사업부 구성 (FY25)

| Segment | FY25 매출 | YoY | 본 테마 연결 | 비중 |
|---|---|---|---|---|
| **CCG** (Client Computing Group, PC Core) | **$32.1B** | +6% | client CPU + AI PC (간접 본 테마) | **60.7%** |
| **DCAI** (Data Center & AI, Xeon·Gaudi·NIC·custom ASIC) | **$13.05B** | +2% | ★ 본 테마 직접 (CPU 병목) | **24.7%** |
| **Intel Foundry** (제조, 내부 + 외부) | **$13.86B** | -21% | ★ 본 테마 인프라 (Foundry 병목) | **26.2%** |
| All Other (Mobileye·IMS·Altera 분사 전) | $3.5B | -37% | Mobileye = 자율주행 별도 트렌드 | 6.6% |
| Intersegment 조정 | -$9.66B | — | — | — |
| **Total Consolidated** | **$52.85B** | **-0.5%** | | 100% |

### 본 테마 직접 매출 노출
- **DCAI $13.05B (24.7%)** = 본 테마 직접 (서버 CPU + AI 가속기)
- **Intel Foundry $13.86B (26.2%)** = 본 테마 인프라 (단, 매출 대부분 내부 CCG·DCAI 향)
- **CCG $32.1B (60.7%)** = 본 테마 간접 (PC 일부 AI PC)
- **순 본 테마 직접 노출 = 약 30%** (DCAI 100% + CCG 30% AI PC + Foundry 외부 매출 일부)
- → SK 60%+ / Micron 70% / 삼성 22% 대비 **중간 수준**, 단 **점유율 잠식 + AI 가속기 부재로 실질 수혜 미미**

---

# 항목 2. 비즈니스 모델 & 해자 (Moat) — Segment별

## 2-1. 비즈니스 모델 — 핵심 차별점

### x86 server CPU (Xeon) — DCAI 핵심
- **Xeon 6 (Granite Rapids P-core + Sierra Forest E-core)** 양산 — 2024-2025
- **Diamond Rapids (next-gen Xeon)** 2026-2027 예정
- **AMD EPYC 5세대 (Turin)** 대비 단일 코어 성능·power efficiency 모두 후발
- ARM server CPU (AWS Graviton 4/5, MSFT Cobalt, Google Axion) 점유 17.7% (YoY +620bp)

### x86 client CPU (PC, Core) — CCG 핵심
- **Intel Core Ultra Series 3 "Panther Lake" (Intel 18A)** — 2025-10 첫 18A 제품
- AMD Ryzen 점유 ~22%, ARM Qualcomm ~3%
- **★ 2026-06-01 NVIDIA + MSFT "N1/N1X" Arm-based PC 칩 Computex Taipei 발표 = client CPU 추가 위협**
- "New era of PC" narrative — Windows on Arm 본격화

### AI 가속기 (Gaudi 3) — DCAI 후순위
- **Habana Labs 인수 ($2B, 2019)** → Gaudi 1/2/3 출시
- Gaudi 3: 5nm process, 8 MME + 64 TPC, FP32/TF32/BF16/FP16/FP8 지원
- "2x performance per dollar vs popular GPU systems" 차별화 시도
- 단 NVIDIA CUDA ecosystem 압도 — 실 매출 매우 미미 (Gaudi 3 ramp 2024-2025, 매출 가시화 부진)

### Intel Foundry 18A — Turnaround 핵심
- **18A 양산 시작 (2025-10)** — RibbonFET (GAAFET) + PowerVia (backside power delivery) **세계 최초**
- **첫 18A 제품**: Intel Core Ultra Series 3 (Panther Lake, CCG) + Clearwater Forest (DCAI Xeon)
- **★ 외부 대형 고객 확보 (2026-01)**: Microsoft Maia 3 ("Griffin") AI 가속기 18A/18A-P 노드 멀티년 계약 — **첫 미국 본토 hyperscaler 첨단 AI 칩 양산**
- Amazon: Xeon 6 custom (Intel 3) + AI fabric chip 18A 확보
- DoD: $3B Secure Enclave 프로그램
- Broadcom·NVIDIA: 테스트 단계 (미확정)
- **14A (외부 고객 전용 첫 노드, 2027-2028)** — Foundry 사업 미래는 14A 외부 고객 확보 성패에 달림 (Tom's Hardware 보도: 미확보 시 14A 중단 가능성)

### 미국 본토 지정학 (CHIPS Act)
- **CHIPS Act $7.86B 확정 funding** (2024-11, 당초 $8.5B에서 -$0.64B 조정, $3B은 DoD Secure Enclave에서 차감)
- **Ohio fab** (당초 $20B, 2025년 슬로우다운으로 일정 지연)
- **Arizona** (Fab 52, 양산 중)
- **New Mexico** (Fab 9, 패키징)
- **Germany·Poland fab 취소** (2025-08, Lip-Bu Tan 부임 후 결정)

### Mobileye (자율주행 ADAS) — 별도 trend
- **79.9% 자회사** (2022-10 NASDAQ:MBLY 상장, 평가 $17B)
- 자율주행 ADAS Tier 1, 본 에이전트AI 테마와 별도 메가 트렌드
- 인텔 가치 평가 시 SOTP 별도 계산 필요

## 2-2. Moat 종류별 Segment 평가 (메모리 3사와 mirror 구조)

### Segment 1. x86 server CPU (Xeon, DC)
| 축 | 인텔 | AMD | ARM (Graviton·Cobalt·Axion) | 핵심 |
|---|---|---|---|---|
| 기술/특허 | 3 | **4** | 4 | AMD Zen 4/5 단일 코어 성능 우위, ARM Neoverse 효율 강점 |
| 메모리 절대 CAPA | **5** (IDM, 자체 fab) | 3 (TSMC dep) | 3 (TSMC dep) | 인텔 유일 IDM (양면) |
| 고객 lock-in | 3 (점유 가속 잠식) | **4** | 4 (hyperscaler 자체 ARM) | x86 ecosystem 점유 약화 |
| 규모 (server CPU 매출) | **4** ($13B DCAI) | 4 (~$13B) | 4 (자체 chip) | 인텔 단일 기업 #1 유지 |
| 병목 포지셔닝 | 2 (CPU 병목 잠식자) | 4 (AMD 점유 +) | **5** (가장 빠른 +) | ARM 가장 빠른 성장 (+6.2%p YoY) |
| **평균** | **3.4** | **3.8** | **4.0** | **ARM·AMD 우위, Intel 후발 가속** |

### Segment 2. x86 client CPU (PC, Core)
| 축 | 인텔 | AMD | ARM (Qualcomm·NVIDIA N1/N1X ★) | 핵심 |
|---|---|---|---|---|
| 기술/특허 | **4** (18A 첫 양산) | 4 | 3 (NVIDIA 신규 진입) | 인텔 18A Panther Lake 시작 |
| CAPA | **5** | 3 | 3 | 인텔 자체 fab |
| 고객 lock-in | **4** (Windows + x86 75%) | 3 | 2 (ARM ecosystem 미숙) | x86 절대 강함 (단 weakening) |
| 규모 (client CPU) | **5** ($32.1B CCG) | 3 | 2 (시장 진입 초기) | 인텔 압도적 매출 |
| 병목 포지셔닝 | 3 (위협 진행 중) | 3 | **4** (NVIDIA+MSFT 협력 신규 위협) | ★ 2026-06-01 NVIDIA Jensen Computex 발표 |
| **평균** | **4.2** | **3.2** | **2.8** | **인텔 client CPU 아직 강함, 단 위협 가속** |

### Segment 3. AI 가속기 (Gaudi 3, GPU)
| 축 | 인텔 | NVIDIA | AMD (MI300/400) | 핵심 |
|---|---|---|---|---|
| 기술/특허 | 2 | **5** | 4 | NVIDIA CUDA ecosystem 압도 |
| CAPA | 3 (자체 fab) | **5** (TSMC capacity) | 3 (TSMC) | NVIDIA 알로케이션 우선 |
| 고객 lock-in | 1 (실 점유 ~0%) | **5** (96%) | 3 (4%) | CUDA lock-in 절대 |
| 규모 | 1 (매출 미미) | **5** ($200B+ DC) | 3 ($5B+ MI) | 인텔 단위 미미 |
| 병목 포지셔닝 | 1 (병목 외) | **5** (병목 자체) | 3 (병목 alt) | 인텔 본 segment 거의 부재 |
| **평균** | **1.6** | **5.0** | **3.2** | **인텔 사실상 부재, NVIDIA 절대 우위** |

### Segment 4. Intel Foundry 18A (★ 주요 catch-up)
| 축 | 인텔 18A | TSMC N2 | 삼성 2GAP | 핵심 |
|---|---|---|---|---|
| 기술/특허 | **4** (RibbonFET + PowerVia 세계 최초) | 4 | 3 | Intel 18A 기술적으로 동급 |
| CAPA | 3 (양산 시작, scale-up 중) | **5** | 3 | TSMC 압도 |
| 고객 lock-in | 3 (Microsoft Maia 3 확보 ★) | **5** (Apple·NVIDIA·AMD·Qualcomm) | 3 | 인텔 첫 외부 대형 |
| 규모 (Foundry 매출) | 2 ($13.86B, 내부 비중 큼) | **5** ($90B+) | 3 (~$15B) | TSMC 격차 큼 |
| 병목 포지셔닝 | **4** (미국 본토 지정학 + AI 인프라) | 4 (지정학 risk) | 3 | 인텔 본 segment 핵심 catch-up |
| **평균** | **3.2** | **4.6** | **3.0** | **TSMC 압도, Intel 18A catch-up 시작, 삼성 약함** |

### Segment 5. 미국 본토 지정학 (CHIPS Act + 첨단 공정)
| 축 | 인텔 | 마이크론 | TSMC AZ | 삼성 TX | 핵심 |
|---|---|---|---|---|---|
| 기술/특허 (첨단 노드) | **5** (18A 양산) | 3 (메모리만) | **5** (N4P AZ) | 4 | Intel·TSMC 첨단 공정 동급 |
| CAPA | **5** (단일 최대) | 4 | 3 (AZ만) | 2 | Intel 미국 본토 단일 최대 |
| 고객 lock-in | 4 (Microsoft·Amazon·DoD 확보) | **5** (메모리 미국 유일) | 4 (Apple·NVIDIA) | 3 | Intel + Micron 양강 |
| 규모 (CHIPS Act 보조) | **5** ($7.86B 최대) | 4 ($6.1B) | 4 ($6.6B) | 3 ($4.7B) | Intel 단일 최대 |
| 병목 포지셔닝 | **5** (미국 본토 첨단 + 양산) | 4 (메모리 본토 유일) | 4 | 3 | Intel 미국 본토 첨단 #1 |
| **평균** | **4.8** | **4.0** | **4.0** | **3.0** | **Intel 미국 본토 지정학 최상 우위** |

### Segment 6. Mobileye (자율주행 ADAS) — 별도 trend
| 축 | Mobileye | NVIDIA Drive | Tesla FSD | 핵심 |
|---|---|---|---|---|
| 기술/특허 | **4** (EyeQ 6세대) | 4 | **4** | Mobileye 약 50+ OEM Tier 1 |
| 규모 | **4** (~$2B 매출) | 4 | 3 (Tesla 단독) | Mobileye 글로벌 #1 ADAS supplier |
| 고객 lock-in | **4** | 4 | 3 | Mobileye 50+ OEM |
| **평균** | **4.0** | 4.0 | 3.3 | **Mobileye 자율주행 강함, 단 본 에이전트AI 테마와 분리** |

### Segment 가중 평균 (Moat 종합)
- DCAI x86 server (3.4) × 25% + CCG client (4.2) × 35% + AI 가속기 (1.6) × 5% + Foundry 18A (3.2) × 20% + 미국 본토 지정학 (4.8) × 10% + Mobileye (4.0) × 5% = **약 3.5**
- **단 본 에이전트AI 테마 직접 segment만 (Mobileye 제외) 가중 시 → 약 2.8**
- 메모리 3사 (SK 4.4 / 삼성 4.3 / Micron 4.0) 대비 **1.2~1.5p 낮음**

## 2-3. 병목 수혜 강도 정량화

### 본 테마 (에이전트AI) 직접 수혜 메커니즘
| 병목 | 인텔의 수혜 메커니즘 | 카테고리 | 정량 추정 |
|---|---|---|---|
| **CPU 절대 수요 ↑** | Xeon 6 매출 +22% YoY (DCAI Q1 2026 $5.1B) | (A) 구조적 메가 병목 | 단 **점유율 잠식이 매출 +를 상쇄** |
| **AI 가속기 ↑** | Gaudi 3 매출 매우 미미 | (A) | **수혜 거의 없음 — NVIDIA·AMD 압도** |
| **AI PC ↑** | Core Ultra Panther Lake (18A) 출시 | (D) 동반 확대 | client CPU 일부 수혜 (단 AMD·NVIDIA N1/N1X 위협) |
| **★ Foundry 첨단 공정 ↑** | Microsoft Maia 3 + Amazon + DoD 외부 고객 확보 | (A) 구조적 메가 병목 | **유일한 명확한 positive — 18A 매출 ramp 2026-2028** |
| **미국 본토 지정학 ↑** | CHIPS Act $7.86B + 단일 최대 미국 fab | (A) | 매출 직접 아님, valuation premium |

→ **본 테마 직접 수혜 = Intel Foundry 18A 외부 고객 ramp이 유일하게 명확**. CPU 매출은 점유율 잠식으로 시장 성장에 미달, AI 가속기는 사실상 부재.

---

# 항목 3. 재무 분석

## 3-1. 실적 추이 (12년 + 12분기, 기업개요 v4.9 reference)

### 12년 사이클 (FY14-FY25, 기업개요 v4.9)
| 연도 | 매출 ($B) | OP ($B) | OPM | 핵심 이벤트 |
|---|---|---|---|---|
| 2014 | 55.87 | 15.35 | 27.5% | PC·서버 CPU 절대 강자 |
| 2018 | **70.85** | **23.32** | **32.9%** | ★ 사이클 정점 1차 |
| 2020 | 77.87 | 23.68 | 30.4% | 코로나 PC 사이클 정점 |
| 2021 | **79.02** | 19.46 | 24.6% | ★ 매출 정점 |
| 2022 | 63.05 | 2.33 | 3.7% | 14nm·10nm 지연, AMD 잠식 |
| 2023 | 54.23 | 0.09 | 0.2% | 매출 침체 본격화 |
| 2024 | 53.10 | **-11.68** | **-22.0%** | **역대 최대 적자**, Foundry 분사 검토 |
| 2025 | 52.85 | 0.26 | 0.5% | ★ Lip-Bu Tan CEO 부임 + 18A 양산 시작 |

**핵심 관찰**:
- **OPM range -22.0% ~ +32.9% = 54.9%p** (메모리 3사 진폭과 비교: SK 77.2%p / 삼성 21.7%p / Micron 83.5%p)
- **단 사이클이 아닌 구조적 침체** — 매출 12년 CAGR **-0.46%** (마이너스)
- 2021 정점 $79B → 2025 $52.85B (-33%) — 사이클 반등 아닌 secular decline
- **메모리 3사 사이클 정점 leverage와 정반대 — 인텔은 정점에서 침체로 진행**

### Q1 2026 분기 실적 (구조적 침체 + Turnaround 초기)

| 항목 | Q1 2026 (CY) | YoY | 비고 |
|---|---|---|---|
| 매출 | **$13.6B** | **+7%** | 7개 분기 만에 의미 있는 + |
| Intel Products 매출 | $12.8B | +9% | CCG + DCAI 합산 |
| GAAP OPM | 0.5% | -2%p → +3%p | 흑자 ($0.07B OP) |
| **GAAP EPS** | **$(0.73)** | n/a | restructuring charge **$2.1B** 차지 |
| **Non-GAAP EPS** | **$0.29** | beat $0.01 컨센서스 28x | 정상 회복 |
| **DCAI 매출** | **$5.1B** | **+22% YoY** | **★ 가장 빠른 segment (AI 인프라 capex 수혜)** |
| **Intel Foundry 매출** | **$5.4B** | **+16% YoY** | 18A 양산 ramp (Microsoft Maia 3 영향) |
| CCG 매출 | $7.7B | +1% | 정체 (AI PC 약함) |

### DCAI Q1 2026 분석 — 본 테마 직접 segment
- **+22% YoY = 메모리 3사 사이클 정점만큼 강한 성장**
- 단 **시장 성장(서버 CPU 전체 +19% YoY) 대비 약간 우위**, 즉 점유율 미미한 회복 또는 평행
- AMD EPYC Q1 2026 매출 비교 필요 (AMD 데이터센터 +57% YoY로 인텔 추월)
- → **DCAI 절대 매출은 +이지만 점유율은 가속 잠식 (Q1 2026 IDC 데이터 기준 -9.5%p YoY)**

## 3-2. 사업부별 PQC 분해 — Q1 2026 fact 기반

| 차원 | CCG (PC) | DCAI (server) | Intel Foundry |
|---|---|---|---|
| **P (ASP 변화)** | +5% (Core Ultra premium) | +10% (Xeon 6 premium) | 양산 가격 normal |
| **Q (출하량 변화)** | -4% (PC 시장 정체) | +10% (서버 시장 +19% 대비 -9%p underperform) | +16% (18A ramp 시작) |
| **매출 (P×Q)** | $7.7B (+1%) | $5.1B (+22%) | $5.4B (+16%) |
| **마진 (OPM)** | 약 10-12% (정상화) | 약 5-8% (회복 초기) | 약 -25% (대규모 적자 지속) |

### 본 테마 직접 분석
- **DCAI +22%는 본 테마 수혜 신호이지만 + 점유율 잠식이 동시 진행** — 시장 성장 +19% 대비 미미한 outperform
- **Intel Foundry +16%는 18A 양산 시작 신호** — 단 OPM 여전히 -25% 적자
- **CCG +1%는 PC 시장 정체** + AI PC 시장 약함 + NVIDIA+MSFT N1/N1X 추가 위협

## 3-3. 재무 건전성 (기업개요 v4.9 fact)

| 항목 | FY24 / FY25 / Q1 2026 |
|---|---|
| 자본총계 | $99.4B → $90.3B (FY24→FY25, -$9B) |
| OCF | $8.3B (FY24) / $8.7B (FY25) — 영업 현금 창출력 정점 대비 -72% |
| FCF | -$15B (FY24) / +$0.5B (FY25) — Lip-Bu Tan 부임 후 회복 |
| **CapEx** | **$24B (FY24) → $8.2B (FY25, -66%)** — 구조조정 단행 (Ohio 슬로우다운, Germany·Poland 취소) |
| Cash + ST Inv | $22.5B (FY25말 추정) |
| Debt | ~$80B 일정 |
| Debt/Equity | 1.13 (FY25) |
| **신용등급** | A2 / BBB+ / BBB+ (2024-10 동반 하향, 메모리 3사 회복 흐름과 반대) |
| **CHIPS Act** | **$7.86B 확정 (2024-11)** — 미국 단일 최대 |
| 배당 | 2024-08 중단, 재개 시점 미정 |
| 자사주 매입 | 2022 이후 중단 |
| 직원 수 | 약 99,500명 (FY25말, -24K YoY) — 15-20% 구조조정 |
| 발행주식수 | 약 4.6B 주 |
| CEO | **Lip-Bu Tan** (2025-03-18~, 前 Cadence CEO, 첫 외부 영입 CEO) |

### 주요 자본 movement
- **2025-09-12 Altera 51% 분사** (Silver Lake에 $4.46B 매각) — 자본 + $4.46B
- **★ 2025-09-18 NVIDIA $5B 지분 인수** (4% 지분) — 자본 + $5B, 주가 +35% 급등
- **Mobileye 79.9% 자회사 유지** — SOTP 별도 계산
- Foundry 분사 검토 진행 중 (Lip-Bu Tan 의사결정 보류)

## 3-4. 피어 수익성 비교 (Non-GAAP OPM 통일)

| 기업 | FY25 매출 | FY25 OPM | 1Q26 OPM | 본 테마 수혜 |
|---|---|---|---|---|
| **인텔** | **$52.85B** | **0.5%** | **1% (Non-GAAP)** | 후발·역방향 (점유 잠식) |
| AMD | $25B+ (CY25 추정) | 25%+ | 30%+ | x86 server·AI MI300 양면 + |
| NVIDIA | $130B+ | 60%+ | 65%+ | AI 가속기 절대 강자 |
| TSMC | $90B+ | 45%+ | 50%+ | Foundry 압도 |
| SK하이닉스 | 66.2조원 | 25%+ | **72%** | HBM 사이클 정점 |
| Micron | $37.38B | 32% | 69% | HBM 가속 회복 + 미국 본토 |

→ **인텔만 OPM 한자릿수** = 메모리 3사·NVIDIA·AMD·TSMC와 완전 분리된 위치. Turnaround 진척 시 OPM 회복 가능, 실패 시 침체 지속.

---

# 항목 4. 성장성 분석

## 4-1. 과거 성장률 (12년 CAGR)

| 기업 | 12년 매출 CAGR | 비고 |
|---|---|---|
| **인텔** | **-0.46% (마이너스)** | 구조적 침체 |
| NVIDIA | +30%+ | AI secular |
| TSMC | +15%+ | Foundry 메가 |
| AMD | +20%+ | 점유 + AI MI |
| SK하이닉스 | +12%+ | HBM 메가 |
| 마이크론 | +7%+ | 메모리 사이클 + HBM |
| 삼성전자 | +5%+ | 전사 |

→ **인텔만 12년 마이너스 CAGR** — 반도체 동종 중 압도적 underperform. 정점 2018 $70.85B 대비 FY25 $52.85B = -25%.

## 4-2. 향후 성장 가시성 — 미래 PQC 전망 (4Q + 2Y)

### CCG (Client CPU) — (D) 동반 확대 (위협 진행)
| 차원 | 4Q | 2Y | 근거 | 출처 |
|---|---|---|---|---|
| P | +5·5·3·3% | +5·0% | Core Ultra premium | Intel IR Q1 26 |
| Q | -3·0·+5·+10% | +10·15% | AI PC 침투 (단 N1/N1X 위협) | IDC PC 전망 |
| **→ 매출** | **+5-10% YoY** | **+15-25% (2Y)** | 위협 진행 중이지만 18A leverage | 9개 셀사이드 컨센 |

### DCAI (Server CPU + AI 가속기) — (A) 구조적 메가 병목 (단 인텔 후발)
| 차원 | 4Q | 2Y | 근거 | 출처 |
|---|---|---|---|---|
| P | +10·10·5·5% | +5·0% | Xeon 6 premium 유지 | Intel IR Q1 26 |
| Q | +10·15·15·15% | +25·15% | 시장 성장 강함, 단 점유 잠식 | IDC server CPU |
| **→ 매출** | **+22-30% YoY** | **+30-40% (2Y, 2026)** | DCAI 가장 빠른 성장 segment | 컨센·테마 v4 |

### Intel Foundry — (A) 구조적 메가 병목 (catch-up 시작)
| 차원 | 4Q | 2Y | 근거 | 출처 |
|---|---|---|---|---|
| P | normal | normal | 양산 단가 안정 | Intel IR |
| Q | +15·20·25·30% | +60·80% | **★ 18A ramp + Microsoft Maia 3 + Amazon + DoD** | 테마 v4 + 외부 고객 |
| **→ 매출** | **+15-30% YoY** | **+100% (2026)·+80% (2027)** | 18A 외부 고객 본격 양산 | 컨센 추정 |
| OPM | -25% → -15% | -10% → +5% | 양산 효율 + 외부 매출 비중 + | — |

### 회사 전체 매출·OPM 전망

| 항목 | FY24 | FY25 | FY26E | FY27E |
|---|---|---|---|---|
| 매출 ($B) | 53.10 | 52.85 | **~60 (+13%)** | **~70 (+17%)** |
| OP ($B) | -11.68 | 0.26 | **~3-5** | **~7-10** |
| **OPM** | -22.0% | 0.5% | **~5-8%** | **~10-15%** |

> **알 수 없음 시나리오**: 14A 외부 대형 고객 (Apple·NVIDIA·Qualcomm 중 1+) 확보 시 → Foundry 분사 가능성 + 별도 valuation. 미확보 시 14A 중단 + Foundry 매물화 + 인텔 CPU 단독 valuation.

### 수주잔고·백로그
- **Microsoft Maia 3 "Griffin" 멀티년 계약** (2026-01) — 18A 양산 핵심
- **Amazon Xeon 6 (Intel 3) + AI fabric chip (18A)** 멀티년 계약 (2025)
- **DoD Secure Enclave $3B** (2024-09)
- Broadcom·NVIDIA: 테스트 단계 (미확정)
- Tata·AMD: 협상 단계

## 4-3. 피어 그룹 비교

| 기업 | FY25 매출 | 5년 CAGR | FY25 OPM | 1Q26 OPM | 핵심 차이 |
|---|---|---|---|---|---|
| **인텔** | $52.85B | **-7%/년** | 0.5% | 1% | Turnaround, x86 잠식, Foundry catch-up |
| AMD | ~$25B | +25%+ | 25%+ | 30%+ | x86 server 점유 + AI MI 양면 |
| NVIDIA | ~$130B+ | +50%+ | 60%+ | 65%+ | AI 가속기 절대 96% |
| TSMC | ~$90B+ | +20% | 45%+ | 50%+ | Foundry 압도, 인텔 기술 동급 단 규모 격차 |
| ARM Holdings | ~$5B | +25%+ | 30%+ | 35%+ | 라이선스 모델, 모든 ARM CPU 수혜 |

→ **인텔만 5년 CAGR 마이너스** + OPM 한자릿수. AMD·NVIDIA·TSMC·ARM과 완전 분리된 위치.

---

# 항목 5. 통합 모드 입력용 Fact 정리

| 항목 | Fact / Raw Data |
|---|---|
| **현재 시장 점유 + 추이** | DC CPU x86: 64.4% → **54.9% (-9.5%p YoY, Q1 2026)**. PC CPU: ~75% (안정, 단 N1/N1X 위협). AI 가속기: ~0% (Habana Gaudi 매출 미미). Foundry: <1% (TSMC ~60% 압도) |
| **현재 CAPA + 증설** | Arizona Fab 52 (양산), Ohio (슬로우다운, 2027~), New Mexico Fab 9 (패키징), Ireland·Israel. **CHIPS Act $7.86B 확정**. Germany·Poland 취소 (2025-08). CapEx FY24 $24B → FY25 $8.2B (-66%) |
| **사이클 마진 진폭 (12년)** | OPM -22.0% (FY24) ~ +32.9% (FY18) = **54.9%p**. 단 사이클이 아닌 secular decline (매출 12년 CAGR -0.46%) |
| **기술 격차·R&D·IP** | **Intel 18A 양산 시작 (2025-10)** — RibbonFET + PowerVia 세계 최초. **14A (2027-2028) 외부 고객 의존**. R&D/Revenue FY24 31% (사상 최고, 매출 줄어 비율 상승) → FY25 26% |
| **고객 분포·집중도** | **★ 18A 외부 고객**: Microsoft Maia 3 (Griffin), Amazon Xeon 6 custom + AI fabric, DoD $3B Secure Enclave 확정. Broadcom·NVIDIA 테스트 단계. Tata·AMD 협상 |
| **신규 수주·계약** | **Microsoft Maia 3 멀티년 (2026-01)** + **NVIDIA $5B 지분 인수 (2025-09)** + Altera 51% 매각 (2025-09, $4.46B) |
| **자본·시총** | 자본 $90.3B (FY25), **시총 약 $100B (2026-05, 2020 정점 $290B 대비 -66%)**, PBR 약 1.0 (역사적 저점) |
| **Q1 2026 실적 (★)** | 매출 $13.6B (+7%) / Intel Products $12.8B (+9%) / **DCAI $5.1B (+22%)** / Foundry $5.4B (+16%) / CCG $7.7B (+1%) / Non-GAAP EPS $0.29 (beat $0.01 컨센서스 28x) / GAAP EPS $(0.73) (restructuring $2.1B 차지) |
| **★ 2026-06-01 GTC Taipei** | NVIDIA + MSFT "N1/N1X" Arm-based PC 칩 Computex 발표 — Windows on Arm 본격화. **"new era of PC"** narrative. Intel client CPU 추가 위협 |
| **Lip-Bu Tan Turnaround 진척** | 1년 차 (2025-03~2026-03): 15-20% 인력 감축 / CapEx -66% / Germany·Poland 취소 / Costa Rica 통합 / Altera 51% 매각 / NVIDIA 시너지 / 18A 양산 시작 / Microsoft Maia 3 확보. **첫 1년 평가 = 비용 절감 가속 + Foundry 외부 고객 확보 성공** |

---

# 항목 6. 구조적 트리거 모니터링

## 상방 트리거 (Turnaround 가속)

| 트리거 | 시점 | 영향 |
|---|---|---|
| **18A 외부 대형 추가 고객 확보 (NVIDIA·Apple·Qualcomm 중 1+)** | 2026 H2 - 2027 | Foundry secular narrative 강화, PBR 1.5+ 가능 |
| **14A 외부 대형 고객 확보** | 2027-2028 | Foundry 사업 미래 유지 (실패 시 Foundry 분사·매물화) |
| **DCAI 매출 5분기 연속 +20%+** | 2026 분기별 | 점유율 잠식 stop 시그널 |
| **AMD DC CPU 점유 정체 (현 27%에서 동결)** | 2026 H2 | x86 ecosystem 안정화 |
| **Lip-Bu Tan 2년 milestone 달성** | 2027-03 | Turnaround 가속 실증 |
| **CHIPS Act 추가 라운드** | 2026-2027 | 미국 정책 신뢰 지속 |
| **NVIDIA 추가 시너지 (joint product·foundry 협력)** | 2026 H2 | $5B 지분 인수 효과 확대 |

## 하방 트리거 (구조적 침체 가속)

| 트리거 | 시점 | 영향 |
|---|---|---|
| **★ NVIDIA + MSFT N1/N1X PC 본격 출시 (2026 H2)** | 2026 Q3-Q4 | client CPU 점유 잠식 가속 (Windows on Arm 본격) |
| **AMD DC CPU 점유 30% 돌파** | 2026 H2 | 인텔 server CPU secular 침체 |
| **18A yield rate 악화 발표** | 2026 분기별 | Foundry 외부 고객 신뢰 흔들림 |
| **14A 외부 고객 미확보 + 14A 중단 발표** | 2027-2028 | Foundry 분사·매물화 + 인텔 단독 CPU 회사로 축소 |
| **AI 가속기 매출 정체 (Gaudi 5 출시 후에도 매출 미미)** | 2026-2027 | NVIDIA·AMD 압도 영구화 |
| **Lip-Bu Tan 사임 또는 board 갈등** | 2027 H1 | Pat Gelsinger 사임 재발 risk |

## 모니터링 캘린더

| 시점 | 이벤트 |
|---|---|
| 분기 어닝콜 (Q1-Q4, 1·4·7·10월) | DCAI·Foundry·외부 고객 가이던스 |
| Intel Foundry Direct Connect (연 1회) | Foundry 신규 고객 발표 |
| NVIDIA GTC (연 2회, 3월·10월) + GTC Taipei (6월) | Arm-based PC 추가 발표 |
| Computex (연 1회, 5-6월) | client CPU 위협 모니터링 |
| CES (연 1회, 1월) | Panther Lake·Diamond Rapids 신제품 |
| ARM Holdings 분기 IR | ARM server·client CPU 점유 변화 |
| AMD 분기 IR | EPYC server 점유 변화 |
| CHIPS Act 정책 변동 | 미국 정부 funding 변경 |

---

# 종합 판단

## 매트릭스 평가

| 차원 | 평가 | 근거 |
|---|---|---|
| 상위 트렌드 적합성 | ★ 후발 | 본 테마 핵심 segment (CPU·AI 가속기)에서 점유 가속 잠식 또는 부재 |
| 산업 위치 | ★★ 약 | x86 #1이지만 secular decline, AI 가속기 ~0%, Foundry 미국 본토 catch-up |
| 해자 강도 (Moat 종합) | ★★ 2.8/5.0 | 메모리 3사 4.0+ 대비 1.5p 낮음. AI 가속기 1.5 / x86 서버 3.0 / Foundry 18A 4.0 |
| 재무 건전성 | ★★ 중 | 자본 $90B 유지, FCF 회복 초기, 신용등급 2024-10 동반 하향, 배당 중단 |
| 성장 가시성 (2~3년) | ★★ 중 | DCAI +22% / Foundry +16% (Q1 2026), 단 점유 잠식 동시 진행. FY26E 매출 +13% 추정 |
| **Turnaround 가능성** | **★★★ 가능** | Lip-Bu Tan 1년 차 비용 절감 가속, Microsoft Maia 3 확보, NVIDIA 시너지 |

## 핵심 투자 포인트 3

1. **★ Intel Foundry 18A 첫 외부 대형 고객 확보 (Microsoft Maia 3 "Griffin")** — 첫 미국 본토 hyperscaler 첨단 AI 칩 양산. Amazon Xeon 6 + DoD Secure Enclave $3B 추가 확보. 14A 외부 고객 ramp이 회사 운명 결정.
2. **★ Lip-Bu Tan Turnaround 1년 차 트랙 record** — CapEx -66% / 15-20% 구조조정 / Germany·Poland 취소 / Altera 51% 매각 / NVIDIA $5B 지분 인수 / 18A 양산 시작. 1년 만에 분기 흑자 회복 (Q1 2026 Non-GAAP EPS $0.29 vs 컨센 $0.01).
3. **미국 본토 지정학 + CHIPS Act $7.86B** — 마이크론과 함께 미국 본토 첨단 공정 메이저. Trump 행정부 onshore narrative 수혜. 단 매출 직접 + 보다는 valuation premium narrative.

## 핵심 리스크 3

1. **x86 server CPU 점유율 가속 잠식** — Q1 2026 IDC 데이터: Intel 64.4%→54.9% (-9.5%p YoY), AMD +3.3%p, **ARM +6.2%p (가장 빠른 +)**. AMD EPYC + ARM Neoverse 양면 압박. ARM 점유 17.7% = 1년 만에 거의 2배.
2. **★ NVIDIA + MSFT "N1/N1X" Arm-based PC 칩 (Computex 2026-06-01 발표)** — Windows on Arm 본격화 → client CPU 점유 75%에 추가 위협. Jensen Huang "new era of PC" narrative. Qualcomm 단독에서 NVIDIA 진입으로 ARM PC 신뢰성 가속.
3. **AI 가속기 완전 부재 + Gaudi 매출 미미** — NVIDIA 96% + AMD 4% 압도. Habana Labs 인수 ($2B, 2019) 이후 7년에도 의미 있는 매출 부재. CUDA ecosystem lock-in 절대. AI 가속기 시장은 인텔이 영구 회복 불가능 시나리오.

---

## 부록: 변경 이력 (Changelog)

### v1 (2026-06-02) — 1차 작성
- 산업 기초 + 테마 v4 + INTC 기업개요 v4.9 자동 참조
- ★ NVIDIA GTC Taipei 2026-06-01 keynote (N1/N1X Arm-based PC 칩) 신규 fact 반영
- ★ Microsoft Maia 3 "Griffin" Intel 18A 양산 확정 (2026-01) 반영
- Q1 2026 실적 (매출 $13.6B / DCAI +22% / Foundry +16%) 반영
- IDC Q1 2026 점유 데이터 (Intel 54.9% / AMD 27.4% / ARM 17.7%) 반영
- 메모리 3사와 mirror 구조 + Turnaround narrative 강조 (메모리 3사 4.0+ 대비 Moat 2.8)
- 본 테마 직접 수혜 = Intel Foundry 18A만 유일하게 명확
