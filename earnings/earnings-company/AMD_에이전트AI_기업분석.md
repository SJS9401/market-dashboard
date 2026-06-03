---
ticker: "AMD"
company_name: AMD (Advanced Micro Devices, Inc.)
country: US
theme_keyword: 에이전트AI
parent_industry: 반도체
cross_ref_industry: 전력 인프라
moat_strength: 3.8              # 본 테마 segment 가중 평균 — 인텔 2.8 < AMD 3.8 < ARM 4.1 < 메모리 4.0+
moat_by_segment:
  x86_server_CPU_EPYC: 4.0      # 점유 24.1% → 27.4% (+3.3%p YoY) 가속, Meta 6th Gen lead
  AI_가속기_MI300_MI400: 3.8    # 점유 9% → 18% (2026E), Meta + OpenAI 6GW+6GW mega deal
  x86_client_CPU_Ryzen: 3.5     # 점유 ~22-28% 안정, AI PC 진입
  FPGA_Xilinx: 4.5              # 글로벌 #1 (Xilinx 인수 2022)
  DPU_Pensando_Embedded: 3.5    # Smart NIC, 신규
  Gaming_Radeon_Console: 3.0    # PS5·Xbox SoC, 사이클 성숙
trend_revenue_share: 60         # Data Center 48% + Client 일부 + Embedded 일부 — 본 테마 직접 노출
last_updated: 2026-06-02
auto_references:
  - 반도체_산업기초.md (2026-05-18)
  - 전력 인프라_산업기초.md (2026-05-18)
  - 에이전트AI_테마분석.md (v4, 2026-05-26)
  - AMD_기업개요.md (v4.9, 2026-05-18 — SEC 10-K 15개·10-Q 47개 + AMD IR Earnings Slides 8개 기반)
analyst_reports_attached:
  - AMD Q1 2026 8-K (2026-05-05 발표)
  - AMD·OpenAI 6GW MI450 deal (2026-Q1, OpenAI 160M 주 warrant $0.01)
  - AMD·Meta 6GW MI450 + 6th Gen EPYC (2026-Q1)
  - MLPerf MI355X benchmark (2026)
notes:
  - AMD는 미국 기업, 회계연도 12월 마지막 토요일 마감 (FY25 = 2024-12-29~2025-12-27, calendar year에 근사)
  - 본 분석 frame: Lisa Su 12년 Turnaround 성공 사례 — 인텔·메모리·ARM·NVIDIA와 다른 angle (Turnaround 완료된 high growth)
---

# AMD (Advanced Micro Devices) 기업 분석 — 에이전트AI 테마

> **본 분석 frame**: 에이전트AI 테마 분석(v4)의 17 segment 중 **AMD는 x86 server CPU 점유 가속 (Intel 잠식) + AI 가속기 NVIDIA 대안 #1 + FPGA Xilinx 글로벌 #1**. **인텔 (Turnaround 시작, Moat 2.8) ↔ AMD (사업 전환(Turnaround) 완료 + 본 테마 직접 수혜, Moat 3.8) ↔ ARM (chipless IP, Moat 4.1) ↔ 메모리 3사 (사이클 정점, Moat 4.0+)** 중 AMD는 **본 테마 직접 수혜자 + 사이클·장기 추세(secular) 양면 + NVIDIA 대안 유일 대안** 위치. **★ 2026-Q1 Meta + OpenAI 6GW + 6GW = 합 12GW MI450 대형 계약(mega deal)**이 스토리(narrative) 정점.

> **점유율·CAPA 표기 기준**: 본 분석의 모든 % 점유율은 **매출 기준** (TrendForce·Counterpoint·IDC·Mercury Research). AMD는 **fabless 회사로 자체 CAPA 부재** — TSMC 양산 capa 의존 (HBM4는 SK·Samsung 알로케이션 의존).

---

## Executive Summary (5줄)

1. **위치**: x86 CPU 글로벌 #2이지만 **DC server CPU 점유 24.1% → 27.4% (+3.3%p YoY, Q1 2026 IDC)** 가속 +. **AI 가속기 점유 9% → 18% (2026E)** = NVIDIA 96% 대비 **유일한 명확한 대안**. **★ Meta 6GW MI450 + 6th Gen EPYC lead (2026-Q1) + OpenAI 6GW MI450 deal (2025-10 발표, 1GW 2H 2026 시작, AMD 주식 160M warrant $0.01)** = 합 **12GW 대형 계약(mega deal)** 확보. FPGA Xilinx 글로벌 #1. PC Ryzen ~22-28% 안정. **★ NVIDIA 독점(monopoly) 깨는 스토리(narrative) 유일 종목**.
2. **해자 종합 (segment 가중)**: <strong>3.8 / 5.0</strong> (인텔 2.8 < AMD 3.8 < ARM 4.1 / 메모리 3사 4.0+) — FPGA Xilinx 4.5 (글로벌 #1) / x86 server 4.0 (점유 가속) / AI 가속기 3.8 (NVIDIA 대안) / x86 client 3.5 / DPU 3.5 / Gaming 3.0. **인텔 Foundry 18A (3.2)·AGI CPU (3.2)·메모리 Micron HBM (4.0) 동급 또는 약간 약함**.
3. **재무 (Lisa Su 12년 사업 전환(Turnaround) 성공)**: **FY25 매출 $34.64B (+34% YoY) / OP $2.74B / NPM 11.8% (사이클 정점 3차 진입)**. **Q1 2026 매출 $10.31B (+38% YoY) / Non-GAAP GM 55% / Non-GAAP EPS $1.37 / Data Center $5.8B (+57%, Instinct GPU $4.2B = DC 73%)**. **★ 12년 매출 CAGR +18.5%** (인텔 -0.46% 대비 정반대). 시총 $290B+ ($3B → 100배 turnaround).
4. **미래**: **★ MI450 (CDNA 5, TSMC 2nm, HBM4 432GB·19.6 TB/s, Helios rack 72 GPU = 1.4-2.9 exaFLOPS) 2026 H2 본격 출하**. Meta + OpenAI 12GW MI450 deal + 5세대 EPYC AWS·Google·Azure·Tencent 전면 채택 + 6세대 EPYC Meta lead. **AI 가속기 점유 18% (2026) → 25-30% (2027) 가능**. **단 NVIDIA CUDA 생태계 압도 + HBM4 알로케이션 Samsung preferred로 SK 의존도 risk**.
5. **종합 판단**: <span class="star">★★★ 본 테마 직접 수혜 종목 (메모리 3사 + ARM + NVIDIA와 동급)</span>. **(a) NVIDIA CUDA 생태계 절대 락인(lock-in), (b) ARM 라이선시 4종 (Grace·Graviton·Cobalt·Axion) AMD server CPU도 잠식 risk, (c) PER 45x+ 이미 가격 반영** 3대 risk. 단 **(1) Meta + OpenAI 12GW MI450 대형 계약(mega deal), (2) Lisa Su CEO 12년 사업 전환(Turnaround) 트랙 record, (3) FPGA Xilinx + Embedded 다각화**가 3대 positive optionality.

---

# 항목 1. 입력 정리 + 기업 포지셔닝

## 1-1. 산업·테마 컨텍스트

- **반도체 산업기초** (v1, 2026-05-18): (A) 구조적 메가 병목 → AMD는 **x86 server 점유 가속 + AI 가속기 대안**로 본 테마 직접 수혜
- **에이전트AI 테마 v4** (2026-05-26): 17 segment 중 GPU·AI 가속기·server CPU·FPGA segment에서 AMD가 명확한 position
- **인텔 분석 (2026-06-02)**: Intel 54.9% → 단 AMD 27.4% 점유 가속 +이지만 ARM 17.7%도 가속 + → **인텔 잠식의 일부가 AMD에게 돌아옴**
- **ARM 분석 (2026-06-02)**: ARM 라이선시 4종은 AMD에게도 server CPU 잠식 risk
- **한국 접근 가능 TAM (2028E)**: $216-262B+ (AMD는 미국이라 한국 TAM 무관, 단 한국 HBM4 알로케이션 의존)

## 1-2. AMD의 위치 (테마 v4 Moat 후보 — segment별)

| Segment | 글로벌 점유 (2025-2026) | 순위 | 비고 |
|---|---|---|---|
| **x86 server CPU (EPYC)** | **24.1% → 27.4% (Q1 2026, +3.3%p YoY)** | **#2** | Intel 54.9% (-9.5%p) 잠식, Meta·AWS·Google·Azure·Tencent 5세대 채택 |
| **★ AI 가속기 (Instinct MI300/350/400)** | **9% (2025) → 18% (2026E)** | **#2** | NVIDIA 90% 대비 대안, MI355X MLPerf 입증 |
| **★ Meta MI450 deal** | **6GW** | — | First 1GW MI450 + 6th Gen EPYC lead customer (2026-Q1) |
| **★ OpenAI MI450 deal** | **6GW** | — | 1GW 2H 2026 시작, **AMD 주식 160M warrant ($0.01 strike, 10% 지분)** (2026-Q1) |
| **x86 client CPU (Ryzen)** | **~22-28%** | **#2** | Intel ~75%, AI PC 진입 (Ryzen AI) |
| **FPGA (Xilinx, 2022 인수)** | **#1 글로벌** | **#1** | Adaptive Computing, FPGA 시장 압도 |
| **DPU (Pensando, 2022 인수)** | small | #3-4 | Smart NIC, NVIDIA BlueField 경쟁 |
| **Gaming (Radeon + 콘솔 SoC)** | PS5·Xbox SoC 독점 | — | 콘솔 사이클 성숙 |
| **HBM 의존도** | 0% (메모리 3사에 의존) | — | MI450 HBM4 432GB — Samsung·SK 알로케이션 |

→ **본 테마 핵심 segment 모두 #2 (CPU·AI 가속기) 또는 #1 (FPGA)** — NVIDIA·Intel 양면 우위 가능 위치. 단 NVIDIA CUDA 생태계 압도가 본질 risk.

## 1-3. 사업부 구성 (FY25, AMD 기업개요 v4.9)

| Segment | FY25 매출 | YoY | 본 테마 연결 | 비중 |
|---|---|---|---|---|
| **Data Center** | **~$16.6B (48%)** | +85% | ★ 본 테마 직접 (EPYC + MI300/MI350/MI355X + Pensando) | **48%** |
| **Client (Ryzen)** | **~$9.0B (26%)** | +52% | client CPU + AI PC (간접) | **26%** |
| **Gaming (Radeon + 콘솔)** | **~$4.5B (13%)** | -36% | console SoC + GPU | **13%** |
| **Embedded (Xilinx FPGA)** | **~$4.5B (13%)** | -33% | Adaptive Computing + DPU | **13%** |
| **Total** | **$34.64B** | **+34%** | | 100% |

### 본 테마 직접 매출 노출
- **Data Center 48% × 100%** (EPYC + Instinct + Pensando 모두 본 테마)
- **Client 26% × ~30%** (AI PC + AI workstation)
- **Embedded 13% × ~50%** (AI 추론(inference) FPGA + DPU)
- **순 본 테마 직접 노출 = 약 60%** (SK 60%+ / Micron 70% / 삼성 22% / 인텔 30% / ARM 85% 중간 수준)
- **★ Q1 2026 Data Center Instinct GPU $4.2B = DC 73%** = AI 인프라 장기 추세(secular) 본격화

---

## ★ 2-0. 에이전트AI 테마 logical flow — 왜 AMD가 부각받는가

> **정성적 인과 사슬** (테마 v4 narrative → AMD 위치 매핑)

### 1단계: 에이전트 AI = 데이터·연산·메모리 폭증의 본질
- 에이전트 1건 = chat 1턴 대비 **토큰 20-30x** (Stanford/NVIDIA 실측, 테마 v4)
- 각 추론 단계·도구 호출·검색·메모리 갱신·tool execution = **연산(GPU/CPU) + 메모리(HBM/DRAM/SSD) + 스토리지(HDD) + IP(ARM) 모든 layer 부하 폭증**
- agent는 stateful → 과거 trace·long-context 보존 필요 = secular 누적

### 2단계: AI 인프라 layer별 분담 — AMD는 어디 위치?

| Layer | 데이터/연산 유형 | 매체·아이템 | 본 테마 수혜 종목 |
|---|---|---|---|
| **Hot (microsec)** | KV cache, activation, 모델 가중치(active) | **HBM** | **SK·삼성·Micron (HBM)** |
| **Warm (msec)** | 모델 가중치(off-package), 활성 dataset | **DRAM·SSD** | 메모리 3사 (DRAM) + SNDK·Solidigm (eSSD) |
| **Warm-Cold (sec)** | 검색 코퍼스, 벡터 DB, 최근 로그 | **eSSD QLC·HBF** | SNDK (122TB QLC, HBF) |
| **Cold (수초~분)** | 학습 데이터셋, 체크포인트, 보관 로그 | **HDD nearline** | WDC·Seagate |
| **Compute (CPU)** | server CPU + host CPU + client CPU | **x86·ARM** | Intel·AMD·ARM 라이선시 |
| **Compute (GPU·AI)** | training·inference 가속 | **GPU·ASIC** | NVIDIA·AMD·ARM |
| **IP layer** | 모든 chip 상위 설계 | **ARM IP** | ARM Holdings (royalty 광범위) |


→ **AMD 위치: **Compute (CPU + AI 가속기)** — NVIDIA 독점 깨는 유일 종목**

### 3단계: 왜 AMD가 본 테마에서 부각받는가? — 3가지 본질적 이유

1. **AI 가속기 점유 9% → 18% (2026E)** = NVIDIA 90% → 75-80% jam = NVIDIA monopoly 깨는 유일 alternative
2. **★ Meta 6GW MI450 + OpenAI 6GW MI450 = 합 12GW mega deal (2025-10·2026-Q1)** = hyperscaler가 직접 NVIDIA 대안으로 AMD 선택한 증거
3. **x86 server CPU 점유 24.1% → 27.4% (+3.3%p YoY)** = Intel 잠식 + AMD EPYC 5세대 (Turin) 양면 우위

### 4단계: 왜 AMD가 NVIDIA alternative 위치인가?

- **MI450 (CDNA 5, TSMC 2nm, HBM4 432GB·19.6 TB/s·40 PFLOPS FP4)** = Helios rack 1.4-2.9 exaFLOPS = NVIDIA GB200 NVL72 직접 경쟁
- **EPYC 6세대 Meta lead + 5세대 AWS·Google·Azure·Tencent 전면 채택** = server CPU + AI 가속기 양면
- **FPGA Xilinx 글로벌 #1 + Pensando DPU + ZT Systems ($4.9B AI 시스템)** 다각화
- **Lisa Su 12년 Turnaround = 시총 $3B → $290B+ (100배)** = 실증된 실행력

### 5단계: 본 분석 frame 결론

**본 테마 직접 수혜 + NVIDIA 독점 깨는 narrative 유일 종목**. Moat 3.8 (인텔 2.8 < AMD 3.8 < ARM 4.1·메모리 4.0+). 단 NVIDIA CUDA ecosystem 절대 lock-in + ARM 라이선시 4종이 AMD EPYC도 잠식 + PER 45x+ 가격 반영 3대 risk.

---


# 항목 2. 비즈니스 모델 & 해자 (Moat) — Segment별

## 2-1. 비즈니스 모델 — 핵심 차별점

### x86 server CPU (EPYC) — Data Center 핵심
- **EPYC 5세대 (Turin, Zen 5)** 양산 — Meta·AWS·Google·Azure·Tencent 전면 채택
- **EPYC 6세대 (2026 H2 양산 예정)** — Meta lead customer 확보
- Intel Xeon 대비 단일 코어 성능·power efficiency 모두 우위
- 5년 동안 server CPU 점유 1% → **35% 도달** (Lisa Su 사업 전환(Turnaround) 12년의 핵심)

### AI 가속기 (Instinct MI300/MI350/MI355X/MI400) — Data Center 폭증
- **MI300 시리즈** (2024-2025 양산) — HBM3 192GB, NVIDIA H100 대안
- **MI350 시리즈** (2025-2026 양산) — HBM3E, MI300 후속
- **MI355X** (2026-Q1 출하) — MLPerf benchmark에서 NVIDIA 대비 경쟁력 입증
- **★ MI450 (CDNA 5, 2026 H2 양산)** — TSMC 2nm, **HBM4 432GB / 19.6 TB/s bandwidth / 40 PFLOPS FP4**
- **★ Helios rack** = 72 MI450 = 1.4 exaFLOPS (FP8) / 2.9 exaFLOPS (FP4) — NVIDIA GB200 NVL72 직접 경쟁
- **AI 가속기 점유 9% (2025) → 18% (2026E)** — NVIDIA 90% → 75-80% 추정 jam

### x86 client CPU (Ryzen) — Client 사업부
- 점유 ~22-28% (Intel ~75%), AI PC Ryzen AI 진입
- NVIDIA + MSFT N1/N1X (Computex 2026-06-01) 위협 = 인텔보다 약하지만 영향
- Apple Silicon (ARM architecture license) = client 시장 별도 경쟁

### FPGA (Xilinx, 2022 인수) — Embedded 핵심
- **글로벌 FPGA 시장 #1** (Xilinx 인수 $49B, 2022)
- Adaptive Computing — 데이터센터 추론(inference), 5G, 자율주행 ADAS
- Versal ACAP (Adaptive Compute Acceleration Platform)

### DPU (Pensando, 2022 인수) — Smart NIC
- $1.9B 인수 (2022)
- AMD Pensando DPU = NVIDIA BlueField 직접 경쟁
- 데이터센터 네트워크 가속

### ★ Meta + OpenAI 12GW MI450 대형 계약(mega deal) — 스토리(narrative) 정점
- **Meta**: 6GW MI450 + 6th Gen EPYC lead customer + first 1GW MI450 deployment (2026-Q1 발표)
- **OpenAI**: 6GW MI450 multi-year deal, 1GW 2H 2026 시작
  - **AMD가 OpenAI에 160M 주 warrant 발행 ($0.01 strike, 약 10% 지분)** — performance 및 stock-price milestone 조건부
  - 즉 OpenAI가 AMD 매출 + AMD 주식 동시 보유 가능 (양사 align 강화)
- **합 12GW MI450** = AMD AI 가속기 매출 $20B+ 추가 (2026-2028 ramp)
- Helios rack 1.4-2.9 exaFLOPS = NVIDIA GB200 NVL72 직접 경쟁

### Lisa Su CEO 12년 사업 전환(Turnaround) (★ 사례 연구)
- **2014.10 부임 시 시총 $3B** (pre-Zen 시기 적자, 점유 침체)
- **2026-Q1 시총 $290B+** = **100배 폭등** (12년)
- Zen 출시 (2017) → Ryzen·EPYC 점유 폭발 → AI MI300 진입 (2024) → Meta·OpenAI 12GW deal (2026)
- 인텔 Lip-Bu Tan (2025-03~ 사업 전환(Turnaround) 시작)과 정반대 — **사업 전환(Turnaround) 완료 + 본 테마 폭증 수혜자**

## 2-2. Moat 종류별 Segment 평가 (메모리 3사·인텔·ARM과 mirror 구조)

### Segment 1. x86 server CPU (EPYC)
| 축 | AMD | Intel | ARM (Grace·Graviton·Cobalt·Axion) | 핵심 |
|---|---|---|---|---|
| 기술/특허 | **5** (Zen 5 단일 코어 우위) | 3 | 4 | AMD 단일 코어 우위 |
| CAPA | 3 (TSMC dep) | 5 (IDM) | 3 (TSMC dep) | Intel 양면 |
| 고객 락인(lock-in) | **4** (Meta 6th Gen lead) | 3 (잠식) | 4 (하이퍼스케일러 자체) | AMD 가속 + |
| 규모 (server CPU) | **4** ($16B+ DC) | 4 ($13B DCAI) | 4 (자체 chip) | AMD = Intel 동급 매출 |
| 병목 포지셔닝 | **4** (점유 +3.3%p YoY) | 2 (잠식자) | 5 (가장 빠른 +) | AMD 명확한 + |
| **평균** | **4.0** | **3.4** | **4.0** | **AMD·ARM 양면 우위, Intel 잠식** |

> **★ 정성: 왜 x86 server CPU에서 AMD가 점유 가속인가?**
> 
> **인과 사슬**: AMD EPYC Zen 4/5 = Intel Xeon 대비 단일 코어 우위 + per-core $·power efficiency 우위 → DC server CPU 점유 24.1% → 27.4% (+3.3%p YoY) 가속 → ★ Meta 6th Gen EPYC lead customer + AWS·Google·Azure·Tencent 5세대 전면 채택
> 
> **추가 동력 1 — ★ Meta 6th Gen EPYC lead customer (2026-Q1)**: hyperscaler lead = 다른 CSP 표준화 trigger
> **추가 동력 2 — AWS·Google·Azure·Tencent 5세대 전면 채택**: 글로벌 hyperscaler 5사 모두 AMD 5세대 = 점유 +3.3%p YoY 가속의 base
> **추가 동력 3 — Intel Xeon 점유 64%→54.9% (-9.5%p YoY)**: Intel 잠식의 일부가 AMD로 (나머지는 ARM)
> 
> **AMD 위치의 특별함**: 본 segment Moat 4.0으로 ARM과 함께 본 테마 양면 우위. NVIDIA 대안 narrative와 함께 AMD thesis 핵심 leg

### Segment 2. AI 가속기 (Instinct MI300/MI400) — ★ NVIDIA 대안 직접
| 축 | AMD MI400 | NVIDIA Blackwell/Rubin | Intel Gaudi 3 | 핵심 |
|---|---|---|---|---|
| 기술/특허 | **4** (CDNA 5, HBM4 432GB) | **5** (CUDA + Blackwell) | 2 | NVIDIA 압도, AMD catch-up |
| CAPA (TSMC) | 3 (TSMC 2nm 양산) | **5** (TSMC 우선 알로케이션) | 3 (자체 fab) | NVIDIA 우선 |
| 고객 락인(lock-in) | **4** (Meta + OpenAI 12GW) | **5** (CUDA 96%) | 1 | AMD 대형 계약(mega deal) 확보 |
| 규모 (AI 가속기 매출) | 3 (Q1 2026 $4.2B run-rate $17B+) | **5** ($200B+ DC) | 1 (미미) | NVIDIA 압도 |
| 병목 포지셔닝 | **4** (NVIDIA 대안 #1) | **5** | 1 | AMD 대안 위치 |
| **평균** | **3.6** | **5.0** | **1.6** | **NVIDIA 절대, AMD 대안 #1** |

> **★ 정성: 왜 AI 가속기에서 AMD가 NVIDIA 독점 깨는 alternative인가?**
> 
> **인과 사슬**: NVIDIA CUDA 96% 절대 독점 → 단 hyperscaler diversification 수요 → ★ Meta 6GW MI450 + OpenAI 6GW MI450 = 합 12GW mega deal (2025-10·2026-Q1) → AMD AI 가속기 점유 9% → 18% (2026E) 가속
> 
> **추가 동력 1 — ★ Meta 6GW + OpenAI 6GW = 12GW mega deal**: hyperscaler 직접 AMD 채택 = NVIDIA 독점 깨는 핵심 증거 (OpenAI는 AMD 주식 160M warrant $0.01 = 10% 지분도 포함)
> **추가 동력 2 — MI450 CDNA 5 + HBM4 432GB·19.6 TB/s + Helios rack 1.4-2.9 exaFLOPS**: 차세대 hardware spec NVIDIA Rubin 동급
> **추가 동력 3 — MLPerf MI355X benchmark 입증 + ROCm software stack 가속**: CUDA 대비 software gap 점진적 축소
> 
> **AMD 위치의 특별함**: NVIDIA 독점 깨는 유일 alternative + 12GW mega deal = AMD thesis 정점. 단 CUDA lock-in 본질 risk 잔존

### Segment 3. x86 client CPU (Ryzen)
| 축 | AMD | Intel | ARM (Apple·Qualcomm·★ NVIDIA N1/N1X) | 핵심 |
|---|---|---|---|---|
| 기술/특허 | 4 (Zen 5) | 4 (Panther Lake 18A) | 3 (NVIDIA 신규) | 동급 |
| CAPA | 3 (TSMC) | 5 (IDM) | 3 (TSMC) | Intel CAPA 양면 |
| 고객 락인(lock-in) | 3 (~22-28%) | 4 (Windows + x86 75%) | 2 | Intel 생태계 |
| 규모 | 3 ($9B) | **5** ($32.1B CCG) | 2 (시장 진입 초기) | Intel 압도 |
| 병목 포지셔닝 | 3 | 3 (위협 진행) | **4** (★ NVIDIA+MSFT) | ARM 신규 + |
| **평균** | **3.2** | **4.2** | **2.8** | **Intel 우위 유지, AMD #2** |

> **★ 정성: 왜 x86 client CPU에서 AMD가 #2 안정인가?**
> 
> **인과 사슬**: Intel x86 client 점유 75% Windows 생태계 lock-in → AMD Ryzen 22-28% #2 안정 → AI PC narrative + Ryzen AI 진입이지만 client market는 ARM (Apple·Qualcomm·★ NVIDIA N1/N1X) 위협이 더 크게 진행
> 
> **추가 동력 1 — AMD Ryzen AI = AI PC 진입**: Copilot+ PC 카테고리 진입이지만 Qualcomm·Apple 강점 = AMD 차별화 제한
> **추가 동력 2 — ★ NVIDIA N1/N1X (2026-06-01 Computex) + MSFT 협력**: ARM PC chip 신규 위협이 AMD·Intel 모두 위협
> **추가 동력 3 — Intel client 매출 $32.1B 압도 vs AMD $9B**: 매출 격차 매우 큼 = AMD 본 segment 영향 제한
> 
> **AMD 위치의 특별함**: 본 segment는 AMD thesis에서 stable #2이지만 ARM 위협이 client market 전체 잠식 risk

### Segment 4. FPGA (Xilinx, Embedded) — ★ AMD 글로벌 #1
| 축 | AMD Xilinx | Intel Altera (분사 51%) | Lattice | 핵심 |
|---|---|---|---|---|
| 기술/특허 | **5** (Versal ACAP) | 4 | 3 | Xilinx 압도 |
| 시장 점유 | **5** (#1 글로벌) | 3 (#2) | 2 (#3) | Xilinx 단독 |
| 고객 락인(lock-in) | **5** (데이터센터·5G·자율주행) | 3 | 2 | Xilinx 생태계 |
| 규모 | **5** ($4.5B Embedded) | 2 | 1 | Xilinx 단일 큰 |
| 병목 포지셔닝 | **5** (Adaptive Computing 본 테마 enabler) | 3 | 2 | Xilinx 본 테마 + |
| **평균** | **5.0** | **3.0** | **2.0** | **AMD Xilinx 글로벌 #1 압도** |

> **★ 정성: 왜 FPGA Xilinx가 AMD optionality인가?**
> 
> **인과 사슬**: AMD 2022 Xilinx $35B 인수 → FPGA 글로벌 #1 (Versal ACAP) → Adaptive Computing = data center·5G·자율주행·국방 광범위 → AI 추론 FPGA + DPU 신규 수요로 본 테마 enabler
> 
> **추가 동력 1 — ★ Xilinx 글로벌 #1 (Intel Altera 분사 51% 후 격차 확대)**: FPGA 시장 단독 dominance, Intel Altera 분사로 격차 더 확대
> **추가 동력 2 — Adaptive Computing = AI 추론 FPGA**: edge AI inference·자율주행·5G base station에 FPGA 채택 = 본 테마 차세대 수혜
> **추가 동력 3 — Versal ACAP = chiplet 차세대 architecture**: chiplet 시대에 FPGA + AI engine 통합 = ASIC alternative
> 
> **AMD 위치의 특별함**: 본 segment Moat 5.0으로 AMD 최강. AI 가속기 외 다각화 optionality + 본 테마 enabler

### Segment 5. DPU (Pensando, Smart NIC)
| 축 | AMD Pensando | NVIDIA BlueField | Marvell | 핵심 |
|---|---|---|---|---|
| 기술/특허 | 4 | **5** | 3 | NVIDIA BlueField 압도 |
| 규모 | 3 | **5** (DC 광범위) | 3 | NVIDIA 단독 |
| 고객 락인(lock-in) | 3 | **5** | 3 | NVIDIA Cumulus + DOCA |
| 병목 포지셔닝 | 4 (DC 네트워크 가속) | **5** | 3 | DPU 신규 segment |
| **평균** | **3.5** | **5.0** | **3.0** | **NVIDIA 압도, AMD #2** |

> **★ 정성: 왜 DPU (Pensando)가 AMD optionality인가?**
> 
> **인과 사슬**: AMD 2022 Pensando 인수 → Smart NIC + DPU 진입 → 단 NVIDIA BlueField + DOCA software stack 압도 → AMD #2 위치이지만 신규 segment 성장 leverage
> 
> **추가 동력 1 — DC 네트워크 가속 = 차세대 hyperscaler 표준**: AI 가속기 cluster 간 통신 + RDMA + offload = DPU 필수
> **추가 동력 2 — NVIDIA BlueField + DOCA 압도**: NVIDIA 자체 GPU·CPU·DPU 통합 stack = AMD #2 진입 어려움
> **추가 동력 3 — Pensando + Xilinx FPGA 통합 = AMD 차세대 differentiator**: FPGA+DPU 통합 architecture로 NVIDIA와 다른 path
> 
> **AMD 위치의 특별함**: 본 segment Moat 3.5 #2. 신규 segment이지만 NVIDIA 압도 우위로 AMD thesis 영향 제한

### Segment 6. Gaming (Radeon + 콘솔 SoC)
| 축 | AMD | NVIDIA (RTX) | Intel Arc | 핵심 |
|---|---|---|---|---|
| 기술/특허 | 3 (RDNA 4) | **5** | 2 | NVIDIA 압도 |
| 시장 점유 (개인 GPU) | 3 (~12%) | **5** (~85%) | 1 (~3%) | NVIDIA 절대 |
| 콘솔 SoC | **5** (PS5·Xbox 독점) | 1 (Nintendo Switch만) | 1 | AMD 콘솔 절대 |
| 규모 | 3 ($4.5B) | 4 | 1 | AMD 콘솔 매출 |
| 병목 포지셔닝 | 2 (사이클 성숙) | 4 | 1 | Gaming = 장기 추세(secular) X |
| **평균** | **3.2** | **3.8** | **1.2** | **콘솔 절대, 개인 GPU 약함** |

> **★ 정성: 왜 Gaming이 AMD thesis 약점 segment인가?**
> 
> **인과 사슬**: AMD Radeon 개인 GPU 점유 12% (NVIDIA RTX 85% 압도) → 콘솔 SoC만 PS5·Xbox 독점이지만 사이클 성숙 → Gaming 매출 -36% YoY (FY25) → 본 테마와 무관 + 사이클 약화 segment
> 
> **추가 동력 1 — 콘솔 SoC PS5·Xbox 독점**: 콘솔 사이클 = 5-7년 = 현재 사이클 후반 = 신규 콘솔 출시 전 매출 약화
> **추가 동력 2 — 개인 GPU NVIDIA 압도 (12% vs 85%)**: Gaming + ray tracing + DLSS 모두 NVIDIA 우위 = AMD 진입 어려움
> **추가 동력 3 — Gaming = secular 부재**: 본 에이전트 AI 테마와 무관, 사이클 산업
> 
> **AMD 위치의 특별함**: 본 segment Moat 3.2 약점 segment. 매출 비중 $4.5B (13%)로 thesis 영향 제한이지만 drag

### Segment 가중 평균 (Moat 종합)
- x86 server (4.0) × 30% + AI 가속기 (3.6) × 25% + Client (3.2) × 15% + FPGA Xilinx (5.0) × 13% + DPU (3.5) × 5% + Gaming (3.2) × 12% = **약 3.8**
- 인텔 (2.8) 대비 **1.0p 우위**, ARM (4.1) 대비 -0.3p, 메모리 3사 (4.0+) 대비 -0.2~0.6p
- **포지션**: 인텔 < AMD < 메모리·ARM (본 테마 frame)

## 2-3. 병목 수혜 강도 정량화 (본 테마 직접 메커니즘)

### 본 테마 수혜 메커니즘

| 본 테마 병목 | AMD 수혜 메커니즘 | 카테고리 | 정량 추정 |
|---|---|---|---|
| **AI 가속기 ↑** | MI300/MI350/MI355X/MI450 매출 폭증 | (A) | $4.2B (Q1 2026) → $20B+ (2026E, run-rate $17B+ 가속) |
| **x86 server CPU ↑** | EPYC 5/6세대 점유 가속 (Meta·AWS·Google·Azure·Tencent) | (A) | DCAI +57% YoY (Intel +22% 대비 ~2.5x) |
| **AI PC ↑** | Ryzen AI client 진입 | (D) | Client +52% YoY (Q1 2026) |
| **FPGA Adaptive Computing ↑** | Xilinx Versal (DC 추론(inference), 5G, 자율주행) | (D) | Embedded 회복 (FY24 -33% → 2026 회복 추정) |
| **DC 네트워크 가속 ↑** | Pensando DPU (NVIDIA BlueField 대안) | (D) | small but growing |
| **★ Meta + OpenAI 12GW MI450** | 대형 계약(mega deal) 직접 매출 | (A) | 2026-2028 ramp, AMD AI 매출 $20B+ 추가 |

→ **AMD = 본 테마 segment 6개 중 5개에서 직접 수혜**. 단 AI 가속기에서 NVIDIA 압도, server CPU에서 ARM 라이선시 4종도 잠식 risk = **양면 압박**.

### vs 메모리 3사·인텔·ARM 비교

| 차원 | 메모리 3사 | 인텔 | ARM | **AMD** |
|---|---|---|---|---|
| 본 테마 노출 | 60-70% (메모리 pure) | 30% (사업 전환(Turnaround)) | 85% (IP 광범위) | **60% (DC + Client AI)** |
| 본 테마 수혜 메커니즘 | wafer capa 병목 + ASP 폭등 | Foundry 18A catch-up | royalty 광범위 | **AI 가속기 NVIDIA 대안 + EPYC 점유 +** |
| Moat 종합 | 4.0-4.4 | 2.8 | 4.1 | **3.8** |
| 1Q26 OPM (Non-GAAP) | 25-72% | 1% | 40%+ | **~25%+** |
| 사이클 진폭 | OPM ±80%p (큰 swing) | -22%~+33% (54.9%p) | 16.3%p (안정) | **34.2%p (중간)** |

---

# 항목 3. 재무 분석

## 3-1. 실적 추이 (12년 + Q1 2026, 기업개요 v4.9)

### 12년 사업 전환(Turnaround) 사이클 (FY14-FY25)
| 연도 | 매출 ($B) | OP ($B) | OPM | 핵심 이벤트 |
|---|---|---|---|---|
| 2014 | 5.51 | -0.16 | -2.9% | pre-Zen, 점유 침체 |
| 2015 | **3.99** | **-0.48** | **-12.0%** | ★ 사이클 저점 1차 (적자) |
| 2017 | 5.33 | 0.13 | 2.5% | Ryzen·EPYC 출시 (★ 사업 전환(Turnaround) 시작) |
| 2018 | 6.48 | 0.45 | 6.9% | Zen 1차 정점 |
| 2020 | 9.76 | 1.37 | 14.0% | 코로나 + Ryzen·EPYC 폭증 |
| 2021 | **16.43** | 3.65 | **22.2%** | ★ 정점 2차 (코로나 IT cycle) |
| 2022 | 23.60 | 1.26 | 5.3% | Xilinx 인수 (무형자산 상각) |
| 2023 | 22.68 | 0.40 | 1.8% | Mid-cycle dip |
| 2024 | 25.79 | 1.90 | 7.4% | MI300 출하 시작 (AI GPU 진입) |
| 2025 | **34.64** | **2.74** | **7.9%** | **★ 정점 3차 진입 (AI GPU + 5세대 EPYC)** |

**핵심 관찰**:
- **매출 12년 CAGR +18.5%** (인텔 -0.46% 대비 정반대)
- **OPM range -12.0% ~ +22.2% = 34.2%p** (메모리 진폭의 절반, 인텔 54.9%p의 60%, ARM 16.3%p의 2배)
- **사이클 정점 3회 (FY18·FY21·FY25 진행 중)**, 저점 2회 (FY15·FY16)
- **시총 $3B → $290B+ = 100배 폭등 (Lisa Su 12년)**

### Q1 2026 분기 실적 (record, IR 2026-05-05)

| 항목 | Q1 2026 (CY) | YoY | 비고 |
|---|---|---|---|
| **Total Revenue** | **$10.31B** | **+38%** | record |
| **Non-GAAP GPM** | **55%** | +170bp | favorable product mix |
| **Non-GAAP EPS** | **$1.37** | record | — |
| **★ Data Center 매출** | **$5.8B** | **+57% YoY** | ★ 가장 빠른 segment |
| **Data Center Instinct GPU** | **$4.2B (DC 73%)** | record | MI355X 출하 |
| Client 매출 | $2.9B (추정) | +52% | Ryzen AI |
| Gaming | $1.0B (추정) | -25% | 콘솔 사이클 성숙 |
| Embedded (Xilinx) | $0.8B (추정) | 회복 시작 | FY24 -33% → 회복 |
| 주가 반응 | **+18% 점프** | — | beat + AI 가속기 스토리(narrative) |

## 3-2. 사업부별 PQC 분해 — Q1 2026 fact

| 차원 | Data Center (EPYC + Instinct) | Client (Ryzen) | Embedded (Xilinx) |
|---|---|---|---|
| **P (ASP 변화)** | +25% (Instinct GPU 프리미엄) | +15% (Ryzen AI) | normal |
| **Q (출하량 변화)** | +30% (Meta·AWS·Google·Azure·Tencent 채택) | +30% (PC 회복) | +5% (회복 시작) |
| **매출 (P×Q)** | $5.8B (+57%) | $2.9B (+52%) | $0.8B (회복) |
| **마진 (OPM)** | 40%+ (Instinct 최고 마진) | 약 15-20% | 약 10-15% |

### Instinct GPU 매출 분해
- **MI300/MI350 series**: 주력 매출
- **MI355X**: 2026-Q1 출하 시작, MLPerf 입증
- **MI450**: 2026 H2 본격 출하 시작 (Meta·OpenAI 12GW)
- Q1 2026 Instinct GPU run-rate **$17B+/year** (Q1 alone $4.2B × 4)

## 3-3. 재무 건전성 (기업개요 v4.9 fact)

| 항목 | FY24 / FY25 / Q1 2026 |
|---|---|
| 자본총계 | 강함 (Xilinx 인수 $49B 흡수 후 안정) |
| OCF | FY25 $5B+ → Q1 2026 가속 |
| FCF | FY25 $3B+ → Q1 2026 record |
| CapEx | Fabless이므로 낮음 ($1-2B/년) |
| Cash + ST Inv | ~$5B |
| Debt / Debt-Equity | 적정 수준 |
| 신용등급 | A3 / A- (안정) |
| 배당 | 분기 배당 X (성장 투자 우선) |
| 자사주 매입 | 분기별 진행 |
| 직원 수 | 약 26,000명 |
| 발행주식수 | 약 1.62B 주 |
| **CEO** | **Lisa Su (2014.10~ 현직, 12년 재임, MIT EE 박사)** — ★ 사업 전환(Turnaround) 영웅 |
| CFO | Jean Hu (2023.01~ 현직, 前 Marvell CFO) |
| **시총** | **약 $290B+ (2026-Q1)** — 2014.10 $3B 대비 **100배** |

### 주요 자본 movement 2025-2026
- **MI355X 출하 + MLPerf 입증** (2026-Q1)
- **★ Meta 6GW MI450 + 6th Gen EPYC lead deal** (2026-Q1)
- **★ OpenAI 6GW MI450 deal + 160M 주 warrant ($0.01 strike)** (2026-Q1)
- **5세대 EPYC AWS·Google·Azure·Tencent 전면 채택** (2025)
- ZT Systems 인수 ($4.9B, 2024) — AI 시스템 통합

## 3-4. 피어 수익성 비교 (Non-GAAP OPM 통일)

| 기업 | FY 매출 | OPM | 1Q26 OPM (Non-GAAP) | 본 테마 수혜 |
|---|---|---|---|---|
| **AMD** | **$34.64B (FY25)** | **7.9% GAAP / ~22% Non-GAAP** | **~25%+** | x86 + AI 양면 |
| NVIDIA | $130B+ | 60%+ | 65%+ | AI 가속기 96% |
| TSMC | $90B+ | 45%+ | 50%+ | Foundry 압도 |
| SK하이닉스 | 97.15조원 (FY25, +44% YoY) | 25%+ | **72%** | HBM 사이클 |
| Micron | $37.38B | 32% | 69% | HBM + 미국 본토 |
| ARM | $4.92B (FY26) | 40.7% | 40%+ | chipless IP |
| 삼성 DS | $80B (DS) | 35% | 25% | DRAM + Foundry |
| **인텔** | **$52.85B** | **0.5%** | **1%** | 사업 전환(Turnaround) 시작 |

→ **AMD OPM 25%+ = 사이클 정점 진행 중**. 메모리 3사 사이클 정점 OPM 60-70%에 미달하지만 안정 + 성장. 인텔 1% 대비 25배.

---

# 항목 4. 성장성 분석

## 4-1. 과거 성장률 (12년 CAGR)

| 기업 | 12년 매출 CAGR | 비고 |
|---|---|---|
| NVIDIA | +30%+ | AI 장기 추세(secular) |
| **AMD** | **+18.5%** | Lisa Su 사업 전환(Turnaround) 100배 |
| ARM | +17% (7년) | 장기 추세(secular) IP |
| TSMC | +15%+ | Foundry 메가 |
| SK하이닉스 | +12%+ | HBM 메가 |
| 마이크론 | +7%+ | 메모리 사이클 + HBM |
| 삼성전자 | +5%+ | 전사 |
| **인텔** | **-0.46%** | 구조적 침체 |

→ **AMD +18.5% = 반도체 동종 중 NVIDIA·ARM과 함께 장기 추세(secular) 성장 그룹**. 인텔과 정반대.

## 4-2. 향후 PQC 전망 (4Q + 2Y)

### Data Center (EPYC + Instinct) — (A) 구조적 메가 병목

| 차원 | 4Q | 2Y | 근거 | 출처 |
|---|---|---|---|---|
| P | +25·20·15·10% | +15·10% | Instinct GPU + EPYC 프리미엄 | AMD IR Q1 26 |
| Q | +30·35·40·45% | +60%·50% | **Meta+OpenAI 12GW MI450 + 5/6세대 EPYC** | 9개 셀사이드 컨센 |
| **→ 매출** | **+57-80% YoY** | **+100% (2026)·+60% (2027)** | AI 인프라 폭증 | 컨센·테마 v4 |

### Client (Ryzen) — (D) 동반 확대

| 차원 | 4Q | 2Y | 근거 | 출처 |
|---|---|---|---|---|
| P | +15·10·5·5% | +5·0% | Ryzen AI 프리미엄 | AMD IR |
| Q | +30·25·20·15% | +25·15% | AI PC 침투 (단 N1/N1X 위협) | IDC PC |
| **→ 매출** | **+50-60% YoY** | **+30% (2Y)** | AI PC 성장 | 컨센 |

### Embedded (Xilinx) — (D) 회복

| 차원 | 4Q | 2Y | 근거 | 출처 |
|---|---|---|---|---|
| P | normal | normal | FPGA 양산 단가 | AMD IR |
| Q | +5·10·15·20% | +25·20% | Adaptive Computing 회복 | AMD IR |
| **→ 매출** | **+10-20% YoY** | **+50% (2Y)** | FPGA 회복 | 컨센 |

### 회사 전체 매출·OPM 전망

| 항목 | FY24 | FY25 | FY26E | FY27E | FY28E |
|---|---|---|---|---|---|
| 매출 ($B) | 25.79 | 34.64 | **~50 (+45%)** | **~65 (+30%, MI450 본격)** | **~80 (+23%)** |
| OP ($B) | 1.90 | 2.74 | **~9-12 (Non-GAAP)** | **~15-20** | **~22-28** |
| **OPM (Non-GAAP)** | 22% | 22% | **~20-25%** | **~25-30%** | **~30%+** |

> **알 수 없음 시나리오**: NVIDIA CUDA 생태계 절대 lock-in을 AMD ROCm이 깰 수 있나? 현재 AI 가속기 점유 18% (2026E) → 25-30% (2027) 가능하지만 NVIDIA 75-80% 영구 유지 가능성.

### 수주잔고·백로그
- **Meta MI450 6GW (2026-Q1 발표)** — first 1GW 진행 + 6th Gen EPYC lead
- **OpenAI MI450 6GW (2026-Q1)** — 1GW 2H 2026 시작
- **5세대 EPYC**: AWS·Google·Azure·Tencent 전면 채택
- **MI355X** MLPerf 입증, 하이퍼스케일러 채택 가속

## 4-3. 피어 그룹 비교

| 기업 | FY 매출 | 5년 CAGR | 1Q26 OPM | PER (2026) | 핵심 차이 |
|---|---|---|---|---|---|
| **AMD** | **$34.64B** | **+25%+** | **25%+** | **~45x** | x86 + AI 양면 + FPGA #1 |
| NVIDIA | ~$130B+ | +50%+ | 65%+ | ~50x | AI 가속기 단일 우위 96% |
| TSMC | ~$90B+ | +20% | 50%+ | ~25x | Foundry 압도 |
| ARM | $4.92B | +25%+ | 40%+ | ~100x+ | chipless IP, 광범위 |
| SK하이닉스 | 97.15조원 (FY25, +44% YoY) | +25%+ | 72% | ~10x | HBM 사이클 정점 |
| Micron | $37.38B | +7%+ | 69% | ~15x | HBM + 미국 본토 |
| **인텔** | **$52.85B** | **-7%/년** | **1%** | N/A | 사업 전환(Turnaround) |

→ **AMD PER 45x = NVIDIA 50x에 근접**. AI 가속기 점유 18% (2026E)·25-30% (2027) 추가 도달 시 NVIDIA 프리미엄 격차 더 좁혀질 가능성.

---

# 항목 5. 통합 모드 입력용 Fact 정리

| 항목 | Fact / Raw Data |
|---|---|
| **현재 시장 점유 + 추이** | x86 server: 24.1% → **27.4% (+3.3%p YoY, Q1 2026 IDC)**. x86 client: ~22-28%. **AI 가속기: 9% (2025) → 18% (2026E)**. FPGA: 글로벌 #1 (Xilinx). 콘솔 SoC: PS5·Xbox 독점 |
| **현재 CAPA** | Fabless — TSMC 양산 의존. **MI450 TSMC 2nm 양산**. CapEx $1-2B/년 (낮음) |
| **사이클 마진 진폭 (12년)** | OPM -12.0% (FY15) ~ +22.2% (FY21) = **34.2%p**. 정점 3회 (FY18·FY21·FY25 진행 중) |
| **기술 격차·R&D·IP** | **EPYC Zen 5/6세대** (Intel Xeon 대비 단일 코어 우위). **MI400 CDNA 5** (HBM4 432GB, 19.6 TB/s, 40 PFLOPS FP4). **Xilinx Versal ACAP** (FPGA 글로벌 #1). R&D/Revenue 약 22% |
| **고객 분포** | **★ Meta 6GW MI450 + 6th Gen EPYC lead** + **★ OpenAI 6GW MI450 + 160M 주 warrant ($0.01)**. AWS·Google·Azure·Tencent 5세대 EPYC. 콘솔 SoC: Sony·MSFT |
| **신규 수주·계약** | **★ Meta 6GW (2026-Q1) + OpenAI 6GW (2026-Q1) = 12GW MI450 대형 계약(mega deal)**. ZT Systems 인수 $4.9B (2024) — AI 시스템 통합 |
| **자본·시총** | 자본 강함, **시총 $290B+ (2026-Q1, 2014.10 $3B 대비 100배)**, PER ~45x |
| **Q1 2026 실적 (★)** | 매출 $10.31B (+38%) / Non-GAAP GM 55% (+170bp) / Non-GAAP EPS $1.37 / **DC $5.8B (+57%, Instinct GPU $4.2B = DC 73%)** / Client +52% / 주가 +18% 점프 |
| **FY25 전체** | 매출 $34.64B (+34%) / GAAP OP $2.74B / NPM 11.8% (정점 3차 진입) |
| **MI450 spec** | CDNA 5, TSMC 2nm, **HBM4 432GB / 19.6 TB/s / 40 PFLOPS FP4**. Helios rack 72 GPU = **1.4 exaFLOPS (FP8) / 2.9 exaFLOPS (FP4)** = NVIDIA GB200 NVL72 직접 경쟁 |
| **★ AI 가속기 점유** | 2025 9% → **2026E 18%** → 2027E 25-30% 가능 (NVIDIA 90% → 75-80% 추정) |
| **Lisa Su 사업 전환(Turnaround)** | 12년 (2014.10~), 시총 $3B → $290B+ (100배), 서버 CPU 점유 1% → 35% (5년) |

---

# 항목 6. 구조적 트리거 모니터링

## 상방 트리거 (수혜 가속)

| 트리거 | 시점 | 영향 |
|---|---|---|
| **★ MI450 본격 출하 (Helios rack 1.4-2.9 exaFLOPS)** | 2026 H2 | AI 가속기 매출 +급증, 시총 +30%+ 가능 |
| **★ Meta 6GW + OpenAI 6GW 추가 하이퍼스케일러 확보** | 2026-2027 | NVIDIA 독점(monopoly) 깨는 스토리(narrative) 가속 |
| **AMD AI 가속기 점유 25-30% 도달** | 2027 | $30B+ AI 매출, NVIDIA 75% 위협 |
| **6세대 EPYC Meta lead 본격 출하** | 2026 H2 | server CPU 점유 30%+ 도달 |
| **Xilinx Versal AI 추론(inference) 채택 가속** | 2026-2027 | Embedded 회복 + 본 테마 enabler |
| **ROCm 생태계 성숙** | 2026-2028 | CUDA 락인(lock-in) 일부 균열 |

## 하방 트리거 (수혜 약화)

| 트리거 | 시점 | 영향 |
|---|---|---|
| **NVIDIA CUDA 생태계 영구 락인(lock-in)** | 지속 | AMD AI 가속기 점유 25%+ 도달 어려움 |
| **★ HBM4 알로케이션 SK·Samsung 부족** | 2026 H2 | MI450 양산 지연 risk (SK는 NVIDIA·Micron preferred) |
| **★ ARM 라이선시 4종 (Grace·Graviton·Cobalt·Axion) AMD EPYC 잠식** | 2027+ | x86 server 점유 +3.3%p 둔화 가능 |
| **NVIDIA Kyber Ultra (660kW/rack) 본격 출하** | 2026 H2 - 2027 | NVIDIA 통합 rack에서 AMD 배제 가속 |
| **TSMC 2nm 양산 지연** | 2026 H2 | MI450 일정 지연 risk |
| **PER 45x 밸류에이션 압축(multiple compression)** | 2026 H2 | macro / AI capex 둔화 시 |
| **Meta·OpenAI deal terms 변경** | 2027+ | 대형 계약(mega deal) 실적 unwind risk |

## 모니터링 캘린더

| 시점 | 이벤트 |
|---|---|
| 분기 어닝콜 (Q1-Q4, 1·4·7·10월) | DC·Instinct GPU 매출 가이던스 |
| AMD Advancing AI (연 1회, 12월) | 신제품 발표 (MI 시리즈) |
| Computex (5-6월) | client·embedded 신제품 |
| CES (1월) | Ryzen 신제품 |
| Hot Chips (8월) | 차세대 CPU·GPU 아키텍처 |
| ISC / SC (5월·11월) | HPC·AI 가속기 채택 |
| MLPerf 벤치마크 | NVIDIA vs AMD 성능 비교 |
| OpenAI·Meta capex 발표 | 대형 계약(mega deal) 진행 상황 |

---

# 종합 판단

## 매트릭스 평가

| 차원 | 평가 | 근거 |
|---|---|---|
| 상위 트렌드 적합성 | ★★★ 최상위 | 본 테마 segment 6개 중 5개에서 직접 수혜 |
| 산업 위치 | ★★★ 강 | x86 server #2 (가속 +), AI 가속기 #2 (NVIDIA 대안), FPGA #1 |
| 해자 강도 (Moat) | ★★★ 3.8/5.0 | 인텔 2.8 < AMD 3.8 < ARM 4.1·메모리 4.0+ |
| 재무 건전성 | ★★★ 강 | OPM 25%+ Non-GAAP, FCF record, 12년 CAGR +18.5% |
| 성장 가시성 (2~3년) | ★★★ 최상위 | DC +57% YoY / FY26 +45% 추정 / Meta·OpenAI 12GW deal |
| **밸류에이션 risk** | **★★ PER 45x** | NVIDIA 프리미엄 격차, 단 NVIDIA 50x 대비 약간 낮음 |

## 핵심 투자 포인트 3

1. **★ Meta + OpenAI 12GW MI450 대형 계약(mega deal) — NVIDIA 독점(monopoly) 깨는 스토리(narrative) 정점** — Meta 6GW + OpenAI 6GW = 합 12GW MI450 (CDNA 5, TSMC 2nm, HBM4 432GB). OpenAI에 **160M 주 warrant ($0.01 strike, 10% 지분)** 발행 = 양사 align 강화. Helios rack 1.4-2.9 exaFLOPS = NVIDIA GB200 NVL72 직접 경쟁. **2026-2028 ramp, AMD AI 매출 $20B+ 추가**.
2. **★ Lisa Su CEO 12년 사업 전환(Turnaround) 트랙 record + 사이클 정점 3차** — 시총 $3B (2014.10) → $290B+ (2026-Q1) = **100배** 폭등. 서버 CPU 점유 1% → 35% (5년). 12년 매출 CAGR +18.5%. **인텔 (2025-03 Lip-Bu Tan 사업 전환(Turnaround) 시작) 대비 12년 앞선 사이클**. FY25 매출 $34.64B (+34%) / 정점 3차 진입.
3. **x86 server CPU 점유 가속 + FPGA Xilinx 글로벌 #1** — EPYC 5/6세대 Meta·AWS·Google·Azure·Tencent 채택, Q1 2026 IDC 점유 +3.3%p YoY. FPGA Xilinx 글로벌 #1 (인텔 Altera 51% 분사 이후 더 단독). Adaptive Computing 본 테마 enabler.

## 핵심 리스크 3

1. **NVIDIA CUDA 생태계 절대 락인(lock-in)** — AMD ROCm 성숙도 부족, AI 가속기 점유 18% (2026E) 도달은 가능하지만 **25-30% 이상 도달 어려움**. NVIDIA Blackwell·Rubin 압도. AMD MI450 spec 우위 (HBM4 432GB) 있지만 software 격차가 본질. **CUDA 락인(lock-in) 영구화 시 AMD AI 매출 ceiling 형성**.
2. **HBM4 알로케이션 SK·Samsung 의존 risk** — MI450 HBM4 432GB가 필수, SK·Samsung 외 공급원 없음. **SK는 NVIDIA preferred / Samsung은 AMD MI455X preferred (테마 v4 분석)**. HBM4E 양산 지연 시 MI450 본격 출하 지연 risk. Micron은 AMD HBM4 진입 없음.
3. **★ ARM 라이선시 4종 AMD EPYC도 잠식 risk** — NVIDIA Grace + AWS Graviton + MSFT Cobalt + Google Axion이 인텔뿐 아니라 AMD EPYC도 잠식 가능. **ARM 17.7% 점유 가속 + AWS Graviton 5 (192-core) + NVIDIA Kyber Ultra 출하** 시 AMD x86 server 점유 +3.3%p 둔화 가능.

---

## 부록: 변경 이력 (Changelog)

### v1 (2026-06-02) — 1차 작성
- 산업 기초 + 테마 v4 + AMD_기업개요 v4.9 자동 참조
- **★ Q1 2026 실적 (2026-05-05)**: 매출 $10.31B (+38%) / DC $5.8B (+57%, Instinct $4.2B) / Non-GAAP EPS $1.37 / 주가 +18% 반영
- **★ Meta 6GW MI450 + 6th Gen EPYC deal (2026-Q1)** 신규 반영
- **★ OpenAI 6GW MI450 deal (2025-10) + 160M 주 warrant ($0.01)** 신규 반영
- **★ MI450 spec (CDNA 5, TSMC 2nm, HBM4 432GB, 19.6 TB/s, 40 PFLOPS FP4)** 반영
- **★ Helios rack (72 MI450 = 1.4-2.9 exaFLOPS)** vs NVIDIA GB200 NVL72 비교
- **★ AI 가속기 점유 9% → 18% (2026E)** — NVIDIA 90% 압박
- 메모리 3사·인텔·ARM과 비교 — Moat 3.8 (인텔 2.8 < AMD 3.8 < ARM 4.1·메모리 4.0+)
- frame: NVIDIA 독점(monopoly) 깨는 스토리(narrative) 유일 종목 + Lisa Su 12년 사업 전환(Turnaround) 100배 성공

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
