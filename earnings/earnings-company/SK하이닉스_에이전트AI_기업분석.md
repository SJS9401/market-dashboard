---
ticker: "000660"
company_name: SK하이닉스
country: KR
theme_keyword: 에이전트AI
parent_industry: 반도체
cross_ref_industry: 전력 인프라
moat_strength: 4.4  # 본 테마 segment 가중 평균
moat_by_segment:
  HBM3E: 5.0          # NVIDIA 단독공급, 절대 우위
  HBM4_NVIDIA: 4.4    # majority 2/3 유지
  HBM4_AMD: 2.8       # Samsung preferred (2026.03 MoU), SK 열위
  HBM4E: 3.4          # 양산 전, SK 선두 시도
  DDR5_server: 4.2    # 삼성 우위 (메모리 절대 CAPA #1), SK 추격
  eSSD: 4.0           # 삼성 1위, SK Group 박빙 #2
trend_revenue_share: 60
last_updated: 2026-05-26
auto_references:
  - 반도체_산업기초.md (2026-05-18)
  - 전력 인프라_산업기초.md (2026-05-18)
  - 에이전트AI_테마분석.md (v3, 2026-05-26)
  - SK하이닉스_기업개요.md (v4.9, 2026-05-11)
analyst_reports_attached:
  - 2026Q1 DS·MERITZ·Samsung·DB·Hanwha·KB·NH·Shinhan·Mirae Asset (9개)
  - SK하이닉스_프리뷰_2026Q1 (BT 자체)
---

# SK하이닉스 기업 분석 — 에이전트AI 테마

> **본 분석 frame**: 에이전트AI 테마 분석(v3)의 16 segment 중 **SK하이닉스는 HBM #1 + DDR5 server #2 + eSSD #2 (3 segment 글로벌 Top 2)**. 단일 기업이 본 테마 반도체 측 핵심 segment 다수에서 글로벌 1-2위를 점유한 매우 예외적 위치. 본 분석은 그 해자 깊이를 정량·정성 검증.

---

## Executive Summary

1. **위치**: 에이전트AI 추론 인프라(반도체+전력)에서 반도체 측 핵심 3 segment 모두 글로벌 Top 2. 본 테마 매출 노출 **60%+**.
2. **해자 종합** (segment 가중 평균): **4.4 / 5.0** (매우 강한 우위, segment별 강약 분명) — **HBM3E 5.0 (절대) / HBM4 NVIDIA 4.4 (majority) / HBM4 AMD 2.8 (Samsung 우위) / DDR5 4.2 (삼성 추격) / eSSD 4.0 (박빙 #2)**.
3. **재무**: FY2025 매출 97.2조·OP 47.2조·OPM 48.6%. **1Q26 매출 52.6조원 (분기 사상 첫 50조 돌파, +198% YoY), OP 37.6조원 (+405%), OPM 72% (창사 최고)** — 컨센서스 초과.
4. **미래 (테마 v3 시간축 PQ)**: HBM Q +35-40% / DDR5 server P 슈퍼사이클 (+30%) / eSSD P+Q 동반 폭증. **1Q26 OPM 72% 실증 + 회사 "향후 3년 수요 capa 훨씬 상회"** 가이던스로 2026 OPM 60%+ 가능성.
5. **종합 판단**: **★★★ 최상위 주도주 후보**. 단 (a) HBM4 dual sourcing 본격화 (b) AMD HBM4 Samsung 이탈 (c) 메모리 사이클 cyclicality 3대 리스크.

---

# 항목 1. 입력 정리 + 기업 포지셔닝

## 1-1. 산업·테마 컨텍스트 요약

### 산업 기초 (반도체_산업기초.md) — 자동 참조
- **산업 유형**: 사이클 산업 (메모리 4-5년 단주기 + 매크로 7-10년 장주기 중첩)
- **공급 구조**: 메모리 CR3 95%+ (삼성·SK하이닉스·Micron 3사 체제)
- **수요 구조 (2025)**: AI/데이터센터 30%+ (5년 전 15%, 2배), B2B 70%+
- **4+5 종합 결론**: **(A) 구조적 메가 병목**

### 테마 분석 (에이전트AI_테마분석.md v3) — 자동 참조
- **테마 frame**: 에이전트AI → 토큰 20-30x 폭증 → 추론 인프라 동시 병목
- **반도체 측 신규 병목 4**: 레거시 메모리·광통신·CPU·CoWoS
- **병목 카테고리**: **(A) 구조적 메가 병목 + (D) 동반 확대 hybrid**
- **한국 접근 가능 TAM (2028E)**: $215-260B+

### SK하이닉스의 위치 (테마 v3 Moat 후보 #1)

| Segment | 글로벌 점유 (2025 Q3-Q4) | 순위 | 비고 |
|---|---|---|---|
| **HBM 전체** | **53-62%** (Q2 62% peak → Q3 53%) | **#1** | NVIDIA HBM 약 90% 공급 |
| **HBM3E (현재 주력)** | NVIDIA H100/H200/Blackwell 단독 | **#1** | 단독공급 유지 |
| **HBM4 (NVIDIA Rubin)** | **약 2/3 (67%) majority** | **#1** | 삼성·Micron 1/3 dual sourcing |
| **HBM4 (AMD MI455X)** | 미공식 (2-3순위) | — | Samsung preferred (2026.03 MoU) |
| **레거시 DRAM (DDR5 server)** | ~33% | **#2** | capa 2026 sold out |
| **eSSD (SK Group)** | **30.2%** (Q4) | **#2** | Q4 +75% QoQ, Solidigm 통합 |

→ **HBM 전체 1위 + NVIDIA Rubin HBM4 majority 유지 + DDR5/eSSD Top 2**. 단일 기업으로 본 테마 다축 포지셔닝 유일.

## 1-2. 기업 포지셔닝

### 사업부 구성 + 본 테마 연결 (기업개요 v4.9 reference)
| 사업부 | 매출 비중 (1Q26) | 본 테마 연결 |
|---|---|---|
| **DRAM** | **80%** | HBM (DRAM의 50%+) + DDR5 server + 모바일·PC DDR5 + 일반 DRAM |
| **NAND** (Solidigm 포함) | **18%** | eSSD enterprise + 모바일·PC NAND |
| Others (Module·MCP) | 2% | 일부 데이터센터 모듈 |

### 본 테마 직접 매출 노출
| 구성 | 매출 비중 | 직접성 |
|---|---|---|
| HBM | 약 40% (1Q26, DRAM의 50%+) | ★★★ |
| DDR5 server | 약 15% | ★★★ |
| eSSD enterprise (Solidigm + SKH) | 약 8% | ★★★ |
| 모바일·PC DDR5 | 약 15% | ★★ |
| 일반 NAND | 약 10% | ★ |
| Others | 2% | — |
| **본 테마 직접 노출 (★★★ 합)** | **~63%** | — |

→ **본 테마 직접 매출 60%+** — 한국 기업 중 본 테마 가장 다축 수혜.

---

# 항목 2. 비즈니스 모델 & 해자 (Moat) — ★ 핵심

## 2-1. 비즈니스 모델 (본 테마 사업부 중심)

### HBM (40% 매출)

- **무엇으로 돈을 버는가**: HBM die 12-stack 적층 (TC본더·MR-MUF) → CoWoS 패키징에서 NVIDIA·AMD GPU와 결합 → AI 가속기 BOM 메모리 부분
- **HBM 세대별 SK 위치**:
  - **HBM3E (현재 주력, 2025-2026 H1)**: NVIDIA H100/H200/Blackwell **단독공급**
  - **HBM4 (NVIDIA Rubin, 2026 H2~)**: SK 약 2/3 majority + 삼성·Micron 1/3 (dual sourcing)
  - **HBM4 NVIDIA 11Gb/s test**: 삼성 먼저 통과, SK 10Gb/s 통과 후 11Gb/s 최적화 진행
  - **HBM4 AMD (MI455X)**: Samsung preferred (2026.03 MoU)
  - **HBM4E (2027 양산)**: SK 2H26 샘플, 2027 양산 목표
- **가격 결정력**: HBM3E 단독공급으로 강함 / HBM4부터 dual sourcing으로 일부 압박
- **다른 사업부 시너지**: DDR5 동일 공정 라인 → wafer allocation flexible

### DDR5 server (15% 매출)
- HBM 우선 생산 squeeze + AI 서버 메인 메모리 수요 폭증
- DRAM 가격 YTD +50% (2025), capa 2026 sold out
- **2026 P 슈퍼사이클 driver**

### eSSD enterprise (8% 매출, Solidigm 포함)
- SK Group 점유 30.2% (Q4 2025), Solidigm 122TB KV cache offload 마케팅
- **(D) 동반 확대 driver** — KV cache offload·VectorDB·체크포인트 신규 수요

### 시너지 (DRAM + NAND + HBM 통합)
- 메모리 종합 IDM의 통합 가치 (HBM + DDR5 + eSSD 하나의 솔루션)
- Solidigm 통합으로 NAND 사이클 buffer 강화
- **1Q26 OPM 72%** — 메모리 종합 IDM의 cyclical leverage 증명

## 2-2. 해자 (Moat) 깊이 분석 — Segment별 평가 ★

> **분석 frame**: 본 테마 직접 노출 segment 6개(HBM3E·HBM4 NVIDIA·HBM4 AMD·HBM4E·DDR5 server·eSSD)별로 SK하이닉스 Moat를 5축 척도로 평가. 글로벌 peer (삼성·Micron)와 segment별 직접 비교. 본 테마 매출 비중 가중 평균으로 종합.

### Segment 1. HBM3E (현재 주력, 매출 비중 ~25%)
| 축 | SK하이닉스 | 삼성 | Micron | 핵심 |
|---|---|---|---|---|
| 기술/특허 | **5** | 4 | 3 | NVIDIA H100/H200/Blackwell 단독공급, MR-MUF |
| HBM CAPA | **5** | 4 | 3 | 현재 sold out, 알로케이션 우선권 |
| 고객 lock-in | **5** | 3 | 3 | NVIDIA 단독 + AMD·Broadcom 메인 |
| 규모 (HBM 점유) | **5** | 4 | 3 | 53% (Q3 2025), HBM 전체 1위 |
| 병목 포지셔닝 | **5** | 3 | 3 | NVIDIA HBM 90% 공급 |
| **평균** | **5.0** | 3.6 | 3.0 | **SK 절대 우위** |

### Segment 2. HBM4 (NVIDIA Rubin, 2H26~, 매출 비중 ~15%)
| 축 | SK하이닉스 | 삼성 | Micron | 핵심 |
|---|---|---|---|---|
| 기술/특허 | 4 | **4** | 3 | 11Gb/s test 삼성 먼저 통과, SK 최적화 중 |
| HBM CAPA | **5** | 4 | 3 | 2026 capa 25K wafer/월 확보 |
| 고객 lock-in | 4 | 4 | 3 | NVIDIA Rubin SK 2/3 majority + 삼성·Micron 1/3 |
| 규모 | **5** | 4 | 3 | NVIDIA Rubin 점유 67% |
| 병목 포지셔닝 | 4 | 4 | 3 | dual sourcing 구조 |
| **평균** | **4.4** | 4.0 | 3.0 | **SK majority 유지** |

### Segment 3. HBM4 (AMD MI455X, 2H26~, 매출 비중 ~5%)
| 축 | SK하이닉스 | 삼성 | Micron | 핵심 |
|---|---|---|---|---|
| 기술/특허 | 3 | **4** | 3 | Samsung HBM3E AMD 단독 → HBM4 우선 협력 |
| HBM CAPA | 4 | **5** | 3 | 알로케이션 Samsung 우위 |
| 고객 lock-in | 2 | **5** | 2 | **Samsung preferred (2026.03 MoU)** |
| 규모 | 2 | **4** | 2 | AMD 채택 비중 작음 |
| 병목 포지셔닝 | 3 | **4** | 2 | Samsung 진입 |
| **평균** | **2.8** | **4.4** | 2.4 | **Samsung 우위, SK 열위** |

### Segment 4. HBM4E (차세대, 2027 양산 목표)
| 축 | SK하이닉스 | 삼성 | Micron | 핵심 |
|---|---|---|---|---|
| 기술/특허 | 4 | 4 | 3 | SK 2H26 샘플, 삼성 추격 |
| HBM CAPA | 3 | 3 | 2 | 양산 미시작 |
| 고객 lock-in | 3 | 3 | 2 | NVIDIA 차세대 인증 대기 |
| 규모 | 3 | 3 | 2 | 양산 전 |
| 병목 포지셔닝 | **4** | 3 | 2 | SK 양산 선두 시도 |
| **평균** | **3.4** | 3.2 | 2.2 | **양산 전, SK 일부 선두** |

### Segment 5. DDR5 server (메모리 절대 capa 비교 포함, 매출 비중 15%)
| 축 | SK하이닉스 | 삼성 | Micron | 핵심 |
|---|---|---|---|---|
| 기술/특허 | 4 | **5** | 3 | 삼성 DRAM 종합 기술 1위 |
| 메모리 절대 CAPA | 4 | **5** | 3 | **삼성 600-650K wafer/월 (#1), SK 450-500K (#2)** |
| 고객 lock-in | 4 | **5** | 3 | hyperscaler·OEM 분산 |
| 규모 (DRAM 점유) | 4 | **5** | 3 | 삼성 42%, SK 33%, Micron 24% |
| 병목 포지셔닝 | **5** | **5** | 4 | HBM squeeze 양면 수혜 (capa 2026 sold out) |
| **평균** | **4.2** | **5.0** | 3.2 | **삼성 우위, SK 추격** |

### Segment 6. eSSD enterprise (메모리 절대 capa 비교 포함, 매출 비중 8%)
| 축 | SK Group | 삼성 | Micron·Kioxia | 핵심 |
|---|---|---|---|---|
| 기술/특허 | 4 | **5** | 3 | Solidigm 122TB KV cache 특화 |
| NAND 절대 CAPA | 3 | **5** | 3 | **삼성 800K wafer/월 (#1), SK Group 500K (#2)** |
| 고객 lock-in | 4 | **5** | 3 | hyperscaler 직접 |
| 규모 (eSSD 점유 Q4) | 4 | **5** | 3 | 삼성 32.3% (#1), SK Group 30.2% (#2, +75% QoQ) |
| 병목 포지셔닝 | **5** | **5** | 3 | KV cache offload 신규 수요 |
| **평균** | **4.0** | **5.0** | 3.0 | **삼성 1위, SK Group 박빙 #2** |

### 본 테마 가중 종합 (Moat × 매출 비중)

| Segment | 매출 비중 | SK 평균 Moat | 가중 기여 | 삼성 비교 |
|---|---|---|---|---|
| HBM3E | ~25% | **5.0** | 1.25 | SK 절대 우위 |
| HBM4 (NVIDIA Rubin) | ~15% | **4.4** | 0.66 | SK 우위 |
| HBM4 (AMD MI455X) | ~5% | 2.8 | 0.14 | Samsung 우위 |
| HBM4E (미래) | (양산 전) | 3.4 | — | 평가 보류 |
| DDR5 server | 15% | 4.2 | 0.63 | 삼성 우위, SK 추격 |
| eSSD enterprise | 8% | 4.0 | 0.32 | 삼성 1위, SK 박빙 |
| **합계 (본 테마 직접 노출)** | **68%** | **가중 평균 4.4** | 3.00 / 68% × 5/5 | — |

### 핵심 종합 결론

**SK하이닉스의 Moat는 segment별로 크게 분화**:

| 구간 | SK 포지셔닝 |
|---|---|
| **HBM3E** (현재 주력) | **절대 우위 (5.0)** — NVIDIA 단독공급 + 모든 축 만점 |
| **HBM4 NVIDIA Rubin** | **majority 우위 (4.4)** — 67% 점유 유지, 단 dual sourcing 진입 |
| **HBM4 AMD MI455X** | **열위 (2.8)** — Samsung preferred MoU (2026.03)로 SK 진입 제한 |
| **HBM4E** (2027) | 평가 보류 (양산 전), SK 선두 시도 |
| **DDR5 server** | **추격 #2 (4.2)** — 메모리 절대 capa·DRAM 종합 기술은 **삼성 1위**, SK는 #2 추격. 단 HBM squeeze 양면 수혜로 병목 포지셔닝은 동급 |
| **eSSD enterprise** | **박빙 #2 (4.0)** — NAND 절대 capa는 삼성 1위, SK Group이 Solidigm 통합으로 30.2% 점유 박빙 추격 |

**본 테마 가중 평균: 4.4 / 5.0** — 매우 강한 우위 (단, segment별 강약 분명)

### Moat 지속성 (2년/5년/10년)

| 시점 | 유효성 | 시그널 |
|---|---|---|
| **2년 (~2028)** | 강력 (HBM3E·HBM4 NVIDIA 중심), 일부 약화 (HBM4 AMD·DDR5 추격) | HBM4 dual sourcing 안착, HBM4E 2027 양산 |
| **5년 (~2030)** | 강력 (HBM4E·HBM5 + Solidigm 시너지) | 메모리 종합 portfolio + MR-MUF 노하우 |
| **10년 (~2035)** | 중상 | 메모리 사이클 본질 + 광·양자·뉴로모픽 등 대체 패러다임 가능 |

### Moat 지속성 (2년/5년/10년)

| 시점 | 유효성 | 시그널 |
|---|---|---|
| **2년 (~2028)** | 강력 | HBM4 dual sourcing 안착·HBM4E 2027 양산. 삼성 HBM4 yield 50% 추가 개선 시 SK majority 압박 |
| **5년 (~2030)** | 강력 | HBM4E·HBM5 + Solidigm 시너지. 메모리 종합 portfolio + MR-MUF 노하우 누적 |
| **10년 (~2035)** | 중상 | 메모리 사이클 본질 + 광·양자·뉴로모픽 등 대체 패러다임 등장 가능 |

### 글로벌 peer 비교

| 비교 항목 | SK하이닉스 | 삼성전자 (DS) | Micron |
|---|---|---|---|
| HBM 전체 점유 (Q3 2025) | **53%** | 35% | 11% |
| **HBM3E 단독공급 (현재)** | NVIDIA H100/H200/Blackwell **단독** | 부분 진입 | 일부 (Hopper) |
| **HBM4 양산 선두 (2026.02)** | 11Gb/s 최적화 중 | **업계 최초 양산 출하** | 1Q26 volume shipment |
| **HBM4 NVIDIA Rubin 분배** | **2/3 (67%) majority** | 일부 | 일부 |
| **HBM4 AMD (MI455X, 2H26)** | 미공식 | **preferred (2026.03 MoU)** | — |
| **HBM4E (차세대)** | 2H26 샘플, **2027 양산 목표** | — | — |
| DRAM 점유 | 33% | **42%** | 24% |
| eSSD 점유 (Q4) | 30.2% (SK Group) | **32.3%** | 10% |
| Solidigm 통합 | ✓ (2025.03) | ❌ | — |
| **1Q26 OPM** | **72% (사상 최고)** | 40-45% 추정 | 30-35% 추정 |
| pure-play 여부 | 메모리 pure | DS 다각화 | 메모리 pure |

> **포지셔닝 결론**: SK하이닉스는 **HBM3E 단독공급 + HBM 전체 1위 + 메모리 종합 #1 + 1Q26 OPM 72%**의 quadruple position. HBM4부터는 dual sourcing 구조이나 NVIDIA Rubin majority 2/3 유지 + HBM4E 2027 양산으로 차세대 narrative 회복 시도.

## 2-3. 병목 수혜 강도 정량화

| Segment | 카테고리 | 수혜 메커니즘 | 정량 추정 (2026E·2027E) |
|---|---|---|---|
| **HBM** | (A) 구조적 메가 병목 | HBM3E 단독 + HBM4 majority (NVIDIA Rubin 2/3) + Q 폭증 | 매출 **+35% (2026)·+25% (2027)**, OPM 60%+ 유지 |
| **레거시 DRAM (DDR5)** | (A) 구조적 메가 병목 | HBM 우선 생산으로 일반 DRAM capa squeeze → P 슈퍼사이클 | 매출 **+30% P + 견조 Q (2026)**. 2025 YTD +50% 진행 |
| **eSSD (NAND)** | (A) → (D) 동반 확대 | KV cache offload 신규 수요 + Solidigm 시너지 | 매출 **+50% (2026)·+40% (2027)** |
| **모바일·PC DDR5** | 사이클 turn | AI 학습 우선 capa squeeze + AI 폰 회복 | 매출 +20-25% (2026) |

**수혜 정량 추정**:
- 본 테마 직접 매출 비중: 60%+
- 마진 프리미엄: HBM OPM 60%+ vs 일반 DRAM 25-30%
- 점유 가능성: HBM3E 단독 + HBM4 majority + DDR5/eSSD Top 2 → 수혜 누락 risk 낮음
- → **2026-2027 OPM 50%+ 지속 가능성** (1Q26 OPM 72% 실증 + 회사 3년 수요 capa 초과 발표)

---

# 항목 3. 재무 분석

## 3-1. 실적 추이

### 12년 연간 (2014~2025) — 기업개요 v4.9 cross-ref

| 연도 | 매출 (조원) | OP (조원) | OPM | 사이클 단계 |
|---|---|---|---|---|
| 2018 | 40.5 | 20.84 | **51.5%** | 정점 1차 (DRAM 슈퍼사이클) |
| 2019 | 27.0 | 2.71 | 10.1% | 저점 1차 |
| 2021 | 43.0 | 12.41 | 28.9% | 코로나 정점 |
| **2023** | 32.8 | **-8.42** | **-25.7%** | **저점 2차 (적자전환)** |
| 2024 | 66.2 | 23.47 | 35.5% | 회복 + HBM 본격화 |
| **2025** | **97.2** | **47.21** | **48.6%** | **정점 2차 (AI HBM)** |

- 12년 매출 CAGR **+15.6%**, 자본총계 17조 → 117조 (**7배**)
- OPM range **-25.7% ~ +51.5%** (77.2%pt 진폭) — 가장 cyclical한 대형주

### ★ 1Q26 분기 실적 — 사상 최고 갱신

| 항목 | 1Q26 | YoY | 컨센서스 | 비고 |
|---|---|---|---|---|
| 매출 | **52.6조원** | **+198%** | 51.9조원 | 분기 사상 첫 50조 돌파 |
| OP | **37.6조원** | **+405%** | 36.4조원 | 컨센서스 +3.4% beat |
| **OPM** | **72%** | — | — | **창사 이래 최고** |
| 회사 가이던스 | "**향후 3년 수요가 공급 캐파 훨씬 상회**" | | | 1Q26 컨퍼런스콜 |

- 1Q26 단일 분기로 FY2024 매출 (66.2조)의 80% 도달
- OPM 72%는 메모리 IDM 역대 최고 분기 실적
- 1Q26 OPM 72%는 정점 신호일 가능성도 — 2027부터 HBM4 dual sourcing 압박 가시화

## 3-2. 사업부별 PQC 분해

| 차원 | 일반 DRAM | **HBM (트렌드)** | **eSSD (신규 트렌드)** |
|---|---|---|---|
| **P (ASP YoY)** | 사이클 ±50% (2025 +50%) | **+20% YoY 6분기 연속 (HBM3E)** | +30-50% |
| **Q (출하 YoY)** | +10-15% | **+50-100% (HBM3E)** / +20-30% (HBM4, dual sourcing 반영) | **+50-75% QoQ** (Q4) |
| **C (원가)** | wafer 효율 좋음 | wafer 3x + TC본더 + MR-MUF | NAND wafer + 컨트롤러 |
| **매출 (P×Q)** | 사이클 ±60% | **YoY +100~150% 지속** | YoY +100%+ |
| **마진 (OPM)** | 25-30% (정상)·-20% (저점) | **60%+ (HBM3E), HBM4는 dual sourcing 경쟁으로 일부 압박** | 35-45% (회복) |

### 1Q26 PQC 실측

| 차원 | 1Q26 |
|---|---|
| DRAM ASP | **+63~65% QoQ** (Bit -0~+0%) |
| NAND ASP | **+73~74% QoQ** (Bit -11~-13%) |
| HBM 매출 | YoY 2배+ (HBM3E 12단 + HBM4 12H 본격 출하 시작) |

> 1Q26은 메모리 P 급등 + HBM mix 상승의 dual 효과로 OPM 72%. HBM4 dual sourcing이 본격화되는 2026 H2부터는 P 일부 둔화 예상.

## 3-3. 재무 건전성

| 항목 | 2025 / 1Q26 |
|---|---|
| 자본총계 | 117조원 (2025) → 145조원+ 추정 (1Q26 후) |
| 부채비율 | ~50% |
| OCF | 50조원+ (2025) / 1Q26 단독 20조원+ 추정 |
| FCF | 24조원+ |
| CapEx | 26.1조원 (2025) → 30조원+ (2026E 추정) |
| 신용등급 | 국내 AA+ / Moody's Baa1 / S&P BBB+ / Fitch BBB |
| 유상증자 가능성 | **매우 낮음** (FCF 견조 + 자본 145조) |

## 3-4. 수익성 트렌드

| 지표 | 12년 평균 | 2018 정점 | 2023 저점 | 2025 정점 | **1Q26 (★)** |
|---|---|---|---|---|---|
| OPM | 26.7% | 51.5% | -25.7% | 48.6% | **72%** |
| NPM | ~22% | 38.4% | -27.9% | 44.2% | ~57% 추정 |
| ROE | ~18% | 36%+ | -20% | 40%+ | 50%+ 추정 |

### 피어 대비 수익성 비교

| 기업 | 2025 OPM | 1Q26 OPM | 비고 |
|---|---|---|---|
| **SK하이닉스** | **48.6%** | **72%** | 사상 최고, HBM3E 단독 + HBM4 majority |
| 삼성전자 DS | ~35% | ~40-45% 추정 | HBM4 양산 선두로 회복 가속 |
| Micron | ~25-30% | ~30-35% 추정 | HBM4 1Q26 진입, 추격 |
| TSMC (참조) | ~45% | ~48% | 파운드리, 비교용 |

→ **SK 1Q26 OPM 72% = 메모리 IDM 글로벌 사상 최고 분기 실적**.

---

# 항목 4. 성장성 분석

## 4-1. 과거 성장률

| 기간 | 매출 CAGR | OP CAGR |
|---|---|---|
| 3년 (2022 → 2025) | **+30%** | +90% |
| 5년 (2020 → 2025) | **+25%** | +57% |
| 12년 (2014 → 2025) | +15.6% | +20% |

피어 비교 (5년 CAGR): SK +25% vs 삼성DS +8% vs Micron +12% — SK 압도

## 4-2. 향후 성장 가시성 — 미래 PQ 전망

테마 분석 v3 Step 5 시간축 PQ를 SK하이닉스 노출 segment에 매핑.

### HBM ((A) 구조적 메가 병목)
| 차원 | 4Q (2Q25E~1Q26E) | 2Y (2026·2027) | 근거 | 출처 |
|---|---|---|---|---|
| **P** | +5·+3·+2·0% | +5·-5% | HBM4 dual sourcing 경쟁 가격 압박 일부 | 테마 v3 Step 5 + TrendForce 2026-01-28·03-09 |
| **Q** | +10·10·8·8% | **+35·25%** | NVIDIA Rubin·hyperscaler allocation. 삼성·Micron 진입으로 SK 점유 일부 약화 | 테마 v3 Step 5 + 회사 1Q26 컨콜 (디일렉) |
| **→ 매출** | **+15-18% YoY** | **+40% (2026)·+20% (2027)** | HBM 단독 매출 | BT 첨부 9개 셀사이드 컨센서스 평균 |
| **→ 마진** | **OPM 60-65%** | 55-60% | HBM4 dual sourcing + HBM4E 양산 (2027) | DS·Mirae Asset·Shinhan 셀사이드 추정 |

### 레거시 DRAM (DDR5 server) — (A) 구조적 메가 병목
| 차원 | 4Q | 2Y | 근거 | 출처 |
|---|---|---|---|---|
| P | +30·20·15·10% | +30·0% | HBM squeeze + 재고 정상화 | 테마 v3 Step 5 + Counterpoint (DDR5 server) |
| Q | +5·5·5·5% | +25·15% | AI 서버 + KV cache offload | 테마 v3 Step 5 |
| **→ 매출** | **+35-40% YoY** | +60% (2026) | DDR5 P 슈퍼사이클 | BT 첨부 9개 셀사이드 컨센서스 평균 |

### eSSD — (A) → (D) 동반 확대
| 차원 | 4Q | 2Y | 근거 | 출처 |
|---|---|---|---|---|
| P | +20·15·10·8% | +25·10% | NAND 사이클 + AI premium | 테마 v3 Step 5 + TrendForce eSSD Q3-Q4 2025 |
| Q | +15·20·20·25% | +50·40% | KV cache·VectorDB | 테마 v3 Step 5 + Solidigm IR (122TB 양산) |
| **→ 매출** | **+40-50% YoY** | +85% (2026)·+55% (2027) | SK Group 30% 점유 | BT 첨부 9개 셀사이드 컨센서스 (NH·Hanwha·KB) |

> **공통 출처**: (1) 테마 분석 v3 Step 5 시간축 PQ 표 — 16 segment 정량 framework / (2) BT 첨부 9개 셀사이드 1Q26 프리뷰 컨센서스 평균 / (3) SK하이닉스 1Q26 컨퍼런스콜 가이던스 ("향후 3년 수요 capa 훨씬 상회") / (4) TrendForce·Counterpoint 월간·분기 점유율 데이터 / (5) Micron·Samsung·NVIDIA 공시·PR.
>
> **추정 method**: 셀사이드 컨센 평균 → 본 분석의 segment 가중 SK Moat (4.4)·HBM4 dual sourcing 진입 risk 반영하여 조정. 일부 차원은 단일 셀사이드가 아닌 본 분석 추정 (HBM4E 2027 양산 반영분 등 — 명시 표기).

### 회사 전체 매출·OPM 전망

| 항목 | 2025 실적 | **1Q26 실적** | 2026E (연간) | 2027E |
|---|---|---|---|---|
| 매출 (조원) | 97.2 | **52.6 (분기)** | **150-170 (+55-75%)** | 175-195 (+15-20%) |
| OP (조원) | 47.2 | **37.6 (분기)** | **90-105 (+90-120%)** | 95-110 (+5-10%) |
| **OPM** | 48.6% | **72%** | **60-62%** | 52-56% |

> **알 수 없음 시나리오**: 2027-2028 사이클 침체 진입 가능. AI capex 변곡점 + Micron·삼성 HBM4 capa 확대 + AMD HBM4 Samsung 우위 누적 영향이 trigger.

### 수주잔고·백로그
- 회사 1Q26 컨콜: **"향후 3년 수요가 공급 캐파 훨씬 상회"** → 사실상 3년+ 백로그
- HBM4 NVIDIA Rubin 2/3 점유 확정 (4Q26 16-high 본격)
- HBM4E 2027 양산 목표 (SK 2H26 샘플)

### OPM 지속 가능성 — 경쟁 심화 시그널

| 시그널 | 현재 상태 | 임팩트 |
|---|---|---|
| Micron HBM4 NVIDIA 인증 | 1Q26 volume shipment 시작 | 중-큼 — SK 단독공급 신화 종료 |
| 삼성 HBM4 NVIDIA 인증 | 2026.02 업계 최초 양산 출하 | 큼 — HBM4부터 dual sourcing |
| AMD HBM4 Samsung MoU (2026.03) | MI455X preferred supplier | 큼 — SK AMD 지위 약화 |
| TSMC CoWoS capa | 75K → 130K (2026) | 양면 |
| AI capex 변곡점 | 2026 $700B → 2027 가능 조정 | 큼 |

## 4-3. 피어 그룹 비교

| 기업 | 2025 매출 (USD B) | 5년 CAGR | 2025 OPM | **1Q26 OPM 추정** | 핵심 차이점 |
|---|---|---|---|---|---|
| **SK하이닉스** | ~$70B | **+25%** | **48.6%** | **72%** | HBM 1위, HBM3E 단독, HBM4 majority |
| 삼성전자 DS | ~$80B | ~+8% | ~35% | 40-45% | DS 다각화, HBM4 양산 선두 + AMD preferred |
| Micron | ~$30B | +12% | 25-30% | 30-35% | HBM4 1Q26 진입, 미국 본토 |
| Kioxia | ~$15B | +5-8% | ~15% | — | NAND only |

---

# 항목 5. 통합 모드 입력용 Fact 정리

> 테마 분석 통합 모드가 Terminal 점유·마진·시총 추정 시 사용할 fact·raw data.

| 항목 | Fact / Raw Data |
|---|---|
| **현재 시장 점유 + 3-5년 추이** | HBM 전체: 2022 ~50% → 2024 60% → 2025 Q3 53%. **HBM3E: NVIDIA H100/H200/Blackwell 단독**. **HBM4 NVIDIA Rubin: SK 2/3 (67%) + 삼성·Micron 1/3**. **HBM4 AMD MI455X: Samsung preferred**. DRAM: 33%. eSSD (SK Group): Q4 2025 30.2% |
| **현재 CAPA + 증설** | HBM wafer ~15K/월 (2025), 2026 25K+ (HBM4 라인 추가). **회사 1Q26 컨콜: 향후 3년 수요 capa 훨씬 상회**. CapEx 26.1조원 (2025) → 30조원+ (2026E 추정) |
| **사이클 마진 진폭 (12년)** | OPM range -25.7% ~ +51.5% (77.2%p). **1Q26 OPM 72% 신규 정점**. 정점 평균 48.4% → 72% 상향 |
| **기술 격차·R&D·IP** | IP 21,859건 (2025.12). HBM4 11Gb/s test: 삼성 먼저 통과, SK 최적화 진행. HBM4E 2H26 샘플, 2027 양산. MR-MUF 기술 강점 유지 |
| **고객사 분포·집중도** | HBM 상위 5: NVIDIA·AMD·Broadcom·MSFT·AWS. NVIDIA HBM 전체 약 90% 공급 (SK 기준). HBM4 NVIDIA majority 2/3 유지. AMD는 Samsung 우선. 양면 risk |
| **신규 수주·계약** | 2025.03 Solidigm 최종 종결. 2026까지 HBM·DRAM·NAND sold out. HBM4 NVIDIA Rubin 2/3 확정. AMD HBM4 Samsung MoU 2026.03. HBM4E 2027 양산 목표 |
| **자본·시총** | 자본 17조 → 117조 (12년 7배) → **145조원+ 추정 (1Q26 후)**. 시총 2025 정점 200조+ → 2026 1Q 추가 상승 |
| **1Q26 실적** | 매출 52.6조 (+198% YoY), OP 37.6조 (+405%), OPM 72%, 컨센서스 초과 |

---

# 항목 6. 구조적 트리거 모니터링

> 단기 진입 시그널은 분기 실적 분석. 여기는 본질적 구조 변화 트리거만.

## 상방 트리거 (해자 강화)

| 트리거 | 시점 | 영향 |
|---|---|---|
| HBM4E 2027 양산 + NVIDIA 차세대 인증 | 2026 H2 샘플 → 2027 양산 | 차세대 narrative 회복 |
| HBM4 NVIDIA Rubin 점유 70%+ 확정 | 2026 H2 | SK majority 강화 |
| Solidigm KV cache 점유 가속 (35%+) | 2026 분기 | eSSD 매출 추가 가속 |
| 1Q26 OPM 72% 추가 분기 유지 (2Q26 70%+) | 2Q26 어닝 | 실증 강화 |
| CapEx 추가 확대 (30조원+) | 2026 IR | 2027+ Q 가시성 |
| 삼성 HBM4 yield 50% 정체 | 2026 H2 | SK HBM4 majority 유지 |

## 하방 트리거 (해자 약화)

| 트리거 | 시점 | 영향 |
|---|---|---|
| **HBM4 NVIDIA dual sourcing 본격화** | 2026 H2 (진행 중) | SK 점유 67% 이하 |
| **AMD HBM4 Samsung preferred** | 2026.03 체결 | SK AMD 지위 약화 (현실화) |
| 삼성 HBM4 11Gb/s NVIDIA test 통과 | 2026 Q1 (진행 중) | SK HBM4 premium 약화 |
| Micron HBM4 NVIDIA 점유 15%+ | 2026 H2 | SK 점유 잠식 |
| AI capex 변곡점 (hyperscaler -10%+) | 2027 | Q 가속 둔화 |
| 메모리 사이클 침체 (DRAM P -20%+) | 2027-2028 | OPM 30%대 reset |
| HBM4E NVIDIA 인증에서 삼성 우위 | 2027+ | 차세대 narrative 약화 |

## 모니터링 캘린더

| 시점 | 이벤트 |
|---|---|
| 분기 어닝콜 (Q1-Q4) | HBM 점유·CapEx 가이던스·고객 mix |
| Investor Day (연 1회) | HBM4·HBM5 로드맵, Solidigm 통합 진행 |
| NVIDIA GTC (3월) | Rubin·차세대 GPU 발표, HBM 사양 |
| Hot Chips (8월) | 차세대 메모리 기술 발표 |
| 삼성·Micron 분기 IR | HBM4 양산·NVIDIA 인증 진행 |
| AMD MI455X 출하 시작 + Samsung 점유 확정 | 2H26 |
| SK HBM4E 샘플 NVIDIA 인증 | 2H26 |
| TSMC CoWoS capa 분기 update | 패키징 병목 변화 |
| TrendForce·Counterpoint 월간·분기 점유 리포트 | HBM·DDR5·eSSD 점유 추적 |

> 분기 실적 분석이 본 트리거의 현재 상태를 점검. narrative shift 감지 시 본 .md 갱신.

---

# 종합 판단

## 매트릭스 평가

| 차원 | 평가 | 근거 |
|---|---|---|
| 상위 트렌드 적합성 | ★★★ 최상 | 에이전트AI 추론 인프라 = AI 메가 트렌드 핵심 |
| 산업 위치 | ★★★ 최상 | 메모리 IDM 글로벌 #1 (1Q26 분기 첫 50조 돌파), HBM #1 |
| **해자 강도** | **4.4 / 5.0** (segment 가중) | HBM3E 5.0 / HBM4 NVIDIA 4.4 / HBM4 AMD 2.8 / DDR5 4.2 / eSSD 4.0 — segment별 강약 분명 |
| 재무 건전성 | ★★★ 최상 | 자본 145조+, FCF 24조+, 신용 AA+ |
| 성장 가시성 (2~3년) | ★★★ 최상 | 2026 매출 +55-75%·OP +90-120%·OPM 60%+ (1Q26 72% 실증 + 회사 3년 수요 발표) |
| 성장 지속성 (5~10년) | ★★ 중상 | HBM4 dual sourcing 누적 + 메모리 사이클 cyclicality |

## 핵심 투자 포인트 3

1. **본 테마 직접 노출 60%+** — 16 segment 중 3 segment 글로벌 Top 2 (HBM #1·DDR5 #2·eSSD #2). 한국 기업 중 본 테마 가장 다축 수혜
2. **3중 슈퍼사이클 합치점 + 1Q26 OPM 72% 실증** — HBM3E 단독 + DDR5 P 슈퍼사이클 + eSSD 신규 driver. 1Q26 사상 최강 분기 실적이 thesis 증명
3. **HBM 전체 #1 + NVIDIA HBM4 majority + HBM4E 차세대 양산 시도** — HBM3E 단독 + NVIDIA HBM 전체 90% 공급 + HBM4E 2027 양산 3중 backup

## 핵심 리스크 3

1. **HBM4 dual sourcing 본격화** — 삼성 2026.02 양산 선두 + Micron 1Q26 진입 + AMD Samsung MoU. SK NVIDIA majority 2/3는 유지하나 단독공급 신화 종료
2. **메모리 사이클 cyclicality** — OPM 77.2%p 진폭. 2027-2028 침체 진입 가능. 1Q26 OPM 72%는 정점 신호일 수도
3. **HBM4E NVIDIA 차세대 인증 경쟁** — 2027+ HBM4E·HBM5 단계에서 삼성·Micron 추격 시 narrative 추가 약화 가능

## 단기 vs 장기 view

| 시점 | View |
|---|---|
| 1-2년 (2026-2027) | **매우 강세** — 3중 슈퍼사이클 + 1Q26 OPM 72% 실증 + 회사 3년 수요 발표 |
| 3-5년 (2028-2030) | **중상** — HBM4 dual sourcing 누적 + 메모리 사이클 침체 진입 risk 가시화 |
| 5-10년 (2030+) | **중상** — 메모리 패러다임 유지 시 강자 지속. 광·양자·뉴로모픽 등 새 패러다임 risk |

---

# 부록 A. Cross-Reference

| 방향 | 참조 |
|---|---|
| 자동 참조 (산업기초) | `반도체_산업기초.md` (2026-05-18) + `전력 인프라_산업기초.md` (2026-05-18, cross-ref) |
| 자동 참조 (테마) | `에이전트AI_테마분석.md` (v3, 2026-05-26) — Step 4-3 권장 #1, Step 5 시간축 PQ 직접 cross-ref |
| 자동 참조 (기업개요) | `SK하이닉스_기업개요.md` (v4.9, 2026-05-11) |
| BT 첨부 (애널리스트) | 9개 셀사이드 리포트 + SK하이닉스 자체 프리뷰 2026Q1 |
| 다음 단계 (통합 모드) | 항목 5 fact가 [테마 분석 통합 모드] 진입 시 Terminal 시총 시나리오 자동 추출 input |
| 다음 단계 (실적 분석) | 분기 실적 프리뷰/리뷰/인뎁스 시 항목 6의 구조적 트리거 reference |

# 부록 B. 주요 자료 출처

| 카테고리 | 출처 |
|---|---|
| 12년 손익·재무 | DART 사업보고서 2014~2025, SK하이닉스 IR 분기경영실적 50개 |
| 1Q26 실적 | SK하이닉스 1Q26 컨퍼런스콜 (디일렉 2026-04), SK하이닉스 IR 뉴스룸 |
| HBM·DDR5·eSSD 점유 | TrendForce, Counterpoint Research, Astute Group |
| HBM4 분배 | TrendForce 2026-01-28·2026-03-09, KED Global 2025-12-03·2026-03 |
| AMD HBM4 Samsung MoU | TrendForce 2026-03-19, AMD 공식 PR 2026-03-18 |
| Micron HBM4 1Q26 양산 | Micron 공식 PR, Digitimes 2026-01-07 |
| 산업·테마 컨텍스트 | 반도체_산업기초.md, 에이전트AI_테마분석.md v3 |
| 셀사이드 컨센서스 | 한국 9개 증권사 SK하이닉스 2026Q1 프리뷰 |
| Solidigm 통합 fact | SK하이닉스 공시 2025.03.28 |

# 부록 C. 메타데이터 갱신 로그

| 버전 | 일자 | 변경 사항 |
|---|---|---|
| v1 | 2026-05-26 | 1차 작성 |
| v2 | 2026-05-26 | HBM4 narrative 정정 (cross-check 반영) |
| **v3** | **2026-05-26** | **Moat 분석 segment별 재구성** (single 5축 → 6 segment × 5축) |

### v1 → v3 변화 요약

| 항목 | v1 | v2 | v3 |
|---|---|---|---|
| HBM4 공급 구조 | NVIDIA 단독공급 | NVIDIA Rubin SK majority 2/3 + 삼성·Micron 1/3 | (유지) |
| HBM4 양산 선두 | SK 6개월 선두 | 삼성 업계 최초 양산 (2026.02) | (유지) |
| HBM4 NVIDIA 11Gb/s test | SK 통과 가정 | 삼성 먼저 통과, SK 최적화 중 | (유지) |
| AMD HBM4 | SK 메인 가정 | Samsung preferred (MI455X, 2026.03 MoU) | (유지) |
| Micron HBM4 | 후발 (2026 H2) | 1Q26 volume shipment 진입 | (유지) |
| 1Q26 실적 | 미반영 | 매출 52.6조·OP 37.6조·OPM 72% | (유지) |
| HBM4E narrative | 미언급 | SK 2H26 샘플, 2027 양산 목표 | (유지) |
| 2026 OPM 전망 | 52-55% | 60-62% (상향) | (유지) |
| **Moat 분석 구조** | single 5축 단일 점수 (5.0) | single 5축 (4.6) | **6 segment × 5축 (HBM3E 5.0 / HBM4 NVIDIA 4.4 / HBM4 AMD 2.8 / HBM4E 3.4 / DDR5 4.2 / eSSD 4.0)** |
| **Moat 종합 (가중 평균)** | 5.0 / 5.0 | 4.6 / 5.0 | **4.4 / 5.0 (segment 가중)** |
| CAPA 정의 모호성 | 본 테마 capa 가중 | 본 테마 capa 가중 (모호) | **segment별 명시 (HBM CAPA·DRAM 절대 CAPA·NAND 절대 CAPA 분리)** |

**전체 thesis**: 한국 주도주 후보 #1 위치 **유지**. 단 segment별 강약이 분명해짐 — HBM3E는 절대 우위, HBM4 NVIDIA majority, HBM4 AMD 열위, DDR5/eSSD는 삼성 우위·SK 추격 구조.

---

**End of SK하이닉스_에이전트AI_기업분석.md**
