---
ticker: "ARM"
company_name: ARM Holdings plc
country: UK (US-listed NASDAQ)
theme_keyword: 에이전트AI
parent_industry: 반도체
cross_ref_industry: 전력 인프라
moat_strength: 4.1              # 본 테마 segment 가중 평균 — 메모리 3사 4.0+ 동급, 인텔 2.8보다 높음
moat_by_segment:
  모바일_CPU_IP_Cortex: 4.5     # 점유 99% (Apple·Qualcomm·MediaTek·Samsung 모두 ARM)
  데이터센터_CPU_IP_Neoverse: 4.5   # FY24 9% → FY26 15%, hyperscaler ~50% 도달 (가장 빠른 성장)
  CSS_Compute_Subsystems: 4.0   # Chip ASP 10%+ 사상 최고 rate, royalty 비중 20%
  AGI_CPU_자체_칩: 3.5          # ★ 2026-03-24 35년 첫 자체 칩, $2B+ committed, 단 라이선시 경쟁 risk
  N1_N1X_NVIDIA_MSFT_협력: 4.0  # ★ 2026-06-01 Computex 발표, client CPU TAM 폭증
  ARMv9_royalty_rate: 4.5       # 이전 세대 2x rate, CY25 25% → 장기 60-70%
trend_revenue_share: 85         # 본 테마 직접 노출 — royalty + licensing 거의 전체가 본 테마 수혜
last_updated: 2026-06-02
auto_references:
  - 반도체_산업기초.md (2026-05-18)
  - 전력 인프라_산업기초.md (2026-05-18)
  - 에이전트AI_테마분석.md (v4, 2026-05-26)
  - ARM_기업개요.md (v4.9, 2026-05-18 — SEC EDGAR 20-F 2개·6-K 24개 + ARM IR Earnings PDF 6개 기반)
analyst_reports_attached:
  - ARM Q4 FY26 Earnings (2026-05-06 발표)
  - ARM AGI CPU Launch (2026-03-24, Meta lead customer)
  - NVIDIA GTC Taipei 2026 keynote (2026-06-01, N1/N1X)
  - Microsoft Maia 3 "Griffin" Intel 18A 발표 (2026-01)
notes:
  - ARM은 영국 본사, US-listed (NASDAQ:ARM). 회계연도 3월 마지막 종료 (FY26 = 2025-04~2026-03)
  - 본 분석 frame: 본 테마 직접 수혜자 (메모리 3사·NVIDIA·TSMC와 함께) + 비즈니스 모델 변화 진행 중 (chipless → 팹리스 진입)
---

# ARM Holdings (ARM) 기업 분석 — 에이전트AI 테마

> **본 분석 frame**: 에이전트AI 테마 분석(v4)의 17 segment 중 **ARM은 chipless IP 모델로 모든 ARM 기반 칩에서 royalty 동시 수혜 + AGI CPU 자체 칩 진입 (2026-03-24) + N1/N1X client CPU TAM 폭증 (2026-06-01)**. **메모리 3사(SK 4.4 / 삼성 4.3 / Micron 4.0)와 본 테마 수혜 동급 위치, Moat 4.1**. 단 **비즈니스 모델 자체가 chipless → 팹리스로 변화 진행 = 라이선시(NVIDIA·AWS·MSFT·Google)와 잠재 경쟁 risk + PER 100x+ 이미 가격 반영**.

> **점유율·CAPA 표기 기준**: 본 분석의 모든 % 점유율은 **매출 기준** (TrendForce·Counterpoint·IDC·Mercury Research). **CAPA는 wafer 기준** (산업 통계). ARM은 IP 회사로 CAPA 부재 — TSMC 등 양산 capa에 의존.

---

## Executive Summary (5줄)

1. **위치**: 반도체 산업의 운영체제 — **모바일 CPU IP 99% (Apple·Qualcomm·MediaTek·Samsung 모두)** + **데이터센터 CPU 점유 FY24 9% → FY26 15%, 하이퍼스케일러 내 ~50% 도달** + 누적 chip shipments **290B+**. 본 테마 직접 수혜 4가지 메커니즘: **(1) ARM 라이선시 4종 (NVIDIA Grace·AWS Graviton·MSFT Cobalt·Google Axion) royalty 동시 수혜, (2) ARMv9 royalty rate 2x (CY25 25% → 장기 60-70%), (3) CSS chip ASP 10%+ rate (사상 최고, royalty 20%), (4) AGI CPU 자체 칩 (★ 2026-03-24, Meta+Oracle+ByteDance $2B+ committed)**.
2. **해자 종합 (segment 가중)**: <strong>4.1 / 5.0</strong> (메모리 3사 4.0+ 동급, 인텔 2.8보다 1.3p 높음) — 모바일 IP 4.5 (사실상 독점(monopoly)) / DC IP 4.5 (가장 빠른 + segment) / ARMv9 royalty rate 4.5 (2x 프리미엄) / CSS 4.0 / AGI CPU 3.5 (신규, 라이선시 경쟁 risk) / N1/N1X 4.0.
3. **재무 (record + Secular)**: **FY26 매출 $4.92B (+23% YoY, 3년 연속 +20%+ 성장) / Non-GAAP OPM 40.7% (record) / 적자 분기 history 0**. **Q4 FY26 매출 $1.49B (+20%) / Royalty $671M (+11%) / License $819M (+29%) / Non-GAAP EPS $0.60 (beat $0.58)**. **Data center royalty 2x YoY** (하이퍼스케일러 ARM 칩 채택 가속). **SoftBank 88% 보유**, 2026 YTD 주가 +84%.
4. **미래**: **★ AGI CPU 2026 H2 volume 출하 + 2028+ material revenue impact** (Meta·Oracle·ByteDance $2B+ committed). N1/N1X client CPU 본격화. ARMv9 비중 25% → 60-70% (royalty rate 2x 자동 적용). CSS 채택 가속 (chip ASP 10%+). **단 PER 100x+ 이미 가격 반영, sharp 상방 여력 어려움**.
5. **종합 판단**: <span class="star">★★★ 본 테마 직접 수혜 메가 종목 (메모리 3사 + NVIDIA + TSMC와 동급)</span>. 단 **(a) AGI CPU 진입 = 라이선시(NVIDIA·AWS·MSFT·Google)와 잠재 경쟁 risk, (b) PER 100x+ 이미 highly valued, (c) RISC-V 부상 + Apple·Qualcomm Nuvia architecture license로 royalty 회피** 3대 risk. **(1) Royalty rate 2x 프리미엄 (ARMv9·CSS 자동 확장), (2) Stargate $400B 인프라 스토리(narrative), (3) 비즈니스 모델 확장 (chipless → 자체 칩)** 3대 positive optionality.

---

# 항목 1. 입력 정리 + 기업 포지셔닝

## 1-1. 산업·테마 컨텍스트

- **반도체 산업기초** (v1, 2026-05-18): (A) 구조적 메가 병목 → **ARM은 IP 레이어에서 모든 첨단 칩의 상위 layer 차지**
- **에이전트AI 테마 v4** (2026-05-26): 17 segment 중 CPU·AI 가속기 segment에서 ARM IP가 핵심 표준
- **인텔 분석 (2026-06-02)**: ARM 라이선시 4종 (Grace·Graviton·Cobalt·Axion) 합산 17.7% server CPU 점유 (+6.2%p YoY) → ARM은 이 모든 칩에서 royalty 수혜
- **한국 접근 가능 TAM (2028E)**: $216-262B+ (ARM은 영국이라 한국 TAM 무관, 단 한국 하이퍼스케일러·삼성 모바일 칩에서 royalty 수익)

## 1-2. ARM의 위치 (테마 v4 Moat 후보 — segment별)

> **★ 본질적 위치**: ARM은 **CPU IP 업계 사실상 독점(monopoly) (글로벌 1위)** — 매출 기준으로도 IP 라이선싱 시장에서 단일 압도적 회사. 본 분석의 모든 점유율은 ARM이 이미 1위인 segment 내 침투율 (현재 vs 장기 잠재). 비교 대상 = RISC-V (오픈 소스, 단기 위협 미미) / x86 (Intel·AMD, ARM 외 유일 대안) / 자체 ISA (Apple·Qualcomm Nuvia architecture license, 정상 royalty 회피).

| Segment | 글로벌 점유 / 비중 | 비고 |
|---|---|---|
| **모바일 CPU IP (Cortex)** | **99%** (Apple iPhone + Android 전체) | Apple·Qualcomm·MediaTek·Samsung·HiSilicon 모두 ARM ISA |
| **데이터센터 CPU IP (Neoverse V/N)** | **FY24 9% → FY26 15% (하이퍼스케일러 내 ~50%)** | NVIDIA Grace·AWS Graviton 4/5·MSFT Cobalt·Google Axion 모두 ARM Neoverse |
| **★ ARMv9 비중 (royalty)** | **CY25 25% → 장기 target 60-70%** | royalty rate ARMv8 대비 2x (자동 매출 +) |
| **CSS (Compute Subsystems)** | royalty 약 **20%** 비중 | Chip ASP **10%+ rate 사상 최고** |
| **★ AGI CPU (자체 칩, 2026-03-24)** | **첫 자체 칩, 136 Neoverse V3, TSMC 3nm** | Meta + Oracle + ByteDance **$2B+ committed**, 2026 H2 ship |
| **★ N1/N1X (NVIDIA + MSFT 협력)** | **2026-06-01 Computex 발표** | Windows on Arm PC TAM 폭증, ARM royalty 직접 수혜 |
| Apple M-series (architecture license) | M1~M5 ARM ISA 기반 | royalty rate 낮음 (architecture license는 정상 royalty 회피) |
| **누적 chip shipments** | **290B+** (회사 history) | 모든 ARM chip 출하 당 royalty |

→ **본 테마 핵심 segment 모든 곳에서 IP 라이선스 수익**. 메모리 3사처럼 wafer capa 병목 없음, NVIDIA·TSMC처럼 단일 product 의존도 없음 → **broadly exposed**.

## 1-3. 매출 구성 (FY26)

| 구분 | FY26 매출 | YoY | 본 테마 연결 | 비중 |
|---|---|---|---|---|
| **License & Other Revenue** | **$2.94B** (Q4 $819M 연간화) | +29% (Q4) | ★ CSS·ARMv9·AGI CPU 라이선스 | **60%** |
| **Royalty Revenue** | **$1.98B** (Q4 $671M 연간화) | +11% (Q4) | ★ 모든 ARM 칩 출하당 | **40%** |
| **Total Revenue** | **$4.92B** | **+23%** | 본 테마 직접 노출 ~85% | 100% |

### 본 테마 직접 매출 노출
- ARM 매출 거의 전부가 본 테마 직접 수혜 — 모바일 (AI agent on-device) + 데이터센터 (server CPU) + AI 가속기 (NVIDIA Grace 등 host CPU)
- IoT·임베디드 매출은 비중 작음
- **순 본 테마 직접 노출 = 약 85%** (모바일 60% × 본 테마 직접 70% + 데이터센터 30% × 100% + 기타)
- → **SK 60%+ / Micron 70% / 인텔 30% 대비 가장 높은 본 테마 노출**

---

## ★ 2-0. 에이전트AI 테마 logical flow — 왜 ARM가 부각받는가

> **정성적 인과 사슬** (테마 v4 narrative → ARM 위치 매핑)

### 1단계: 에이전트 AI = 데이터·연산·메모리 폭증의 본질
- 에이전트 1건 = chat 1턴 대비 **토큰 20-30x** (Stanford/NVIDIA 실측, 테마 v4)
- 각 추론 단계·도구 호출·검색·메모리 갱신·tool execution = **연산(GPU/CPU) + 메모리(HBM/DRAM/SSD) + 스토리지(HDD) + IP(ARM) 모든 layer 부하 폭증**
- agent는 stateful → 과거 trace·long-context 보존 필요 = secular 누적

### 2단계: AI 인프라 layer별 분담 — ARM는 어디 위치?

| Layer | 데이터/연산 유형 | 매체·아이템 | 본 테마 수혜 종목 |
|---|---|---|---|
| **Hot (microsec)** | KV cache, activation, 모델 가중치(active) | **HBM** | **SK·삼성·Micron (HBM)** |
| **Warm (msec)** | 모델 가중치(off-package), 활성 dataset | **DRAM·SSD** | 메모리 3사 (DRAM) + SNDK·Solidigm (eSSD) |
| **Warm-Cold (sec)** | 검색 코퍼스, 벡터 DB, 최근 로그 | **eSSD QLC·HBF** | SNDK (122TB QLC, HBF) |
| **Cold (수초~분)** | 학습 데이터셋, 체크포인트, 보관 로그 | **HDD nearline** | WDC·Seagate |
| **Compute (CPU)** | server CPU + host CPU + client CPU | **x86·ARM** | Intel·AMD·ARM 라이선시 |
| **Compute (GPU·AI)** | training·inference 가속 | **GPU·ASIC** | NVIDIA·AMD·ARM |
| **IP layer** | 모든 chip 상위 설계 | **ARM IP** | ARM Holdings (royalty 광범위) |


→ **ARM 위치: **IP layer (전체)** — 모든 ARM 기반 chip royalty 광범위**

### 3단계: 왜 ARM IP가 본 테마에서 부각받는가? — 3가지 본질적 이유

1. **모든 ARM chip royalty 동시 수혜** = NVIDIA Grace + AWS Graviton + MSFT Cobalt + Google Axion 4종 hyperscaler ARM 칩이 모두 ARM IP → ARM은 chip 1개 출하당 royalty 수금
2. **ARMv9 rate ARMv8 대비 2x + CSS rate chip ASP 10%+** = 자동 매출 + (CY25 25% → 60-70%)
3. **AGI CPU 자체 칩 진입 (2026-03-24)** = 35년 첫 자체 칩 (Meta+Oracle+ByteDance $2B+ committed) = 비즈니스 모델 chipless → 팹리스 확장

### 4단계: 왜 ARM이 광범위 수혜 종목인가?

- **모바일 CPU IP 99%** (Apple·Qualcomm·MediaTek·Samsung 모두 ARM)
- **DC CPU 점유 FY24 9% → FY26 15% (hyperscaler ~50%)**
- **누적 chip shipments 290B+** = 매 chip 출하당 royalty
- **Q4 FY26 Data center royalty 2x YoY** + N1/N1X (2026-06-01) client CPU TAM 폭증

### 5단계: 본 분석 frame 결론

**본 테마 모든 segment에서 royalty 동시 수혜 (메모리 3사·NVIDIA·TSMC와 함께 메가 종목)**. Moat 4.1 (메모리 동급). 단 PER 100x+ 이미 가격 반영 + AGI CPU 진입으로 라이선시 경쟁 risk + RISC-V·Apple architecture license royalty 회피 3대 risk.

---


# 항목 2. 비즈니스 모델 & 해자 (Moat) — Segment별

## 2-1. 비즈니스 모델 — 핵심 차별점

### ARM 비즈니스 모델 (chipless IP licensor)

ARM의 비즈니스 모델은 3개 레이어 중 가장 상위에 위치:

| Layer | 회사 | ARM과 관계 |
|---|---|---|
| **(1) IP licensor (chipless)** | **ARM Holdings** — CPU 코어 IP 설계도 라이선스 | ARM 본업 |
| (2) 팹리스 (chip designer) | NVIDIA, AMD, Qualcomm, AWS Annapurna, Apple, MSFT, Google | ARM 라이선시 (royalty 지급) |
| (3) Foundry (양산) | TSMC, Samsung Foundry, Intel Foundry | ARM 라이선시 칩 양산 |

**라이선스 모델 2종**:
1. **Per-core 라이선스**: ARM Cortex/Neoverse 코어 IP 그대로 사용 (정상 royalty rate)
   - NVIDIA Grace, AWS Graviton, MSFT Cobalt, Google Axion (server)
   - Qualcomm Snapdragon (대부분 모바일)
2. **Architecture license**: ARM ISA만 받아 코어 자체 설계 (royalty rate 낮음 — 정상의 ~1/3)
   - **Apple M-series + A-series** (M1~M5, A시리즈 모두)
   - Qualcomm Snapdragon X (Nuvia 인수)

### 매출 모델 — Royalty + Licensing

**Royalty Revenue (40%, FY26)**:
- 출하된 ARM 칩 1개당 % rate (chip ASP의 1-3%)
- ARMv8 rate < ARMv9 rate (2x) < CSS rate (chip ASP 10%+)
- **칩 출하 → 6-12개월 지연 royalty 수금**

**Licensing Revenue (60%, FY26)**:
- IP 라이선스 fee ($ 일시 또는 multi-year subscription)
- Subscription model 확장 중 (예측 가능성 ↑)

### CSS (Compute Subsystems) — 신규 비즈니스 모델
- ARM이 chiplet/IP block subsystem을 통째로 라이선스 → 라이선시가 빠르게 chip 설계 가능
- **Chip ASP 10%+ rate** = 사상 최고 royalty rate (정상 ARMv9 대비 또 추가 프리미엄)
- Royalty 비중 약 20%, 빠르게 +

### ★ AGI CPU — 비즈니스 모델 확장 (chipless → 팹리스 진입)
- **2026-03-24 발표**: ARM 35년 역사상 첫 자체 칩
- 136 Neoverse V3 코어 / TSMC 3nm / 300W TDP
- 비교: AMD EPYC 128코어 500W / Intel Xeon 동급 → **power efficiency 강점**
- **Meta = co-developed lead customer** + Oracle + ByteDance
- **$2B+ committed orders** (2026 H2 volume ship, 2028+ material revenue)
- SoftBank Ampere 인수 (2025) 영향, Stargate $400B 인프라 스토리(narrative)
- **비즈니스 모델 변화**: ARM이 IP만 라이선스하던 chipless에서 → IP + 자체 칩 (단 양산은 TSMC 위탁 = 팹리스 진입)
- **잠재 risk**: NVIDIA·AWS·MSFT·Google 등 기존 라이선시와 server CPU 시장에서 잠재 경쟁

### ★ N1/N1X (NVIDIA + MSFT 협력) — 2026-06-01 Computex
- NVIDIA가 Arm Neoverse 코어 + 자체 GPU 결합한 PC 칩
- Microsoft Windows on Arm 본격화
- ARM 입장: client CPU TAM 폭증 + royalty 직접 수혜

## 2-2. Moat 종류별 Segment 평가

### Segment 1. 모바일 CPU IP (Cortex)
| 축 | ARM | RISC-V | x86 (Intel·AMD) | 핵심 |
|---|---|---|---|---|
| 기술/특허 | **5** (Cortex X·A·M 시리즈) | 3 (오픈 소스) | 2 (모바일 부재) | ARM 거의 독점(monopoly) |
| 점유 | **5** (99%) | 1 (IoT/임베디드 일부) | 1 (모바일 거의 0%) | ARM 절대 |
| 고객 락인(lock-in) | **5** (Apple·Qualcomm·Android 전체) | 2 (중국 일부) | 1 | ARM 생태계 |
| 규모 (모바일 매출) | **5** (FY26 ~$1.5B) | 1 | 1 | ARM 단일 |
| 병목 포지셔닝 | **5** (on-device AI agent 수혜) | 2 (장기 위협) | 1 | ARM 절대 |
| **평균** | **5.0** | **1.8** | **1.2** | **ARM 거의 독점(monopoly)** |

> **★ 정성: 왜 모바일 CPU IP에서 ARM이 독점인가?**
> 
> **인과 사슬**: ARM Cortex 시리즈 = 모바일 chip 표준 → Apple·Qualcomm·MediaTek·Samsung·중국 SoC 모두 ARM IP 사용 → 점유 99% → on-device AI agent (LLM phone) 수혜 추가
> 
> **추가 동력 1 — 모바일 chip 99% 점유 = 절대 독점**: ARM 외 alternative 사실상 없음 (RISC-V IoT만)
> **추가 동력 2 — Apple Silicon (M·A 시리즈) 포함**: Apple도 ARM architecture license 사용 = royalty 지급
> **추가 동력 3 — on-device AI agent narrative (Apple Intelligence·Galaxy AI)**: LLM phone 수요 폭증 = 모바일 chip ASP +·royalty rate +
> 
> **ARM 위치의 특별함**: 본 segment Moat 5.0으로 완전 독점. 모바일 chip 시장 자체가 ARM 매출

### Segment 2. 데이터센터 CPU IP (Neoverse V/N)
| 축 | ARM | x86 (Intel·AMD) | RISC-V | 핵심 |
|---|---|---|---|---|
| 기술/특허 | **5** (Neoverse V3/N2) | 4 (Xeon·EPYC) | 3 | ARM 표준 |
| 점유 | **4** (15%, 하이퍼스케일러 50%) | 4 (인텔+AMD 82%) | 1 | ARM 빠른 + |
| 고객 락인(lock-in) | **5** (NVDA·AWS·MSFT·Google) | 3 (잠식) | 1 | ARM 라이선시 4종 |
| 규모 (DC 매출) | **4** (Q4 FY26 royalty +11%·데이터센터 2x YoY) | 4 | 1 | ARM 빠른 + |
| 병목 포지셔닝 | **5** (가장 빠른 + segment) | 2 (잠식자) | 1 | ARM 본 테마 수혜 |
| **평균** | **4.6** | **3.4** | **1.4** | **ARM 장기 추세(secular) +, x86 정체** |

> **★ 정성: 왜 DC CPU IP가 본 테마 핵심인가?**
> 
> **인과 사슬**: 에이전트 AI = host CPU 부담 폭증 + power efficiency·TCO 요구 → 하이퍼스케일러 4종 (AWS Graviton·Google Axion·MSFT Cobalt·NVIDIA Grace) 모두 ARM Neoverse 기반 → DC ARM 점유 15% (하이퍼스케일러 50%+) → ARM 본 테마 최대 수혜
> 
> **추가 동력 1 — ★ 하이퍼스케일러 자체 ARM chip 4종 합 = Intel 잠식**: AWS·Google·MSFT·NVIDIA Grace 모두 ARM Neoverse 라이선스 = ARM royalty 4배 leverage
> **추가 동력 2 — Neoverse V3/N2 = data center 표준화**: data center 매출 Q4 FY26 2x YoY 가속
> **추가 동력 3 — Intel Xeon 점유 64%→54.9% (-9.5%p YoY)**: x86 점유 잠식 = ARM 매출로 직접 전환
> 
> **ARM 위치의 특별함**: 본 segment가 ARM 본 테마 핵심 leg. royalty 비즈니스 모델로 4종 라이선시 매출 모두 ARM royalty로 들어옴

### Segment 3. CSS (Compute Subsystems)
| 축 | ARM CSS | 일반 ARM IP | x86 | 핵심 |
|---|---|---|---|---|
| 기술/특허 | **5** (chiplet subsystem) | 4 | 3 | ARM CSS 신규 |
| 점유 | **4** (royalty 20% 비중) | 5 | 4 | CSS 빠른 + |
| 고객 락인(lock-in) | **4** (라이선시 chip 시간 단축) | 4 | 3 | CSS 락인(lock-in) 강함 |
| 규모 (CSS 매출) | **4** (chip ASP 10%+ rate) | 5 | 3 | CSS 사상 최고 rate |
| 병목 포지셔닝 | **4** (chip 설계 가속) | 4 | 3 | CSS 본 테마 enabler |
| **평균** | **4.2** | **4.4** | **3.2** | **CSS 신규 + 사상 최고 rate** |

> **★ 정성: 왜 CSS (Compute Subsystems)가 본 테마에서 부각받는가?**
> 
> **인과 사슬**: chiplet 시대 = chip 설계 복잡도 폭증 → ARM CSS = chiplet subsystem 통째 제공 → 라이선시 chip 설계 시간 단축 + ASP 10%+ royalty rate (사상 최고) → ARM 매출 leverage 추가
> 
> **추가 동력 1 — ★ CSS chip ASP 10%+ royalty rate (사상 최고)**: 일반 ARM IP royalty rate (1-3%) 대비 3-10배 = 매출 leverage 극대
> **추가 동력 2 — chiplet 시대 = CSS 채택 가속**: AGI CPU·hyperscaler ASIC 모두 CSS 채택 시도
> **추가 동력 3 — Royalty 비중 20%로 빠른 +**: 일반 IP에서 CSS로 매출 mix shift = ARM 평균 royalty rate 자동 상승
> 
> **ARM 위치의 특별함**: CSS는 ARM 매출 mix shift driver. 일반 IP royalty 대비 3-10배 rate으로 long-term ARPU + driver

### Segment 4. AGI CPU (자체 칩, ★ 신규)
| 축 | ARM AGI CPU | NVIDIA Grace | AWS Graviton | AMD EPYC | 핵심 |
|---|---|---|---|---|---|
| 기술/특허 | **4** (136 Neoverse V3) | 4 | 4 | **5** (Zen 5) | AGI CPU 신규 |
| CAPA | 3 (TSMC dep, 신규) | 4 (TSMC) | 4 (TSMC) | 4 (TSMC) | 동급 |
| 고객 락인(lock-in) | 3 (Meta·Oracle·ByteDance committed) | **5** (GB200 rack 표준) | **5** (AWS 자체) | 4 | AGI CPU 후발 |
| 규모 | 2 ($2B committed, 2028+ material) | **5** (Grace rack 표준) | 4 (AWS 50%+) | 4 (~$13B) | AGI CPU 초기 |
| 병목 포지셔닝 | **4** (power efficiency 300W) | 5 | 4 | 4 | AGI CPU 차별화 |
| **평균** | **3.2** | **4.6** | **4.2** | **4.2** | **AGI CPU 신규, 라이선시와 경쟁 risk** |

> **★ 정성: 왜 AGI CPU (자체 chip)가 ARM thesis 양날의 검인가?**
> 
> **인과 사슬**: ARM이 자체 AGI CPU (136 Neoverse V3 cores) 출시 → Meta·Oracle·ByteDance committed → 단 NVIDIA Grace·AWS Graviton·AMD EPYC 라이선시와 경쟁 → ARM 자기잠식 risk vs 매출 leverage 양면
> 
> **추가 동력 1 — Meta·Oracle·ByteDance $2B+ committed (2028+ material)**: 초기이지만 hyperscaler 직접 수주 = AGI CPU 진입 chance
> **추가 동력 2 — power efficiency 300W = NVIDIA Grace 대안**: 자체 chip이 라이선시 chip 대비 efficiency 우위 = market segment 가능
> **추가 동력 3 — ★ 라이선시와 경쟁 risk = 사업 모델 ambiguity**: ARM = IP supplier vs 자체 chip = 사업 모델 충돌 = long-term risk
> 
> **ARM 위치의 한계**: 본 segment Moat 3.2로 가장 약함. 라이선시 경쟁 risk와 매출 leverage trade-off

### Segment 5. ARMv9 Royalty Rate (프리미엄 pricing)
| 축 | ARMv9 | ARMv8 (구세대) | RISC-V | 핵심 |
|---|---|---|---|---|
| 기술/특허 | **5** (SVE2, CCA confidential computing) | 4 | 3 | ARMv9 차세대 |
| 채택 비중 | **4** (CY25 25%, 장기 60-70%) | 4 (감소) | 1 | ARMv9 가속 |
| Royalty rate | **5** (ARMv8 대비 2x) | 3 | 2 | ARMv9 프리미엄 |
| 규모 (royalty +) | **5** (자동 매출 +) | 3 | 1 | ARMv9 driver |
| 병목 포지셔닝 | **5** (모든 신규 칩 ARMv9) | 3 | 1 | ARMv9 표준 |
| **평균** | **4.8** | **3.4** | **1.6** | **ARMv9 자동 매출 + driver** |

> **★ 정성: 왜 ARMv9 Royalty Rate가 본 테마에서 자동 매출 + driver인가?**
> 
> **인과 사슬**: ARMv9 = SVE2 + CCA (confidential computing) 차세대 → 모든 신규 chip ARMv9 채택 → ARMv9 royalty rate = ARMv8 대비 2배 → 채택 비중 25% (CY25) → 장기 60-70% = ARM 매출 자동 +
> 
> **추가 동력 1 — ★ ARMv9 royalty rate 2배 (ARMv8 대비)**: 같은 chip 매출에서 ARM royalty 2배 = 매출 자동 leverage
> **추가 동력 2 — ARMv9 채택 25% → 60-70% (장기)**: 모든 신규 chip ARMv9 표준 = 자동 mix shift
> **추가 동력 3 — SVE2 + CCA = AI agent 필수 기능**: vector instruction + confidential computing = AI agent 표준 = ARMv9 가속
> 
> **ARM 위치의 특별함**: 본 segment는 chip volume 동일해도 매출 2배 = ARM Royalty 비즈니스 모델의 핵심 leverage

### Segment 6. N1/N1X 협력 (NVIDIA + MSFT, ★ 2026-06-01)
| 축 | ARM (N1/N1X royalty) | NVIDIA | Qualcomm Snapdragon X | 핵심 |
|---|---|---|---|---|
| 기술/특허 | **4** (Cortex X·Neoverse 기반) | 4 (자체 chip) | 3 (Nuvia architecture license) | ARM IP 표준 |
| 점유 | **4** (PC ARM TAM 폭증) | 3 (신규 진입) | 2 (단독 위치 약화) | ARM 전체 + |
| Royalty rate | **4** (per-core license, 정상 rate) | — (NVIDIA royalty 지급) | 3 (architecture, 낮음) | NVIDIA = 정상 rate |
| 규모 | **3** (2026 H2 본격 출하) | 3 | 2 | 초기 |
| 병목 포지셔닝 | **5** (모든 ARM PC 칩 수혜) | 4 | 2 | ARM 본 테마 + |
| **평균** | **4.0** | **3.6** | **2.4** | **ARM N1/N1X 직접 수혜** |

> **★ 정성: 왜 N1/N1X (NVIDIA + MSFT) 협력이 ARM 신규 driver인가?**
> 
> **인과 사슬**: ★ 2026-06-01 NVIDIA Jensen Computex 발표 → NVIDIA ARM PC chip (N1/N1X) + Microsoft Windows on ARM 지원 + Qualcomm Nuvia 단독 위치 약화 → ARM PC TAM 폭증 + N1/N1X royalty rate = per-core 정상 rate (Qualcomm Nuvia architecture license보다 높음)
> 
> **추가 동력 1 — ★ NVIDIA N1/N1X royalty = 정상 per-core rate**: Qualcomm Snapdragon X (Nuvia architecture license, 낮은 rate)와 달리 NVIDIA는 standard royalty 지급 = ARM 매출 leverage
> **추가 동력 2 — Microsoft Windows on ARM 본격 지원**: PC OS 호환성 확보 = ARM PC market take-off
> **추가 동력 3 — ARM PC market 전체 + → 모든 ARM PC chip royalty 수혜**: Apple·Qualcomm·NVIDIA 3사 동시 + = ARM 광범위 수혜
> 
> **ARM 위치의 특별함**: 본 segment는 ARM 차세대 driver. NVIDIA N1/N1X 추가로 PC market에서 x86 잠식 가속 = ARM royalty 추가 leg

### Segment 가중 평균 (Moat 종합)
- 모바일 IP (5.0) × 30% + DC IP (4.6) × 30% + ARMv9 royalty (4.8) × 15% + CSS (4.2) × 10% + AGI CPU (3.2) × 5% + N1/N1X (4.0) × 10% = **약 4.6**
- 단 본 테마 직접 segment만 가중 평균 시 → **약 4.1** (메모리 3사 4.0+ 동급)
- 인텔 (2.8) 대비 **1.3p 우위**
- 메모리 3사와 직접 비교: SK 4.4 / 삼성 4.3 / Micron 4.0 — ARM은 **Micron과 동급, SK·삼성보다 약간 낮음**

## 2-3. 병목 수혜 강도 정량화 (본 테마 직접 메커니즘)

### Royalty 수혜 메커니즘 — chipless IP의 광범위 노출

| 본 테마 병목 | ARM 수혜 메커니즘 | 정량 추정 |
|---|---|---|
| **AI 가속기 ↑** (NVIDIA·AMD) | NVIDIA Grace = ARM Neoverse V2 → royalty | 데이터센터 royalty 2x YoY (Q4 FY26) |
| **서버 CPU ↑** | AWS Graviton + MSFT Cobalt + Google Axion = ARM Neoverse → royalty | 하이퍼스케일러 ARM 50%+ |
| **AI PC ↑** | Qualcomm Snapdragon X + ★ NVIDIA N1/N1X (2026-06-01) = ARM 라이선스 → royalty | client CPU TAM 폭증 (2026 H2) |
| **모바일 agent ↑** | Apple A·M + Qualcomm Snapdragon + MediaTek Dimensity = ARM ISA → royalty (Apple은 architecture rate) | 99% 점유 안정 |
| **ARMv9 채택 ↑** | royalty rate 2x 프리미엄 | CY25 25% → 60-70% (자동 매출 +) |
| **CSS 채택 ↑** | chip ASP 10%+ rate | royalty 20% → 30%+ 가능 |
| **★ AGI CPU 매출** | 자체 칩 매출 (Meta·Oracle·ByteDance $2B+ committed) | 2026 H2 ship, 2028+ material |

→ **본 테마 모든 segment에서 ARM royalty 수혜**. 메모리 3사처럼 단일 product 의존 X, 인텔처럼 점유 잠식 X → **broadly exposed**.

### vs 메모리 3사 비즈니스 모델 차이

| 차원 | 메모리 3사 (SK·삼성·Micron) | ARM Holdings |
|---|---|---|
| **공급 제약** | wafer capa 병목 (HBM 알로케이션 = 가격 ↑) | IP는 무제한 라이선스 가능 |
| **가격 결정력** | ASP YoY +30~115% (1Q26) | Royalty rate 고정 (CSS 10%+, ARMv9 2x 단계적 상승) |
| **수익 시점** | 즉시 (출하 → 매출) | 지연 (칩 출하 → 6-12개월 후 royalty) |
| **CAPEX 필요** | $15-25B/년 | ~$0 (R&D만) |
| **사이클 진폭** | OPM 70%+ ↔ -37% (큰 swing) | OPM 24-41% (안정) |
| **대체 가능성** | 메모리는 3사 외 사실상 없음 | RISC-V 부상 + Apple·Qualcomm Nuvia architecture license |
| **수익 비유** | "wafer 1장 = $5K-50K" | "chip 1개 출하 = $0.10-1.00" |

**핵심 차이**: 메모리는 **(A) 구조적 메가 병목** (공급 제한 + 수요 폭증 → ASP 직접 폭등), ARM은 **(D) 동반 확대** (공급 무제한 + 수요 폭증 → 수량 +, 가격은 점진).

---

# 항목 3. 재무 분석

## 3-1. 실적 추이 (7년 + 12분기, 기업개요 v4.9 reference)

### 7년 장기 추세(secular) 성장 (FY20-FY26)
| 연도 | 매출 ($B) | OP ($B) | OPM | 핵심 이벤트 |
|---|---|---|---|---|
| FY20 | 1.91 | 0.51 | 26.7% | 매출 base |
| FY21 | 2.03 | 0.59 | 29.1% | — |
| FY22 | 2.70 | 0.99 | 36.7% | NVIDIA 인수 시도 (FTC 차단) |
| FY23 | 2.68 | 0.65 | 24.4% | IPO 직전 마진 후퇴 |
| FY24 | 3.23 | 1.05 | 32.5% | IPO 후 첫 standalone year |
| FY25 | 4.00 | 1.41 | 35.3% | AI 채택 본격화 |
| **FY26** | **4.92** | **2.00** | **40.7%** | **★ Record, AI Inflection Point** |

**핵심 관찰**:
- **매출 7년 CAGR +17%** (메모리·HDD 정반대 장기 추세(secular) 성장)
- **Non-GAAP OPM range 24.4% ~ 40.7% = 16.3%p** (메모리 진폭 1/3)
- **적자 분기 history 0** (IPO 후 7년, 사이클성 매우 약함)
- 3년 연속 매출 +20%+ 성장 (FY24·FY25·FY26)

### Q4 FY26 분기 실적 (record, IR Earnings 2026-05-06)

| 항목 | Q4 FY26 (2026-01~03) | YoY | 비고 |
|---|---|---|---|
| **Total Revenue** | **$1.49B** | **+20%** | record (3분기 연속 $1B+) |
| **License & Other** | **$819M** | **+29%** | CSS·AGI CPU 라이선스 가속 |
| **Royalty Revenue** | **$671M** | **+11%** | ARMv9·CSS 자동 매출 + |
| **Data Center Royalty** | **2x YoY** | record | NVIDIA Grace·Graviton·Cobalt·Axion |
| **Non-GAAP EPS** | **$0.60** | beat $0.58 | record |
| **Non-GAAP OPM** | **~40%+** | 정점 | software 수준 |

### FY26 전체 + 사업부 분해

| 구분 | FY26 매출 | YoY | 비중 |
|---|---|---|---|
| Royalty | $1.98B | +11% (Q4) | 40% |
| Licensing | $2.94B | +29% (Q4) | 60% |
| **Total** | **$4.92B** | **+23%** | 100% |

## 3-2. PQC 분해 — Royalty + Licensing 모델

| 차원 | Royalty (40% of revenue) | Licensing (60%) |
|---|---|---|
| **P (per-unit rate 변화)** | ARMv8 → ARMv9 (2x) / CSS (10%+ ASP) | Subscription / multi-year fee |
| **Q (chip 출하량 변화)** | 데이터센터 chip +50%+ / 모바일 일정 / IoT + | License 신규 + 갱신 |
| **매출 (P×Q)** | $1.98B (+11%) | $2.94B (+29%) |
| **마진** | 매우 높음 (CapEx 거의 없음) | 동일 (IP 한계비용 0) |

### Royalty의 시차 효과
- **Royalty 11%는 chip 출하의 후행 지표** (6-12개월 지연)
- 즉 1Q26 chip 출하 → 3Q26-4Q26 royalty 매출 인식
- **장기 royalty +가 더 강할 가능성** (ARMv9 비중 25% → 60-70% 단계적 + AGI CPU 2028+)

## 3-3. 재무 건전성 (기업개요 v4.9 fact)

| 항목 | FY26 |
|---|---|
| 자본총계 | 매우 강함 (메모리 3사처럼 CapEx 부담 없음) |
| OCF | 매출 대비 매우 높음 (software 수준) |
| FCF | 매출 대비 매우 높음 |
| **CapEx** | **거의 없음 (R&D만)** — 메모리 3사 $15-25B 대비 0에 가까움 |
| Debt | 거의 없음 |
| Cash | 강함 |
| Dividend / 자사주 | IPO 후 미실시 (성장 투자 우선) |
| **★ SoftBank 보유** | **88% (점진 매각 중)** — Stargate $400B 인프라 funding 압박 |
| CEO | **Rene Haas** (2022.02~ 현직, 前 NVIDIA·Tessera) |
| CFO | Jason Child (2023.09 IPO 직전 부임, 前 Splunk) |
| 발행주식수 | 약 1.07B 주 |
| 2026 YTD 주가 | **+84%** |

### 주요 자본 movement 2025-2026
- **SoftBank Ampere 인수 (2025)** — AGI CPU 디자인 기반 + Stargate 인프라 스토리(narrative)
- **AGI CPU 발표 (2026-03-24)** — 비즈니스 모델 확장
- **Q4 FY26 record (2026-05-06)** — Data center royalty 2x YoY

## 3-4. 피어 수익성 비교 (Non-GAAP OPM 통일)

| 기업 | FY 매출 | OPM | 1Q26 OPM | 본 테마 수혜 |
|---|---|---|---|---|
| **ARM Holdings** | **$4.92B (FY26)** | **40.7% (record)** | **~40%+** | 본 테마 직접 (royalty 4종) |
| NVIDIA | $130B+ | 60%+ | 65%+ | AI 가속기 96% |
| TSMC | $90B+ | 45%+ | 50%+ | Foundry 압도 |
| SK하이닉스 | 66.2조원 | 25%+ | **72%** | HBM 사이클 정점 |
| Micron | $37.38B | 32% | 69% | HBM + 미국 본토 |
| AMD | $25B+ | 25%+ | 30%+ | x86 + AI MI |
| **인텔** | **$52.85B** | **0.5%** | **1%** | 사업 전환(Turnaround), 점유 잠식 |

→ **ARM OPM 40%+ = software 수준의 안정 마진**. 메모리 3사 사이클 정점 OPM 70%+에는 미달하지만 사이클 진폭 매우 작음 — **안정 장기 추세(secular) 수익 모델**.

---

# 항목 4. 성장성 분석

## 4-1. 과거 성장률

| 기업 | 7년 매출 CAGR | 비고 |
|---|---|---|
| **ARM** | **+17%** | 장기 추세(secular) IP licensing |
| NVIDIA | +50%+ | AI 가속기 폭증 |
| TSMC | +15%+ | Foundry 메가 |
| SK하이닉스 | +12%+ | HBM 메가 |
| AMD | +20%+ | x86 + AI |
| Micron | +7%+ | 메모리 사이클 + HBM |
| **인텔** | **-0.46%** | 구조적 침체 |

→ **ARM +17% CAGR = 3년 연속 +20%+ 성장**, 안정성 매우 높음 (적자 분기 0).

## 4-2. 향후 PQC 전망 (4Q + 2Y)

### Royalty Revenue — (A) 구조적 메가 병목 + (D) 동반 확대

| 차원 | 4Q | 2Y | 근거 | 출처 |
|---|---|---|---|---|
| P (per-chip rate) | ARMv9 25%→30%·35%·40%·45% | 50%·60% | ARMv9 채택 가속 (자동 rate 2x) | ARM IR FY26 |
| P (CSS rate) | 20%→22%·25%·28%·30% | 35%·40% | Chip ASP 10%+ rate 확대 | ARM IR |
| Q (chip 출하) | +15·20·20·25% | +50%·40% | 데이터센터 + 모바일 + AI PC 통합 | IDC + 컨센 |
| **→ 매출** | **+20-30% YoY** | **+50-60% (2Y)** | 장기 추세(secular) + AI inflection | 컨센 |

### Licensing Revenue — (A) 구조적 메가 병목

| 차원 | 4Q | 2Y | 근거 | 출처 |
|---|---|---|---|---|
| P | normal | normal | 안정 라이선스 fee | ARM IR |
| Q | +25·30·25·20% | +40%·30% | CSS + AGI CPU + 신규 라이선스 가속 | ARM IR |
| **→ 매출** | **+25-30% YoY** | **+40-50% (2Y)** | CSS·AGI CPU driver | 컨센 |

### AGI CPU (★ 신규) — (A) 구조적 메가 병목

| 차원 | 4Q | 2Y | 근거 | 출처 |
|---|---|---|---|---|
| P | 자체 칩 가격 (TBD) | TBD | TSMC 3nm 양산 단가 | ARM IR |
| Q | 2026 H2 volume ship 시작 | +급증 | $2B+ committed (Meta·Oracle·ByteDance) | ARM IR |
| **→ 매출** | 미미 (2026), 본격 (2027~) | **$2B+ (2028+ material)** | committed orders | ARM IR |

### 회사 전체 매출·OPM 전망

| 항목 | FY24 | FY25 | FY26 | FY27E | FY28E |
|---|---|---|---|---|---|
| 매출 ($B) | 3.23 | 4.00 | 4.92 | **~6.5 (+32%)** | **~9-10 (+40%+, AGI CPU 본격)** |
| OP ($B) | 1.05 | 1.41 | 2.00 | **~2.8** | **~4.5+** |
| **OPM** | 32.5% | 35.3% | 40.7% | **~43%** | **~45%+** |

> **알 수 없음 시나리오**: AGI CPU가 NVIDIA Grace·AWS Graviton·MSFT Cobalt·Google Axion과 server CPU 시장에서 경쟁 진입 → **라이선시가 ARM 라이선스 재협상 또는 RISC-V 대안 검토 가능성**. 단기는 영향 미미하지만 2028+ 잠재 risk.

### 수주잔고·백로그
- **AGI CPU committed**: Meta + Oracle + ByteDance **$2B+** (2026-03 발표)
- **CSS 라이선스 확대**: 신규 라이선시 지속 증가
- **N1/N1X (NVIDIA + MSFT)**: 2026 H2 본격 출하
- **Stargate $400B 인프라 스토리(narrative)**: SoftBank 주도, ARM 핵심 IP supplier

## 4-3. 피어 그룹 비교

| 기업 | FY 매출 | 5년 CAGR | 1Q26 OPM | PER (2026) | 핵심 차이 |
|---|---|---|---|---|---|
| **ARM** | $4.92B | +25%+ | ~40%+ | **~100x+** | chipless IP, royalty 광범위 노출 |
| NVIDIA | ~$130B+ | +50%+ | 65%+ | ~50x | AI 가속기 단일 우위 |
| TSMC | ~$90B+ | +20% | 50%+ | ~25x | Foundry 압도 |
| SK하이닉스 | 97.15조원 (FY25, +44% YoY) | +25%+ | 72% | ~10x | HBM 사이클 |
| AMD | ~$25B | +25%+ | 30%+ | ~45x | x86 + AI MI |
| Micron | $37.38B | +7%+ | 69% | ~15x | HBM + 미국 본토 |

→ **ARM PER 100x+ = 광범위 노출과 안정성에 대한 프리미엄**. 단 sharp 상방 여력 어려움 (이미 가격 반영).

---

# 항목 5. 통합 모드 입력용 Fact 정리

| 항목 | Fact / Raw Data |
|---|---|
| **현재 시장 점유 + 추이** | 모바일 CPU 99% (Apple·Qualcomm·MediaTek·Samsung 모두). **DC CPU FY24 9%→FY26 15%, 하이퍼스케일러 ~50%** (Q1 2026 IDC server CPU 17.7%, +6.2%p YoY). 누적 chip shipments **290B+** |
| **ARM 라이선시 4종 (DC)** | NVIDIA Grace (Neoverse V2, GB200 NVL72 host CPU) + AWS Graviton 4/5 (50%+ AWS compute) + MSFT Cobalt 100 + Google Axion — 모두 TSMC 양산 |
| **현재 CAPA** | ARM은 IP 회사 — 자체 CAPA 부재. TSMC 등 양산 capa 의존. **CapEx ~$0** |
| **사이클 마진 진폭 (7년)** | OPM 24.4% (FY23) ~ 40.7% (FY26) = **16.3%p** (메모리 진폭 1/3). 적자 분기 history 0 |
| **기술 격차·R&D·IP** | **ARMv9 (SVE2, CCA confidential computing)** — royalty 2x. **CSS (Compute Subsystems)** — chip ASP 10%+ rate. **AGI CPU (136 Neoverse V3, TSMC 3nm)** — 자체 칩 진입 |
| **고객 분포** | Apple (architecture license) + Qualcomm + MediaTek + Samsung (모바일). NVIDIA·AWS·MSFT·Google (DC). **★ AGI CPU 고객**: Meta + Oracle + ByteDance ($2B+ committed) |
| **신규 수주·계약** | **★ AGI CPU $2B+ committed (2026-03-24)** + **★ N1/N1X (2026-06-01 Computex)** + CSS 라이선스 가속 |
| **자본·시총** | SoftBank 88% 보유, **2026 YTD 주가 +84%**, PER 100x+ |
| **Q4 FY26 실적 (★)** | 매출 $1.49B (+20%) / Royalty $671M (+11%) / License $819M (+29%) / **Non-GAAP EPS $0.60 (beat $0.58)** / **Data center royalty 2x YoY** |
| **FY26 전체** | 매출 $4.92B (+23%) / Non-GAAP OPM 40.7% record / 3년 연속 +20%+ 성장 |
| **ARMv9 비중** | CY25 **25%** → 장기 target **60-70%** (royalty rate 2x 자동 +) |
| **CSS 비중** | royalty 약 **20%**, ASP **10%+ rate** (사상 최고) |
| **AGI CPU 일정** | **2026 H2 volume 출하 / 2028+ material revenue** ($2B+ committed) |

---

# 항목 6. 구조적 트리거 모니터링

## 상방 트리거 (수혜 가속)

| 트리거 | 시점 | 영향 |
|---|---|---|
| **★ AGI CPU $2B → $5B+ 추가 committed** | 2026 H2 - 2027 | 비즈니스 모델 확장 실증, FY28+ 매출 +50%+ |
| **★ N1/N1X 본격 출하 (2026 H2)** | 2026 Q3-Q4 | client CPU TAM 폭증, royalty +30%+ |
| **ARMv9 비중 25% → 40%+ 도달** | 2026-2027 | royalty rate 2x 자동 매출 + 가속 |
| **CSS 채택 라이선시 추가 확보** | 2026 분기별 | chip ASP 10%+ rate 적용 chip 확대 |
| **NVIDIA Kyber Ultra (660kW/rack) 출하** | 2026 H2 - 2027 | Grace CPU 비중 ↑, ARM royalty 가속 |
| **AWS Graviton 5 (192-core) 양산** | 2026 H2 | AWS 자체 compute 50%+→60%+, ARM royalty + |
| **Stargate 인프라 본격 capex 집행** | 2026-2030 | $400B + 인프라, ARM IP 핵심 supplier |
| **데이터센터 royalty 추가 2x+** | FY27 | 데이터센터 비중 가속 (현재 royalty 2x YoY) |

## 하방 트리거 (수혜 약화)

| 트리거 | 시점 | 영향 |
|---|---|---|
| **★ AGI CPU 진입 = 라이선시 라이선스 재협상 또는 RISC-V 검토** | 2027-2028 | NVIDIA·AWS·MSFT·Google이 ARM 의존도 축소 risk |
| **RISC-V 하이퍼스케일러 채택 본격화** | 2027+ | 중국 디커플링·임베디드 → server·client 단계적 진입 |
| **Apple·Qualcomm Nuvia가 architecture license만 사용** | 지속 | 정상 royalty rate 회피 (rate 낮음) |
| **PER 100x+ 밸류에이션 압축(multiple compression)** | 2026 H2 | macro risk / AI capex 둔화 시 |
| **SoftBank 매각 압박** | 분기별 | 88% 보유, Stargate funding 위해 매각 가능 |
| **AGI CPU 라이선시 경쟁 risk가 actual로** | 2028+ | server CPU 시장 직접 경쟁 |
| **NVIDIA·AMD가 자체 ARM 대안 (자체 ISA)** | 장기 | RISC-V 또는 자체 ISA로 ARM royalty 회피 시도 |

## 모니터링 캘린더

| 시점 | 이벤트 |
|---|---|
| 분기 어닝콜 (Q1-Q4, 1·5·8·11월) | Royalty·License·Data center 매출 가이던스 |
| ARM TechCon (연 1회, 10월) | 신규 IP·CSS·AGI CPU 발표 |
| NVIDIA GTC (연 2회, 3월·10월) + Taipei (6월) | Grace·N1/N1X·ARM 협력 |
| AWS re:Invent (연 1회, 11월) | Graviton 5 + ARM 채택 확대 |
| Microsoft Build (연 1회, 5월) | Cobalt + Windows on Arm |
| Apple WWDC (연 1회, 6월) | M·A 시리즈 (architecture license rate) |
| Stargate funding 발표 | SoftBank Ampere·ARM 위치 |
| RISC-V International conference | 위협 모니터링 |

---

# 종합 판단

## 매트릭스 평가

| 차원 | 평가 | 근거 |
|---|---|---|
| 상위 트렌드 적합성 | ★★★ 최상위 | 본 테마 모든 segment에서 royalty 수혜 |
| 산업 위치 | ★★★ 최상위 | 반도체 산업의 운영체제 (IP 표준) |
| 해자 강도 (Moat 종합) | ★★★ 4.1/5.0 | 메모리 3사 4.0+ 동급, 인텔 2.8보다 1.3p 높음 |
| 재무 건전성 | ★★★ 최상위 | OPM 40.7% record / 적자 history 0 / CapEx ~$0 |
| 성장 가시성 (2~3년) | ★★★ 최상위 | 3년 연속 +20%+ / AGI CPU 추가 / FY28+ +40%+ 가능 |
| **밸류에이션 risk** | **★★ PER 100x+ 가격 반영** | sharp 상방 여력 어려움, 밸류에이션 압축(multiple compression) risk |

## 핵심 투자 포인트 3

1. **★ Royalty 4종 매핑 — chipless IP 모델의 광범위 수혜** — NVIDIA Grace + AWS Graviton 4/5 + MSFT Cobalt + Google Axion 모두 ARM Neoverse IP, TSMC 양산. 1Q26 IDC server CPU 점유 17.7% (+6.2%p YoY) = 4종 합산, **ARM이 모든 chip에서 royalty 동시 수혜**. Q4 FY26 데이터센터 royalty 2x YoY로 실증.
2. **★ ARMv9 + CSS royalty rate 프리미엄** — ARMv9 royalty rate ARMv8 대비 **2x**, CY25 25% → 장기 60-70% (자동 매출 +). **CSS Chip ASP 10%+ rate (사상 최고)**, royalty 20% 비중 가속. ARMv9·CSS 채택 확대만으로 매출 +30%+ 자동 발생.
3. **★ AGI CPU 비즈니스 모델 확장 (2026-03-24)** — ARM 35년 첫 자체 칩. 136 Neoverse V3 / TSMC 3nm / 300W TDP (AMD 500W·Intel 500W 대비 power efficiency). **Meta + Oracle + ByteDance $2B+ committed**, 2026 H2 ship, 2028+ material revenue. SoftBank Stargate $400B 인프라 스토리(narrative) + Ampere 인수 시너지.

## 핵심 리스크 3

1. **★ AGI CPU 진입 = 라이선시와 잠재 경쟁 risk** — ARM이 자체 server CPU 시장 진입하면 NVIDIA Grace·AWS Graviton·MSFT Cobalt·Google Axion과 직접 경쟁. **라이선시가 ARM 의존도 축소 시도 (라이선스 재협상 또는 RISC-V 대안 검토) 가능성**. 단기 영향 미미하지만 2028+ 본격화 risk.
2. **PER 100x+ 이미 highly valued** — 모든 + 가격 반영. 메모리 3사 PER 10-15x, NVIDIA 50x, TSMC 25x 대비 명확히 valuation 프리미엄. macro risk / AI capex 둔화 / 밸류에이션 압축(multiple compression) 시 주가 하락 폭 클 risk.
3. **RISC-V 부상 + architecture license 회피** — 중국 RISC-V 가속 (디커플링), Apple·Qualcomm Nuvia가 architecture license만 받아 정상 royalty rate 회피. **장기 ARM IP 표준성 약화 risk**. 단 단기 5년은 ARM 표준 유지 견고.

---

## 부록: 변경 이력 (Changelog)

### v1 (2026-06-02) — 1차 작성
- 산업 기초 + 테마 v4 + ARM_기업개요 v4.9 자동 참조
- **★ AGI CPU (2026-03-24) — ARM 35년 첫 자체 칩** 신규 반영
- **★ Q4 FY26 record (2026-05-06)** — 매출 $1.49B (+20%) / Royalty $671M (+11%) / License $819M (+29%) / 데이터센터 royalty 2x YoY 반영
- **★ N1/N1X (2026-06-01 Computex)** NVIDIA+MSFT 협력 clien

---

## ★ v2 fact-check 정정 (2026-06-02) — 사용자 피드백 반영

**핵심 정정**:
1. **삼성 DS 1Q26 OPM**: "~25%" → **65.7%** (DS 매출 81.7조원 / OP 53.7조원, 메모리 사이클 정점 record, SK 72%·Micron 69%와 동급)
2. **삼성 전사 1Q26 OPM**: 42.7% (매출 133.9조원 / OP 57.2조원), DX 흡수 효과
3. **SK FY25 매출**: 97.15조원 (+44% YoY)
4. **SK 1Q26 매출**: 52.6조원 alone (+60% Q/Q, +198% YoY)
5. **SK HBM 점유 Q1 2026**: 52% (TrendForce) — 단 시점·자료에 따라 50-62% 범위
6. **AMD OpenAI 6GW MI450 deal 시점**: 2025-10 발표 (2026-Q1 X)
7. **Micron HBM 점유**: Q1 2026 5-10% (TrendForce), 2026 H2 추정치 20% 도달 (Astute Group)

**영향**: 본 분석의 peer 비교 차트에서 삼성 DS OPM 25 → 65.7으로 일괄 정정. 스토리(narrative) "삼성 = DX 분산 흡수"는 부정확 → "삼성 DS는 record, 전사 OPM은 DX 흡수"로 정정.
