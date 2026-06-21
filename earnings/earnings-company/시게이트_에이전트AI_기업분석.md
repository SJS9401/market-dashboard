---
ticker: "STX"
company_name: Seagate Technology Holdings plc
country: US
theme_keyword: 에이전트AI
parent_industry: 반도체
cross_ref_industry: 전력 인프라
moat_strength: 4.1              # 본 테마 segment 가중 평균 — WDC 4.0 + Mozaic HAMR 선행 premium
moat_by_segment:
  HDD_nearline_DataCenter: 4.6   # Mass Capacity 84% 집중, WDC와 박빙 + DC 80%
  차세대_HDD_HAMR: 5.0           # ★ Mozaic 양산 글로벌 선행 (WDC 대비 ~1세대 우위)
  사이클_정점_pure_play: 4.5     # HDD pure-play 최대 leverage, GPM 47% record
  자본_환원_king: 4.5            # ★ vs WDC 차별점 — 배당 지속·자사주 재개·FCF margin 30%
  HDD_client: 3.0                # 성숙·축소, 매출 비중 작음
trend_revenue_share: 88
last_updated: 2026-06-21
auto_references:
  - 반도체_산업기초.md (2026-05-18)
  - 전력 인프라_산업기초.md (2026-05-18)
  - 에이전트AI_테마분석.md (v4, 2026-05-26)
  - STX_기업개요.md (v4.9, 2026-05-18)
  - 웨스턴디지털_에이전트AI_기업분석.md (peer 비교 — HDD 양강)
analyst_reports_attached:
  - STX Q3 FY26 8-K (2026-04-28 발표)
  - STX Q3 FY26 Earnings Call (Motley Fool transcript)
  - STX Analyst Day 2025
  - STX Q3 FY26 Supplemental
  - 2026-Q1_STX_리뷰.md (BT 자체)
notes:
  - Seagate는 미국 기업 (아일랜드 등기). 회계연도 6월 마감 (FY26 = 2025-07~2026-06, Q3 FY26 = 2026-Q1 calendar)
  - 본 분석 frame: HDD duopoly의 다른 한 축 — WDC (nearline #1 + 분사) ↔ STX (Mass Capacity 84% + ★ HAMR 선행 + 자본 환원 king). 양사 모두 cold storage layer 본 테마 직접 수혜
---

# 시게이트 (Seagate) 기업 분석 — 에이전트AI 테마

> **본 분석 frame**: 에이전트AI 테마 분석(v4)의 17 segment 중 **STX는 HDD 단일사업(pure-play) + Mass Capacity 84% concentrate + ★ Mozaic HAMR 양산 글로벌 선행**. **WDC (HDD nearline #1 + 분사 스토리) ↔ STX (HDD 글로벌 #1 + ★ HAMR 선행 + 자본 환원 king)** 양강 구도. STX는 **차세대 HDD 기술 (HAMR) 선두 + 자본 환원 우월 + Mozaic 4 (40TB) 양산 시작**으로 WDC와 차별. **★ Q3 FY26 매출 $3.11B (+44% YoY), Non-GAAP GPM 47.0% (사상 최고), EPS $4.10 record + "minimum 20% over the next few years" 가이던스 직접 상향**.

> **점유율·CAPA 표기 기준**: 본 분석의 모든 % 점유율은 **매출 또는 exabyte 기준** (TrendForce·IDC·Trendfocus). HDD 산업은 **WDC 52% nearline / Seagate ~40-45% nearline / Toshiba ~10-15%** 3사 oligopoly. STX는 **HDD 전체 점유 45% 글로벌 #1** (WDC 40% / Toshiba 15%, STX 기업개요 v4.9). **Nearline segment에 한정**하면 WDC가 #1 (52%), STX가 #2 (~40%). 본 분석은 양 기준 병기.

---

## Executive Summary (5줄)

1. **위치**: HDD 글로벌 #1 (45%, WDC 40% / Toshiba 15% 3사 oligopoly) + **Nearline #2 (~40%, WDC 52% 대비 박빙)** + **Mass Capacity 84% concentrate** (FY25). 본 테마 노출 88%. ★ **Mozaic HAMR 양산 글로벌 선행** — Mozaic 3 (30TB) 양산 중 + Mozaic 4 (40TB) March 2026 출하 시작 + Mozaic 5 (50TB) late 2027 qualification (in-house photonics).
2. **해자 종합 (segment 가중)**: <strong>4.1 / 5.0</strong> — HDD nearline 4.6 / 차세대 HDD HAMR **5.0 (★ WDC 4.0 대비 premium)** / 사이클 정점 4.5 / 자본 환원 king 4.5 / Client 3.0. **WDC 4.0 < STX 4.1**.
3. **재무 (HAMR Mozaic 양산 효과 폭발)**: **FY25 매출 $9.10B (+39% YoY) / OP $1.91B / OPM 21.0% (FY14 이후 최고)**. **Q3 FY26 매출 $3.11B (+44% YoY, +10% QoQ) / Non-GAAP GPM 47.0% (사상 최고) / Non-GAAP EPS $4.10 record / OCF $1.1B / FCF $953M (margin 30%+)**. Q4 FY26 가이던스 $3.45B ± $150M / EPS $5.00 ± $0.25.
4. **미래**: ★ **연간 성장 가이던스 직접 상향**: "low-to-mid teens" → **"minimum 20% over the next few years"** (CEO Dave Mosley). **Nearline 용량 FY27까지 거의 완전 할당** ("Vast majority allocated during the next 4 quarters"). FY26E $12.0B (+32%) / FY27E $15.5B (+29%, EPS $22.0).
5. **종합**: <span class="star">★★★ 본 테마 cold storage layer 직접 수혜 + HAMR 양산 선두 premium</span>. (a) HAMR yield 안정 risk (b) WDC EPMR/UltraSMR 추격 (c) SSD 가격 하락 시 cold tier 잠식 risk 3대 risk. (1) ★ Mozaic 양산 선행 (2) 자본 환원 king (배당 + 자사주) (3) FY27 build-to-order 가시성 3대 positive.

---

# 항목 1. 입력 정리 + 기업 포지셔닝

## 1-1. 산업·테마 컨텍스트

- **반도체 산업기초** (v1, 2026-05-18): (A) 구조적 메가 병목 → STX는 **HDD nearline cold storage + HAMR 양산 선행**으로 본 테마 직접 수혜
- **에이전트AI 테마 v4** (2026-05-26): 17 segment 중 **HDD nearline cold storage** segment에서 STX가 WDC와 양강 + HAMR 기술 선두
- **WDC 기업분석 (2026-06-03)**: WDC nearline 52% #1 vs STX nearline ~40% #2. 단 STX **Mozaic HAMR 글로벌 선행** = 차세대 ASP·점유 premium
- **테마 분석 cold storage layer**: 메모리 3사 (Hot/HBM) + SNDK·Solidigm (Warm-Cold/eSSD) + **WDC·STX (Cold/HDD nearline)** layer 분담 구조

## 1-2. STX의 위치 (테마 v4 Moat 후보)

| Segment | 글로벌 점유 (2025-2026) | 순위 | 비고 |
|---|---|---|---|
| **HDD 전체 (매출)** | **45%** | **#1** | WDC 40% / Toshiba 15% 3사 oligopoly |
| **HDD nearline (exabyte)** | **~40%** | **#2** | WDC 52% #1 박빙 |
| **Mass Capacity 비중** | **84%** | — | FY23 64% → FY25 84% 폭증 |
| **★ HAMR Mozaic 양산** | **#1 (글로벌 선행)** | **#1** | Mozaic 3 (30TB) 양산 + Mozaic 4 (40TB) March 출하 + Mozaic 5 (50TB) 2027 qual |
| **★ 5개 global CSP qualified on Mozaic 3+ TB/disk** | — | — | 36TB drive, 나머지 3개 CY2026 H1 완료 예정 |
| **자본 환원 (FCF margin)** | **30%+ (Q3 FY26)** | — | FCF $953M / 매출 $3.11B = 30.6% |
| **Data Center 매출 비중** | **80.4% (Q3 FY26)** | — | $2.5B (+55% YoY) |

→ **HDD 글로벌 #1 + Mass Capacity 84% + ★ HAMR Mozaic 양산 선행**. WDC와 양강이지만 차세대 기술 선두 + 자본 환원 우월로 차별화.

## 1-3. 사업부 구성 (FY25, STX 기업개요 v4.9)

| Segment | FY25 매출 | YoY | 본 테마 연결 | 비중 |
|---|---|---|---|---|
| **Mass Capacity (Cloud/CSP)** | **~$7.65B (84%)** | +60%+ | ★ 본 테마 직접 (HDD nearline + HAMR Mozaic) | **84%** |
| **Legacy (PC·외장·소비자)** | **~$1.45B (16%)** | -5% | 성숙·축소 | **16%** |
| **Total** | **$9.10B** | **+39%** | | 100% |

### 본 테마 직접 매출 노출
- **Mass Capacity 84% × 100%** (CSP·hyperscaler·enterprise nearline + HAMR Mozaic)
- **Legacy 16% × ~25%** (일부 enterprise client·외장 NAS)
- **순 본 테마 직접 노출 = 약 88%** (메모리 3사 60%+ / WDC 88% / SNDK 90% 동급)
- **★ Q3 FY26 Data Center 80% + Exabyte +47% YoY** = AI cold storage secular 본격 가속

---

## ★ 2-0. 에이전트AI 테마 logical flow — 왜 시게이트가 부각받는가

> **정성적 인과 사슬** (테마 v4 narrative → STX 위치 매핑)

### 1단계: 에이전트 AI = 데이터·연산·메모리 폭증의 본질
- 에이전트 1건 = chat 1턴 대비 **토큰 20-30x** (Stanford/NVIDIA 실측, 테마 v4)
- 각 추론 단계·도구 호출·검색·메모리 갱신·tool execution = **연산(GPU/CPU) + 메모리(HBM/DRAM/SSD) + 스토리지(HDD) + IP(ARM) 모든 layer 부하 폭증**
- agent는 stateful → 과거 trace·long-context·compliance 데이터 영구 보존 필요 = secular 누적
- ★ **CEO Mosley quote (Q3 FY26)**: *"On Agentic AI, you need historical data for agents to reason, and you need to store that data for compliance"* — 에이전트 AI = HDD cold tier 직접 수혜 명시

### 2단계: AI 인프라 layer별 분담 — Seagate는 어디 위치?

| Layer | 데이터/연산 유형 | 매체·아이템 | 본 테마 수혜 종목 |
|---|---|---|---|
| **Hot (microsec)** | KV cache, activation, 모델 가중치(active) | **HBM** | SK·삼성·Micron (HBM) |
| **Warm (msec)** | 모델 가중치(off-package), 활성 dataset | **DRAM·SSD** | 메모리 3사 (DRAM) + SNDK·Solidigm (eSSD) |
| **Warm-Cold (sec)** | 검색 코퍼스, 벡터 DB, 최근 로그 | **eSSD QLC·HBF** | SNDK (122TB QLC, HBF) |
| **Cold (수초~분)** | **학습 데이터셋, 체크포인트, 보관 로그, 과거 trace, compliance** | **HDD nearline** | **★ WDC + Seagate (HDD 양강)** |
| **Compute (CPU)** | server CPU + host CPU + client CPU | x86·ARM | Intel·AMD·ARM 라이선시 |
| **Compute (GPU·AI)** | training·inference 가속 | GPU·ASIC | NVIDIA·AMD·ARM |
| **IP layer** | 모든 chip 상위 설계 | ARM IP | ARM Holdings (royalty 광범위) |

→ **Seagate 위치: Cold (HDD nearline) — WDC와 양강. Mass Capacity 84% concentrate로 가장 집중적**

### 3단계: 왜 HDD nearline이 본 테마에서 부각받는가? — 3가지 본질적 이유

1. **데이터 폭증 영구화** → 에이전트 trace·체크포인트·compliance 로그·학습 데이터셋 = stateful agent 부산물 = **장기 보관 필수** → HDD nearline 폭증
2. **GB당 cost 우위 영구화** → HDD GB당 비용 = SSD 대비 **5-10배 저렴** → AI workload 데이터 폭증 시 cold tier는 HDD가 unbeatable cost structure (SSD로 대체 불가 영역)
3. **공급 절제(supply discipline) 누적 → 2026 sold out** → HDD 산업 10년+ 침체 동안 3사 모두 CAPA 증설 정지 → AI 수요 폭증 시 즉시 sold out → 가격·점유·마진 3중 +

### 4단계: 왜 시게이트가 부각? — HAMR 양산 선행 + 자본 환원 king

- **★ Mozaic HAMR 양산 글로벌 선행** — Mozaic 3 (30TB) 양산 + Mozaic 4 (40TB) March 2026 출하 + Mozaic 5 (50TB) late 2027 qualification (in-house photonics 통합)
- **HDD 글로벌 #1 (45%) + Mass Capacity 84% concentrate** — WDC (분사 후 HDD pure)와 다른 차원의 집중
- **★ "최소 20% 성장" 가이던스 직접 상향** (Mosley, Q3 FY26): 이전 "low-to-mid teens" → "minimum 20% over the next few years"
- **★ Nearline 용량 FY27까지 거의 완전 할당** — build-to-order contracts (SNDK NBM과 유사한 multi-quarter 가시성)
- **★ 자본 환원 king** — FY18 이전 capital return 누적 매우 높음, Q3 FY26 부채 $641M 상환 후 **"Next place we go is back to returning value to shareholders"** (Mosley) — 자사주 매입 본격화 시그널

### 5단계: 본 분석 frame 결론

**HDD duopoly 두 축 중 차세대 HAMR 기술 선두 + 자본 환원 우월 + Mass Capacity 84% 가장 집중**. 본 테마 매출 노출 88%, Moat 4.1 (WDC 4.0 대비 HAMR premium). HDD pure-play 사이클 정점 leverage + **build-to-order FY27 가시성**으로 valuation 정당화. 단 HAMR yield 안정 risk + SSD 가격 하락 시 cold tier 잠식 risk 잔존.

---

# 항목 2. 비즈니스 모델 & 해자 (Moat) — ★ 핵심

## 2-1. 비즈니스 모델 (본 테마 사업부 중심)

### Mass Capacity (84% 매출)

- **무엇으로 돈을 버는가**: HDD platter (Mozaic HAMR 30TB·40TB) → CSP·hyperscaler·enterprise nearline storage 시스템에 BoM 공급 → exabyte 단위 build-to-order 계약
- **HAMR 세대별 STX 위치**:
  - **Mozaic 1·2 (구세대, 20-26TB)**: 양산 안정, 기존 nearline 주력
  - **★ Mozaic 3 (30TB, 3+ TB/disk)**: 양산 중 + 5개 global CSP qualified (Q1 FY26)
  - **★ Mozaic 4 (40TB)**: late March 2026 출하 시작, Mozaic 3 → 4 crossover end of CY2026
  - **★ Mozaic 5 (50TB)**: late 2027 qualification, **in-house photonics 통합 (수직 통합)**
- **가격 결정력**: ★ Q3 FY26 매출/EB +5.9% YoY = pricing power 유지 (Mosley: "no changes to pricing strategy"). **2026 공급 매진 + build-to-order = WDC와 동일 가격 결정력 + HAMR premium**
- **고객 구성**: hyperscaler Top 3 (AWS·Azure·Google) + Meta·Oracle·Alibaba·Tencent + 기업 nearline
- **수직 통합**: ★ **in-house photonics** (HAMR 핵심 부품 laser) — WDC·Toshiba는 외부 의존, STX만 자체 supply chain

### Legacy (16% 매출) — 성숙·축소
- PC·노트북·외장·소비자 HDD
- 매출 -5% YoY, 회사 전체 영향 미미 (Mass Capacity +60%+가 압도)
- **점진적 wind down**, FY27까지 비중 10%대로 축소 전망

### 시너지 — HDD pure-play asset-light 모델
- HDD 단일사업 → 사이클 정점 leverage 극대
- ★ **CapEx 효율화**: HAMR 양산 안정으로 CapEx 비중 매출의 4-5% (FY25) → **자본 환원 여력 폭증**
- ★ **수직 통합 (in-house photonics, head media)**: 차세대 노드 trajectory 안정 + 외부 의존도 최소

## 2-2. 해자 (Moat) 깊이 분석 — Segment별 평가 ★

> **분석 frame**: 본 테마 직접 노출 segment 5개 (HDD nearline·차세대 HDD HAMR·사이클 정점 pure-play·자본 환원 king·Client 성숙)별로 STX Moat를 5축 척도로 평가. WDC·Toshiba peer와 직접 비교.

### Segment 1. HDD nearline (Mass Capacity 84% — Data Center 80%)
| 축 | STX | WDC | Toshiba | 핵심 |
|---|---|---|---|---|
| 기술/특허 | **5** (HAMR Mozaic 선행) | 4 (EPMR + 일부 HAMR) | 3 | STX HAMR 양산 글로벌 #1 |
| Mass Capacity 비중 | **5** (84%) | 4 (~70%) | 3 (~60%) | STX 가장 집중 |
| 고객 락인(lock-in) | **5** (★ FY27 build-to-order 거의 완전 할당) | **5** (2026 sold out) | 3 | 양사 동급 lock-in |
| 규모 (nearline 점유) | 4 (~40%, #2) | **5** (52%, #1) | 2 (~8%) | WDC #1 박빙 |
| 병목 포지셔닝 | **5** (HAMR + 2026 sold out) | **5** (2026 sold out) | 3 | 양사 동급 강함 |
| **평균** | **4.8** | **4.6** | **2.8** | **★ STX HAMR 선행 premium** |

> **★ 정성: 왜 HDD nearline이 본 테마에서 부각받는가?**
> 
> **인과 사슬**: 에이전트 AI = 학습 데이터셋·체크포인트·trace·compliance 로그 폭증 → cold storage 수요 영구 + → HDD nearline = SSD 대비 GB당 5-10배 저렴 = 영구 우위 → 공급 절제 누적으로 ★ FY27까지 nearline 거의 완전 할당
> 
> **추가 동력 1 — ★ FY27 build-to-order 거의 완전 할당 (Romano CFO, Q3 FY26)**: *"Vast majority of nearline capacity is allocated during the next 4 quarters"* — SNDK NBM과 유사한 multi-quarter 가시성. P 안정 + Q 가시성 동시
> **추가 동력 2 — HAMR Mozaic 양산 선행으로 cost per TB 우위**: Mozaic 3 (30TB) vs Mozaic 4 (40TB) = capacity 33% 증가 + cost per exabyte 동시 감소 = 마진 + leverage
> **추가 동력 3 — Mass Capacity 84% concentrate (WDC ~70%, Toshiba ~60% 대비)**: STX는 가장 집중적 = data center pure-play
> 
> **STX 위치의 특별함**: nearline 점유는 WDC #1에 박빙 #2이지만 **HAMR 양산 선행 + Mass Capacity 가장 집중**으로 차세대 ASP·점유 premium. 본 segment Moat 4.8로 WDC 4.6 약간 우위

### Segment 2. ★ 차세대 HDD (Mozaic HAMR 양산)
| 축 | STX Mozaic | WDC (UltraSMR + EPMR + HAMR) | Toshiba | 핵심 |
|---|---|---|---|---|
| 기술/특허 | **5** (HAMR 양산 글로벌 선행) | 4 (UltraSMR·EPMR + HAMR 후발) | 3 (HAMR 개발 중) | **★ STX 양산 선행 ~1세대 우위** |
| 양산 CAPA | **5** (Mozaic 3 양산 + Mozaic 4 March 출하) | 4 (UltraSMR 60%+ FY27 + HAMR sample) | 2 | STX 양산 진입 |
| 고객 인증 | **5** (5개 global CSP qualified on Mozaic 3+) | 4 (UltraSMR enterprise 일부) | 2 | ★ CSP 인증 우위 |
| Mozaic 5 (50TB) | **5** (★ in-house photonics, late 2027 qual) | 3 (HAMR roadmap 2H 2026) | 2 | STX 수직 통합 |
| 병목 포지셔닝 | **5** (★ HAMR 양산 선두 + capacity 33% 증가) | 4 (UltraSMR 점진) | 2 | STX 차세대 ASP premium |
| **평균** | **5.0** | **3.8** | **2.2** | **★ STX 차세대 HDD 절대 선두** |

> **★ 정성: 왜 차세대 HDD (HAMR Mozaic)가 STX thesis 정점인가?**
> 
> **인과 사슬**: HDD nearline 수요 폭증 + 기존 PMR (perpendicular magnetic recording) 용량 한계 → HAMR (Heat-Assisted Magnetic Recording) 차세대 기술 필수 → ★ STX Mozaic 양산 글로벌 선행 (WDC 대비 ~1세대 우위) → Mozaic 3 (30TB) 양산 중 + Mozaic 4 (40TB) March 2026 출하 + Mozaic 5 (50TB) 2027 → 차세대 ASP·점유 premium 영구
> 
> **추가 동력 1 — ★ Mozaic 4 (40TB) March 2026 출하 시작**: Mozaic 3 → Mozaic 4 crossover end of calendar 2026 = capacity 33% 증가 = exabyte 출하 + leverage. ★ Q3 FY26 Exabyte 175 EB (+47% YoY)
> **추가 동력 2 — ★ 5개 global CSP qualified on Mozaic 3+ TB/disk**: hyperscaler 인증 통과 = lock-in + 알로케이션 우선권. 나머지 3개 CY2026 H1 완료 예정
> **추가 동력 3 — ★ Mozaic 5 in-house photonics 통합 (수직 통합)**: HAMR laser 자체 공급 = WDC·Toshiba 외부 의존 대비 supply chain 우위 + 차세대 노드 trajectory 안정
> 
> **STX 위치의 특별함**: 본 segment Moat 5.0으로 STX 최강 segment. **WDC 대비 ~1세대 기술 우위** = HDD duopoly의 차세대 dominance 선점. WDC EPMR/UltraSMR은 PMR 변형 (단기 회피), STX HAMR은 차세대 patform (영구 대안)

### Segment 3. 사이클 정점 leverage (HDD pure-play 최대 진폭)
| 축 | STX | WDC (분사 후) | SNDK | 핵심 |
|---|---|---|---|---|
| 사이클 진폭 (OPM range, 12년) | **±23pt** (-2.2 ~ +21.0, FY14-FY25) | ±41pt (분사 효과 축소) | ±61pt (NAND 최대) | STX 안정 |
| 현재 정점 (Non-GAAP) | **GPM 47.0% record + EPS $4.10 record (Q3 FY26)** | GM 50.5% record (Q3 FY26) | OPM 70.9% record (Q3 FY26) | 동급 정점 |
| 정점 매출 가속 | **+44% YoY (Q3 FY26)** | +45% YoY | +251% YoY | STX·WDC 동급 |
| 침체 risk | -2.2% OPM 적자 (FY23) | -10% (분사 전) | -25% (FY23) | STX 가장 안정 |
| **평균 (정점)** | **4.5** | **4.5** | **5.0** | **STX = WDC 동급, SNDK 더 sharp** |

> **★ 정성: 왜 사이클 정점 leverage가 STX thesis 핵심인가?**
> 
> **인과 사슬**: STX = HDD pure-play → 사이클 진폭 ±23pt (FY14 21.0% ~ FY23 -2.2%) → 정점 GPM 47% record + EPS $4.10 record → HDD nearline 사이클 정점 + HAMR premium 동시 = 매출 + & 마진 + double leverage
> 
> **추가 동력 1 — ★ 사이클 진폭 ±23pt (WDC 분사 후 ±41pt 대비 안정)**: STX는 분사 없이도 사이클 진폭 작음 = 침체 risk 가장 작은 HDD pure-play
> **추가 동력 2 — ★ 정점 GPM 47% record (Q3 FY26) + EPS $4.10 record**: HAMR ramp + nearline sold out + 가격 결정력 유지 trifecta
> **추가 동력 3 — ★ FY27 build-to-order = 사이클 변동성 추가 축소**: Multi-quarter 가시성으로 사이클 정점에서 침체 risk 감소
> 
> **STX 위치의 특별함**: HDD pure-play + 분사 무관 + 사이클 진폭 최소 + 정점 GPM record. **WDC는 분사로 진폭 축소, STX는 분사 없이도 진폭 가장 안정** = HDD 양강 중 가장 방어적 모델

### Segment 4. ★ 자본 환원 king (vs WDC 분사 차별 segment)
| 축 | STX | WDC (분사 후) | 비교 |
|---|---|---|---|
| FCF margin | **30%+ (Q3 FY26 = $953M / $3.11B)** | ~25% (Q3 FY26) | STX 우위 |
| 배당 정책 | **★ 지속 배당 (분기 $0.72, FY18 이후 유지)** | 일시 중단 → 재개 시도 | STX 우위 |
| 자사주 매입 | **★ Q3 FY26 부채 $641M 상환 후 본격 재개 시그널** (Mosley: "Next place we go is back to returning value to shareholders") | 분사 1년차 성장 투자 우선 | STX 우위 |
| 자본 환원 누적 (12년) | **$10B+ (배당 + 자사주 + 부채 상환)** | $5B+ (분사 전 누적, 분사 후 재시작) | STX 압도 |
| PBR 비교 | 자사주 누적으로 자본 인위적 축소 (PBR 부적합) | 분사로 일부 자본 재정비 | STX 더 극단 |
| **평균** | **4.5** | **4.0** | **★ STX 자본 환원 king** |

> **★ 정성: 왜 자본 환원이 STX vs WDC 핵심 차별점인가?**
> 
> **인과 사슬**: WDC는 NAND 분사 (2025-02)로 분사 1년차 성장 투자 우선 → 배당 일시 중단 → STX는 분사 없이 HDD pure로 안정 + ★ FCF margin 30%+ + ★ 부채 $641M 상환 (Q3 FY26) + ★ "Next place we go is back to returning value to shareholders" → **자본 환원 king 위치 재확인**
> 
> **추가 동력 1 — ★ 배당 지속 (FY18 이후 분기 $0.72 유지)**: WDC는 분사로 배당 일시 중단, STX는 사이클 정점·침체 무관 배당 지속 = capital return king
> **추가 동력 2 — ★ Q3 FY26 부채 $641M 상환 → 자사주 매입 본격 시그널**: 부채 감소 + FCF 폭증 + Mosley 명시 = 자사주 재개 임박
> **추가 동력 3 — ★ FCF margin 30%+ (HDD pure asset-light)**: CapEx 효율화 + HAMR 양산 안정 = FCF 폭증 = 자본 환원 여력 누적
> 
> **STX 위치의 특별함**: **WDC 분사 스토리 vs STX 자본 환원 king** — HDD duopoly 두 축의 정반대 strategic angle. WDC = 성장 투자 + 분사 프리미엄, STX = 안정 환원 + HAMR 선두. **PER + EV/EBITDA + FCF Yield 혼합 valuation 가능 = WDC 분사 1년차 valuation 어려움 대비 simpler thesis**

### Segment 5. HDD client (PC·외장) — 성숙·축소
| 축 | STX | WDC | 핵심 |
|---|---|---|---|
| 시장 성장 | 마이너스 (SSD 잠식) | 마이너스 | 동급 |
| 매출 비중 | 16% (Mass Capacity 84% 대비) | 10% (Cloud 89% 대비) | 동급 |
| **평균** | **3.0** | **3.0** | **양사 모두 본 테마 영향 미미** |

> **★ 정성: 왜 이 segment는 부각받지 못하는가?**
> 
> **인과 사슬**: PC·노트북·외장 시장 = SSD가 HDD 잠식 progressing → client HDD = secular 축소 → 본 테마와 거의 무관
> 
> **STX 입장**: client 매출 비중 16% (Mass Capacity 84% 대비)로 매우 작음 → 본 분석 frame에서 영향 미미
> **단기 wind down narrative**: Legacy 매출 -5% YoY 지속, 회사 전체 매출에 부정 영향 미미 (Mass Capacity +60%+가 압도)

### 본 테마 가중 종합 (Moat × 매출 비중)

| Segment | 매출 비중 | STX 평균 Moat | 가중 기여 | WDC 비교 |
|---|---|---|---|---|
| HDD nearline (Mass Capacity) | 70% | **4.8** | 3.36 | WDC 4.6 (STX 약간 우위) |
| 차세대 HDD HAMR | (overlay) | **5.0** | **+0.5 overlay** | WDC 3.8 (★ STX 절대 우위) |
| 사이클 정점 pure-play | (overlay) | **4.5** | overlay | WDC 4.5 (동급) |
| 자본 환원 king | (overlay) | **4.5** | **+0.3 overlay** | WDC 4.0 (★ STX 우위) |
| Client | 16% | 3.0 | 0.48 | WDC 3.0 (동급) |
| **합계 (overlay 포함)** | **88%** | **가중 평균 4.1** | — | WDC 4.0 |

### 핵심 종합 결론

**STX의 Moat는 WDC 대비 + premium (차세대 HAMR 선두 + 자본 환원 king)**:

| 구간 | STX 포지셔닝 |
|---|---|
| **HDD nearline** | **박빙 #2 (4.8)** — WDC 52% 대비 ~40%이지만 Mass Capacity 84% 가장 집중 |
| **★ 차세대 HDD HAMR** | **절대 선두 (5.0)** — Mozaic 양산 + Mozaic 4 (40TB) March 출하 + in-house photonics |
| **★ 자본 환원 king** | **우위 (4.5)** — vs WDC 분사 차별 segment, 배당 지속·자사주 재개 |
| **사이클 정점** | **동급 (4.5)** — GPM 47% record, ±23pt 진폭 가장 안정 |
| **Client** | 영향 미미 (3.0) — Legacy 16% wind down |

→ **종합 Moat 4.1** (WDC 4.0 + HAMR premium 0.1). **인텔 2.8 < AMD 3.8 < Micron·SNDK·WDC 4.0 < STX 4.1 < ARM 4.1 ≤ 삼성 4.3 < SK 4.4**.

## 2-3. 병목 수혜 강도 정량화

### 본 테마 직접 수혜 메커니즘

| 본 테마 병목 | STX 수혜 메커니즘 | 카테고리 | 정량 추정 |
|---|---|---|---|
| **AI cold storage ↑** | nearline #2 (~40% exabyte), Mass Capacity 84% | (A) 구조적 메가 병목 | DC 매출 $2.5B (Q3 FY26, +55% YoY) |
| **데이터 폭증 (training set, 체크포인트, compliance)** | Exabyte 출하 175 EB Q3 FY26 (+47% YoY) | (A) | 매출/EB +5.9% YoY (pricing power) |
| **★ 차세대 HAMR ↑** | Mozaic 3 (30TB) 양산 + Mozaic 4 (40TB) March 출하 | (D) 동반 확대 | 5개 CSP qualified + capacity 33% 증가 |
| **★ FY27 nearline 거의 완전 할당** | build-to-order multi-quarter 가시성 | (A) | "Minimum 20% over the next few years" |
| **HDD vs SSD 가격 우위** | GB당 5-10x 저렴 = 영구 cold tier 우위 | (A) | secular cost advantage |

→ **STX = 본 테마 cold storage layer 직접 수혜 + HAMR 선두 premium**. WDC와 동일 layer + 차세대 기술 우위 + 자본 환원 우월.

### vs WDC 비교 (HDD 양강의 정반대 strategic angle)

| 차원 | WDC (분사 + nearline #1) | **STX (HDD #1 + HAMR 선두 + 자본 환원 king)** |
|---|---|---|
| 본 테마 노출 | 88% | **88%** |
| 본 테마 layer | cold (nearline) | **cold (nearline) + ★ HAMR 선두** |
| Moat 종합 | 4.0 | **4.1 (+ HAMR premium)** |
| Strategic angle | NAND 분사 (2025-02), HDD pure 재시작 | HDD pure 안정 + HAMR 양산 선행 |
| 사이클 진폭 (12년 OPM) | ±41pt (분사 효과 축소) | **±23pt (가장 안정)** |
| 정점 OPM | GM 50.5% (Q3 FY26) | GPM 47% (Q3 FY26) |
| 차세대 기술 | UltraSMR + EPMR + HAMR (후발) | **★ Mozaic HAMR 양산 선행 (~1세대 우위)** |
| 자본 환원 | 분사 1년차 성장 투자 우선 | **★ 배당 지속 + 자사주 재개 시그널** |
| Multi-quarter 가시성 | 2026 sold out | **★ FY27 거의 완전 할당** (4 quarters out) |
| 사이클 leverage | sharp (분사 1년차 매출 +60%) | **안정 secular** (HAMR + 자본 환원) |

**핵심 차이**: WDC = 분사 프리미엄 + nearline #1 점유, **STX = HAMR 선두 + 자본 환원 king + Mass Capacity 가장 집중**. 양사 모두 본 테마 직접 수혜, 단 risk-reward 프로파일 다름. **WDC는 분사 후 1년차 성장 가속, STX는 안정 환원 + 차세대 dominance 선점**.

---

# 항목 3. 재무 분석

## 3-1. 실적 추이 — 12년 매출·OPM·EPS (Mozaic HAMR 변곡점)

| FY | 매출 ($B) | YoY | OP ($B) | OPM | NPM | EPS ($) | 사이클 |
|---|---|---|---|---|---|---|---|
| FY14 | 13.74 | — | 1.93 | **14.0%** | 11.7% | — | 1차 정점 (pre-SSD) |
| FY15 | 13.74 | 0% | 1.78 | 13.0% | 11.3% | — | 유지 |
| FY16 | 11.16 | -19% | 0.79 | 7.1% | 2.3% | — | SSD 잠식 시작 |
| FY17 | 10.77 | -3% | 0.99 | 9.2% | 7.0% | — | 회복 |
| FY18 | 11.18 | +4% | 1.55 | 13.9% | 11.0% | — | mini peak |
| FY19 | 10.39 | -7% | 1.20 | 11.6% | 9.9% | — | |
| FY20 | 10.51 | +1% | 1.06 | 10.1% | 9.6% | — | |
| FY21 | 10.68 | +2% | 1.27 | 11.9% | 10.4% | — | |
| FY22 | 11.66 | +9% | 1.62 | 13.9% | 13.5% | — | 코로나 IT |
| FY23 | 7.38 | -37% | -0.16 | **-2.2%** | -10.3% | — | 메모리 다운사이클 저점 (적자) |
| FY24 | 6.55 | -11% | 0.43 | 6.6% | 5.6% | 0.79 | 회복 초기 |
| **FY25** | **9.10** | **+39%** | **1.91** | **21.0%** | 16.1% | **7.40** | **★ Mozaic HAMR 양산 본격화, 2차 정점 진입** |
| **FY26E (Post-Q3)** | **12.0** | **+32%** | — | — | — | **14.50** | **★ HAMR ramp + nearline sold out** |
| **FY27E** | **15.5** | **+29%** | — | — | — | **22.00** | **★ Mozaic 4 + 5 + build-to-order** |

**OPM range (12년)**: -2.2% ~ +21.0% = **23.2%pt** (WDC 분사 후 ±41pt 대비 안정, HDD pure-play 중 가장 작은 진폭)

## 3-2. PQC 분해 — Mass Capacity vs Legacy 비교 (FY25 → Q3 FY26)

| 차원 | Legacy (PC·외장) | Mass Capacity (Cloud/CSP) | 비고 |
|---|---|---|---|
| **P (ASP, $/TB)** | -3% YoY (성숙) | **+5.9% YoY ($14.3/TB, Q3 FY26)** | ★ Mass Capacity pricing power |
| **Q (exabyte 출하)** | -8% YoY (SSD 잠식) | **+47% YoY (175 EB, Q3 FY26)** | ★ Mass Capacity 폭증 |
| **C (원가 구조)** | 일반 PMR, marginal cost | Mozaic HAMR 자본 효율적, 마진 +leverage | ★ HAMR cost per exabyte -10% YoY |
| **매출 = P × Q** | -11% YoY ($1.45B FY25) | **+60%+ YoY ($7.65B FY25)** | Mass Capacity 폭증 |
| **마진 (Non-GAAP GPM)** | ~20% (성숙) | **47%+ (Q3 FY26)** | **★ 해자 작동 신호** |

→ **Mass Capacity vs Legacy = 매출·마진·점유 모든 축에서 양극화**. ★ Mass Capacity가 회사 thesis 본질, Legacy는 wind down 진행.

## 3-3. 재무 건전성 & 자본 환원

- **부채비율**: Q3 FY26 부채 $641M 상환 후 순부채/EBITDA ~1.5x (HDD pure-play 안정)
- **이자보상배율**: EBITDA $1.2B vs 이자비용 $70M = **17배 (매우 안정)**
- **OCF/FCF**: Q3 FY26 OCF $1.1B + FCF $953M (FCF margin **30%+**)
- **자본 환원**:
  - **★ 배당 지속 (FY18 이후 분기 $0.72, 무중단)** — 사이클 정점·침체 무관
  - **★ 자사주 매입 본격 재개 시그널** (Mosley: "Next place we go is back to returning value to shareholders")
  - 12년 누적 capital return $10B+ (배당 + 자사주)
- **CapEx 부담**: 매출의 4-5% (FY25) — HDD asset-light 모델 안정 + HAMR 양산 안정 후 추가 감소 가능

## 3-4. 수익성 트렌드 — 회사 레벨

- **GPM 추이**: FY24 24% → FY25 32% → ★ Q3 FY26 47.0% record (12분기 연속 +180bps QoQ)
- **OPM 추이**: FY24 6.6% → FY25 21.0% → Q3 FY26 Non-GAAP ~30%+
- **NPM 추이**: FY24 5.6% → FY25 16.1% → Q3 FY26 ~25%+
- **vs WDC 비교**: GPM 동급 (WDC GM 50.5% vs STX GPM 47.0%) + EPS leverage 동급. **OPM leverage STX 약간 약함** (Mass Capacity 84% concentrate로 fixed cost 분산)
- **vs SNDK 비교**: 사이클 진폭 STX (±23pt) < WDC (±41pt) < SNDK (±61pt). **STX 정점 OPM은 SNDK 70.9% 대비 약함, 단 사이클 안정성 압도**

---

# 항목 4. 성장성 분석

## 4-1. 과거 성장률 (CAGR)

| 기간 | 매출 CAGR | OP CAGR | EPS CAGR |
|---|---|---|---|
| 3년 (FY22→FY25) | -7.8% (다운사이클 후 회복) | +5.6% | +급증 (FY24 적자 → FY25 $7.40) |
| 5년 (FY20→FY25) | -2.8% (SSD 잠식 후 HAMR 회복) | +12% | +급증 |
| 12년 (FY13→FY25) | -3.5% (SSD 잠식 + 다운사이클) | -0.1% | — |

→ **12년 CAGR 마이너스이지만 FY24 저점 → FY25 +39% 회복 + ★ FY26·FY27 +30% 가속 = 차세대 사이클 진입**.

## 4-2. 향후 성장 가시성 — 미래 PQC 전망

| 차원 | 전망 | 근거 | 6 카테고리 연동 |
|---|---|---|---|
| **P 전망** | ★ ASP 안정 + Mozaic 4 premium | 매출/EB +5.9% YoY (Q3 FY26), no pricing changes | (A) 구조적 메가 병목 = 안정 P |
| **Q 전망** | ★ Exabyte +47% YoY 지속 | Mozaic 4 (40TB) March 출하, capacity 33% 증가 | (A) + (D) = 폭증 |
| **C 전망** | HAMR cost per exabyte 추가 -10% YoY | Mozaic 4 vs Mozaic 3 cost 효율화 | 마진 + 지속 |
| **→ 매출 성장 가시성** | **★ "최소 20% over the next few years"** | Mosley CEO 가이던스 직접 상향 (Q3 FY26) | ★ build-to-order FY27 가시성 |
| **→ 마진 지속 가능성** | **★ GPM 47% → 48-50% 추가 상승** | Q4 FY26 가이던스 ~48.5% | ★ Mozaic mix shift |

### 수주잔고/백로그
- ★ **Nearline 용량 FY27까지 거의 완전 할당** (Romano CFO): "Vast majority of nearline capacity is allocated during the next 4 quarters"
- SNDK $42B NBM과 유사한 multi-quarter 가시성 = ★ 매출 변동성 축소
- Q4 FY26 가이던스 매출 $3.45B ± $150M, EPS $5.00 ± $0.25 = +48% YoY

### 성장 지속성 구조적 근거 + 저해 리스크
**구조적 +**:
- 에이전트 AI = 데이터 영구 보존 필수 (compliance) — Mosley quote
- HDD vs SSD GB당 5-10x 가격 우위 영구
- HAMR Mozaic 양산 선행 = 차세대 ASP·점유 premium
- HDD oligopoly 3사 + 공급 절제 누적

**저해 risk**:
- HAMR yield 안정 risk (Mozaic 4·5 ramp 시)
- WDC EPMR/UltraSMR 추격 (단기적 PMR 변형으로 30-40TB 가능)
- SSD 가격 하락 시 cold tier 일부 잠식 (장기적, 5년+)
- 다운사이클 진입 시 사이클성 (FY23 -2.2% OPM 적자 재현 risk)

### OPM 지속 가능성
- Q3 FY26 GPM 47% record + Q4 가이던스 ~48.5%
- **★ FY27 build-to-order = OPM 변동성 축소**
- 단 사이클 다운 진입 시 -10pt 가능 (FY23 사이클 reference)

## 4-3. 피어 그룹 비교

| 기업 | 매출 CAGR (3년) | Non-GAAP GPM | 핵심 차이점 |
|---|---|---|---|
| **STX** | **-7.8% (다운→회복)** | **47% (Q3 FY26 record)** | ★ HAMR Mozaic 양산 선행 + 자본 환원 king + Mass Capacity 84% |
| **WDC (분사 후)** | +50% (FY26E 추정) | 50.5% (Q3 FY26) | nearline 52% #1 + 분사 스토리 + UltraSMR/EPMR 가속 |
| **SNDK (NAND pure)** | +150% (FY26E) | 78%+ (NAND 사이클) | NAND pure + 사이클 진폭 ±61pt + $42B NBM |
| Toshiba | -10% (정체) | ~25% (HDD only) | 3위 15%, 매각 가능성 거론 |

→ **STX vs WDC = HDD 양강 동등 사이클 정점**, 단 ★ STX HAMR 선두 + 자본 환원 king으로 차별. SNDK는 다른 layer (NAND warm-cold).

---

# 항목 5. 통합 모드 입력용 Fact 정리

(테마 분석 통합 모드가 점유율·마진·Terminal 추정 시 사용할 raw fact)

| 항목 | 정리 |
|---|---|
| **현재 시장 점유율** | HDD 전체 45% #1 (WDC 40%, Toshiba 15%), Nearline ~40% #2 (WDC 52% #1) |
| **CAPA + 발표 증설 계획** | CapEx 매출의 4-5% (HAMR 양산 안정 후 효율화) |
| **현재 사업부별 마진** | Mass Capacity GPM ~50% / Legacy GPM ~20% / 회사 전체 47% (Q3 FY26) |
| **사이클 진폭** | OPM 12년 ±23pt (-2.2% ~ +21.0%) |
| **기술 격차** | ★ HAMR Mozaic 양산 글로벌 선행 (~1세대 우위 vs WDC) + in-house photonics 통합 |
| **R&D 강도** | 매출의 ~5% (FY25), HDD asset-light |
| **핵심 특허** | HAMR Mozaic platform + in-house photonics + heat-assisted recording technology |
| **고객사 분포** | hyperscaler Top 3 (AWS·Azure·Google) ~40% + Meta·Oracle·Alibaba·Tencent + 기업 nearline |
| **신규 수주** | ★ 5개 global CSP qualified on Mozaic 3+, 나머지 3개 CY2026 H1 완료 예정. FY27 nearline 거의 완전 할당 |
| **자본 환원 누적** | 12년 $10B+ (배당 + 자사주). 배당 분기 $0.72 (FY18~), 자사주 재개 시그널 |
| **현재 EV/EBITDA·PER·FCF Yield** | (분기 실적 분석에서 cross-ref) |

---

# 항목 6. 구조적 트리거 모니터링

(단기 진입 시그널은 분기 실적 분석. 여기는 구조적·본질적 변화만)

## 상방 트리거

- ★ **Mozaic 4 (40TB) qualification 통과** (CY2026 H1) — 추가 CSP 인증
- ★ **Mozaic 5 (50TB) qualification 시작** (late 2027) — in-house photonics 검증
- **자사주 매입 본격 재개 발표** (Q4 FY26 또는 FY27 Q1)
- WDC EPMR/UltraSMR ramp 지연 (STX HAMR 우위 강화)
- Toshiba 매각·인수 (STX 점유 추가 확대 catalyst)

## 하방 트리거

- HAMR yield 안정성 issue (Mozaic 4·5 ramp 지연)
- WDC EPMR 30-40TB 양산 가속 (HAMR 우위 축소)
- 다운사이클 진입 (FY23 -2.2% OPM 재현)
- CSP CapEx 동시 cut (드물지만 가능)

## 모니터링 캘린더

- **Q4 FY26 실적** (2026-08, 예정): 매출 가이던스 비트 여부 + 자사주 재개 발표
- **STX Analyst Day 2026** (예상): Mozaic 5 roadmap update + 자본 환원 가이던스
- **WDC Q3 FY26 실적** (2026-Q3): EPMR/UltraSMR ramp 비교
- **Hyperscaler CapEx 가이던스** (분기별): AWS·Microsoft·Google·Meta

---

# 종합 판단

## 매트릭스

| 차원 | 평가 | 근거 |
|---|---|---|
| **메가 트렌드 적합성** | ★★★ | 에이전트 AI = cold storage 폭증 (Mosley quote) |
| **산업 위치** | ★★★ | HDD #1 (45%) + Mass Capacity 84% concentrate |
| **해자 강도** | 4.1 / 5.0 | HAMR 선두 premium + 자본 환원 king |
| **재무 건전성** | ★★★ | FCF margin 30%+, 부채 상환, 배당 무중단 |
| **성장 가시성** | ★★★ | FY27 build-to-order, "Minimum 20% over the next few years" |

## 핵심 투자 포인트 3

1. **★ HAMR Mozaic 양산 글로벌 선행 (vs WDC ~1세대 우위)**: Mozaic 3 양산 + Mozaic 4 (40TB) March 출하 + Mozaic 5 (50TB) 2027 in-house photonics. 5개 global CSP qualified로 lock-in 강화. 차세대 ASP·점유 premium 영구.
2. **★ 자본 환원 king (vs WDC 분사 차별)**: 배당 무중단 (FY18~), Q3 FY26 부채 $641M 상환 후 자사주 재개 시그널, FCF margin 30%+. WDC는 분사 1년차 성장 투자 우선 vs STX는 안정 환원 → valuation simpler thesis.
3. **★ FY27 build-to-order 가시성 + "Minimum 20%" 가이던스 상향**: Nearline 거의 완전 할당 (Romano CFO) = SNDK $42B NBM 유사 multi-quarter 가시성. Mosley 가이던스 직접 상향 ("low-to-mid teens" → "minimum 20% over the next few years").

## 핵심 리스크 3

1. **HAMR yield 안정 risk**: Mozaic 4·5 ramp 시 yield issue 가능 (WDC EPMR/UltraSMR는 검증된 PMR 변형). yield 지연 시 ASP·매출 plan 차질.
2. **WDC EPMR/UltraSMR 추격 + Nearline #1 유지**: WDC 점유 52% > STX ~40%. WDC가 EPMR 60%+ FY27 양산 가속 + UltraSMR 30-40TB 시장 진입 시 HAMR 우위 축소.
3. **SSD 가격 하락 시 cold tier 일부 잠식 (장기)**: SSD GB당 가격 하락 가속 시 HDD cold tier 일부 잠식 가능. 단기 5년+ 영향 제한, 장기 risk.

→ **종합**: <span class="star">★★★ HDD duopoly의 차세대 dominance 선점 종목</span>. WDC와 동급 본 테마 직접 수혜이지만 ★ HAMR Mozaic 양산 선행 + ★ 자본 환원 king + ★ FY27 build-to-order로 valuation premium 정당화.

---

# 향후 관찰 포인트

1. **Mozaic 4 (40TB) qualification 진행** (CY2026 H1) — CSP 인증 통과 수
2. **자사주 매입 본격 재개 발표 시점** (Q4 FY26 또는 FY27 Q1)
3. **Q4 FY26 가이던스 ($3.45B ± $150M, EPS $5.00 ± $0.25) 비트 여부**
4. **WDC EPMR/UltraSMR ramp 비교** (HAMR 우위 유지 vs 추격)
5. **Mozaic 5 (50TB) qualification 시작** (late 2027) — in-house photonics 검증
6. **Toshiba 매각·인수 동향** (HDD oligopoly 재편 catalyst)

---

## 부록: v1 changelog

**v1 (2026-06-21)**: 최초 작성
- WDC 분석 frame 채택 + Phase 2 (logical flow 2-0) + Phase 3 (Segment별 정성 narrative) 통합
- HDD duopoly의 다른 한 축 — WDC (분사 + nearline #1) vs STX (★ HAMR 선두 + 자본 환원 king)
- Mozaic HAMR 양산 선행 + Mass Capacity 84% concentrate + FY27 build-to-order 강조
- Moat 4.1 = WDC 4.0 + HAMR premium 0.1
- Q3 FY26 GPM 47% record + EPS $4.10 record + "Minimum 20% over the next few years" 가이던스 상향 반영
