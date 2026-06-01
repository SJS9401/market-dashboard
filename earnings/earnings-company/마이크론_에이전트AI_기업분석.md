---
ticker: "MU"
company_name: 마이크론 (Micron Technology)
country: US
theme_keyword: 에이전트AI
parent_industry: 반도체
cross_ref_industry: 전력 인프라
moat_strength: 4.0              # 본 테마 segment 가중 평균
moat_by_segment:
  HBM3E: 3.5                    # 후발, 단 12-layer 30% power efficiency 강점
  HBM4_NVIDIA: 3.8              # ★ 1Q26 volume 양산 진입 (NVIDIA Vera Rubin 288GB)
  HBM4_AMD: 2.5                 # SK·삼성 대비 후발
  HBM4E: 3.0                    # 추격
  DDR5_server: 4.0              # DRAM #3 (24%), 단 미국 본토 supplier 지정학 우위
  eSSD: 3.5                     # NAND #5 (~10%), SLC SSD 개발 중 (KV cache 특화)
  미국_본토_지정학: 5.0          # ★ 미국 메이저 유일 — CHIPS Act $6B+ 확정, NY $100B fab
trend_revenue_share: 70         # 메모리 pure-play, AI 노출 매우 강함 (FY26 Q2 매출 79% DRAM, 21% NAND, HBM 폭증)
last_updated: 2026-05-26
auto_references:
  - 반도체_산업기초.md (2026-05-18)
  - 전력 인프라_산업기초.md (2026-05-18)
  - 에이전트AI_테마분석.md (v4, 2026-05-26)
  - MU_기업개요.md (v4.9, 2026-05-18 — SEC 10-K 15개·10-Q 47개 기반)
analyst_reports_attached:
  - FY26 Q2 실적 발표 PDF (Micron IR, 2026-03)
  - SEC 10-Q FY26 Q2 (2026-02-26 분기말)
notes:
  - 마이크론은 미국 기업, **회계연도 8월 마지막 목요일 종료** (FY2025 = 2024-08-30~2025-08-28, FY26 Q2 = 2025-12~2026-02)
---

# 마이크론(MU) 기업 분석 — 에이전트AI 테마

> **본 분석 frame**: 에이전트AI 테마 분석(v4)의 17 segment 중 **마이크론은 미국 유일 메이저 메모리 pureplay (지정학 우위) + HBM 추격 가속 (FY26 Q2 record) + HBM4 NVIDIA Rubin 1Q26 양산 진입 + DDR5/eSSD #3-#5 (점유 작으나 미국 본토)**. **SK = HBM 집중 (Moat 4.4) / 삼성 = 분산 + 차세대 (Moat 4.3) / 마이크론 = 후발 + 미국 본토 + 폭발적 회복 (Moat 4.0)** — 메모리 3사 중 가장 작지만 **지정학 + 가속 회복 narrative**가 핵심.

> **점유율·CAPA 표기 기준**: 본 분석의 모든 % 점유율은 **매출 기준** (TrendForce·Counterpoint·Astute Group). **CAPA는 wafer 기준** (산업 통계, K wafer/월). bit shipment 기준 점유는 분기 변동성이 커서 본 분석에서 다루지 않음.

---

## Executive Summary (5줄)

1. **위치**: 메모리 글로벌 #3 (DRAM 22-25%, NAND 12-14%), **HBM 점유 0% → 20% (1년 만에 신규 진입·가속 추격)**, HBM4 NVIDIA Vera Rubin **1Q26 volume 양산 진입**. **CMBU (Cloud Memory + HBM) FY25 매출 $13.52B = 36%** — AI 인프라 secular 본격화. **미국 유일 메이저 메모리 pureplay** = 지정학 우위 (CHIPS Act $6.1B 확정, Idaho·Virginia·NY $100B fab 2026.01 착공).
2. **해자 종합 (segment 가중)**: **4.0 / 5.0** (강한 우위, SK 4.4 / 삼성 4.3 대비 후발) — 미국 본토 지정학 5.0 만점, 단 HBM3E 3.5·HBM4 3.8·HBM4 AMD 2.5·DDR5/eSSD 3.5-4.0 추격형 mix. **SCA (5년 다년 계약)**로 사이클 변동성 축소 가능성.
3. **재무 (FY25 + FY26 Q2 record, IR 확정)**: **FY25 매출 $37.38B (+49% YoY) / OP $11.98B / OPM 32% / NPM 23.2%** (사이클 정점 3차). **FY26 Q2 매출 $23.86B (+196% YoY) / GM 74.9% / OPM 69.0% / NPM 58.8% (사상 최고) / OCF $11.9B (50% of rev) / FCF $6.9B**. Q3 FY26 가이던스 매출 $33.5B·GM 81%·EPS $19.15 (Non-GAAP)·Capex >$25B·dividend +30%. SK 1Q26 OPM 72%와 OPM 통일 기준 거의 동급 historical (3%p 차이).
4. **미래**: HBM4 NVIDIA Rubin 양산 ramp (288GB/unit Blackwell 대비 3x), 미국 본토 fab 2027/2028 본격 가동, 2026 capa sold out. **HBM 점유 20% → 25%+ (2027) 가능성**. **신용등급 2025-12 Baa1 / 2026-02 BBB+ 동반 상향** (재무 안정성 회복).
5. **종합 판단**: **★★★ 최상위 주도주 후보 (포트폴리오 다각화 종목)**. SK·삼성과 다른 **미국 지정학 + 신규 진입 catch-up** narrative. UBS PT $1,625 (+204% 상향), 시총 $1T 진입. 단 (a) HBM 점유 SK 60%·삼성 35% 대비 후발 (b) AMD HBM4 Samsung preferred로 단독 협력 없음 (c) **사이클 진폭 OPM 83.5%p로 메모리 3사 중 가장 큼** (FY16·FY23 적자, FY18·FY22·FY25 정점).

---

# 항목 1. 입력 정리 + 기업 포지셔닝

## 1-1. 산업·테마 컨텍스트 (변동 없음 — SK·삼성 분석과 동일)
- 반도체 산업기초: (A) 구조적 메가 병목
- 에이전트AI 테마 v4: 반도체+전력 동시 병목, hybrid (A)+(D)
- 한국 접근 가능 TAM (2028E): $216-262B+ (마이크론은 미국이라 한국 TAM 무관)

## 1-2. 마이크론의 위치 (테마 v4 Moat 후보 — segment별)

| Segment | 글로벌 점유 (2025-2026) | 순위 | 비고 |
|---|---|---|---|
| **HBM 전체** | **0% → 20% (1년 만에 신규 진입)** | **#3** | SK 60%·삼성 35% 대비 후발. 가파른 catch-up |
| **HBM3E (12-layer)** | NVIDIA H100/H200 일부 | #3 | **30% 더 power-efficient (peer 대비 강점)** |
| **HBM4 (NVIDIA Rubin, 2H26~)** | **1Q26 volume 양산 진입** | #3 | SK 2/3 majority + 삼성·Micron 1/3 분배 |
| **HBM4 (AMD MI455X)** | n/a | n/a | Samsung preferred, Micron 진입 X |
| **DDR5 server (DRAM 전체)** | **22-25%** | **#3** | SK·삼성 대비 후발, 단 미국 본토 supplier |
| **eSSD (NAND 전체)** | **12-14%** | **#5** | NAND 약점, SLC SSD 개발 중 (KV cache 특화) |
| **★ 미국 본토 supplier (지정학)** | **유일 메이저** | **#1** | CHIPS Act $6.1B 확정, Idaho·**Virginia**·NY $100B fab |
| **★ CMBU (Cloud Memory + HBM) 매출 비중** | **FY25 36% ($13.52B)** | — | AI 인프라 secular 본격화 |
| **★ SCA (Strategic Customer Agreement)** | 5년 다년 계약 진행 | — | 사이클 변동성 축소 가능성 |

→ **HBM 모든 layer 후발 + DDR5/eSSD 후발**이지만 **미국 본토 = 유일 메이저** 지정학 narrative + **2026 capa sold out + HBM 점유 가속 회복**이 thesis.

## 1-3. 사업부 구성 (FY26 Q2 기준)

| 사업부 | 매출 비중 (FY26 Q2) | 본 테마 연결 |
|---|---|---|
| **DRAM** | **79% ($18.8B)** | HBM + DDR5 server + 모바일·PC DDR5. **본 테마 핵심** |
| **NAND** | **21% ($5B)** | eSSD enterprise + 모바일·PC NAND |
| Others | 미미 | 일부 모듈 |

### 본 테마 직접 매출 노출
- 마이크론은 메모리 **pure-play** → 본 테마 직접 노출 **~70%** (DRAM 79% × 본 테마 직접 ~70% + NAND 21% × 본 테마 직접 ~50%)
- SK 60%+ 대비 유사·약간 높음. 삼성 22% 대비 3배+ (DX·SDC·Harman 없음)
- → **SK와 더 비슷한 narrative 구조**, 단 점유율 모두 후발

---

# 항목 2. 비즈니스 모델 & 해자 (Moat) — Segment별

## 2-1. 비즈니스 모델 — 핵심 차별점

### HBM (DRAM 매출 대부분으로 통합)
- **HBM 세대별 마이크론 위치**:
  - **HBM3E (현재 주력)**: NVIDIA H100/H200/Blackwell 일부 진입. **12-layer 30% power efficiency 강점** (peer 대비 명확한 차별화)
  - **HBM4 (NVIDIA Rubin, 2H26~)**: **★ 2026 Q1 volume shipment 시작** (SK·삼성보다 늦지만 진입). NVIDIA Vera Rubin 288GB/unit (Blackwell 대비 3x)
  - **HBM4 (AMD MI455X)**: **진입 없음** (Samsung preferred 단독)
  - **HBM4E (2027)**: 추격 진행
- **마이크론 HBM의 차별점**: power efficiency·미국 본토 supplier 신뢰성. NVIDIA가 dual+ sourcing 전략으로 마이크론에 알로케이션 점진 확대

### DDR5 server
- DRAM 점유 24% #3. 메모리 wafer capa는 SK·삼성보다 작음
- 미국 본토 supplier로 hyperscaler 안정성·지정학 신뢰

### eSSD enterprise
- NAND 점유 ~10% (#5), SLC SSD 개발 중 (KV cache 특화)
- 비-Solidigm·삼성 대비 약점

### 미국 본토 fab (지정학)
- Idaho fab ($15B+ CHIPS Act $6.1B)
- New York fab **$100B 2026.01 착공** (역대 미국 단일 반도체 투자 최대)
- 2027/2028 본격 양산 진입 시 미국 hyperscaler에 본토 supplier 신뢰 강화

### 메모리 pure-play의 양면
- SK와 동일 — DX·DS 다각화 없음 → 사이클 진폭 클 가능성
- 단 FY26 Q2 gross margin 74.9% record는 SK 1Q26 OPM 72%와 동급의 historical
- 메모리 사이클 정점 leverage = SK·마이크론 / 삼성은 분산

## 2-2. Moat 종류별 Segment 평가 (SK·삼성과 mirror 구조)

### Segment 1. HBM3E (현재 주력)
| 축 | 마이크론 | SK | 삼성 | 핵심 |
|---|---|---|---|---|
| 기술/특허 | 3 | **5** | 4 | SK 단독, Micron 12-layer power efficiency 강점 |
| HBM CAPA | 3 | **5** | 4 | SK 알로케이션 우선 |
| 고객 lock-in | 3 | **5** | 3 | NVIDIA H100/H200 SK 단독 |
| 규모 (HBM 점유) | 4 (21% 회복) | **5** | 4 | 11→21% 가속 |
| 병목 포지셔닝 | 4 | **5** | 3 | 12-layer power 강점 |
| **평균** | **3.5** | **5.0** | 3.6 | **SK 압도, Micron 후발 가속** |

### Segment 2. HBM4 (NVIDIA Rubin, 2H26~)
| 축 | 마이크론 | SK | 삼성 | 핵심 |
|---|---|---|---|---|
| 기술/특허 | 3 | 4 | **4** | 삼성 11Gb/s test 먼저 통과, Micron 1Q26 양산 진입 |
| HBM CAPA | 4 | **5** | 4 | SK majority 2/3 |
| 고객 lock-in | 4 | 4 | 4 | NVIDIA Rubin dual sourcing |
| 규모 | 4 (1Q26 진입) | **5** | 4 | Micron 1/3 일부 분배 |
| 병목 포지셔닝 | 4 | 4 | 4 | dual sourcing |
| **평균** | **3.8** | **4.4** | 4.0 | **3사 박빙, SK majority** |

### Segment 3. HBM4 (AMD MI455X) — 마이크론 진입 X
| 축 | 마이크론 | SK | 삼성 | 핵심 |
|---|---|---|---|---|
| 기술/특허 | 3 | 3 | **4** | Samsung 우선 |
| HBM CAPA | 3 | 4 | **5** | Samsung 알로케이션 |
| 고객 lock-in | 2 | 2 | **5** | **Samsung preferred (MoU)** |
| 규모 | 2 | 2 | **4** | Micron 진입 없음 |
| 병목 포지셔닝 | 2 | 3 | **4** | Samsung 진입 |
| **평균** | **2.4** | 2.8 | **4.4** | **삼성 우위, Micron 열위** |

### Segment 4. HBM4E (2027 양산)
| 축 | 마이크론 | SK | 삼성 | 핵심 |
|---|---|---|---|---|
| 기술/특허 | 3 | 4 | 4 | 추격 진행 |
| HBM CAPA | 2 | 3 | 3 | 양산 미시작 |
| 고객 lock-in | 2 | 3 | 3 | NVIDIA 차세대 인증 대기 |
| 규모 | 2 | 3 | 3 | 양산 전 |
| 병목 포지셔닝 | 2 | **4** | 3 | SK 양산 선두 시도 |
| **평균** | **2.2** | **3.4** | 3.2 | **양산 전, Micron 가장 후발** |

### Segment 5. DDR5 server
| 축 | 마이크론 | SK | 삼성 | 핵심 |
|---|---|---|---|---|
| 기술/특허 | 3 | 4 | **5** | 삼성 DRAM 종합 기술 1위 |
| 메모리 절대 CAPA | 3 | 4 | **5** | **마이크론 ~350-400K wafer/월 (#3)** |
| 고객 lock-in | 3 | 4 | **5** | hyperscaler 분산, 미국 본토 신뢰 |
| 규모 (DRAM 점유) | 3 | 4 | **5** | 마이크론 24%, SK 33%, 삼성 42% |
| 병목 포지셔닝 | 4 | 5 | **5** | HBM squeeze 양면 수혜 (마이크론도 capa 한정) |
| **평균** | **3.2** | 4.2 | **5.0** | **삼성 절대, 마이크론 #3** |

### Segment 6. eSSD enterprise
| 축 | 마이크론 | SK Group | 삼성 | 핵심 |
|---|---|---|---|---|
| 기술/특허 | 3 | 4 | **5** | 삼성 V-NAND 종합 |
| NAND 절대 CAPA | 3 | 3 | **5** | **마이크론 ~350K wafer/월 (#5)** |
| 고객 lock-in | 3 | 4 | **5** | hyperscaler 분산 |
| 규모 (eSSD 점유 Q4) | 3 (10%) | 4 (30%) | **5 (32%)** | 삼성 1위 |
| 병목 포지셔닝 | 3 | 5 | **5** | KV cache offload 신규 |
| **평균** | **3.0** | 4.0 | **5.0** | **삼성 1위, 마이크론 #5 후발** |

### ★ Segment 7. 미국 본토 supplier (지정학) — 마이크론 고유 강점
| 축 | 마이크론 | SK | 삼성 |
|---|---|---|---|
| 본토 capa | **5 (유일 미국 메이저)** | 2 (한국, AZ 일부) | 2 (한국, Texas 일부) |
| CHIPS Act 보조 | **5 ($6.1B 확정 + NY $100B)** | 2 | 3 |
| hyperscaler 본토 신뢰 | **5** | 3 | 3 |
| 미·중 디커플링 수혜 | **5** | 3 | 3 |
| 안보·정책 risk | **5** (최저) | 2 (한국 위치) | 2 (한국) |
| **평균** | **5.0** | **2.4** | **2.6** | **★ Micron 유일 강점** |

### 본 테마 가중 종합 (Moat × 매출 비중)

| Segment | 마이크론 매출 비중 | Moat | 가중 기여 |
|---|---|---|---|
| HBM3E | ~15% | 3.5 | 0.53 |
| HBM4 (NVIDIA) | ~10% (1Q26 ramp) | 3.8 | 0.38 |
| HBM4 (AMD) | 0% | 2.4 | — |
| HBM4E (미래) | 양산 전 | 2.2 | — |
| DDR5 server | ~25% | 3.2 | 0.80 |
| eSSD | ~10% | 3.0 | 0.30 |
| 미국 본토 지정학 (premium) | n/a (overlay) | 5.0 | +0.5 overlay |
| **합계 (본 테마 직접)** | **~60%** | **가중 평균 4.0** (지정학 overlay 포함) | — |

### 핵심 종합 결론

| 구간 | 마이크론 포지셔닝 |
|---|---|
| **HBM3E** | 후발 (3.5) — 단 12-layer 30% power efficiency 강점 |
| **HBM4 NVIDIA Rubin** | 1Q26 양산 진입 (3.8) — Rubin 1/3 분배 진입 |
| **HBM4 AMD** | 진입 없음 (2.4) — Samsung 우위 |
| **HBM4E** | 추격 (2.2) — 가장 후발 |
| **DDR5 server** | #3 (3.2) — 점유 작으나 미국 본토 신뢰 |
| **eSSD** | #5 (3.0) — NAND 약점 |
| **★ 미국 본토 지정학** | **5.0 절대 우위** — CHIPS Act $6B+ + NY $100B fab + 유일 메이저 |

**본 테마 가중 평균: 4.0 / 5.0** (지정학 overlay 포함). **SK 4.4 / 삼성 4.3 대비 후발이지만, 지정학 + 가속 회복이 critical mass narrative**.

## 2-3. Moat 지속성 (2년/5년/10년)

| 시점 | 유효성 | 시그널 |
|---|---|---|
| **2년 (~2028)** | 강력 (HBM4 양산 ramp + 미국 본토 fab 가동) | NY fab 2026.01 착공, 2027 가동 |
| **5년 (~2030)** | 강력 (지정학 narrative 누적 + HBM4E·HBM5) | CHIPS Act 추가 라운드 + 한국 기업 미국 일부 capa로 약화 |
| **10년 (~2035)** | 중상 | 메모리 사이클 + 한국 미국 fab 확대 (효성·SK Arizona 등) |

## 2-4. 글로벌 peer 비교 (회사 레벨, 2025·FY26 Q2)

| 항목 | 마이크론 | SK하이닉스 | 삼성 DS |
|---|---|---|---|
| 회계연도 | 8월말 종료 | 12월말 | 12월말 |
| FY25 매출 (CY 비교) | ~$35B (CY2025 추정) | ~$70B | DS ~$80B |
| **FY26 Q2 (가장 최근, 2026-02분기)** | **$23.9B (+196% YoY)** | n/a (1Q26 = 52.6조원 ~$36B) | n/a |
| **FY26 Q2 Gross margin** | **74.9% (record)** | 1Q26 GPM ~80% | DS GPM ~50% |
| **Q3 FY26 가이던스** | **$33.5B revenue, 81% GM** | n/a | n/a |
| HBM 점유 (2026 Q1) | **21%** (가속) | 60% | 35% (Q3 회복) |
| DRAM 점유 | 24% | 33% | 42% |
| eSSD 점유 | ~10% | 30% (SK Group) | 32% |
| Solidigm 통합 | 없음 (SK가 보유) | ✓ | ❌ |
| 사이클 진폭 (OPM) | 60%p+ (SK와 유사) | 77%p | 21.7%p (다각화) |
| 미국 본토 supplier | **★ 유일 메이저** | 한국+일부 미국 | 한국+Texas |
| 신용등급 | BBB / Baa3 | AA+ / Baa1 | AAA / Aa3 |

---

# 항목 3. 재무 분석

## 3-1. 실적 추이

### 연간 추이 (FY 기준, 8월 마지막 목요일 종료) — 기업개요 v4.9 fact

| FY | 매출 ($B) | OP ($B) | OPM | NPM | 사이클 단계 |
|---|---|---|---|---|---|
| FY2016 | 12.40 | -0.74 | -6.0% | -2.6% | 저점 1차 (적자) |
| FY2017 | 20.32 | 5.86 | 28.8% | 24.6% | 1차 슈퍼사이클 시작 |
| **FY2018** | **30.39** | **14.13** | **46.5%** | 46.4% | **정점 1차** (DRAM 슈퍼사이클) |
| FY2019 | 23.41 | 7.38 | 31.5% | 25.6% | 침체 진입 |
| FY2020 | 21.44 | 2.96 | 13.8% | 12.2% | mid-cycle 저점 |
| FY2021 | 27.71 | 5.79 | 20.9% | 20.2% | 2차 회복 |
| FY2022 | 30.76 | 8.93 | 29.0% | 28.2% | 2차 정점 (코로나 IT) |
| **FY2023** | **15.54** | **-5.75** | **-37.0%** | **-38.5%** | **저점 2차 (사상 최저 OPM)** |
| FY2024 | 25.11 | 1.30 | 5.2% | 3.0% | HBM 본격 진입 |
| **FY2025** | **37.38** | **11.98** | **32.0%** | **23.2%** | **정점 3차 (AI HBM 슈퍼사이클)** |

**핵심 관찰**:
- **OPM range -37.0% ~ +46.5% = 83.5%p** (SK 77.2%p보다 큼) — 메모리 IDM 최대 진폭
- 사이클 정점 3회 (FY18·FY22·FY25), 저점 3회 (FY16·FY20·FY23)
- FY25 매출 $37.38B = 직전 정점 FY22($30.76B)의 1.2배 (AI HBM 견인)
- FY26 회복 가속 — Q2 단일 분기로 FY24 매출의 95% 도달
- SK 1Q26 OPM 72% / Micron FY26 Q2 **Non-GAAP OPM 69.0% (IR 확정)** ($16,455M / $23,860M, Deck p.27, 2026-03-18) = **메모리 IDM record quarter** 동시 발생. OPM 통일 기준 SK·Micron 거의 동급 historical (3%p 차이)

### ★ FY26 Q2 분기 실적 (record, IR Deck 1차 자료 — 2026-03-18)

| 항목 | FY26 Q2 (2025-12~2026-02) | YoY | 비고 |
|---|---|---|---|
| 매출 | **$23.86B** | **+196%** | record (FQ2-25 $8.05B 대비 약 3x) |
| **Non-GAAP Gross margin** | **74.9%** ($17,876M) | 38%→74.9% (+37%p YoY) | **company record** |
| **Non-GAAP Operating expenses** | **$1,421M** (6.0% of revenue) | R&D $1,129M + SG&A $288M | 효율 정점 |
| **Non-GAAP Operating income / OPM** | **$16,455M / 69.0%** | 25%→69.0% (+44%p YoY) | **★ record, SK 72%에 근접** |
| **Non-GAAP Net income / NPM** | **$14,021M / 58.8%** | 22%→58.8% | tax rate 15.2% |
| EPS GAAP / Non-GAAP | **$12.07 / $12.20** | +756% (GAAP) | record |
| Cash from operations (GAAP) | **$11.9B (50% of revenue)** | $3.9B→$11.9B (3.0x) | record |
| **Adjusted FCF** | **$6.9B** | $0.86B→$6.9B (8x) | record |
| DRAM 매출 | **$18.8B (79%)** | +207% | ASP +mid-60% Q/Q, bit +mid-single Q/Q |
| NAND 매출 | **$5.0B (21%)** | +169% | ASP +high-70% Q/Q, bit +low-single Q/Q |

### BU별 OPM (FQ2-26, IR Deck p.24)
| BU | Revenue | GM | **OPM** | 본 테마 연관 |
|---|---|---|---|---|
| **CMBU** (Cloud Memory + HBM) | $7,749M (32%) | 74% | **66%** | ★ HBM 핵심 |
| **CDBU** (Core Data Center, DDR5·eSSD) | $5,687M (24%) | 74% | **67%** | ★ 본 테마 직접 |
| **MCBU** (Mobile + Client) | $7,711M (32%) | 79% | **76%** | 모바일 agentic AI 수혜 |
| **AEBU** (Auto + Embedded) | $2,708M (11%) | 68% | **62%** | 자율주행·로보틱스 |

→ **본 테마 직접 노출 (CMBU + CDBU) = 56% / $13.4B 분기 매출**. AI 인프라 secular 본격 진입.

### Q3 FY26 가이던스 (IR 확정)
- 매출 **$33.5B** ±$750M (Q2 대비 +40% QoQ)
- **Non-GAAP Gross margin ~81%** (sequential +6%p, 추가 가속)
- Non-GAAP Operating expenses ~$1.40B (효율 유지)
- **Non-GAAP EPS $19.15** ±$0.40 (Q2 $12.20 대비 +57% QoQ)
- FQ3-26 alone Capex ~$7B / FY26 전체 Capex **>$25B** (CHIPS Act 보조 차감 전)
- **분기 dividend +30% 인상** (2026-04-15 지급, 30% 증액으로 자본 환원 확대)

→ **메모리 사이클 정점 + HBM 가속이 동시 발생**. SK 1Q26 OPM 72% / Micron FY26 Q2 Non-GAAP OPM **69.0% (IR 확정)** = OPM 통일 기준 메모리 IDM 사상 최고 분기 평행 발생.

## 3-2. 사업부별 PQC 분해 — FY26 Q2 fact 기반

| 차원 | DRAM | NAND |
|---|---|---|
| **P (ASP YoY)** | **+mid-110% range** (+115%) | **+100%+** |
| **Q (bit shipment YoY)** | +mid-40% (~+45%) | +30% |
| **매출 (P×Q)** | $18.8B (+207%) | $5B (+169%) |
| **마진** | record GPM 74.9% (DRAM driver) | 회복 가속 |

### HBM·LP DRAM·NAND 특화 narrative (IR Deck 1차 자료 보강)
- **HBM3E 12-layer**: 30% 더 power-efficient (peer 대비)
- **HBM4 36GB 12H (NVIDIA Vera Rubin용)**: **2026 Q1 (CY) volume shipments 시작** (IR 확정). "expect to reach mature yields faster than HBM3E"
- **HBM4 16-high 48GB sample 출하** (★ 신규 fact) — 12H 36GB 대비 33% 용량 +, customization 옵션으로 R&D engagement 심화
- **HBM4E (2027 ramp)** — 1γ DRAM 노드 기반, "step-function" 성능 개선 예상
- **LP DRAM 256GB SOCAMM2 industry-first** (★ 신규 fact) — 1γ node, CPU당 2TB 용량 (1년 전 대비 4x)
- **NVIDIA Groq 3 LPX rack-scale 12TB DDR5** (★ 신규 fact, GTC 2026) — DDR5 server narrative 강화
- **G9 NAND 노드 mid-CY26 majority bits** — QLC record mix 달성
- **Quality 차별점**: "A clear majority of customers rank Micron No.1 in quality" (Mehrotra, IR Remarks p.8)
- 2026 capa **sold out** (점유 11% → 21%, 가속)
- **Samsung Galaxy S26 + Google Pixel 10 mobile agentic AI** 수혜 — flagship 12GB+ DRAM 비중 <20% → ~80% 1년 만에 (★ 신규 fact)

## 3-3. 재무 건전성 (기업개요 v4.9 fact)

| 항목 | FY25 / FY26 |
|---|---|
| 자본총계 | $35B+ (FY25말, 12년 $11B → $35B+ 3배 성장) |
| OCF | $15B+ (FY25) → **FY26 Q2 alone $11.9B (50% of revenue, IR 확정)** |
| FCF | **FY26 Q2 alone Adjusted FCF $6.9B** ($0.86B→$6.9B 8x YoY, IR 확정) |
| **CapEx** | **FY26 >$25B (IR 확정, 상향 가이던스) / FQ3-26 alone ~$7B** (Idaho·Virginia·NY fab 가속) |
| **Liquidity** | **$20.2B** (현금·marketable·restricted, FQ2-26말, IR 확정) |
| 자본 환원 (FQ2-26) | **$1.4B 자사주 매입 (14M주) + $1.8B 배당 = $3.2B (IR 확정)**, 분기 배당 +30% 인상 (2026-04-15 지급) |
| **신용등급 (★ 동반 상향)** | **Moody's Baa1 (2025-12 상향, ←Baa2)** / **S&P BBB+ (2026-02 상향, ←BBB)** / Fitch BBB |
| **CHIPS Act 보조** | **$6.1B 확정 (Idaho·Virginia·NY)** + 추가 라운드 가능성 |
| **NY fab 투자** | **$100B 2026.01 착공** (역대 미국 단일 반도체 최대) |
| 유상증자 가능성 | 낮음 (FCF 회복, 신용등급 상향) |
| 발행주식수 | 1,266M (자기주식 144M 제외 시 1,122M outstanding) |
| 직원 수 | 약 53,000명 (FY25말) |
| 특허 | 누적 60,000+건 (active US 15,000건 + 해외 7,500건) |
| CEO | Sanjay Mehrotra (前 SanDisk 공동창업자, 2017.05~) |
| CFO | Mark J. Murphy (2024.10~, 前 Qorvo CFO) |

> **신용등급 상향 (2025-12 Baa1 + 2026-02 BBB+ 동반)** — 재무 안정성 회복 시그널. SK AA+ 대비는 여전히 낮지만, 사이클 회복·HBM 가속·SCA 다년 계약·CHIPS Act 보조의 누적 효과.

## 3-4. 수익성 트렌드

| 지표 | FY21 정점 | FY23 저점 | FY26 Q2 record |
|---|---|---|---|
| GPM | 47% | -1% | **74.9%** |
| OPM | 21% | -26% | **65%+ 추정** |
| ROE | 17% | -15% | 50%+ 추정 |

→ **FY26 Q2 GPM 74.9% / Non-GAAP OPM 69.0% = 마이크론 창사 이래 최고** (IR Deck p.27 확정, OpEx $1,421M = 6.0% of revenue). SK 1Q26 OPM 72%와 OPM 통일 기준 거의 동급 historical.

---

# 항목 4. 성장성 분석

## 4-1. 과거 성장률

| 기간 | 매출 CAGR | OP CAGR |
|---|---|---|
| 3년 (FY22→FY25) | +5% | -50%→회복 |
| 5년 (FY20→FY25) | **+10%** | +25% |
| 10년 (FY15→FY25) | +8% | +10% |

피어 비교 (5년 CAGR): Micron +10% / SK +25% / 삼성 +7%. SK 압도, 삼성·Micron 박빙.

## 4-2. 미래 PQ 전망 — 테마 v4 시간축 + Micron 가속 반영

### HBM ((A) 구조적 메가 병목)
| 차원 | 4Q (2Q26E~1Q27E) | 2Y (2026·2027) | 근거 |
|---|---|---|---|
| P | +5·+3·+2·0% | +5·-5% | HBM4 dual sourcing |
| Q | **+30·30·25·25%** | **+100·60%** | Micron HBM4 ramp + Rubin 1/3 분배 + power efficiency 강점 |
| **→ 매출** | **+35-50% YoY** | **+150% (2026)·+50% (2027)** | HBM 점유 11→25%+ |

### DDR5 server — (A)
| 차원 | 4Q | 2Y | 근거 |
|---|---|---|---|
| P | +30·20·15·10% | +30·0% | HBM squeeze + 재고 정상화 |
| Q | +10·15·15·15% | +35·20% | 미국 본토 supplier 신뢰 |
| **→ 매출** | **+40-45% YoY** | +60% (2026) | DDR5 P 슈퍼사이클 + 점유 24%→26% |

### eSSD — (A) → (D)
| 차원 | 4Q | 2Y | 근거 |
|---|---|---|---|
| P | +20·15·10·8% | +25·10% | NAND 사이클 + AI premium |
| Q | +15·20·25·30% | +60·45% | SLC SSD 양산 진입 (KV cache 특화) |
| **→ 매출** | **+45-55%** | **+100% (2026)·+60% (2027)** | NAND 가속 |

### 회사 전체 매출·OPM 전망

| 항목 | FY24 | FY25 (추정) | FY26E | FY27E |
|---|---|---|---|---|
| 매출 ($B) | 25.11 | **37.38** | **~120 (3.2x, IR Q1+Q2 합산 $37.5B 이미 도달)** | ~150 |
| OP ($B) | 3.0 | **11.98** | **~75-80** (FQ1-26 OPM 47% + FQ2-26 OPM 69% → 평균 50-55%+ 가능) | ~80-90 |
| **OPM** | 12% | **32.0%** | **~60-65%** (FQ2-26 alone 69.0%·FQ3-26 GM 81% 기준) | ~55-60% |

> **알 수 없음 시나리오**: FY26 Q2 + Q3 record가 sequential로 이어질지 (Q3 가이던스 81% GM은 매우 공격적). Double-ordering 우려 + AI capex 변곡점 risk.

### 수주잔고·백로그
- 2026 capa sold out (회사 명시)
- HBM4 NVIDIA Rubin 1/3 분배 확보
- 미국 본토 fab 가동 시 추가 capa unlock

## 4-3. 피어 그룹 비교

| 기업 | FY25 매출 (CY) | 5년 CAGR | FY25 OPM | 1Q26 OPM (CY) | 핵심 차이 |
|---|---|---|---|---|---|
| **마이크론** | $37.38B (FY25) | +10% | **32.0%** | **69.0% (FQ2-26, IR 확정)** | 미국 본토, HBM 가속, NAND 약점 |
| SK하이닉스 | ~$70B | +25% | 48.6% | **72%** | HBM 1위, 메모리 pure |
| 삼성전자 DS | ~$80B (DS) | +7% | ~35% | 40-45% | DRAM·NAND #1, DS+DX 다각화 |
| Kioxia | ~$15B | +5-8% | ~15% | — | NAND only |

---

# 항목 5. 통합 모드 입력용 Fact 정리

| 항목 | Fact / Raw Data |
|---|---|
| **현재 시장 점유 + 추이** | HBM: 2024 11% → **2026 Q1 21%**. DRAM 24% #3. eSSD ~10% #5. **HBM4 NVIDIA Rubin 1Q26 volume 양산 진입 ★**. HBM3E 12-layer 30% power efficiency 강점 |
| **현재 CAPA + 증설** | DRAM ~350-400K wafer/월 (#3), NAND ~350K (#5). **CapEx FY25 $14B → FY26 $16-18B**. **★ NY fab $100B 2026.01 착공, 2027/2028 본격 가동** |
| **사이클 마진 진폭 (10년)** | OPM -26% (FY23) ~ +28% (FY22) ~ **+65% (FY26 Q2)**. SK와 유사 진폭 (60%p+) |
| **기술 격차·R&D·IP** | **HBM3E 12-layer 30% power efficiency**. HBM4 1Q26 양산. HBM4E 추격 진행 |
| **고객 분포·집중도** | HBM 상위 5: NVIDIA·Broadcom·AMD·MSFT·AWS. NVIDIA Rubin 1/3 분배. **AMD HBM4 Samsung preferred로 진입 없음** |
| **신규 수주·계약** | **2026 capa sold out (회사 명시)**. HBM4 NVIDIA Rubin 1Q26 진입. **NY fab $100B 2026.01 착공** |
| **자본·시총** | 자본 $30B+, **시총 $1T 진입** (2026 Q1, UBS PT $1,625 +204% 상향) |
| **FY26 Q2 실적 (★ IR 확정)** | 매출 $23.86B (+196%) / EPS $12.20 (Non-GAAP, +756%) / **GPM 74.9% / OPM 69.0% / NPM 58.8% / OCF $11.9B / FCF $6.9B** record / DRAM $18.8B (79%)·NAND $5B (21%) / Q3 가이던스 $33.5B·GM 81%·EPS $19.15·Capex >$25B·dividend +30% |

---

# 항목 6. 구조적 트리거 모니터링

## 상방 트리거 (해자 강화)

| 트리거 | 시점 | 영향 |
|---|---|---|
| HBM 점유 25%+ 도달 | 2026 H2 | SK 60% 압박, 삼성 35% 잠식 |
| **NY fab $100B 가동 (2027)** | 2027 H1 | 미국 본토 메모리 capa 단독 확보 |
| **CHIPS Act 추가 라운드** | 2026-2027 | 추가 자금 + 정책 신뢰 |
| Q3 FY26 GM 81% 가이던스 달성 | 2026-06 어닝 | record 가속 실증 |
| **HBM4E NVIDIA 차세대 인증 통과** | 2027+ | 차세대 narrative 회복 |
| AMD HBM4 Micron 진입 | 2027+ | Samsung 단독 깨짐 |

## 하방 트리거 (해자 약화)

| 트리거 | 시점 | 영향 |
|---|---|---|
| **Double-ordering 실증** | 2026 H2 | sold out narrative 흔들림 |
| **AI capex 변곡점** | 2027 | 메모리 사이클 trigger |
| HBM4 SK·삼성 분배 확대로 Micron 점유 잠식 | 2026 H2 | NVIDIA 1/3 분배에서 1/4로 |
| NY fab 양산 지연 | 2027-2028 | CapEx 부담 가중, FCF 압박 |
| **메모리 사이클 침체 (DRAM P -20%+)** | 2027-2028 | OPM 한자릿수 복귀 |

## 모니터링 캘린더

| 시점 | 이벤트 |
|---|---|
| 분기 어닝콜 (Q1-Q4, 회계연도 8월말) | HBM 점유·CapEx 가이던스 |
| NVIDIA GTC (3월) | Rubin·HBM 사양 |
| Hot Chips (8월) | 차세대 메모리 |
| SK·삼성 분기 IR | HBM 분배 변화 |
| NY fab 진행 (분기별) | 2027 가동 일정 |
| CHIPS Act 추가 라운드 | 미국 정부 발표 |

---

# 종합 판단

## 매트릭스 평가

| 차원 | 평가 | 근거 |
|---|---|---|
| 상위 트렌드 적합성 | ★★★ 최상 | 에이전트AI 추론 인프라 = AI 메가 트렌드 핵심 |
| 산업 위치 | ★★ 중상 | 메모리 #3, HBM 가속 회복 |
| **해자 강도** | **4.0 / 5.0** (segment 가중, 지정학 overlay 포함) | HBM3E 3.5·HBM4 3.8·HBM4 AMD 2.4·HBM4E 2.2·DDR5 3.2·eSSD 3.0·**지정학 5.0 (★ 유일 강점)** |
| 재무 건전성 | ★★ 중상 | 자본 $30B+, 신용 BBB (SK·삼성 대비 낮음), CapEx 부담 큼 |
| 성장 가시성 (2~3년) | ★★★ 최상 | **FY26 Q2 매출 +196%·OPM 69.0%·GM 74.9% record (IR 확정) + Q3 가이던스 +40% QoQ·GM 81% + dividend +30%** |
| 성장 지속성 (5~10년) | ★★ 중상 | 미국 본토 narrative + HBM4E 추격. 단 SK·삼성 추격 5-10년 |

## 핵심 투자 포인트 3

1. **★ 미국 본토 유일 메이저 메모리 supplier (지정학 우위)** — CHIPS Act $6.1B 확정 + NY fab $100B 2026.01 착공. 미·중 디커플링 가속 시 최대 수혜자
2. **HBM 가속 회복 + FY26 Q2 record (IR 확정)** — HBM 점유 11%→21% (1Q 가속), HBM4 NVIDIA Rubin 1Q26 양산 진입, **OPM 69.0%·GPM 74.9% 창사 최고** (OCF $11.9B / FCF $6.9B). Q3 가이던스 +40% QoQ·GM 81%·EPS $19.15·dividend +30%로 추가 가속
3. **메모리 pure-play 사이클 정점 leverage** — SK와 동일 구조, FY26 EBITDA·FCF 폭증 예상. 시총 $1T 진입, UBS PT $1,625 (+204% 상향)

## 핵심 리스크 3

1. **HBM 점유 SK·삼성 대비 후발** — 21% vs SK 60%·삼성 35%. 5년 이상 추격 필요. AMD HBM4 Samsung 단독으로 자체 단독 협력 narrative 없음
2. **CapEx 부담 + NY fab 양산 리스크** — $100B 투자 + 2027 가동 일정. 메모리 사이클 침체와 겹치면 FCF 압박. 신용등급 BBB로 SK·삼성 대비 낮음
3. **Double-ordering + AI capex 변곡점** — 2026 sold out narrative가 sustained demand인지 검증 필요. 2027-2028 사이클 침체 진입 시 OPM 다시 한자릿수

## 단기 vs 장기 view

| 시점 | View |
|---|---|
| 1-2년 (2026-2027) | **매우 강세** — FY26 Q2 record + Q3 가이던스 + HBM 가속 + 미국 본토 narrative |
| 3-5년 (2028-2030) | **강세** (지정학 + HBM4E·HBM5) | 단 SK·삼성 미국 fab 확대 가능성 |
| 5-10년 (2030+) | **중상** — 메모리 사이클 + 한국 미국 진출 누적 + 광·양자 risk |

## SK·삼성·마이크론 3사 비교 (포트폴리오)

| 항목 | SK하이닉스 | 삼성전자 | 마이크론 |
|---|---|---|---|
| 본 테마 직접 노출 | 60%+ | 22% (전사) | 70% |
| Moat 종합 | **4.4** | 4.3 | 4.0 |
| 핵심 강점 | HBM3E 단독·HBM 1위 | DDR5/eSSD #1·HBM4 양산 선두·AMD preferred | **★ 미국 본토 유일 + HBM 가속 회복** |
| 사이클 진폭 | 77%p (높음) | 21.7%p (낮음) | 60%p+ (높음) |
| 신용등급 | AA+ | **AAA** | BBB |
| FY/CY 정점 분기 OPM (Non-GAAP 통일) | 1Q26 OPM 72% | DS 1Q26 OPM ~25%, FY 13.1% | **FQ2-26 OPM 69.0% (IR 확정)** |
| 적합 투자자 | 한국 사이클 정점 | 한국 다각화·주주환원 | **미국 본토·지정학·후발 catch-up** |

→ **메모리 3사가 본 테마에서 3가지 다른 angle을 제공**. 포트폴리오 다각화 종목으로 마이크론은 미국·지정학 angle의 유일한 선택.

---

# 부록 A. Cross-Reference

| 방향 | 참조 |
|---|---|
| 자동 참조 (산업기초) | `반도체_산업기초.md` + `전력 인프라_산업기초.md` |
| 자동 참조 (테마) | `에이전트AI_테마분석.md` v4 |
| 자동 참조 (기업개요) | ✓ `MU_기업개요.md` (v4.9, 2026-05-18 — SEC 10-K 15개·10-Q 47개·Micron IR 기반) |
| BT 첨부 | Micron FY26 Q2 IR (2026-03) |
| Peer cross-ref | `SK하

---

## 부록: 변경 이력 (Changelog)

### v3 (2026-06-02) — IR 1차 자료 fact-check 정정
**출처**: `Micron_FY26_Q2_Deck.pdf` (2026-03-18 발표, 45p) — 마이크론 IR Quarterly Results 직접 추출

**정정 사항**:
1. **OPM 추정 67% → 확정 69.0%** (Operating income $16,455M / Revenue $23,860M, Deck p.27)
2. **NPM 신규** = 58.8% ($14,021M / $23,860M, GAAP $12.07 / Non-GAAP $12.20)
3. **Non-GAAP OpEx** = $1,421M = 6.0% of revenue (R&D $1,129M + SG&A $288M, Deck p.39)
4. **OCF (GAAP)** = $11.9B (50% of revenue, 3.0x YoY) — record
5. **Adjusted FCF** = $6.9B ($0.86B → 8x YoY) — record
6. **Liquidity** = $20.2B (FQ2-26말)
7. **FY26 Capex 상향 가이던스** = $16-18B → **>$25B** (FQ3-26 alone ~$7B)
8. **분기 dividend +30% 인상** (2026-04-15 지급) — 자본 환원 확대
9. **자본 환원 (FQ2-26)** = $1.4B 자사주 매입 (14M주) + $1.8B 배당 = $3.2B
10. **Q3 FY26 가이던스 보강**: 매출 $33.5B ± $750M / GM ~81% / OpEx ~$1.40B / **Non-GAAP EPS $19.15 ± $0.40** / Capex ~$7B (단일 분기)

**BU별 OPM 신규 (Deck p.24)**:
- CMBU (Cloud Memory + HBM): $7,749M, OPM **66%** ★ HBM 핵심
- CDBU (Core Data Center, DDR5·eSSD): $5,687M, OPM **67%** ★ 본 테마 직접
- MCBU (Mobile + Client): $7,711M, OPM **76%**
- AEBU (Auto + Embedded): $2,708M, OPM **62%**
- → **본 테마 직접 노출 (CMBU + CDBU) = 56% / $13.4B 분기 매출**

**HBM·LP DRAM·NAND 신규 fact**:
- HBM4 36GB 12H NVIDIA Vera Rubin **2026 Q1 (CY) volume shipment 시작** (IR 확정)
- HBM4 16-high 48GB sample 출하 (12H 대비 33% 용량 +)
- HBM4E (2027 ramp) — 1γ DRAM 노드, "step-function" 성능 개선
- LP DRAM 256GB SOCAMM2 industry-first (1γ node, CPU당 2TB, 1년 전 대비 4x)
- NVIDIA Groq 3 LPX rack-scale 12TB DDR5 (GTC 2026)
- G9 NAND 노드 mid-CY26 majority bits + QLC record mix
- "Clear majority of customers rank Micron No.1 in quality" (Mehrotra, IR p.8)
- Samsung Galaxy S26 + Google Pixel 10 mobile agentic AI 수혜 — flagship 12GB+ DRAM 비중 <20% → ~80% 1년 만에

### v2 (2026-05-26)
기업개요 `MU_기업개요.md` v4.9 fact 전면 반영: FY25 매출 $37.38B·OPM 32% / HBM 0→20% 신규 진입 / CMBU 36% / 신용등급 Baa1·BBB+ 동반 상향 / Virginia fab 추가.

### v1 (2026-05-26)
초기 분석 — 메모리 3사 framework (SK 4.4 / 삼성 4.3 / 마이크론 4.0).
