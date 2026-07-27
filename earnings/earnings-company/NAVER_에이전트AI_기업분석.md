---
ticker: "035420"
company_name: NAVER
country: KR
theme_keyword: 에이전트AI
sub_theme: 한국 Neocloud/AI Factory (sovereign AI)
parent_industry: 클라우드
moat_strength: 3.2                # 1~5 종합 척도 (하기 채점 근거)
moat_subscores:
  tech: 3                          # HyperCLOVA X + DSX platform (그러나 GPU cloud 운영 미검증)
  capa: 3                          # 200MW→1GW 계획 있으나 미준공 (55MW 1H27 가동)
  customer_lockin: 4               # 국내 검색·커머스·핀테크 생태계 + 공공 CSAP + sovereign 정책
  scale: 3                         # 국내 #1, 글로벌 하이퍼스케일러·CoreWeave 대비 소형
trend_revenue_share: 5             # % (현재 AI Factory 매출 fact 비중, 클라우드 부문 KRW 171.8B ÷ 총매출 12.04T = 1.4%. 사업부 넓게 잡을 시 5% 이내)
last_updated: 2026-07-27
handoff_source: 에이전트AI_테마분석.md v5.1 (반도체/에이전트AI 세션 → 클라우드 세션)
overview_ref: null                 # NAVER_기업개요.md 미존재 — fact 정확도 일부 부족 명시
---

# NAVER (035420) 기업 심층 분석 — 에이전트AI 테마 (한국 Neocloud/AI Factory)

> **본 리포트의 frame**: "네이버 = 한국의 코어위브" narrative의 해자 검증. Pure-play CoreWeave 대비 mixed NAVER의 밸류에이션·수익성·실행력이 본 분석의 핵심. **단위 밸류에이션·Terminal 밸류는 본 스킬에서 다루지 않음** (분기 실적 분석·테마 분석 통합 모드에 위임).
>
> **자동 참조 상태**: 클라우드_산업기초.md (v1.0 2026-05-18) ✓ / 에이전트AI_테마분석.md v5.1 (2026-07-27) ✓ / NAVER_기업개요.md **누락 (실적 분석 세션에서 미작성)** — 재무 fact는 IR·보도 기반으로 보완하되 사업보고서 원본 대조 미이행 명시.

---

## Executive Summary (5줄)

1. **NAVER는 "국내 IaaS+SaaS(HyperCLOVA X)+검색 광고+커머스+핀테크+콘텐츠"의 conglomerate**이며, 2026-07-24 발표된 $10B AI Factory 프로젝트(NVIDIA $1B + Brookfield $9B nonbinding + NAVER 자기부담)로 **"한국의 코어위브"라는 신규 밸류에이션 렌즈**가 시장에 강제 주입됐다.
2. **해자 종합 3.2/5 — 국내 sovereign lock-in(4)이 핵심이고 tech·capa·scale은 3점대**. CoreWeave 대비 순수 GPU cloud 실행력(SemiAnalysis ClusterMAX "Unavailable Tier")·규모(NVIDIA→CoreWeave $225B급 backlog vs NAVER 20조 목표는 계획)·자본조달 자립도 모두 미검증. **국내 sovereign 카테고리(정책·데이터·언어) 안에서는 준독점 경쟁자 부재**가 유일한 강한 해자.
3. **"코어위브 멀티플"이 NAVER 전체에 적용되는 것은 부당 — AI Factory 사업은 현재 fact 매출 비중 1-5% 미만**. CoreWeave (2026E $12-13B, P/S forward 3.8-4.0x) 프리미엄을 NAVER 시총 31조원 전체에 씌우면 검색·커머스 등 기존 12조 매출 사업이 오히려 저평가 이슈. **적정 접근 = SoTP 방식으로 AI Factory 사업부만 CoreWeave 프록시 적용 + 기존 사업부는 개별 멀티플**.
4. **NVIDIA 신주 7,241,564주 @204,500원 (1.48조원, 4.5% stake) 신주 발행 → 8/3 자사주 4.9백만주(~1조) 소각으로 순 희석 완화 (실질 희석 ~1.5%)**. 시장 우려는 dilution보다 **Brookfield $9B nonbinding term sheet의 실제 이행 리스크** — credit 환경 악화 시 첫 철회 후보 (이그전 자본공급자 프레임).
5. **투자 판단 = "narrative 견인 O, 수익성 검증 X, sovereign moat O, 실행력 U"**. 단기(1년) 주가는 narrative 지속으로 상방 유지 가능, **중기(2-3년) trigger = 55MW 1H27 가동 후 GPU cloud 매출·마진 실측치**. **하방 최대 risk = Brookfield 이탈 (자본구조 붕괴) + NAVER 자체 CapEx 자립 시 FCF 붕괴**.

---

# 항목 1. 입력 정리 + 기업 포지셔닝

## 1-1. 산업·테마 컨텍스트 요약

### 클라우드 산업기초 핵심 (2026-05-18 base)
- 클라우드 산업 전체 위치 = **(A) 구조적 메가 병목** (수요 급증 × 공급 제한). Big 4 하이퍼스케일러 2026 CapEx 합계 $725B (+77% YoY).
- 레이어별 분화: **인프라(전력·DC·HBM·GPU) = A 극단** / IaaS = A / SaaS = E~중립.
- Neocloud 카테고리(CoreWeave·Nebius·Lambda·Crusoe·CRWV IPO 2026.3)가 유일한 신규 진입 경로 — **"전력 확보 + GPU 임대" 단일 BM + 자본은 사모·채권 시장에서 조달** (자본집약).
- 한국 IaaS(네이버·NHN·KT)의 산업기초 시점(2026-05) 진단: "글로벌 경쟁력 없음, 정부 클라우드 네이티브 전환 정책 수혜 한정". → **v5.1 (2026-07) 이 진단이 뒤집힘**.

### 에이전트AI 테마분석 v5.1 핵심 (2026-07-27)
- 테마 병목 = **(A) 구조적 메가 병목 + (D) 동반 확대 hybrid**. 에이전트 1건 = chat 대비 토큰 **20-30x**.
- **★ 신설 #18 segment: 한국 Neocloud/AI Factory (sovereign AI), 카테고리 (D) 동반 확대**.
  - ASP 안정 (GPU cloud 시세 연동) + Q 폭증 (55MW → 1GW).
  - 향후 (B) 수요 견인 전환 가능.
- 한국 접근 TAM 기존 $216-262B → **$226-277B+** (AI Factory +$10-15B 추가).
- 글로벌 peer = **CoreWeave (미국 #1 Neocloud, NVIDIA 투자 + $225B급 backlog), Lambda, Nebius**.
- 한국 플레이어 = **NAVER (GAK 세종 #1), SK Group (SKT GW급, 2GW+), 삼성SDS·KT클라우드 (후보)**.

### 테마 분석의 Moat 후보 리스트 중 NAVER 위치
- v5.1 add-on에서 NAVER는 **한국 Neocloud/AI Factory segment의 #1 플레이어**로 명시.
- 다만 v5.1의 14개사 thesis 영향 매핑에서 NAVER는 별도 종목 라인이 아니라 **"수요 주체" 프레임에 위치**(빅테크 4사 macro layer와 동일 계열의 "국가 단위 발주자" 등장).
- **본 리포트가 검증할 것**: NAVER 자체가 "공급 측 Moat 보유 기업"인지, 아니면 단지 "수요 주체 겸 자본조달자"에 그치는지.

## 1-2. NAVER 기업 포지셔닝

### 밸류체인 위치 (클라우드 산업기초 5 레이어 매핑)

| 레이어 | NAVER 활동 | 강도 |
|---|---|---|
| ① 전력·DC | GAK 세종 hyperscale DC 자체 보유·건설 중 (55MW→200MW→1GW). Government National Growth Fund 400B 저리대출 (2026-04) | ★★★ (신규 강화) |
| ② 서버·GPU·메모리 | NVIDIA DSX platform 도입 (H200/B200/Rubin 예정). GPU 260K 배치 계획 중 60K 공용 클라우드 | ★★ (NVIDIA 파트너로 승격) |
| ③ 네트워킹·광 | DSX 표준 채택 (NVIDIA reference architecture) | ★ (수동적) |
| ④ IaaS | 네이버 클라우드 (한국 한정) — 공공·금융·게임 | ★★ (국내 #1, 글로벌 microscopic) |
| ⑤ PaaS | HyperCLOVA X + NVIDIA Nemotron 3 Ultra fine-tune (sovereign 한국어 모델) | ★★ (국내 #1) |
| ⑥ SaaS | 검색광고·네이버플러스·N페이·CHZZK·웹툰·라인프렌즈 (자체 SaaS 콘텐츠 자산) | ★★★ (한국 #1 인터넷 SaaS) |
| ⑦ SI/MSP | 별도 사업부 아님 | - |

→ **NAVER는 클라우드 밸류체인 5 레이어 중 5개(①②④⑤⑥)에 걸친 vertically integrated 플레이어**. 이건 CoreWeave (단일 레이어 ①+②+④의 인프라 pure-play)와 근본적으로 다른 구조.

### 사업부 구성 (Q1 2026 재분류 기준)

Q1 2026부터 revenue classification 개편: **NAVER Platform (Ads·Services) / Financial Platform / Global Initiatives (C2C·Content·Enterprise)** 3분류. (기존은 서치플랫폼·커머스·핀테크·콘텐츠·엔터프라이즈 5분류)

Q1 2026 매출 (KRW):

| 사업부 | Q1 2026 매출 | YoY | 비고 |
|---|---|---|---|
| **NAVER Platform (Ads·Services)** | 1.8398조 | +14.7% | 광고 견조 + 커머스 서비스 +35.6% |
| **Financial Platform** | 459.7B | +18.9% | N페이 payment volume KRW 24.2조 (+23.4%) |
| **Global Initiatives (C2C·Content·Enterprise)** | 941.6B | +18.4% | Poshmark·라인·웹툰 + **Enterprise(클라우드 포함) 재분류** |
| **총 매출** | **3.2411조** | **+16.3%** | OPM 16.7% |
| 영업이익 | 541.8B | +7.2% | |

FY2025 참고:
- 총매출 12.04조원 (+12.1%), 영업이익 2.21조원 (+11.6%)
- **클라우드 부문 KRW 171.8B (연간)**, 엔터프라이즈 연간 587.8B (+4.3% YoY, GPUaaS·사우디 super app·디지털 트윈 견인)
- Content 영업이익 456.7B, Fintech 영업이익 453.1B

### 이 테마(에이전트AI/Neocloud)와 직접 연결된 사업부

- **AI Factory / GPU cloud 부문 (Global Initiatives의 Enterprise 하위)**:
  - FY25 클라우드 매출 KRW 171.8B = 총매출의 **1.4%**
  - 엔터프라이즈 전체(587.8B, HyperCLOVA·GPUaaS·해외 포함) = **4.9%**
  - AI Factory 20조원 매출 목표 = 현재 대비 100x 성장 필요 시나리오 (근거·시점 IR 발표 그대로, 회계 fact 아님 [전망])

- **간접 시너지 사업부**:
  - HyperCLOVA X → 검색 광고·커머스·핀테크 개인화·CHZZK 콘텐츠 추천 (모든 사업부 관통)
  - GAK 세종 DC → 내부 사용 + 외부 GPU cloud 겸용

## 1-3. 상위 트렌드 매출 비중

- **현재 fact**: AI Factory·GPU cloud 직접 매출 = 총매출의 **1.4% (좁게) ~ 4.9% (엔터프라이즈 전체)**
- **2028E 전망**: NAVER IR 목표 20조원 매출 = 2025 대비 매출 규모의 **~1.7배 규모 신사업 신설 시나리오** [전망, IR 목표]
- **자본 배분 관점**: $10B AI Factory 총투자 규모는 2025 매출(12조원=$9B)을 **초과**하는 규모. 현재 회사 규모 대비 **자산 double-down 결정**

---

# 항목 2. 비즈니스 모델 & 해자 (Moat) — **핵심**

## 2-1. AI Factory 사업부 BM

### 무엇으로 돈을 버는가

| 매출 vector | 설명 | 참고 peer |
|---|---|---|
| **GPU 시간당 임대 (IaaS-GPU)** | H200/B200/Rubin 인스턴스 시간당 종량제 + 다년 reserve. 한국·미국 AI 이노베이터 대상 | CoreWeave, Lambda, Nebius |
| **HyperCLOVA X API (PaaS-AI 모델)** | 한국어 LLM API 사용료 (chat, agent, embedding). Nemotron 3 Ultra fine-tune 기반 | OpenAI API, Anthropic API (한국어 특화 프리미엄) |
| **Sovereign IaaS (공공·금융 특화)** | CSAP 인증 기반 공공·금융 클라우드 (경쟁 배제 영역) | 국내 NHN Cloud, KT Cloud, 삼성SDS |
| **Enterprise SaaS on HyperCLOVA** | 사우디 super app·디지털 트윈 등 해외 프로젝트 | 없음 (틈새) |

### 원가 구조 (Neocloud 모델 기본)

| 원가 항목 | 비중 (Neocloud 표준) | NAVER 특이점 |
|---|---|---|
| GPU 감가상각 | 40-50% | NVIDIA와 파트너십으로 조달 우선순위 확보 (긍정) / 그러나 200MW 200K GPU 등 규모는 미실측 |
| 전력·냉각 OpEx | 20-30% | 한국 산업용 전력요금은 미국 대비 저렴하나, 1GW급 신규 전력 확보 자체가 리스크 (한국 전력망 제약) |
| DC 감가상각 | 15-20% | GAK 세종 자체 소유 → REIT 임차료 없음 (긍정) |
| 인력·운영 | 5-10% | GPU cloud 운영 SRE 경험치 부족 (ClusterMAX Unavailable = 검증 미달) |

### 다른 사업부와의 시너지

- **검색·커머스·핀테크의 데이터 → HyperCLOVA 학습·튜닝 원재료** (한국 데이터 lock-in)
- **HyperCLOVA → 검색광고·커머스 개인화 → 광고 CTR·GMV 상승** (내부 순환)
- **GAK 세종 → 내부 워크로드 + 외부 GPU cloud 겸용** (utilization 개선 여지)
- → **NAVER는 CoreWeave에는 없는 "내부 앵커 수요 + 데이터 자산"을 갖고 있음**. 이는 Neocloud pure-play가 못 갖는 강점.

## 2-2. 해자 (Moat) 깊이 분석

### Moat 종류별 점수 (5점 척도)

| Moat 종류 | 점수 | 근거 |
|---|---|---|
| **기술·특허 (tech)** | **3/5** | HyperCLOVA X (한국어 sovereign LLM) + NVIDIA DSX platform + Nemotron fine-tune 파트너십. **그러나 GPU cloud 운영 SW·SRE 스택은 미검증 (ClusterMAX Unavailable)**. CoreWeave는 SlurmGPU·Weka·NCP native 스택 3-4년 축적. NVIDIA·Anthropic·OpenAI 대비 뒤진 자체 모델 등급 |
| **CAPA·자본 (capa)** | **3/5** | GAK 세종 hyperscale DC 자체 소유 (긍정). 55MW 1H27 가동 → 200MW 2028 → 1GW 장기 계획. **아직 준공되지 않은 계획 단계**. Brookfield $9B nonbinding 조달 시 실현 가능성 UP but 미확정 |
| **고객 lock-in (customer)** | **4/5** | ★ 국내 검색·커머스·핀테크·콘텐츠 생태계 lock-in (해자 최강 부분). CSAP 공공 클라우드 인증 = 외산 진입 배제. Sovereign 정책 driven 수요(정부 2030년 1만 시스템). Nemotron fine-tune으로 한국어 API 우위. **단, 이 lock-in은 국내 한정** — 글로벌 시장에서는 lock-in 없음 |
| **규모의 경제 (scale)** | **3/5** | 국내 인터넷·SaaS #1 (매출 12조원) — 규모 있음. 그러나 IaaS·GPU cloud 순수 규모는 CoreWeave TTM $6.23B (2026E $12-13B) 대비 NAVER GPU cloud 매출은 극소 (fact 1000억 원대 이하) — **글로벌 IaaS·Neocloud 대비 microscopic** |
| **네트워크 효과 (network)** | **참고 3/5** | 인터넷 서비스(검색·커머스·핀테크·CHZZK)에서는 강한 네트워크 효과, GPU cloud 사업 자체는 network effect 없음 |
| **규제 장벽 (regulation)** | **참고 4/5** | CSAP + sovereign 정책 = 국내 방어. 반대로 해외 진출에는 규제가 방어벽 아닌 장애 |

### Moat 종합 점수: **3.2/5** (내부 종합)

**5점 척도 anchor 위치**:
- 5 (절대 우위) = ASML EUV / NVIDIA CUDA
- 4 (강력) = TSMC 파운드리 / Salesforce CRM / SK하이닉스 HBM
- **3 (평균 이상) = 국내 인터넷 #1 + Neocloud 후발 진입자 = NAVER 현재 위치** ← 여기
- 2 (평균 또는 약함)
- 1 (약함)

### Moat 지속성

| 시점 | Moat 유효성 판단 | 약화·강화 시그널 |
|---|---|---|
| **2년 (2028)** | 3.2 → **3.5로 상승 가능** | 조건: 55MW 가동 성공 + Brookfield $9B 실질 집행 + 200MW 완공. 실패 시 3.0 이하 |
| **5년 (2031)** | 3.5 → **3.0~4.0 시나리오 분화** | 상방: 1GW 완공 + 해외 sovereign 수요 확보 + HyperCLOVA 글로벌 진입. 하방: CoreWeave·글로벌 하이퍼스케일러가 한국 리전 강화 → sovereign lock-in 약화 |
| **10년 (2036)** | **불확실** | 클라우드 자체 산업 구조 변화 (분산 컴퓨팅·on-device AI·양자 컴퓨팅 등) 예측 불가 |

### 글로벌 peer 비교 — 같은 병목(Neocloud) 경쟁자

| Peer | Moat | 주요 강점 | NAVER 대비 |
|---|---|---|---|
| **CoreWeave (CRWV)** | ~4.0 | ClusterMAX Platinum (유일 산업 표준) / NVIDIA 우선 순위 배정 / $225B급 backlog / 3-4년 순수 GPU cloud SRE 축적 / 2026E $12-13B, ARR $18-19B | **NAVER는 실행력·규모 모두 미달**. 유일 우위 = sovereign lock-in |
| **Nebius (NBIS)** | ~3.5 | 유럽 데이터 주권 + Yandex 인프라 유산 | 유사 (sovereign) — but 유럽 CSP 진입 강함 |
| **Lambda** | ~3.3 | 학습용 GPU + SW 커뮤니티 | NAVER는 커뮤니티 미보유 |
| **Crusoe** | ~3.5 | 저비용 전력 (텍사스 flare gas) | NAVER는 전력 확보가 리스크 |
| **한국 국내: SK Group (SKT GW급)** | ~3.5 | ★ NVIDIA-SK Group 2GW+ AI DC (SKT AI cloud + 하이닉스 HBM + 두산 SMR·발전) — **재벌 그룹 수직 통합 + HBM 자체 조달** | NAVER 대비 자본·인프라·수직 통합에서 앞섬. **국내에서 NAVER의 최대 경쟁자** |
| **한국 국내: 삼성SDS, KT Cloud** | ~3.0 | 그룹 IT + 공공 실적 | NAVER 대비 sovereign AI 카테고리에서는 늦음 |

### 포지셔닝 결론

**NAVER = "국내 sovereign AI 시장의 준독점 후보 + 글로벌 Neocloud 시장의 후발 미검증 진입자"** — 두 시장의 성격을 이중으로 갖고 있어 단일 프레임(예: 코어위브 pure-play 프리미엄)으로 평가하면 왜곡.

**빠른 추격자 (challenger)** 카테고리보다는 **틈새 독점 (국내 sovereign)** 카테고리에 더 가깝다. 글로벌 Neocloud 시장 리더 지위를 두고 CoreWeave·Nebius와 경쟁하는 것은 fact가 아닌 narrative.

## 2-3. 병목 수혜 강도 정량화

### 테마 병목 + 카테고리 (D) 동반 확대 → 수혜 메커니즘

| 수혜 메커니즘 | 강도 | 정량 추정 |
|---|---|---|
| **가격 결정력** | 중 | ASP는 글로벌 GPU cloud 시세 연동 (H200 시간당 $30-50 등). 국내 sovereign 프리미엄 +10-30% 가능 |
| **점유율** | 중~강 | 국내 sovereign GPU cloud 시장 점유 40-60% 가능 (SK와 양분). 글로벌 시장 점유는 <1% |
| **마진** | **약 (약점)** | Neocloud 모델 자체가 자본집약·저마진 (CoreWeave 손실). NAVER도 초기 마이너스 → BEP 도달 시점 미검증. 규모의 경제 도달 전에는 OPM -10% ~ 5% 시나리오 [전망] |
| **신규 시장** | 강 | Sovereign AI Factory = 없던 시장 (D 카테고리). 초기 진입자 프리미엄 |

### 수혜 정량 추정 (2028E 시나리오)

| 시나리오 | AI Factory 매출 | OPM | 영업이익 기여 |
|---|---|---|---|
| **낙관** | 5-8조원 (55→200MW 완공 + 90%+ 활용) | 10-15% | 5000-1.2조 |
| **중립** | 2-4조원 (55→100MW 부분 완공 + 60-70% 활용) | 0-5% | -1000-2000억 |
| **비관** | 0.5-1조원 (55MW만 가동 + 활용 저조) | -20~-10% | -1000~-2000억 |
| NAVER 회사 목표 (2028+) | **20조원** | 미공개 | - |

→ **회사 목표 20조원과 중립·비관 시나리오의 gap이 크다**. narrative는 낙관 시나리오 반영 중이나, **operating fact는 아직 어느 시나리오도 확정할 evidence가 없음**.

---

# 항목 3. 재무 분석

## 3-1. 실적 추이 (사업부 mix 관점)

> ⚠️ **NAVER_기업개요.md 미존재** — 10년 연간 + 12분기 시계열은 실적 분석 세션이 owns. 본 리포트는 최근 3년 요약과 사업부 mix 중심.

### 최근 3년 연간

| 연도 | 총매출 | YoY | 영업이익 | OPM | 클라우드 매출 | 클라우드 비중 |
|---|---|---|---|---|---|---|
| 2023 | 9.67조 | +17.6% | 1.49조 | 15.4% | - | - |
| 2024 | 10.74조 | +11.1% | 1.98조 | 18.5% | - | - |
| **2025** | **12.04조** | **+12.1%** | **2.21조** | **18.4%** | **171.8B** | **1.4%** |
| Q1 2026 | 3.24조 | +16.3% | 541.8B | 16.7% | (엔터프라이즈 재분류 이후 별도 공시 대기) | - |

### 사업부별 (Q1 2026 재분류 기준)

| 사업부 | Q1 2026 매출 | YoY | 특징 |
|---|---|---|---|
| NAVER Platform (Ads·Services) | 1.84조 | +14.7% | 커머스 서비스 매출 +35.6% |
| Financial Platform | 460B | +18.9% | N페이 GMV +23.4% |
| Global Initiatives (C2C·Content·Enterprise) | 942B | +18.4% | Poshmark·라인·웹툰·클라우드·HyperCLOVA·해외 |

**해자 작동 신호 관점**:
- 광고·커머스 사업부는 국내 인터넷 lock-in의 결과 → 성숙기이지만 안정
- Financial Platform은 확장기 → N페이 lock-in 강화 중
- Global Initiatives의 Enterprise(클라우드) 하위 = **에이전트AI 테마 노출부** — 재분류 이후 별도 disaggregation 미공개가 아쉬움

## 3-2. PQC 분해 — 일반 사업 vs AI Factory 사업

### 일반 사업 (검색광고·커머스·핀테크) vs AI Factory (신설)

| 차원 | 일반 사업 (검색·커머스·핀테크) | AI Factory / GPU cloud | 해자 작동 signal |
|---|---|---|---|
| **P (단가)** | 광고 CPM 안정·소폭 상승 / 커머스 take-rate 3-5% 상승 / N페이 fee 안정 | GPU 시간당 시세 (H200 $30-50, B200 $50-70) — 글로벌 시세 연동. 국내 sovereign +10-30% 프리미엄 가능 [전망] | P는 두 사업 모두 안정. **AI Factory는 P 결정력이 sovereign 프리미엄에서 나옴 (강함) vs 글로벌 시세 연동 (약함)** 상충 |
| **Q (물량)** | GMV·검색·페이 볼륨 저성장(한 자릿수 후반~두 자릿수 초반) | **폭증 예정** (55MW → 200MW → 1GW = 20배). GPU 260K 중 60K 공용 예정 | AI Factory Q는 CAPA 자체가 driver — CoreWeave 성장 pattern 참고 |
| **C (원가)** | 인건비·데이터센터·마케팅 → 마진 안정 | GPU 감가상각 40-50% + 전력 20-30% + DC 15-20% + 인력 5-10%. **원가 구조가 완전 다름 (자본집약)** | 원가 구조가 다른 사업을 회사 평균 OPM으로 볼 수 없음 → SoTP 필요 |
| **매출 성장** | 12-16% YoY (Q1 2026) | 현재 미미(2028+ 폭증 시나리오) | 두 사업의 성장률·마진 프로파일이 근본적으로 다름 |
| **마진** | OPM 16-18% (안정) | **초기 -10% ~ +5%** (BEP 도달 미검증) | ★ **AI Factory 사업이 회사 전체 OPM을 낮출 것** (자본집약·저마진 특성). 순수 코어위브 프리미엄 부당한 이유 |

### 핵심 인식

**AI Factory 사업부의 PQC 프로파일 = 검색·커머스와 완전 다른 종류의 사업**. 두 사업을 하나의 회사 OPM(현재 16-18%)으로 평가하면 왜곡. **AI Factory 사업 편입 후 회사 OPM은 오히려 하락 압박**. 이는 리스크가 아니라 **자본집약 사업의 본질**.

→ **밸류에이션은 반드시 SoTP (Sum of the Parts)**:
- 기존 사업부 (광고·커머스·핀테크·콘텐츠): 성숙기 OPM 안정 → PER·EV/EBITDA 방식
- AI Factory 사업부: 성장기 자본집약 → P/S 방식 (CoreWeave 프록시)

## 3-3. 재무 건전성 & 유상증자

### 최근 재무 건전성 (사업보고서 미대조 — 대략 IR 기준)

- 부채비율: 최근 안정적 100% 미만 유지
- 순차입금/EBITDA: 낮음 (역사적으로 순현금 or 낮은 순차입)
- OCF: 안정적 (내수 인터넷 사업 특성)
- FCF: 안정 (CapEx는 회사 규모 대비 낮음, 지금까지)

### ★ NVIDIA 신주 발행 (2026-07)

| 항목 | 내용 |
|---|---|
| 신주 규모 | 7,241,564주 |
| 발행가 | 204,500원 |
| 조달금액 | KRW 1.4809조원 (~$1B) |
| NVIDIA stake | 4.5% (신주 발행 후 기준) |
| 발행 후 순서 | NPS·BlackRock 다음 3대주주 |

### ★ 상쇄 조치 — 자사주 소각 (2026-08-03 예정)

- 소각 규모: 약 4.9백만주 (KRW 1조원 상당)
- 순 희석 계산:
  - 발행 전 발행주식수 (대략): 약 1.5-1.6억주 (KRW 기준 시총 31조 ÷ 주가 22.7만원)
  - 신주 7.24M주 발행 = **+4.5% 희석**
  - 자사주 4.9M주 소각 = **-3.0% 상쇄**
  - **순 희석 = ~1.5%** (실질적으로 매우 완화)

**해석**: 시장이 dilution을 크게 우려할 이유는 없음. 신주 발행가 204,500원은 발표 시점 주가 대비 discount 없음 (7/24 종가 ~200,000원 수준 base로 시가 발행). NVIDIA는 3년 lock-up 없이 자유 매도 가능 (fact 확인 필요) — 그러나 NVIDIA가 CoreWeave 지분과 유사 전략적 파트너십으로 유지할 유인 강함.

### ★ Brookfield $9B nonbinding 리스크 (핵심)

| 항목 | 상세 |
|---|---|
| 규모 | 최대 $9B (~13조 원) — NAVER 시총 31조의 42% 수준 |
| 성격 | **exclusive capital partner, nonbinding term sheet** (구속력 없음) |
| 위치 | AI Factory 인프라 조달 (외부 인프라 펀드) |
| 이그전 프레임 | "자본공급자" 첫 사례 → credit 환경 악화 시 첫 철회 후보 |
| Precedent | 다른 인프라 프로젝트 유사 term sheet가 실제 이행되지 않은 사례 다수 (미국 offshore wind 등) |
| 모니터링 지표 | Oracle CDS, Neocloud 채권 스프레드, 미국 금리 |

**만약 Brookfield가 이탈하면**:
- NAVER 자체 CapEx 부담 = $9B → 회사 자체 FCF 붕괴 or 추가 유상증자 필요
- 55MW → 200MW → 1GW 로드맵의 실제 실현 속도 지연 or 축소
- narrative "한국의 코어위브" 지속성 훼손 → 주가 조정

**만약 Brookfield가 실제 집행하면**:
- NAVER 자체 CapEx 부담 최소화 → FCF 방어
- Neocloud playbook (자본은 외부 인프라 펀드 조달) 성공 사례로 검증
- narrative 강화

## 3-4. 수익성 트렌드 — 회사 레벨

### 회사 전체 OPM 장기 추이

- 2023: 15.4% → 2024: 18.5% → 2025: 18.4% → Q1 2026: 16.7%
- **AI Factory 사업 편입 후 회사 OPM은 하락 압박 예상** (자본집약 저마진 편입 효과)
- 낙관 시나리오도 AI Factory 초기 OPM은 5-10% 수준, 회사 blended OPM 하락은 불가피

### 피어 대비 수익성 비교

| 비교 대상 | OPM (2025) | 사업 특성 |
|---|---|---|
| NAVER | 18.4% | 국내 인터넷 광고·커머스 + 클라우드 초기 |
| 카카오 | 5-8% | 유사 사업 mix, 콘텐츠 비중 큼 |
| Google (Alphabet) | 30%+ | 글로벌 광고 dominant |
| Alibaba | 15% 내외 | 커머스 + 클라우드 mix |
| Salesforce | 20%+ | 순수 SaaS |
| **CoreWeave** | **-25%~-30% (GAAP)** | 순수 Neocloud, adj EBITDA 25%+ but GAAP 큰 손실 |
| Snowflake | -20%~0% | PaaS 데이터 |

→ NAVER는 mix의 결과로 국내 카카오보다 훨씬 높은 OPM. **AI Factory 편입 후 CoreWeave·Snowflake 방향으로 OPM이 이동할 것 = 회사 성숙 프레임 변경**.

---

# 항목 4. 성장성 분석

## 4-1. 과거 성장률

| 지표 | 3년 CAGR (2022-2025) | 5년 CAGR |
|---|---|---|
| 매출 | ~13% | ~15% |
| 영업이익 | ~10% | ~13% |
| EPS | 유사 | - |

→ 매출·이익 두 자릿수 초반 안정 성장. 국내 인터넷 시장 성숙 반영. **AI Factory가 매출·이익 성장률의 새로운 driver로 편입될 수 있는지가 향후 3-5년 판단 포인트**.

## 4-2. 향후 성장 가시성 — 미래 PQC 전망

**병목 카테고리 (D) 동반 확대 — anchor**: ASP 안정 + Q 폭증. 즉 매출 성장의 driver는 P가 아닌 Q.

| 차원 | 전망 | 근거 | 6 카테고리 anchor |
|---|---|---|---|
| **P 전망** | 안정 (~시세 연동) + sovereign 프리미엄 10-30% 가능 | GPU cloud 시장이 CoreWeave·하이퍼스케일러 다각화로 경쟁 심화 | (D): 안정 |
| **Q 전망** | ★ **폭증 (2027-2030)** | 55MW (1H27) → 100MW (2H27) → 200MW (2028) → 1GW (장기). **CAPA 자체가 driver** | (D): 폭증 |
| **C 전망** | 자본집약·초기 저마진 → 규모 성숙 후 마진 상승 (CoreWeave 궤도 참고) | GPU 감가상각 + 전력 + DC. 규모의 경제·utilization 개선에 마진 달림 | - |
| **→ 매출 성장** | ★★★ 급성장 잠재 | AI Factory 20조 목표 달성 시 회사 매출 +100% (2028+) [전망] | |
| **→ 마진 지속** | ★ 초기 하락 압박, 중장기 회복 시나리오 | 자본집약 사업 편입 → OPM 감소 + 자본집약 사업 성숙 시 OPM 회복 (BEP → 흑자 전환) | |

### 수주잔고·백로그

- **CoreWeave와의 결정적 차이**: CoreWeave는 $225B급 계약 backlog (OpenAI·MSFT 등 대형 앵커 고객)이 있는 반면, **NAVER는 명시적 backlog fact 미공개**. 앵커 고객이 없음 (또는 미공개)
- **잠재 앵커**: HyperCLOVA X 사용 국내 대기업, 정부 공공, 사우디 super app 등 — narrative는 있으나 backlog 정량 없음
- **NVIDIA·Brookfield는 조달측 파트너지 앵커 고객이 아님** (혼동 주의)

### 성장 지속성 구조적 근거 + 저해 리스크

**구조적 근거**:
1. 한국 sovereign AI 정책 driven (정부 2030년 1만 시스템 클라우드 전환, 400B 저리대출)
2. 한국어 LLM 데이터·튜닝 lock-in (Naver 검색·커머스 데이터 자산)
3. NVIDIA 파트너십 → GPU 우선 배정
4. GAK 세종 자체 소유 → 임차료 절감

**저해 리스크**:
1. 전력망 제약 (1GW급 계통 연결 실제 병목)
2. GPU cloud 운영 경험 (ClusterMAX Unavailable)
3. Brookfield 이탈 시 CapEx 자립 부담
4. 글로벌 하이퍼스케일러의 한국 리전 강화 (AWS·Azure 한국 리전 확장 시 sovereign lock-in 약화)

### OPM 지속 가능성

- **단기(1-2년)**: 기존 사업부 OPM 16-18% 유지 가능. AI Factory 초기 손실은 회사 전체 OPM에 -1~-3%p 영향
- **중기(3-5년)**: AI Factory 규모 확장 → OPM -3~-5%p 영향 가능 (자본집약 사업 편입 효과)
- **장기(5-10년)**: AI Factory BEP·흑자 전환 시 회사 blended OPM 15-20% 회복 시나리오

## 4-3. 피어 그룹 비교

| 기업 | 매출 CAGR (3y) | OPM (2025) | 핵심 차이점 |
|---|---|---|---|
| **NAVER** | ~13% | 18.4% | 국내 인터넷 mix + Neocloud 후발 진입 |
| CoreWeave | 100%+ (2년 CAGR) | -25% (GAAP) | 순수 GPU cloud, 앵커 고객 (MSFT·OpenAI) |
| Nebius | 100%+ | 마이너스 | 유럽 sovereign |
| 카카오 | 5-8% | 5-8% | 유사 mix, AI Factory 부재 |
| Google | 12-15% | 30%+ | 글로벌 광고 dominant |
| Alibaba | 5-8% | 15% | 커머스 + 클라우드 |

→ NAVER의 사업 성장률·수익성은 국내 인터넷 성숙기 기준으로 견조. **CoreWeave와 직접 비교는 원리적으로 부적절 — 다른 사업 카테고리**. 굳이 비교하면 "국내 안정 + AI Factory upside optionality" 조합.

---

# 항목 5. 통합 모드 입력용 Fact 정리

> 테마 분석 통합 모드가 점유율·마진·Terminal 도달 기간을 추정할 때 사용할 fact·raw data만 정리. 추정·예측은 통합 모드의 역할.

| 항목 | 정리 |
|---|---|
| **국내 sovereign IaaS 점유율 (fact + 추이)** | Q1 2026 NAVER 엔터프라이즈 매출 +18.8% YoY, NHN 클라우드 +20.2%, KT Cloud +0.4%, 삼성SDS 클라우드 +23.5% (2024 base). 국내 sovereign 카테고리 CR2 ~50%+ 추정 (NAVER + 삼성SDS). AI Factory 가동 후 NAVER +30-40%p 점유 예상 [전망] |
| **CAPA 실측치 + 발표된 증설 계획** | GAK 세종 55MW (1H27 가동 예정, 미준공) → 100MW (2H27) → 200MW (2028, NVIDIA DSX + Brookfield $9B 이행 조건) → 1GW (장기). GPU: 260K 중 60K 공용 (fact 발표 기준) |
| **현재 사업부별 마진 구조** | 회사 전체 OPM 18.4% (2025). 사업부별 세부 마진은 별도 disaggregation 미공개 |
| **기술 격차** | HyperCLOVA X + Nemotron 3 Ultra fine-tune (한국어 sovereign LLM). ClusterMAX Unavailable (GPU cloud 운영 SW·SRE 미검증) |
| **고객 분포·집중도** | Q1 2026 재분류로 세부 미공개. 국내 검색 광고 M/S ~55-60% (Naver 검색 + 자회사), 커머스 GMV 국내 top 3. AI Factory 앵커 고객 fact 없음 |
| **자본 조달 이력 + 최근 이벤트** | NVIDIA 신주 7,241,564주 @204,500원 (KRW 1.48조, 4.5% stake). 자사주 4.9M주 소각 (2026-08-03 예정, ~1조). Brookfield $9B (nonbinding). Government National Growth Fund 400B 저리대출 (2026-04) |
| **peer 멀티플 히스토리** | CoreWeave 시총 ~$48B / TTM 매출 $6.23B = P/S ~7.7x, 2026E 매출 $12-13B → forward P/S 3.8-4.0x. NAVER 시총 31.05조 / 2025 매출 12.04조 = P/S ~2.6x (회사 전체) |

---

# 항목 6. 구조적 트리거 모니터링

## 상방 트리거

1. **★ 55MW 1H27 실제 가동 + 초기 GPU cloud 매출·마진 공개** — 실행력 검증 이벤트 (narrative → fact 전환 트리거)
2. **Brookfield $9B nonbinding → binding 전환 공시** — 자본 구조 확정, 이그전 자본공급자 프레임 실증
3. **글로벌 앵커 고객 계약 공시** (해외 AI lab, 정부 sovereign 계약 등) — CoreWeave의 OpenAI·MSFT 계약과 유사 이벤트
4. **HyperCLOVA X 국내외 API 매출 정량 disclosure** — sovereign LLM의 P·Q 정량화

## 하방 트리거

1. **★ Brookfield 이탈 or 축소 공시** — 자본구조 붕괴, narrative 훼손 최대 위험
2. **한국 전력망 계통 연결 지연** (200MW 이상 hyperscale DC 그리드 승인) — 로드맵 지연 실현
3. **글로벌 하이퍼스케일러 한국 리전 대폭 확장** (AWS·Azure·GCP) — sovereign lock-in 약화
4. **GAK 세종 초기 utilization 저조 or ClusterMAX 등급 개선 실패** — 실행력 미검증 확정
5. **국내 sovereign 경쟁 심화**: SK Group 2GW+ AI DC (SKT + 하이닉스 + 두산) 실질 가동 → NAVER 국내 준독점 지위 약화

## 모니터링 캘린더

| 시점 | 이벤트 | 관찰 포인트 |
|---|---|---|
| 2026 Q3-Q4 | Q2·Q3 실적 발표 | 재분류 이후 Enterprise 하위 disaggregation 여부 |
| 2026 하반기 | Brookfield term sheet 진행 | binding 전환·집행 스케줄 |
| 2027 상반기 | 55MW 첫 가동 예정 | 실질 GPU cloud 서비스 launch, 초기 고객 |
| 2027 하반기 | 100MW 확장 예정 | 진척도 fact 확인 |
| 2028 | 200MW 완공 목표 + AI Factory 매출 20조 목표 진척 | 회사 목표 달성 vs 시장 예상 gap |
| 상시 | SemiAnalysis ClusterMAX 등급 재평가 | Unavailable → 상위 tier 진입 여부 |
| 상시 | NVIDIA·Anthropic·OpenAI 한국 발주 뉴스 | 앵커 고객 확보 evidence |
| 상시 | Oracle CDS·Neocloud 채권 스프레드 | 자본공급자 프레임 스트레스 지표 (Brookfield 이탈 선행 신호) |

> 분기 실적 분석이 본 트리거의 현재 상태를 점검. narrative shift 감지 시 본 .md 갱신.

---

# 종합 판단

## 매트릭스

| 축 | 평가 | 근거 |
|---|---|---|
| **상위 트렌드 적합성** | ★★★ 높음 | 에이전트AI/AI 인프라 메가 정면 노출 (테마 v5.1 #18 segment) |
| **산업 위치** | ★★ 중 | Neocloud 후발 진입자 (글로벌) + 국내 sovereign #1 후보 |
| **해자 강도** | ★★★ 3.2/5 (중상) | Customer lock-in(4) 강함, tech·capa·scale은 3점대 |
| **재무 건전성** | ★★★ 견조 | 순현금 기반 + NVIDIA 신주로 자본 유입 + Brookfield 조달 여지 |
| **성장 가시성** | ★★ 중 (upside optionality) | AI Factory 성공 시 매출 doubling 가능. 실패 시 기존 성장률 12-13% 유지 |

## 핵심 투자 포인트 3

1. **"한국의 코어위브" narrative의 유일한 순수 대표주** — 국내 sovereign AI Factory 카테고리 자체가 없던 시장(D). NAVER가 국내 #1 후보 지위를 legitimacy 있게 확보한 첫 이벤트가 2026-07-24 NVIDIA 신주 발행. 이 자체가 국내 시장에서 반복 재평가되기 어려운 이벤트.
2. **CoreWeave·Nebius가 못 갖는 "내부 앵커 수요 + 데이터 자산" 구조** — 검색·커머스·핀테크·콘텐츠 사업이 HyperCLOVA X의 지속적 튜닝 데이터·utilization 수요를 자동 공급. Neocloud pure-play의 최대 약점(앵커 고객 편중)을 자체적으로 해소.
3. **NVIDIA·Brookfield·정부 3자 자본 조달로 자체 CapEx 최소화** — Neocloud playbook (자본은 외부 조달, 회사는 인프라 운영·데이터 소유)의 한국 첫 사례. Brookfield 이행 시 회사 FCF·balance sheet 압박 최소.

## 핵심 리스크 3

1. **★ Brookfield $9B nonbinding term sheet 이탈 리스크 (최대 위험)** — 이그전 자본공급자 프레임상 credit 환경 악화 시 첫 철회 후보. 이탈 시 NAVER 자체 CapEx 부담 $9B → FCF 붕괴 or 추가 유상증자 → narrative 훼손. Oracle CDS·Neocloud 채권 스프레드가 선행 신호.
2. **GPU cloud 실행력 미검증 (ClusterMAX Unavailable Tier)** — CoreWeave는 Platinum, NAVER는 최하위. 55MW 1H27 가동 후 SLA·SRE·SW 스택 실증까지 최소 1-2년. 앵커 고객 확보 지연 시 매출 20조 목표는 지연·미달.
3. **한국 전력망 제약** — 1GW급 계통 연결이 실제 병목. 한국 전력 인프라 (변압기·GSU·송전선) 제약이 GAK 세종 로드맵 지연 유발 가능. LS ELECTRIC·효성·HD현대일렉·두산의 실제 발주가 병행돼야 로드맵 실현.

## "코어위브 멀티플 정당성" 판단 (핸드오프 특별 요청)

**시장이 NAVER 전체에 코어위브 프리미엄을 씌우는 것은 부당**:
- CoreWeave forward P/S ~3.8-4.0x (2026E 매출 $12-13B / 시총 ~$48B)
- NAVER 회사 전체 P/S ~2.6x (2025 매출 12.04조 / 시총 31.05조)
- **AI Factory 사업부 현재 매출 fact 비중 = 1.4% (좁게) ~ 4.9% (엔터프라이즈 전체)**
- **20조 매출은 2028+ 회사 목표이지 fact 아님** → 이 회사 목표에 CoreWeave 프리미엄을 적용해 NAVER 전체 시총을 재평가하는 접근은 double-counting

**적정 접근 = SoTP**:
- 기존 사업부 (광고·커머스·핀테크·콘텐츠): 안정 성숙 → 국내 인터넷 peer PER·EV/EBITDA
- AI Factory 사업부: 성장기 자본집약 → CoreWeave forward P/S 프록시 (단, ClusterMAX 등급 차이로 discount 30-50% 적용 권고)
- **주가 227,500원 · 시총 31.05조원의 현재 프리미엄은 narrative 반영 초기 단계** — 검증 이벤트(55MW 가동, Brookfield binding, 앵커 고객) 통과 시 지속, 통과 실패 시 조정

**정량 SoTP 가이드 (본 스킬 밖 밸류에이션이므로 참고용)**:
- 기존 사업부 fair value: 대략 시총의 70-80% 수준 (24-25조)
- AI Factory optionality: 6-8조 (narrative 프리미엄 반영)
- Downside (Brookfield 이탈 시): 기존 사업부 fair value로 회귀 = 24-25조 = -20~-25%
- Upside (전 시나리오 낙관 성공): 40조+ = +30%
→ **이 SoTP 정량화는 분기 실적 분석·통합 모드가 갱신할 것**. 본 스킬은 프레임만 제시.

---

# 향후 관찰 포인트

1. **Q2 2026 실적 발표** (예정) — Enterprise 하위 disaggregation, 클라우드·AI 매출 정량 공개 여부
2. **NVIDIA 신주 발행 이사회 결의·주주총회 통과** — 신주 발행 절차 공식 완료 (fact 확정)
3. **Brookfield term sheet 진행 상태** — binding 전환 · 자금 인출 스케줄 공시
4. **55MW 첫 GPU cloud 서비스 launch (예정 1H 2027)** — 실행력 첫 검증 이벤트
5. **SemiAnalysis ClusterMAX 재평가** — Naver GPU cloud 실증 후 등급 변경 여부
6. **SK Group 2GW+ AI DC 실질 가동 progress** — 국내 경쟁 강도 실측
7. **Oracle CDS·Neocloud 채권 스프레드** — Brookfield 이탈 선행 신호 (테마 분석 v5.1 Step 8 지표와 공유)
8. **글로벌 AI lab의 한국 리전 발주 뉴스** — 앵커 고객 확보 evidence

---

## 참조

- 자동 참조 (사용됨): 클라우드_산업기초.md (v1.0 2026-05-18), 에이전트AI_테마분석.md (v5.1 2026-07-27)
- 자동 참조 (누락): NAVER_기업개요.md → 실적 분석 세션에서 미작성. **추가 요청 필요 (재무 fact 정확도 보강 위해)**
- 외부 fact 출처: NAVER Corp IR (Q1 2026, FY 2025), NVIDIA Newsroom (2026-07-24), Bloomberg, 코리아타임스·코리아중앙, SemiAnalysis ClusterMAX 2.0 (Naver Review), 스톡애널리시스 CRWV, Companiesmarketcap

---

# 부록 A. Terminal SoTP 정량화 + 검증 마일스톤 (2026-07-27 add-on)

> **본 부록의 성격**: 스킬 정의상 Terminal 밸류는 [테마 분석 통합 모드] 소관이나, 핸드오프 특별 요청에 따라 SoTP 프레임을 정량화하여 참조용으로 제시. **최종 통합 밸류·주도주 순위는 통합 모드가 갱신 담당**.
>
> **본 부록 목적**: (1) AI Factory가 회사 목표(20조원)에 도달했을 때 Terminal 매출·영업이익 시나리오 3종, (2) 기존 사업부는 현행 유지 가정으로 SoTP Terminal 밸류 총합, (3) 현재 시총(31조) 대비 업사이드 %, (4) Terminal 도달까지 검증해야 할 phase별 마일스톤 체크리스트.

## A-1. AI Factory Terminal 매출·영업이익 시나리오 (2030+ 1GW 기준)

### 전제 계산

| 항목 | 수치 | 근거 |
|---|---|---|
| MW당 GPU 밀도 | ~500 GPU (실용) | GB200 NVL72 = 120kW/rack (72 GPU), 1MW = 8.3 rack ≈ 600 GPU, 냉각·PDU 여유 감안 500 |
| 200MW GPU | ~100K GPU | 실용 밀도 기준 |
| 1GW GPU | ~500K GPU | 실용 밀도 기준 (NAVER 발표 260K + 확장 궤도 부합) |
| GPU당 연간 매출 (CoreWeave 프록시) | $18-35K | TTM $6.23B / ~250K GPU = $25K, 2026E $12-13B / ~450K = $27-29K. 낙관 B200 premium $35K / 중립 $27K / 비관 $18K |
| 원화 환산 (KRW 1,400/USD) | 낙관 4,900만원 / 중립 3,780만원 / 비관 2,520만원 per GPU/y | - |

### 200MW (2028 완공 시나리오) 중간 지점 매출

| 시나리오 | 매출 계산 | 매출 | Utilization |
|---|---|---|---|
| 낙관 | 100K GPU × $35K × 90% util | ~$3.2B = **4.4조원** | 90% |
| 중립 | 100K × $25K × 70% | ~$1.75B = **2.5조원** | 70% |
| 비관 | 100K × $15K × 50% | ~$0.75B = **1.05조원** | 50% |

### ★ 1GW (2030+ Terminal) 매출

| 시나리오 | 매출 계산 | Terminal 매출 | IR 목표 20조원 대비 |
|---|---|---|---|
| **낙관** | 500K GPU × $35K × 90% util | ~$15.75B = **22조원** | 110% (IR 목표 상회) |
| **중립** | 500K × $27K × 75% | ~$10.1B = **14조원** | 70% (목표 하회) |
| **비관** | 500K × $18K × 60% | ~$5.4B = **7.6조원** | 38% (크게 미달) |

→ **회사 IR 목표 20조원은 낙관 시나리오에 해당**. 중립·비관은 목표 하회.

### AI Factory Terminal OPM 시나리오

CoreWeave 참고:
- Adj EBITDA margin ~50%, but GAAP OPM ~-25% (감가상각 부담 큼)
- FCF 마이너스

NAVER 국내 특이점 (긍정): GAK 세종 자체 소유(REIT 임차료 없음), 국내 산업용 전력 저렴, HyperCLOVA 내부 앵커 수요

| 시나리오 | Terminal OPM | 근거 |
|---|---|---|
| 낙관 | **15%** | CoreWeave 대비 국내 원가 우위 + 앵커 lock-in 반영. 규모 도달 + utilization 80%+ |
| 중립 | **5%** | CoreWeave 궤도 (GAAP 개선 후) |
| 비관 | **-10%** | Utilization 낮음, 감가상각 부담 초과 |

### Terminal 영업이익

| 시나리오 | 매출 | OPM | Terminal 영업이익 |
|---|---|---|---|
| **낙관** | 22조 | 15% | **3.3조** |
| **중립** | 14조 | 5% | **0.7조** |
| **비관** | 7.6조 | -10% | **-0.76조 (손실)** |

## A-2. SoTP Terminal 밸류 (기존 사업부 현행 유지 가정)

### 기존 사업부 fair value (2025 fact 유지, 성장 X 보수 가정)

| 사업부 | 매출 (2025) | 영업이익 | 밸류 방식 | Fair Value |
|---|---|---|---|---|
| NAVER Platform (검색·커머스·서비스) | 대략 65-70% | 대부분 이익 | 국내 인터넷 peer PER 17x × 순이익 ~1.4조 | **~24조** |
| Financial Platform (N페이) | 15% | 저마진 성장 | 성장 프리미엄 반영 | **~3조** |
| Global Initiatives (콘텐츠·C2C·라인·웹툰·라인프렌즈) | 20% | 편의성 이익 | Sum | **~3-4조** |
| **소계 기존 사업부** | **12.04조** | **2.21조** | 순이익 ~1.7-1.8조 (세율 25%) | **~30조** |

→ 국내 인터넷 대장 PER 17x 기준. 성장 없음 가정으로 보수. 현재 시총(31조)과 유사.

### AI Factory Terminal 밸류 (CoreWeave P/S 프록시 + discount 적용)

| 요인 | 낙관 | 중립 | 비관 |
|---|---|---|---|
| Base P/S (CoreWeave forward) | 4.0x | 4.0x | 4.0x |
| ClusterMAX 등급 discount | -25% (Silver 진입 가정) | -40% (Unavailable 벗어남 정도) | -50% (등급 유지) |
| Sovereign 시장 규모 한계 discount | -0% (해외 진출 성공) | -10% (국내 한정) | -15% (국내 소형) |
| **Effective P/S** | **3.0x** | **2.2x** | **1.5x** |
| × Terminal 매출 | 22조 | 14조 | 7.6조 |
| = **AI Factory Terminal 밸류** | **66조** | **31조** | **11조** |

### 전체 SoTP Terminal 시총

| 시나리오 | 기존 사업부 | AI Factory | Terminal 시총 합계 | 현재 시총 (31조) 대비 upside |
|---|---|---|---|---|
| **★ 낙관 (Bull)** | 30조 | 66조 | **96조** | **+210%** |
| **중립 (Base)** | 30조 | 31조 | **61조** | **+97%** |
| **비관 (Bear)** | 30조 | 11조 | **41조** | **+32%** |
| **실패 (Brookfield 이탈 · narrative 소멸)** | 30조 | 3-5조 (부분 CAPA + discount 심화) | **33-35조** | **+6~+13%** |

### SoTP 결론

| 판단 | 근거 |
|---|---|
| **★ Expected Value (확률 가중, 임의 assign)** | 낙관 25% × 210% + 중립 40% × 97% + 비관 20% × 32% + 실패 15% × 10% = **약 +100% (2배)** |
| **최대 downside** | 실패 시나리오 = 현재 대비 -10% ~ +10% (narrative 프리미엄 소멸 후 기존 사업부 fair value) |
| **최대 upside** | 낙관 시나리오 = 현재 대비 +210% (3배). 5년 시나리오 |

**★ 인사이트**:
- 기존 사업부만으로도 fair value가 현재 시총과 거의 일치 → **현재 주가는 이미 narrative 프리미엄이 반영된 수준**이 아니라, **AI Factory optionality를 사실상 무료로 얹은 수준**
- 이는 upside skew가 강한 asymmetric 구조 (downside -10~+10% vs upside +100~+210%)
- 단, **Brookfield 이탈 시나리오(-narrative)에서는 프리미엄 소멸로 조정 가능** → 자본 조달 확정이 첫 검증 게이트

## A-3. Terminal 도달까지 검증 마일스톤 체크리스트

> Terminal(1GW, 2030+ 도달) 판단은 4개 phase 통과 여부에 따라 시나리오 확정.

### Phase 1 · 자본구조 확정 (2026 H2 ~ 2027 H1)

| ☐ | 마일스톤 | 시점 | 통과 시 | 실패 시 |
|---|---|---|---|---|
| ☐ | NVIDIA 신주 발행 이사회·주총 통과 | 2026 Q3 | 자본 유입 확정 | narrative 조기 훼손 |
| ☐ | Brookfield term sheet **binding 전환** | 2026 Q4 ~ 2027 Q1 | ★ 실패 시나리오 회피 확정 | **★ 실패 시나리오 진입 → 시총 30-35조로 회귀** |
| ☐ | Brookfield 1차 tranche 실제 자금 인출 | 2027 H1 | 이행 검증 시작 | 부분적 실패 → 비관 |

**Phase 1 통과 판정**: **binding 전환 & 1차 인출이 최대 이벤트**. 통과 실패 시 SoTP 낙관·중립 모두 제거.

### Phase 2 · 첫 실행 검증 (2027 H1 ~ 2028)

| ☐ | 마일스톤 | 시점 | 통과 시 | 실패 시 |
|---|---|---|---|---|
| ☐ | 55MW GPU cloud 첫 launch (SLA 안정) | 2027 H1 | 실행력 첫 검증 | 로드맵 6개월+ 지연 |
| ☐ | ★ 앵커 고객 계약 공시 (해외 AI lab, 정부, 대기업) | 2027 Q3-Q4 | 매출 가시성 확보 | narrative "고객 없음" 우려 확산 |
| ☐ | 55MW utilization 60%+ | 2027 Q4 | 수요 실증 | 비관 시나리오 진입 |
| ☐ | 100MW 확장 진척 발표 | 2027 하반기 | 로드맵 유효성 | 시장 회의론 |
| ☐ | **★ ClusterMAX 등급 Unavailable → Bronze/Silver 상향** | 2028 상반기 | tech Moat 3 → 4 상향 | tech Moat 정체 → discount 유지 |

**Phase 2 통과 판정**: 앵커 고객 + utilization 60%+ + ClusterMAX 상향 3개 통과 시 **중립→낙관 시나리오 전환 가능**. 반대로 대부분 실패 시 **비관**.

### Phase 3 · 규모 검증 (2028 ~ 2029)

| ☐ | 마일스톤 | 시점 | 통과 시 | 실패 시 |
|---|---|---|---|---|
| ☐ | 200MW 완공 | 2028 Q4 | 로드맵 물리 검증 | 지연 시 목표 20조 신뢰도 하락 |
| ☐ | AI Factory 연간 매출 3-5조 (annualized run-rate) | 2028 | 중립 시나리오 진입 확정 | 비관 |
| ☐ | ★ AI Factory OPM **BEP (0% 이상)** 도달 | 2028 | 수익성 검증 | CoreWeave 방식 GAAP 손실 지속 |
| ☐ | ClusterMAX **Gold** 진입 | 2029 | 낙관 시나리오 무게 | - |
| ☐ | ★ 글로벌 매출 비중 30%+ (한국 sovereign 넘어) | 2029 | Terminal 매출 22조 궤도 검증 | 국내 한정 시 매출 상한 노출 |

**Phase 3 통과 판정**: **BEP + 글로벌 매출 비중이 낙관 시나리오의 결정적 게이트**. 통과 시 밸류에이션 재평가 이벤트.

### Phase 4 · Terminal 도달 검증 (2029 ~ 2030+)

| ☐ | 마일스톤 | 시점 | 통과 시 | 실패 시 |
|---|---|---|---|---|
| ☐ | 1GW 로드맵 인허가·부지·전력 확보 | 2029 | Terminal 달성 궤도 | 국내 전력망 병목 노출 |
| ☐ | AI Factory 매출 10조+ 도달 | 2030 | 낙관 궤도 검증 | 중립·비관 확정 |
| ☐ | AI Factory OPM **10%+ 안정화** | 2030+ | 성숙 사업 인정 | 자본집약 저마진 낙인 |
| ☐ | 1GW 부분 가동 시작 | 2030-2031 | Terminal 밸류 = 96조 실현 궤도 | Terminal 지연 |
| ☐ | SK Group 2GW+ AI DC 진입 vs NAVER 국내 점유 방어 | 상시 | 국내 sovereign lock-in 유지 | 국내 점유 잠식 → Sovereign discount 심화 |

### 상시 모니터링 지표 (모든 phase 관통)

| 지표 | 트래킹 이유 |
|---|---|
| **Oracle CDS · Neocloud 채권 스프레드** | 자본공급자 프레임 스트레스 = Brookfield 이탈 선행 신호 (테마 v5.1 Step 8 지표 공유) |
| SemiAnalysis ClusterMAX 정기 재평가 | tech Moat 등급 실증 |
| 하이퍼스케일러 CapEx 가이던스 | AI 인프라 사이클 정점 시그널 (통과 시 Terminal 매출 상한 압박) |
| 한국 전력망 계통 연결 lead time | 1GW 로드맵 실현 물리 조건 |
| 글로벌 하이퍼스케일러 한국 리전 확장 | Sovereign lock-in 약화 시그널 |

## A-4. 최종 정리 — Terminal 밸류·Upside·마일스톤 통합 표

| 시나리오 | 확률 | Terminal 시총 | Upside | 판별 마일스톤 |
|---|---|---|---|---|
| **★ 낙관 (Bull)** | 25% | 96조 | +210% | Phase 1-2-3 통과 + ClusterMAX Gold + 글로벌 30% |
| **중립 (Base)** | 40% | 61조 | +97% | Phase 1 통과 + Phase 2 부분 + 200MW 완공 |
| **비관 (Bear)** | 20% | 41조 | +32% | Phase 1 통과 + Phase 2 실패 (utilization·ClusterMAX·앵커) |
| **★ 실패 (Fail)** | 15% | 33-35조 | +6~+13% | **Brookfield 이탈** or Phase 1 실패 |
| **확률 가중 EV** | - | ~63조 | **~+100%** | - |

→ 핵심 시나리오 분기점은 순서대로 **① Brookfield binding (Phase 1) → ② 앵커 고객 + ClusterMAX 상향 (Phase 2) → ③ OPM BEP + 글로벌 30% (Phase 3)**.

> **★ 통합 모드 갱신 안내**: 본 SoTP 정량화는 참조용이며, 최종 Terminal 밸류·주도주 순위는 [테마 분석 통합 모드]가 통합본에서 갱신. 본 부록은 통합 모드의 fact input.

