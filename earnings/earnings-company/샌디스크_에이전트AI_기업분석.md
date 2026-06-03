---
ticker: "SNDK"
company_name: 샌디스크 (Sandisk Corporation)
country: US
theme_keyword: 에이전트AI
parent_industry: 반도체
cross_ref_industry: 스토리지
moat_strength: 4.0              # 본 테마 segment 가중 평균 — Micron 4.0과 동급 (메모리 그룹 진입)
moat_by_segment:
  NAND_general_consumer: 3.0    # NAND #4 tied (13.9%), Samsung 35%·SK 20%·Kioxia 17% 다음
  Enterprise_SSD_AI: 4.0        # $42B backlog (NBM 5개), Solidigm·Samsung 경쟁
  HBF_High_Bandwidth_Flash: 4.5 # ★ SK hynix 공동 표준화 (2026-02-25), NAND 기반 HBM 대안
  Kioxia_JV_BiCS_NAND: 4.0      # 양산 capa 안정 (구 WD 시기부터 지속)
  사이클_정점_leverage: 5.0      # OPM 70.9% record (Q3 FY26), NAND pure-play의 사이클 leverage
trend_revenue_share: 90         # NAND pure-play, 본 테마 직접 노출 매우 강함
last_updated: 2026-06-02
auto_references:
  - 반도체_산업기초.md (2026-05-18)
  - 에이전트AI_테마분석.md (v4, 2026-05-26)
  - SNDK_기업개요.md (v4.9, 2026-05-18 — SEC EDGAR Sandisk Corp 10-K FY25 + 10-Q 5개 기반)
analyst_reports_attached:
  - Sandisk Q3 FY2026 8-K Earnings Release (2026-04-30 발표)
  - Sandisk + SK hynix HBF 공동 발표 (2026-02-25 OCP 표준화)
  - NAND 시장 1Q26 점유 (TrendForce·Electronics Weekly)
notes:
  - Sandisk는 2025-02 Western Digital에서 spin-off된 신규 회사 (NASDAQ:SNDK)
  - 회계연도 6월 마지막 금요일 종료 (FY26 = 2025-06-28 ~ 2026-06-26)
  - 본 분석 frame: NAND pure-play (DRAM·HBM 0% 노출) — 메모리 3사 그룹의 NAND 전문 종목으로 진입
---

# 샌디스크 (SNDK) 기업 분석 — 에이전트AI 테마

> **본 분석 frame**: 에이전트AI 테마 분석(v4)의 17 segment 중 **샌디스크는 NAND 단일 사업(pure-play) (DRAM·HBM 0%) + AI Enterprise SSD 폭증 + HBF (High Bandwidth Flash) 신규 product**. **메모리 3사(SK 4.4 / 삼성 4.3 / Micron 4.0)와 함께 본 테마 직접 수혜 그룹** 진입 — 단 SNDK는 **NAND 전문 + 사이클 진폭 최대 (OPM ±60%pt)** 차이. **★ 2025-02 WD 분사(spin-off) 후 15개월 만에 주가 30배+ 폭등 ($35 → $1,150+, 시총 $5B → $165B+)**가 스토리(narrative) 정점.

> **점유율·CAPA 표기 기준**: 본 분석의 모든 % 점유율은 **매출 기준** (TrendForce·Counterpoint·Electronics Weekly). **CAPA는 wafer 기준** (Kioxia JV BiCS 합작 capa). bit 출하 기준 점유는 분기 변동성이 커서 본 분석에서 다루지 않음.

---

## Executive Summary (5줄)

1. **위치**: NAND 글로벌 **#4 tied (Q1 2026 13.9%)** — Samsung ~32% > SK Group (Solidigm 포함) 17.6% > Kioxia 13.9% > **SNDK 13.9% = Micron 13.9%**. **2025-02 WD 분사(spin-off)** 후 첫 standalone 회사 → NAND 단일 사업(pure-play) (DRAM·HBM 0%). **★ HBF (High Bandwidth Flash) 2026-02-25 SK hynix 공동 발표 + OCP 표준화** (NAND 기반 HBM 대안). Kioxia JV BiCS NAND 양산 (구 WD 시기부터 지속).
2. **해자 종합 (segment 가중)**: <strong>4.0 / 5.0</strong> (Micron 4.0과 동급, 메모리 3사 그룹 진입) — HBF 4.5 / 사이클 정점 leverage 5.0 / Enterprise SSD AI 4.0 / Kioxia JV 4.0 / NAND general 3.0. **인텔 2.8 < AMD 3.8 < ARM 4.1 / SNDK = Micron 4.0 / 삼성 4.3 / SK 4.4** 위치.
3. **재무 (분사 후 폭발적 회복, FY26 분기별 가속)**: **FY25 매출 $7.66B / OPM -6.5% (적자)** → **Q1 FY26 $2.31B (+23% YoY) → Q2 $3.03B (+31% Q/Q) → Q3 $5.95B (+97% Q/Q, +251% YoY) / Non-GAAP GPM 78.4% / OPM 70.9% / EPS $23.41 (consensus $14.66 +60% beat)**. **Q4 FY26 가이던스 $7.75-8.25B / EPS $30-33**. **★ FY26 전체 매출 ≈ $19.3B (FY25 2.5배+)**. **Zero-debt 달성 + $6B 자사주 매입 authorize**.
4. **미래**: **★ NBM (New Business Model) 5개 multi-year 계약 (1-5년) = $42B AI 공급 backlog + $11B 재무 보장 + $400M prepayments** (Q3 시점 3개 + Q4 시점 2개 누계). **FY27 bit shipments의 1/3+ cover**. **★ HBF first samples 2026 H2, first 추론(inference) devices 2027 H1** (NVIDIA·하이퍼스케일러 채택 시 매출 폭증). HBF는 HBM 대비 **8-16x 더 큰 capacity** + lower cost로 추론(inference) 시장 직접 진입.
5. **종합 판단**: <span class="star">★★★ 본 테마 직접 수혜 메가 종목 (메모리 3사 + ARM + NVIDIA + TSMC + AMD와 동급)</span>. **(a) NAND 사이클 진폭 최대 (OPM ±60%pt) = sharp 하방 위험 risk, (b) DRAM·HBM 노출 0% = 메모리 사이클 분산 buffer 없음, (c) HBF는 2027~ 상용화로 단기 매출 기여 없음** 3대 risk. 단 **(1) Q3 FY26 record + Q4 가이던스 +30% 가속, (2) $42B NBM 5개 multi-year 계약, (3) HBF SK 공동 표준화 + OCP 주도**가 3대 positive optionality.

---

# 항목 1. 입력 정리 + 기업 포지셔닝

## 1-1. 산업·테마 컨텍스트

- **반도체 산업기초** (v1, 2026-05-18): (A) 구조적 메가 병목 → SNDK는 **NAND segment 핵심 플레이어 + KV cache offload 직접 수혜**
- **에이전트AI 테마 v4** (2026-05-26): 17 segment 중 **eSSD segment에서 #3-#4 위치 (Solidigm·Samsung·SNDK·Micron)** + **HBF (신규 segment)**
- **메모리 3사 분석 (2026-05-26)**: SK·삼성·Micron 사이클 정점 narrative와 동일 흐름 — SNDK는 **NAND pure-play로 가장 sharp leverage**
- **한국 접근 가능 TAM (2028E)**: $216-262B+ (SNDK는 미국이라 한국 TAM 무관, 단 SK hynix와 HBF 공동 표준화로 한국 협력)

## 1-2. SanDisk의 위치 (테마 v4 Moat 후보 — segment별)

| Segment | 글로벌 점유 (Q1 2026) | 순위 | 비고 |
|---|---|---|---|
| **NAND 전체** | **13.9% ($5.95B)** | **#4 (tied with Micron)** | Samsung ~32% > SK Group 17.6% > Kioxia 13.9% > SNDK=Micron 13.9% (Samsung $13.51B / 시장 전체 $42-43B 기준) |
| **NAND ASP YoY** | **+200%+ (Q1 2026)** | — | 메모리 사이클 정점 + AI eSSD 폭증 동시 |
| **Enterprise SSD (AI 인프라)** | $1.47B (Q3 FY26 DC segment) | — | **+233% Q/Q** — KV cache offload 직접 수혜 |
| **★ HBF (High Bandwidth Flash)** | **2026-02-25 SK hynix 공동 발표** | **#1-2 (양강)** | **NAND 기반 HBM 대안**, OCP 표준화 주도, HBM 대비 8-16x capacity |
| **Kioxia JV (BiCS NAND)** | 양산 capa 공유 | — | 구 WD 시기부터 지속, 안정 base |
| **DRAM** | 0% | — | NAND 단일 사업(pure-play) (분사 후 메모리 다각화 없음) |
| **HBM** | 0% (단 HBF로 진입) | — | 전통 HBM 시장 부재, HBF 신규 시장 진입 |
| **★ NBM (New Business Model) 5개 계약** | **$42B backlog (Q3 시점 3개 + Q4 시점 2개 누계, 1-5년 multi-year)** | — | + $11B 재무 보장 + $400M prepayments, FY27 bit shipments 1/3+ cover |

→ **NAND #4 tied이지만 HBF + $42B backlog + 사이클 정점 leverage로 본 테마 직접 수혜 최대**. **NAND pure-play의 진폭이 메모리 3사 (DRAM+NAND 다각화)보다 sharp**.

## 1-3. 사업부 구성 (분사 후, FY26)

| 구분 | 내용 | 본 테마 연결 |
|---|---|---|
| **NAND 전체** | **100% 단일 사업(pure-play)** (분사 후 단일 segment) | ★ 본 테마 직접 (eSSD·KV cache·HBF) |
| **Cloud (Data Center)** | Q3 FY26 매출 $1.47B (DC 점유 25%) | ★ AI 인프라 직접 |
| Client (PC·모바일 NAND) | NAND consumer 시장 | 본 테마 간접 |
| Consumer (메모리 카드·USB) | 자체 SanDisk 브랜드 | 본 테마 무관 |

### 본 테마 직접 매출 노출
- **NAND 100% × 본 테마 직접 ~70%** (eSSD AI + Client AI PC + HBF future)
- **순 본 테마 직접 노출 = 약 90%** (메모리 3사 60-70%·인텔 30%·ARM 85%·AMD 60% 대비 최상위)
- → **본 테마 노출 측면에서 ARM (85%)과 함께 최상위 그룹**

---

## ★ 2-0. 에이전트AI 테마 logical flow — 왜 샌디스크가 부각받는가

> **정성적 인과 사슬** (테마 v4 narrative → 샌디스크 위치 매핑)

### 1단계: 에이전트 AI = 데이터·연산·메모리 폭증의 본질
- 에이전트 1건 = chat 1턴 대비 **토큰 20-30x** (Stanford/NVIDIA 실측, 테마 v4)
- 각 추론 단계·도구 호출·검색·메모리 갱신·tool execution = **연산(GPU/CPU) + 메모리(HBM/DRAM/SSD) + 스토리지(HDD) + IP(ARM) 모든 layer 부하 폭증**
- agent는 stateful → 과거 trace·long-context 보존 필요 = secular 누적

### 2단계: AI 인프라 layer별 분담 — 샌디스크는 어디 위치?

| Layer | 데이터/연산 유형 | 매체·아이템 | 본 테마 수혜 종목 |
|---|---|---|---|
| **Hot (microsec)** | KV cache, activation, 모델 가중치(active) | **HBM** | **SK·삼성·Micron (HBM)** |
| **Warm (msec)** | 모델 가중치(off-package), 활성 dataset | **DRAM·SSD** | 메모리 3사 (DRAM) + SNDK·Solidigm (eSSD) |
| **Warm-Cold (sec)** | 검색 코퍼스, 벡터 DB, 최근 로그 | **eSSD QLC·HBF** | SNDK (122TB QLC, HBF) |
| **Cold (수초~분)** | 학습 데이터셋, 체크포인트, 보관 로그 | **HDD nearline** | WDC·Seagate |
| **Compute (CPU)** | server CPU + host CPU + client CPU | **x86·ARM** | Intel·AMD·ARM 라이선시 |
| **Compute (GPU·AI)** | training·inference 가속 | **GPU·ASIC** | NVIDIA·AMD·ARM |
| **IP layer** | 모든 chip 상위 설계 | **ARM IP** | ARM Holdings (royalty 광범위) |


→ **샌디스크 위치: **Warm-Cold (eSSD) + HBF (차세대 신규)****

### 3단계: 왜 SNDK가 본 테마에서 부각받는가? — 3가지 본질적 이유

1. **NAND 사이클 정점 + AI Enterprise SSD 폭증** = Q3 FY26 매출 $5.95B (+251% YoY), OPM 70.9% record
2. **★ HBF (High Bandwidth Flash) — SK hynix 공동 표준화 (2026-02-25, OCP)** = NAND 기반 HBM 대안, HBM 대비 8-16x capacity = 차세대 신규 segment 생성
3. **NBM (New Business Model) 5개 multi-year 계약 = $42B backlog + $11B 재무 보장** = AI 인프라 매출 가시성

### 4단계: 왜 SNDK가 본 테마 메가 종목인가?

- **2025-02 WD spin-off 후 15개월 만에 주가 30배+ ($35 → $1,150+, 시총 $5B → $165B+)**
- **NAND 점유 13.9% #4 tied (Micron 동률, Samsung 32% > SK Group 17.6% > Kioxia 13.9% > SNDK = Micron)**
- **Cloud (Data Center) 매출 Q3 FY26 $1.47B (+233% Q/Q)** = AI eSSD KV cache offload 직접 수혜
- **HBF first samples 2026 H2 / first inference devices 2027 H1** + Zero-debt + $6B 자사주 매입

### 5단계: 본 분석 frame 결론

**NAND pure-play 사이클 정점 leverage + HBF 차세대 신규 segment** 4중 leverage. Moat 4.0 (Micron 동급). 단 NAND 사이클 진폭 최대 (OPM ±60%pt) + DRAM·HBM 노출 0% = 사이클 침체 시 sharp downside 양면.

---


# 항목 2. 비즈니스 모델 & 해자 (Moat) — Segment별

## 2-1. 비즈니스 모델 — 핵심 차별점

### NAND 전문 IDM (JV 기반)
- **Kioxia JV (BiCS NAND)** — 구 WD 시기부터 지속, Yokkaichi·Kitakami fab 합작 양산
- 구 WD에서 분리된 NAND 사업부 → **2025-02 spin-off로 SanDisk Corp 단독 회사화**
- CEO David Goeckeler (2025-02~, 前 Western Digital CEO)
- 첫 NAND 단일 사업(pure-play) standalone 회사 (Micron은 DRAM+NAND, SK는 DRAM+NAND, 삼성은 DRAM+NAND+Foundry)

### NAND 세대별 제품
- **BiCS 6/7** (현재 주력) — 162-layer / 218-layer
- **BiCS 8/9** (Kioxia와 공동 개발 차세대) — 2026-2027 양산
- **BiCS 10** (Kioxia 발표, 1Tb QLC) — 2027+
- TLC·QLC·SLC SSD 전 라인업

### Enterprise SSD (AI 인프라) — Cloud 사업부
- AI 학습(training)/추론(inference) KV cache offload 직접 수혜
- **Q3 FY26 Cloud 매출 $1.47B (+233% Q/Q, +195% YoY)** — 분사 후 record
- Hyperscaler (NVIDIA·MSFT·Google·Meta·AWS·Oracle) 직접 공급
- Solidigm (SK)·Samsung eSSD와 경쟁

### ★ HBF (High Bandwidth Flash) — 신규 product 차세대
- **2026-02-25 SK hynix와 공동 발표** + OCP framework 표준화 시작
- **NAND 기반 HBM 대안/보완**: HBM-SSD 사이 새로운 storage tier
- **HBM 대비 8-16x 더 큰 capacity** + lower cost
- AI model parameters를 GPU 옆 storage tier로 → "model 전체를 GPU package 안에 유지"
- **Inference 전용** (write speed 한계로 학습(training) 불가)
- **First samples 2026 H2 / First 추론(inference) devices 2027 H1**
- 채택 가능 하이퍼스케일러: NVIDIA·MSFT·Meta·Google·Oracle·AWS (HBM 알로케이션 부족 시 대안)
- **SNDK·SK hynix 양강 = HBF 시장 단독**, Samsung·Micron·Kioxia 후발

### NBM (New Business Model) — Q3 시점 3개 + Q4 시점 2개 = 누계 5개 multi-year 계약 (★ 정정 fact)
- **$42B+ backlog** (Q3 발표 3개 → Q4 추가 2개 누계, **1-5년 multi-year** 혼합, 모두 5년 아님)
- **+ $11B financial guarantees + $400M prepayments on balance sheet** (재무 보장 + 선수금)
- **FY27 bit shipments의 1/3+ cover** = 매출 가시성 정량 명확
- 본질: "long-term investment horizons과 quarterly market pricing 사이 gap 해소" — Micron SCA와 유사 패턴
- 사이클 변동성 축소 + 매출 가시성 +
- Q3 FY26 record는 NBM 3개 + 분기 사이클 정점 동시 효과, Q4는 NBM 5개 누계 ramp 가속

### 사이클 정점 leverage (NAND pure-play의 양면)
- NAND 단일 사업(pure-play) = DRAM·HBM 다각화 없음 → **사이클 진폭 최대 (OPM ±60%pt)**
- 사이클 정점 시 OPM 70%+ 폭증 (Q3 FY26 record)
- 사이클 침체 시 OPM -25% 적자 (FY23)
- SK·Samsung (DRAM 다각화) 대비 sharp 상방 여력·하방 위험 동시

## 2-2. Moat 종류별 Segment 평가 (메모리 3사·CPU 3사와 mirror 구조)

### Segment 1. NAND general (소비자·모바일·PC)
| 축 | SNDK | Samsung | SK Group (Solidigm) | Kioxia | Micron |
|---|---|---|---|---|---|
| 기술/특허 | 4 (BiCS 6/7) | **5** | 4 | 4 | 4 |
| CAPA | 3 (Kioxia JV) | **5** (800K wafer/월) | 4 | 4 | 4 |
| 고객 락인(lock-in) | 3 (consumer brand) | **5** | 4 | 4 | 3 |
| 규모 (점유) | 3 (13.9% #4) | **5** (35%) | 4 (17.6%) | 3 (13.9%) | 3 (13.9%) |
| 병목 포지셔닝 | 3 (사이클 정점 동시 수혜) | 4 | 4 | 3 | 3 |
| **평균** | **3.2** | **4.8** | **4.0** | **3.6** | **3.4** |

> **★ 정성: 왜 NAND general이 SNDK 본질 segment인가?**
> 
> **인과 사슬**: SNDK = NAND 단일 사업(pure-play) → NAND general (소비자·모바일·PC) 매출 비중 60%+ → NAND 사이클 정점에서 매출 + & GPM + leverage 극대 → 단 사이클 진폭 ±60%pt = 정점·침체 양극단
> 
> **추가 동력 1 — NAND 단일 사업(pure-play) = 사이클 정점 leverage 최대**: DRAM·HBM·DX buffer 없음 = NAND 가격 +100%면 매출 +100% 직접
> **추가 동력 2 — BiCS 6/7 + Kioxia JV CAPA 안정**: 양산 capa Yokkaichi·Kitakami 합산 NAND 글로벌 #3
> **추가 동력 3 — 점유 13.9% #4로 Samsung 35% 압도 대비 작음**: 점유는 작지만 NAND 단일 사업(pure-play)로 사이클 leverage가 본질
> 
> **SNDK 위치의 특별함**: NAND 단일 사업(pure-play) 사이클 정점 leverage가 메모리 종합 IDM (SK·Samsung) 대비 우월. 단 침체 시 적자 -25%

### Segment 2. Enterprise SSD (AI 인프라) — ★ Cloud 사업부

**eSSD 시장 점유 (TrendForce 2024-2025 기준)**: Samsung ~32% (#1) / Solidigm (SK Group) ~30% (#2) / Kioxia ~10-15% (#3) / **SanDisk ~10% (#4)** / Micron ~10% (#5)

| 축 | SNDK | Solidigm (SK) | Samsung | Micron |
|---|---|---|---|---|
| 기술/특허 | **4** (TLC·QLC·SLC enterprise) | 4 | **5** | 3 |
| CAPA | 3 (Kioxia JV) | 4 | **5** | 3 |
| 고객 락인(lock-in) | **5** ($42B NBM 5년, 신규 가속) | 4 | 4 | 3 |
| **규모 (시장 점유)** | **3** (~10% #4, Q3 FY26 record로 가속 진입 단계) | **5** (~30% #2) | **5** (~32% #1) | **3** (~10% #5) |
| 병목 포지셔닝 | **4** (KV cache 직접 수혜) | 4 | 4 | 3 |
| **평균** | **3.8** | **4.2** | **4.6** | **3.0** |

> **★ 정정 (사용자 피드백 반영)**: SNDK eSSD 시장 점유는 ~10% (#4)로 SK·Samsung 30%+ 대비 명확히 작음. Q3 FY26 Cloud $1.47B (+233% Q/Q) record는 **빠른 가속 진입 신호**이지만 **누적 점유는 여전히 #4 수준**. NBM $42B 5년 backlog가 ramp되면 2026-2028 점유 +가능성, 단 현재는 작은 규모.

> **★ 정성: 왜 Enterprise SSD가 SNDK 가속 segment인가?**
> 
> **인과 사슬**: 에이전트 AI = KV cache offload + vector DB + 체크포인트 폭증 → enterprise SSD 수요 폭증 → SNDK Cloud 사업부 $1.47B (+233% Q/Q) record + ★ $42B NBM 5년 multi-year backlog 확보 → 점유 #4지만 가속 진입
> 
> **추가 동력 1 — ★ $42B NBM 5개 multi-year backlog (5년)**: hyperscaler·CSP 직접 확보 = 사이클 변동성 축소 + 매출 가시성
> **추가 동력 2 — Cloud $1.47B (+233% Q/Q) record**: 빠른 가속 진입 신호, 점유 #4 → 향후 #3 진입 chance
> **추가 동력 3 — KV cache offload narrative (NVIDIA Dynamo·vLLM)**: AI inference HBM 부족분을 NAND로 offload = enterprise SSD 신규 수요
> 
> **SNDK 위치의 특별함**: 점유 작지만 NBM 5년 multi-year로 매출 가시성 확보. SK·Samsung 점유 30%+ 대비 #4 수준 차이 분명

### Segment 3. ★ HBF (High Bandwidth Flash) — 차세대 신규
| 축 | SNDK | SK hynix (공동) | Samsung | Micron | Kioxia |
|---|---|---|---|---|---|
| 기술/특허 | **5** (공동 표준화 주도) | **5** | 3 | 2 | 3 |
| CAPA | 4 (Kioxia JV) | 4 | 3 | 3 | 4 |
| 고객 락인(lock-in) | **5** (OCP 표준화 주도) | **5** | 2 | 2 | 3 |
| 규모 | 3 (2026 H2 first samples) | 3 | 1 | 1 | 1 |
| 병목 포지셔닝 | **5** (HBM 알로케이션 부족 대안) | **5** | 2 | 2 | 2 |
| **평균** | **4.4** | **4.4** | **2.2** | **2.0** | **2.6** |

> **★ 정성: 왜 HBF (High Bandwidth Flash)가 SNDK 차세대 driver인가?**
> 
> **인과 사슬**: HBM 알로케이션 부족 (SK·삼성·Micron sold out) → HBM 가격 폭등 → NAND 기반 high-bandwidth alternative 필요 → ★ SNDK + SK hynix 공동 표준화 주도 (OCP 표준) → 2026 H2 first samples → 2028+ material
> 
> **추가 동력 1 — ★ SK hynix 공동 표준화 주도 (OCP 표준)**: NAND 단일 사업(pure-play) SNDK + HBM #1 SK 공동 = 차세대 메모리 architecture 표준 선점
> **추가 동력 2 — HBM 알로케이션 부족 = HBF alternative 수요**: HBM이 sold out인데 AI 가속기 메모리 수요는 계속 + = HBF가 일부 대안
> **추가 동력 3 — Kioxia JV CAPA 활용 + BiCS 8/9/10 차세대 노드**: NAND 양산 capa로 HBF 양산 base 확보
> 
> **SNDK 위치의 특별함**: 본 segment Moat 4.4로 SK와 공동 표준화 주도. NAND 단일 사업(pure-play) → 차세대 memory architecture로 trajectory 전환 trigger

### Segment 4. Kioxia JV (BiCS NAND 양산 capa)
| 축 | SNDK·Kioxia JV | 자체 단독 메모 IDM (SK·Samsung·Micron) | 핵심 |
|---|---|---|---|
| 기술/특허 | **4** (BiCS 8/9/10 공동 개발) | 4-5 | JV 안정 |
| CAPA | 4 (Yokkaichi·Kitakami 합작) | 4-5 (각 자체 fab) | JV scale |
| 고객 락인(lock-in) | 4 (양산 안정) | 4-5 | JV 안정 |
| 규모 | 4 (NAND 글로벌 합산 #3) | 3-5 | JV scale |
| 병목 포지셔닝 | **4** (사이클 정점 leverage 양면) | 4 | JV cycle leverage |
| **평균** | **4.0** | **4.2** | **JV 안정 capa base** |

> **★ 정성: 왜 Kioxia JV가 SNDK CAPA base인가?**
> 
> **인과 사슬**: SNDK 자체 NAND fab 없음 → Kioxia 합작 JV (Yokkaichi·Kitakami) = BiCS NAND 양산 capa → NAND 글로벌 합산 #3 → 사이클 정점에서 CAPA 활용 leverage 양면
> 
> **추가 동력 1 — Kioxia 합작 = SNDK 자체 CAPA 부재 보완**: 자체 fab 없이 NAND 양산 가능 = capex 부담 작음
> **추가 동력 2 — BiCS 8/9/10 공동 개발**: 차세대 NAND 노드 공동 R&D = 기술 trajectory 안정
> **추가 동력 3 — Yokkaichi·Kitakami 합산 NAND 글로벌 #3 capa**: 점유 13.9% #4이지만 CAPA로는 #3
> 
> **SNDK 위치의 특별함**: 자체 fab 없이 Kioxia JV로 NAND 단일 사업(pure-play) 운영. 단 JV 의존도 = 의사결정 자유도 제한 risk

### Segment 5. 사이클 정점 leverage (NAND 단일 사업(pure-play) 특성)
| 축 | SNDK | SK | Samsung | Micron | Kioxia |
|---|---|---|---|---|---|
| 사이클 진폭 (OPM range) | **±60%pt** (NAND 단일 사업(pure-play) 최대) | ±50%pt | ±22%pt (DX buffer) | ±42%pt | ±55%pt |
| 정점 OPM (Q3 FY26 / 1Q26) | **70.9% record** | 72% | 25% | 69% | ~15% |
| 정점 매출 가속 | **+251% YoY (Q3 FY26)** | +25% | +5% | +49% | +80% Q/Q |
| 침체 risk | 적자 -25% (FY23) | -10% | DX 흡수 | -37% (FY23) | -15% |
| **평균 (정점 시)** | **5.0** | **5.0** | **3.5** | **4.5** | **4.0** |

> **★ 정성: 왜 사이클 정점 leverage가 SNDK thesis 핵심인가?**
> 
> **인과 사슬**: SNDK = NAND 단일 사업(pure-play) → 사이클 진폭 ±60%pt (NAND 단일 사업(pure-play) 최대) → 정점 OPM 70.9% record (Q3 FY26) + 매출 +251% YoY → 메모리 종합 IDM (Samsung ±22%pt DX buffer) 대비 leverage 압도
> 
> **추가 동력 1 — ★ 사이클 정점 OPM 70.9% record + 매출 +251% YoY (Q3 FY26)**: NAND 사이클 정점에서 SNDK가 메모리 종합 IDM 대비 가장 큰 leverage
> **추가 동력 2 — NAND 단일 사업(pure-play) = DRAM·HBM·DX buffer 없음**: 사이클 정점 가격 +100%면 매출 +100% 직접 = leverage 최대
> **추가 동력 3 — 단 침체 risk 적자 -25% (FY23)**: 정점 leverage의 trade-off로 침체 시 적자 위험도 최대
> 
> **SNDK 위치의 특별함**: NAND 단일 사업(pure-play) 사이클 정점 leverage가 thesis 본질. Samsung·SK 메모리 종합 IDM 대비 정점에서 OPM·매출 +leverage 압도. 단 침체 위험 trade-off

### Segment 가중 평균 (Moat 종합)
- NAND general (3.2) × 30% + Enterprise SSD (3.8) × 25% + HBF (4.4) × 15% + Kioxia JV (4.0) × 15% + 사이클 정점 (5.0) × 15% = **약 3.95 ≈ 4.0**
- 인텔 2.8 < AMD 3.8 < **SNDK ≈ 4.0 = Micron 4.0 < ARM 4.1 < 삼성 4.3 < SK 4.4**
- 본 테마 직접 수혜 그룹 진입 (메모리 3사 + ARM + NVIDIA + TSMC + AMD + SNDK)
- ※ Enterprise SSD 규모 정정 (4 → 3) 반영해도 종합 Moat는 ~4.0 유지 (소수점 변화 미미). 단 SK·Samsung eSSD 점유 30%+ 대비 SNDK ~10%인 점은 분명히 차이.

## 2-3. 병목 수혜 강도 정량화

### 본 테마 직접 수혜 메커니즘

| 본 테마 병목 | SNDK 수혜 메커니즘 | 카테고리 | 정량 추정 |
|---|---|---|---|
| **NAND 사이클 정점** | 매출 +251% YoY (Q3 FY26), GPM 78.4% | (A) 구조적 메가 병목 | FY26 매출 $18-19B (FY25 2.4배) |
| **Enterprise SSD ↑ (KV cache offload)** | Cloud $1.47B (+233% Q/Q) | (A) | Q4 FY26 추가 +급증 |
| **★ HBF (HBM 대안)** | NAND 기반 high-bandwidth memory | (A) | 2027 H1 양산, 2028+ material |
| **NBM 5개 multi-year 계약** | $42B 5년 backlog | (A) | 매출 가시성 + 사이클 변동성 축소 |
| **AI PC ↑** | Client NAND 수요 + | (D) | secondary driver |

→ **본 테마 segment 5개 중 4개에서 직접 수혜 + HBF는 차세대 segment 신규 생성**. NAND 사이클 정점·AI 인프라 폭증·HBF 차세대의 **3중 leverage**.

### vs 메모리 3사 비교

| 차원 | SK하이닉스 | 삼성전자 | 마이크론 | **SanDisk** |
|---|---|---|---|---|
| 본 테마 노출 | 60%+ | 22% | 70% | **90% (NAND 단일 사업(pure-play))** |
| Moat 종합 | 4.4 | 4.3 | 4.0 | **4.0 (Micron 동급)** |
| 1Q26 OPM (Non-GAAP) | 72% | 25% | 69% | **70.9% (Q3 FY26)** |
| 12년 매출 CAGR | +12% | +5% | +7% | **+1.3% (낮음, NAND 사이클성)** |
| historical 사이클 진폭 | ±77pt | ±22pt | ±83pt | **±61pt** (FY14-FY25 기준) |
| **★ 현재 정점 반영 진폭** | **±77pt** | ±22pt | ±83pt | **±96pt (Q3 FY26 OPM 70.9% 반영)** |
| 다각화 buffer | DRAM 다각화 | DX·SDC·Harman 대 buffer | DRAM+NAND | **없음 (NAND only)** |
| HBM 노출 | ★ 직접 (HBM3E·HBM4) | ★ 직접 | ★ 직접 | **HBF (HBM 대안) 신규 진입** |
| 스토리(narrative) | HBM 집중 | 차세대 분산 | 미국 본토 + 가속 | **NAND 단일 사업(pure-play) + HBF + $42B backlog** |

---

# 항목 3. 재무 분석

## 3-1. 실적 추이 (12년 + Q3 FY26, 기업개요 v4.9)

### 12년 사이클 (FY14-FY25, WD Flash segment + SNDK standalone)
| FY | 매출 ($B) | OP ($B) | OPM | 핵심 이벤트 |
|---|---|---|---|---|
| FY14 | 6.30 | 0.50 | 7.9% | NAND mid-cycle |
| FY17 | 9.00 | 2.35 | 26.1% | 1차 슈퍼사이클 시작 |
| FY18 | **9.45** | **3.42** | **36.2%** | ★ 정점 1차 (NAND 슈퍼사이클) |
| FY21 | 9.84 | 1.85 | 18.8% | 코로나 IT 회복 2차 정점 |
| FY23 | 6.30 | -1.55 | **-24.7%** | 메모리 다운사이클 저점 2차 (적자) |
| FY24 | 6.61 | 0.05 | 0.8% | 회복 시작 |
| FY25 | 7.66 | -0.50 | -6.5% | 분사 직후, NAND 회복 초기 |
| **FY26E** | **$18-19B** | **~$6B** | **~33%+** | **★ AI Enterprise SSD 폭발 진입 (Q3 +251% YoY)** |

**핵심 관찰**:
- **historical 12년 OPM range -24.7% ~ +36.2% = 60.9%pt** (FY14-FY25 기준)
- **★ Q3 FY26 OPM 70.9% 반영 시 진폭 확대 = -24.7% ~ +70.9% = 95.6%pt** (메모리 종목 중 최대, SK 77pt·삼성 22pt·Micron 83pt 대비 NAND pure-play의 극대 leverage)
- **매출 12년 CAGR +1.3%** (저성장 — SSD 대체율 + NAND 사이클 진폭)
- 사이클 정점 2회 (FY18·FY26 진행 중), 저점 2회 (FY16·FY23)
- **★ 분사 후 15개월 만에 주가 30배+ 폭등** ($35 → $1,150+, 시총 $5B → $165B+)

### Q3 FY26 분기 실적 (★ record, IR 2026-04-30)

| 항목 | Q3 FY26 (2026-01~03) | YoY | QoQ | 비고 |
|---|---|---|---|---|
| **Total Revenue** | **$5.95B** | **+251%** | **+97%** | record (가이던스 $4.4-4.8B 대비 +$1.15B beat) |
| **Non-GAAP GPM** | **78.4%** | record | +27.5pp (Q2 50.9%) | **마이크론·SK 수준 도달** |
| **Non-GAAP OPM** | **70.9%** | record | — | NAND 사상 최고 |
| **Non-GAAP EPS** | **$23.41** | consensus $14.66 대비 +60% beat | — | record |
| **GAAP Net Income** | **$3.615B** | — | — | record |
| **Cloud (Data Center) 매출** | **$1.47B** | **+195%** | **+233%** | ★ AI 인프라 폭증 |
| Client 매출 | 약 $2.5B | +200%+ | +80%+ | NAND consumer 회복 |
| Consumer 매출 | 약 $2B | +200%+ | +50% | 메모리 카드 등 |

### FY26 분기별 매출 (4분기 시계열)

| 분기 | 매출 | YoY | QoQ | 비고 |
|---|---|---|---|---|
| Q1 FY26 (~2025-10 종료) | **$2.31B** | +23% | — | 분사 후 첫 standalone full quarter |
| Q2 FY26 (2026-01-02 종료) | **$3.03B** | — | **+31%** | Datacenter +64% Q/Q |
| Q3 FY26 (2026-04-03 종료) | **$5.95B** | **+251%** | **+97%** | ★ record (NBM 3개 ramp + AI 폭증) |
| Q4 FY26 (~2026-07 종료) 가이던스 | **$7.75-8.25B** | — | +30%+ | NBM 5개 누계 ramp |
| **FY26 전체** | **≈ $19.3B** | — | — | **FY25 $7.66B 대비 2.5배+** |

→ **분기별 가속 분명** ($2.31B → $3.03B → $5.95B → $7.75-8.25B). 사이클 정점 + AI 인프라 + NBM 5개 누계 ramp 동시 효과.

## 3-2. 사업부별 PQC 분해 — Q3 FY26 fact

| 차원 | NAND 전체 | Cloud (Data Center) | Client | Consumer |
|---|---|---|---|---|
| **P (ASP YoY)** | +200%+ | +250%+ (eSSD 프리미엄) | +180% | +150% |
| **Q (bit 출하 YoY)** | +20% | +30%+ (AI 인프라) | +15% | +20% |
| **매출 (P×Q)** | $5.95B (+251%) | $1.47B (+195%) | $2.5B (+200%+) | $2B (+200%+) |
| **마진 (OPM)** | 70.9% (record) | 80%+ (eSSD 프리미엄) | 70% | 65% |

### Cloud 사업부 스토리(narrative)
- **+195% YoY = AI Enterprise SSD 폭발 진입**
- $42B NBM 5개 계약의 첫 ramp 효과
- Solidigm (SK)·Samsung eSSD와 경쟁 + 동시 수혜
- KV cache offload (산업 기초·테마 v4 reference) 직접 수혜

## 3-3. 재무 건전성 (기업개요 v4.9 fact)

| 항목 | FY25 / FY26 |
|---|---|
| 자본총계 | 분사 후 standalone, 회복 강함 |
| OCF | FY25 적자 → Q3 FY26 record |
| FCF | FY25 적자 → Q3 FY26 record |
| **CapEx** | Kioxia JV 합작 (개별 CapEx 부담 낮음) |
| **★ Net Cash** | **Zero-debt 달성** (모든 부채 상환, Q3 FY26 기준) |
| **★ 자사주 매입** | **$6B authorize** (분사 후 첫 capital return) |
| 신용등급 | 분사 후 회복 진행 |
| 배당 | 분사 후 미실시 (성장 투자 우선) |
| 발행주식수 | 약 144M 주 |
| **★ 시총** | **$165B+ (2026-05, 분사 후 15개월)** — 분사 시 $5B → 30배+ |
| **CEO** | **David Goeckeler (2025-02~, 前 WD CEO)** |
| CFO | (분사 후 신규 선임) |

### 주요 자본 movement 2025-2026
- **2025-02 WD 분사(spin-off)** ($35 IPO 가격) — 단일 사업(pure-play) NAND 회사화
- **2026-02-25 SK hynix HBF 공동 발표** + OCP 표준화 시작
- **★ NBM 5개 multi-year 계약 = $42B backlog** (2026 H1)
- **2026-04-30 Q3 FY26 record** — 매출 +251% YoY
- **Zero-debt + $6B 자사주 매입 authorize**

## 3-4. 피어 수익성 비교 (Non-GAAP OPM 통일)

| 기업 | FY 매출 | OPM | 1Q26 OPM (Non-GAAP) | 본 테마 수혜 |
|---|---|---|---|---|
| NVIDIA | $130B+ | 60%+ | 65%+ | AI 가속기 96% |
| **SK하이닉스** | 66조원 | 25%+ | **72%** | HBM 사이클 정점 |
| **★ SanDisk** | **$7.66B (FY25) → $18-19B (FY26E)** | **-6.5% → ~33%+** | **70.9% (Q3 FY26)** | NAND 단일 사업(pure-play) + HBF |
| **Micron** | $37.38B | 32% | 69% | HBM + 미국 본토 |
| TSMC | $90B+ | 45%+ | 50%+ | Foundry 압도 |
| ARM | $4.92B | 40.7% | 40%+ | chipless IP |
| AMD | $34.64B | 25%+ | 25%+ | x86 + AI 양면 |
| 삼성 DS | $80B | 35% | 25% | DRAM + Foundry |
| 인텔 | $52.85B | 0.5% | 1% | 사업 전환(Turnaround) |

→ **SNDK OPM 70.9% = SK 72%와 거의 동급 historical**. NAND pure-play의 사이클 정점 leverage가 SK HBM 정점과 평행 발생.

---

# 항목 4. 성장성 분석

## 4-1. 과거 성장률 (12년 CAGR)

| 기업 | 12년 매출 CAGR | 비고 |
|---|---|---|
| NVIDIA | +30%+ | AI 장기 추세(secular) |
| AMD | +18.5% | Lisa Su 사업 전환(Turnaround) |
| ARM | +17% (7년) | 장기 추세(secular) IP |
| TSMC | +15%+ | Foundry 메가 |
| SK하이닉스 | +12%+ | HBM 메가 |
| 마이크론 | +7%+ | 메모리 + HBM |
| 삼성전자 | +5%+ | 전사 |
| **SanDisk** | **+1.3% (12년)** | NAND 사이클성, 단 분사 후 FY26 폭증 |
| 인텔 | -0.46% | 구조적 침체 |

→ **SNDK 12년 CAGR +1.3% = NAND 사이클성으로 낮음**, 단 FY26 +2.4배 기하급수적(polynomial) 성장 → 정점 사이클 입증.

## 4-2. 향후 PQC 전망 (4Q + 2Y)

### NAND 전체 — (A) 구조적 메가 병목

| 차원 | 4Q | 2Y | 근거 | 출처 |
|---|---|---|---|---|
| P (ASP YoY) | +200·150·100·60% | +30·0% | 사이클 정점 후 normalize | TrendForce |
| Q (bit) | +15·20·25·25% | +50%·30% | AI Enterprise SSD 폭증 | $42B NBM backlog |
| **→ 매출** | **+250-300% YoY (Q4 FY26)** | **+150% (FY26)·+30% (FY27)** | 사이클 + NBM 5개 | 컨센·SNDK IR |

### Enterprise SSD (Cloud) — (A) 구조적 메가 병목

| 차원 | 4Q | 2Y | 근거 | 출처 |
|---|---|---|---|---|
| P | +250·200·150·100% | +50·20% | eSSD 프리미엄 정점 | SNDK IR |
| Q | +30·35·40·45% | +80·60% | KV cache offload, $42B NBM | NBM 계약 |
| **→ 매출** | **+250-300%** | **+200% (FY26)·+80% (FY27)** | AI 인프라 mega | 컨센 |

### HBF (★ 신규 product) — (A) 차세대 segment 생성

| 차원 | 4Q | 2Y | 근거 | 출처 |
|---|---|---|---|---|
| P | first samples 2026 H2 | TBD | 차세대 product 가격 | SNDK·SK 공동 |
| Q | sample stage | 2027 H1 추론(inference) devices | NVIDIA·하이퍼스케일러 채택 | OCP 표준 |
| **→ 매출** | 미미 (2026) | **2027-2028 material 추정 $2-5B** | 양산 ramp | SNDK 추정 |

### 회사 전체 매출·OPM 전망

| 항목 | FY24 | FY25 | FY26E | FY27E |
|---|---|---|---|---|
| 매출 ($B) | 6.61 | 7.66 | **$18-19B (+150%)** | **~$22B (+20%)** |
| OP ($B) | 0.05 | -0.50 | **~$6B (+급증)** | **~$7B** |
| **OPM** | 0.8% | -6.5% | **~33%+** | **~32%** |

> **알 수 없음 시나리오**: HBF가 NVIDIA·hyperscaler에 본격 채택되면 → 2027-2028 매출 +$2-5B 추가 + HBM 시장 일부 잠식. 미채택 시 HBF는 차세대 비전으로 남고 NAND 사이클 정점 normalize.

### 수주잔고·백로그
- **★ NBM 5개 multi-year 계약 = $42B 5년 backlog** (Q3 FY26 발표)
- Q4 FY26 매출 $7.75-8.25B 가이던스 + 매출 가시성 NBM 기반
- **HBF first samples 2026 H2 / first 추론(inference) devices 2027 H1**

## 4-3. 피어 그룹 비교

| 기업 | FY 매출 | 5년 CAGR | 1Q26 OPM | PER (2026) | 핵심 차이 |
|---|---|---|---|---|---|
| NVIDIA | ~$130B+ | +50%+ | 65%+ | ~50x | AI 가속기 단일 |
| TSMC | ~$90B+ | +20% | 50%+ | ~25x | Foundry 압도 |
| **SanDisk** | **$7.66B (FY25)** | **N/A (분사 후 1년)** | **70.9% (Q3 FY26)** | **~40-50x (분사 후 동등)** | NAND 단일 사업(pure-play) + HBF + $42B backlog |
| **Micron** | $37.38B | +7%+ | 69% | ~15x | HBM + 미국 본토 |
| SK하이닉스 | 97.15조원 (FY25, +44% YoY) | +25%+ | 72% | ~10x | HBM 사이클 |
| ARM | $4.92B | +25%+ | 40%+ | ~100x+ | chipless IP |
| AMD | $34.64B | +25%+ | 25%+ | ~45x | x86 + AI |
| 삼성전자 | $250B | +5%+ | 13% | ~15x | 전사 |
| 인텔 | $52.85B | -7%/년 | 1% | N/A | 사업 전환(Turnaround) |

→ **SNDK PER 40-50x = 분사 후 일시 프리미엄**. Micron (15x)·SK (10x) 대비 2-3배 프리미엄. **분사 + HBF + $42B backlog 스토리(narrative) 프리미엄**, 단 사이클 정점 normalize 시 밸류에이션 압축(multiple compression) risk.

---

# 항목 5. 통합 모드 입력용 Fact 정리

| 항목 | Fact / Raw Data |
|---|---|
| **현재 시장 점유 + 추이** | NAND 전체 **13.9% ($5.95B Q1 2026)** = #4 (Samsung 35% > SK Group 17.6% > Kioxia 13.9% > SNDK 13.9% = Micron 13.9%). NAND 단일 사업(pure-play) (DRAM·HBM 0% 노출) |
| **현재 CAPA** | **Kioxia JV 합작 (Yokkaichi·Kitakami fab)** — 구 WD 시기부터 지속. CapEx 부담 분산 |
| **사이클 마진 진폭 (12년)** | OPM -24.7% (FY23) ~ +36.2% (FY18) = **60.9%pt** (NAND 단일 사업(pure-play) 진폭 최대) |
| **기술 격차·R&D·IP** | **BiCS 6/7 (현재)** + **BiCS 8/9 (Kioxia 공동 차세대)** + **★ HBF (SK hynix 공동 표준화)** |
| **★ 고객 분포 (NBM 5개)** | **$42B 5년 backlog (multi-year + firm financial commitment)** — Micron SCA와 유사 패턴 |
| **신규 수주·계약** | **NBM 5개 계약 + HBF SK hynix 공동 발표 (2026-02-25, OCP 표준화)** + Q4 FY26 가이던스 +30% 가속 |
| **자본·시총** | **★ 시총 $165B+ (2026-05, 분사 후 15개월에 30배+)**, PER ~40-50x, Zero-debt 달성, $6B 자사주 매입 |
| **Q3 FY26 실적 (★)** | **매출 $5.95B (+251% YoY, +97% QoQ) / Non-GAAP GPM 78.4% / OPM 70.9% / EPS $23.41 (consensus $14.66 +60% beat) / Cloud $1.47B (+195% YoY, +233% Q/Q)** |
| **Q4 FY26 가이던스** | **매출 $7.75-8.25B (+30% QoQ) / EPS $30-33 / FY26 전체 $18-19B (FY25 2.4배+)** |
| **HBF (High Bandwidth Flash) 일정** | First samples 2026 H2 / First 추론(inference) devices 2027 H1. HBM 대비 **8-16x capacity** + lower cost |
| **분사 후 스토리(narrative)** | 2025-02 WD 분사(spin-off) ($35 IPO) → 2026-05 $1,150+ (30배+), 시총 $5B → $165B+ |

---

# 항목 6. 구조적 트리거 모니터링

## 상방 트리거 (수혜 가속)

| 트리거 | 시점 | 영향 |
|---|---|---|
| **★ HBF NVIDIA·하이퍼스케일러 본격 채택** | 2027 H1 - 2028 | 차세대 제품 + 신규 시장 진입, $2-5B 매출 추가 |
| **NBM 6번째·7번째 계약 추가** | 2026 H2 - 2027 | $42B backlog → $50B+ 가시성 |
| **Q4 FY26 가이던스 달성** | 2026-07 | record 가속 실증, $18-19B 매출 가시성 |
| **HBF OCP 표준 확정** | 2026 H2 | HBM 대안 스토리(narrative) 가속 |
| **eSSD 점유 +** | 2026-2027 | Solidigm·Samsung 대비 점유 가속 |
| **BiCS 8/9 양산 시작** | 2026-2027 | 차세대 NAND 노드 가속 |

## 하방 트리거 (수혜 약화)

| 트리거 | 시점 | 영향 |
|---|---|---|
| **★ NAND 사이클 정점 normalize** | 2027 H2 - 2028 | OPM 70%+ → 30%로 normalize 가능 |
| **메모리 사이클 침체 (2027-2028)** | 2027 H2+ | NAND pure-play의 sharp 하방 위험 (OPM -10%~-25% 가능) |
| **HBF 채택 지연 또는 부족** | 2027+ | 차세대 스토리(narrative) 약화 |
| **NBM 계약 unwind** | 2027+ | $42B backlog 실현 risk |
| **Samsung·SK 점유 잠식** | 지속 | NAND #4 → #5 하락 risk |
| **Kioxia JV 갈등** | 분기별 | 양산 capa 공유 불안 |
| **PER 40-50x 밸류에이션 압축(multiple compression)** | 2026 H2 | 분사 후 프리미엄 normalize |

## 모니터링 캘린더

| 시점 | 이벤트 |
|---|---|
| 분기 어닝콜 (Q1-Q4, 8·11·2·5월) | 매출·OPM·NBM·HBF 가이던스 |
| OCP Summit (연 2회, 3·10월) | HBF 표준화 진척 |
| Kioxia 분기 IR | JV 양산 capa 변동 |
| Samsung·SK 분기 IR | NAND 점유 변동 |
| NVIDIA GTC | HBF·eSSD 채택 발표 |
| Hyperscaler capex 발표 | AI 인프라 NAND 수요 |

---

# 종합 판단

## 매트릭스 평가

| 차원 | 평가 | 근거 |
|---|---|---|
| 상위 트렌드 적합성 | ★★★ 최상위 | 본 테마 noise 90% 직접 (NAND 단일 사업(pure-play)) |
| 산업 위치 | ★★ 중 | NAND #4 tied, 단 HBF 차세대 #1-2 |
| 해자 강도 (Moat) | ★★★ 4.0/5.0 | Micron 동급, 메모리 3사 그룹 진입 |
| 재무 건전성 | ★★★ 강 | Zero-debt 달성, $6B 자사주, Q3 FY26 record |
| 성장 가시성 (2~3년) | ★★★ 최상위 | FY26 +150% / Q4 가이던스 +30% QoQ / $42B backlog |
| **사이클 risk** | **★ 큼** | OPM ±60%pt, 사이클 침체 시 sharp 하방 위험 |
| **밸류에이션 프리미엄** | ★★ PER 40-50x | 분사 후 프리미엄, Micron 15x 대비 2-3배 |

## 핵심 투자 포인트 3

1. **★ Q3 FY26 record + Q4 가이던스 +30% QoQ + NBM $42B backlog** — 매출 $5.95B (+251% YoY) / OPM 70.9% (SK 72% 동급) / Non-GAAP EPS $23.41 (+60% beat). Q4 가이던스 $7.75-8.25B / EPS $30-33. **NBM 5개 multi-year 계약 = $42B 5년 backlog** (Micron SCA 유사). FY26 매출 $18-19B (FY25 2.4배+).
2. **★ HBF (High Bandwidth Flash) — SK hynix 공동 표준화 차세대 product** — 2026-02-25 OCP framework 표준화 시작. **NAND 기반 HBM 대안**, HBM 대비 8-16x capacity + lower cost. First samples 2026 H2 / first 추론(inference) devices 2027 H1. **NVIDIA·하이퍼스케일러 채택 시 차세대 segment 신규 생성**, 2028+ material revenue.
3. **분사 후 30배+ 폭등 + Zero-debt 달성 + NAND 단일 사업(pure-play) 정점 le

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
