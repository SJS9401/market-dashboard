# 워치리스트 — 2026-Q1 (섹터)

> 분기별 in-place 갱신. tier 분류는 분기 시작 시 BT가 직접 결정.
> Stage 2가 자동 로드해 tier별 처리. 메타데이터 헤더 [섹터] 필드와 정확 일치 필요.
>
> **명칭 컨벤션**: 본 워치리스트의 T1-T3은 "섹터 T1·T2·T3"로 호칭한다 (이슈 워치리스트의 T1-T3과 구분).
>
> **종목 정렬 룰 (2026-11-01 변경)**: 각 섹터 내 종목은 **서브섹터(세부 테마) 순** — 아래 "섹터 리뷰 단위" 표의 서브섹터 순서, 각 서브섹터 안에서는 핵심 → 확장 순. 대시보드 섹터 카드도 같은 순서로 서브섹터별 구분 표시. (이전: 실적 발표일 순)
> 섹터 안에 한국 + 글로벌 피어 통합 운영 (예: 전력 인프라 = 한국 3사 + 글로벌 6사).

---

## 섹터 리뷰 단위 (서브섹터)

> [섹터 리뷰 모드]의 묶음 단위 (2026-11-01 신설). 섹터 리뷰는 서브섹터별 파일 하나에 분기마다 누적.
> 핵심 = 기본 묶음, 확장 = BT가 지시할 때 추가로 엮는 종목. 실적 리뷰 메타데이터 [서브섹터] 필드와 정확히 일치.
> 대시보드 카드 위치(섹터 T1~T3)와 별개 — 예: Nvidia는 카드는 미국 빅테크, 섹터 리뷰는 반도체 로직·CPU.
> 파일: `earnings\sector-review\{서브섹터}_섹터리뷰.md`

| 섹터 | 서브섹터 | 핵심 | 확장 |
|---|---|---|---|
| 미국 빅테크 | 하이퍼스케일러 | Microsoft, Alphabet, Amazon, Meta | SpaceX |
| 미국 빅테크 | 소비자·모빌리티 | Apple, Tesla | SpaceX |
| 반도체 | 메모리 | SK하이닉스, 삼성전자, Micron | SanDisk, Western Digital, Seagate |
| 반도체 | 로직·CPU | Nvidia, AMD | Intel, ARM |
| 반도체 소부장 | 전공정 장비 | ASML, Applied Materials, Lam Research | KLA, Tokyo Electron |
| 반도체 소부장 | 후공정·HBM | 한미반도체, BESI | Disco, Advantest, 리노공업 |
| 반도체 소부장 | 기판·부품 | 삼성전기 | - |
| 전력 인프라 | 송변전 | 효성중공업, HD현대일렉트릭, Hitachi Energy | - |
| 전력 인프라 | 배전·DC 전력관리 | Schneider Electric, Eaton | ABB, LS일렉트릭 |
| 전력 인프라 | 발전 | GE Vernova, Siemens Energy | - |
| 전력 인프라 | 전력 인프라 | GE Vernova, Siemens Energy, Hitachi Energy, Schneider Electric, ABB, Eaton, 효성중공업, HD현대일렉트릭, LS일렉트릭 | - |
| 배터리 | 배터리 셀 | LG에너지솔루션, 삼성SDI | - |
| 배터리 | 양극재 | 에코프로비엠, 포스코퓨처엠 | 엘앤에프 |
| 조선 | 조선 | 한화오션, HD현대중공업, 삼성중공업 | - |
| 방산 | 방산 | 한화에어로스페이스, 현대로템, LIG D&A | 한화시스템, 한국항공우주 |
| 방산 | 방산 글로벌 | Lockheed Martin, RTX, General Dynamics, Rheinmetall, BAE Systems, Leonardo, Thales, Saab, Elbit Systems, Aselsan | - |
| 원전 | 원전 설계 | 한전기술 | - |
| 원전 | 원전 기자재 | 두산에너빌리티 | - |
| 원전 | 원전 시공 | 현대건설 | 대우건설 |
| 원전 | 원전 정비 | 한전KPS | - |
| 로봇 | 로봇 | 현대차, 현대모비스, 현대오토에버 | - |
| 화장품 | 화장품 | 에이피알, 달바글로벌 | - |
| 음식료 | 음식료 | 삼양식품 | - |
| 엔터 | 엔터 | 하이브, JYP, 에스엠, 와이지엔터 | - |

---

## 섹터 T1 — 메인 (분기 주도 섹터)

- **미국 빅테크** (Microsoft(MSFT, industry=클라우드), Alphabet(GOOGL, industry=광고|클라우드), Amazon(AMZN, industry=이커머스|클라우드), Meta(META, industry=광고), SpaceX(SPCX, industry=클라우드|우주|통신), Apple(AAPL, industry=소비자 전자제품), Tesla(TSLA, industry=자동차|자율주행), Nvidia(NVDA, industry=반도체))
- **반도체** (SK하이닉스, 삼성전자, Micron(MU), SanDisk(SNDK), Western Digital(WDC), Seagate(STX), AMD(AMD), Intel(INTC), ARM(ARM))

## 섹터 T2 — 주도 후보

- **반도체 소부장** (ASML(ASML), Applied Materials(AMAT), Lam Research(LRCX), KLA(KLAC), Tokyo Electron(8035.T), 한미반도체, BESI(BESI), Disco(6146.T), Advantest(6857.T), 리노공업, 삼성전기)
- **전력 인프라** (효성중공업, HD현대일렉트릭, Hitachi Energy(HE), LS일렉트릭, Schneider Electric(SU), Eaton(ETN), ABB(ABB), GE Vernova(GEV), Siemens Energy(ENR))
- **배터리** (LG에너지솔루션, 삼성SDI, 에코프로비엠, 포스코퓨처엠, 엘앤에프)
- **조선** (한화오션, HD현대중공업, 삼성중공업)
- **방산** (한화에어로스페이스, 현대로템, LIG D&A, 한화시스템, 한국항공우주, Lockheed Martin(LMT), RTX(RTX), General Dynamics(GD), Rheinmetall(RHM), BAE Systems(BAE), Leonardo(LDO), Thales(HO), Saab(SAAB), Elbit Systems(ESLT), Aselsan(ASELS))
- **원전** (한전기술, 두산에너빌리티, 현대건설, 대우건설, 한전KPS)
- **로봇** (현대차, 현대모비스, 현대오토에버)

## 섹터 T3 — 트래킹

- **화장품** (에이피알, 달바글로벌)
- **음식료** (삼양식품)
- **엔터** (하이브, JYP, 에스엠, 와이지엔터)

---
