# 워치리스트 — 2026-Q1 (섹터)

> 분기별 in-place 갱신. 메타데이터 헤더 [섹터] 필드와 정확 일치 필요.
>
> **그룹 구조 (2026-11-14 변경)**: 섹터는 산업 대분류 4개(테크 / 산업재 / 모빌리티·에너지전환 / 소비재)에 속한다. **섹터 T1**은 BT가 더 집중해서 볼 섹터를 필요할 때 옮겨 두는 칸이다 — T1으로 옮긴 섹터는 `[대분류]` 표시를 붙여 원래 대분류를 남긴다. (이전: T1 주도 / T2 후보 / T3 트래킹 우선순위)
> **대분류끼리 합산·델타 비교는 하지 않는다** — 대분류마다 사이클이 겹치지 않는다. 델타 판정은 섹터 리뷰(섹터·서브섹터) 단위까지만.
> 명칭: "섹터 T1"은 이슈 워치리스트의 T1과 구분해 부른다.
>
> **종목 정렬 룰 (2026-11-01 변경)**: 각 섹터 내 종목은 **서브섹터(세부 테마) 순** — 아래 "섹터 리뷰 단위" 표의 서브섹터 순서, 각 서브섹터 안에서는 핵심 → 확장 순. 대시보드 섹터 카드도 같은 순서로 서브섹터별 구분 표시. (이전: 실적 발표일 순)
> 섹터 안에 한국 + 글로벌 피어 통합 운영 (예: 전력 인프라 = 한국 3사 + 글로벌 6사).
> **공시 주기** (2026-11-14): 대시보드 종목 행 "공시 주기" 칸에 분기 / 반기 / 연간 표시. 아래 두 줄에 없는 종목은 분기. 반기·연간 종목은 1·3분기(연간은 1~3분기)에 그 분기 리뷰가 없으니 섹터 리뷰 전에 확인
> **연간 공시 종목** (손익이 연간에만 — Q4 리뷰): 
> **반기 공시 종목** (손익이 나온 분기에만 리뷰 — 1H→Q2, 2H→Q4. 1·3분기 대시보드는 직전 반기 리뷰에 그 분기 업데이트가 덧붙었을 때(`> 분기 업데이트: 3Q26` 줄)만 "실적 리뷰(2Q)"로 표시, 아니면 비활성): 양쯔장조선, Seatrium, BAE Systems, Thales

---

## 섹터 리뷰 단위 (서브섹터)

> [섹터 리뷰 모드]의 묶음 단위 (2026-11-01 신설). 섹터 리뷰는 서브섹터별 파일 하나에 분기마다 누적.
> 핵심 = 기본 묶음, 확장 = BT가 지시할 때 추가로 엮는 종목. 실적 리뷰 메타데이터 [서브섹터] 필드와 정확히 일치.
> 대시보드 카드 위치(섹터 T1·대분류)와 별개 — 예: Nvidia는 카드는 미국 빅테크, 섹터 리뷰는 반도체 로직·CPU.
> 파일: `earnings\sector-review\{서브섹터}_섹터리뷰.md`
> **합산 제외 핵심 종목 (2026-11-14)**: 로봇 부품의 Sanhua·Tuopu는 핵심 부품 기업 위치를 유지하되, 로봇 매출이 미분리·미미해 섹터 델타 합산에서는 제외한다 (개별 리뷰·숫자 표는 계속).
> 트래킹 피어 = 개별 리뷰 없이 섹터 리뷰 안 숫자 표로만 따라가는 비교 대상 (셀사이드 없음, 합산 제외). 글로벌 편입 종목(숫자 중심 리뷰 작성)은 핵심·확장 열에 넣는다 — 섹터 리뷰 스킬 "글로벌 피어 편입 원칙" (2026-11-14)

| 섹터 | 서브섹터 | 핵심 | 확장 | 트래킹 피어 |
|---|---|---|---|---|
| 미국 빅테크 | 하이퍼스케일러 | Microsoft, Alphabet, Amazon, Meta | SpaceX | - |
| 미국 빅테크 | 소비자·모빌리티 | Apple, Tesla | SpaceX | - |
| 반도체 | 메모리 | SK하이닉스, 삼성전자, Micron | SanDisk, Western Digital, Seagate | - |
| 반도체 | 로직·CPU | Nvidia, AMD | Intel, ARM | - |
| 전력 인프라 | 송변전 | 효성중공업, HD현대일렉트릭, Hitachi Energy | - | - |
| 전력 인프라 | 배전·DC 전력관리 | Schneider Electric, Eaton | ABB, LS일렉트릭 | - |
| 전력 인프라 | 발전 | GE Vernova, Siemens Energy | - | - |
| 전력 인프라 | 전력 인프라 | GE Vernova, Siemens Energy, Hitachi Energy, Schneider Electric, ABB, Eaton, 효성중공업, HD현대일렉트릭, LS일렉트릭 | - | - |
| 배터리 | 배터리 셀 | LG에너지솔루션, 삼성SDI | SK온 | - |
| 배터리 | 양극재 | 에코프로비엠, 포스코퓨처엠 | 엘앤에프 | - |
| 배터리 | 배터리 셀 글로벌 | CATL, Panasonic Energy | - | - |
| 배터리 | 양극재 글로벌 | Ronbay, Easpring | - | - |
| 조선 | 조선 | 한화오션, HD현대중공업, 삼성중공업 | - | - |
| 조선 | 조선 글로벌 | 중국선박공업, 양쯔장조선, Seatrium, HII, Fincantieri, TKMS | - | General Dynamics(Marine Systems 부문) |
| 방산 | 방산 | 한화에어로스페이스, 현대로템, LIG D&A | 한화시스템, 한국항공우주 | - |
| 방산 | 방산 글로벌 | Lockheed Martin, RTX, General Dynamics, Rheinmetall, BAE Systems, Leonardo, Thales, Saab, Elbit Systems, Aselsan | - | - |
| 원전 | 원전 설계 | 한전기술 | - | - |
| 원전 | 원전 기자재 | 두산에너빌리티 | - | - |
| 원전 | 원전 시공 | 현대건설 | 대우건설 | - |
| 원전 | 원전 정비 | 한전KPS | - | - |
| 로봇 | 휴머노이드 완성체 | 현대차, 레인보우로보틱스, Unitree, UBTech | Tesla | - |
| 로봇 | 로봇 부품 | Sanhua, Tuopu, 현대모비스 | Leaderdrive, 로보티즈 | 에스비비테크 |
| 로봇 | 산업·물류 자동화 | 두산로보틱스, 현대오토에버, Symbotic | - | Teradyne(Universal Robots 부문) |
| 뷰티 | 브랜드사 | 에이피알, 달바글로벌, 아모레퍼시픽 | 브이티 | - |
| 뷰티 | ODM | 코스맥스, 한국콜마 | 코스메카코리아 | - |
| 뷰티 | 유통 | 실리콘투 | - | - |
| 음식료 | 음식료 | 삼양식품 | - | - |
| 엔터 | 엔터 | 하이브, JYP, 에스엠, 와이지엔터 | - | - |

---

## 섹터 T1 — 집중 (BT가 필요할 때 배치)

(현재 없음 — 집중해서 볼 섹터를 여기로 옮기고 `[대분류]` 표시를 붙인다)

## 대분류: 테크

- **미국 빅테크** (Microsoft(MSFT, industry=클라우드), Alphabet(GOOGL, industry=광고|클라우드), Amazon(AMZN, industry=이커머스|클라우드), Meta(META, industry=광고), SpaceX(SPCX, industry=클라우드|우주|통신), Apple(AAPL, industry=소비자 전자제품), Tesla(TSLA, industry=자동차|자율주행), Nvidia(NVDA, industry=반도체))
- **반도체** (SK하이닉스, 삼성전자, Micron(MU), SanDisk(SNDK), Western Digital(WDC), Seagate(STX), AMD(AMD), Intel(INTC), ARM(ARM))

## 대분류: 산업재

- **전력 인프라** (효성중공업, HD현대일렉트릭, Hitachi Energy(HE), LS일렉트릭, Schneider Electric(SU), Eaton(ETN), ABB(ABB), GE Vernova(GEV), Siemens Energy(ENR))
- **원전** (한전기술, 두산에너빌리티, 현대건설, 대우건설, 한전KPS)
- **조선** (한화오션, HD현대중공업, 삼성중공업, 중국선박공업(600150.SS), 양쯔장조선(BS6.SI), Seatrium(5E2.SI), HII(HII), Fincantieri(FCT.MI), TKMS(TKMS.DE))
- **방산** (한화에어로스페이스, 현대로템, LIG D&A, 한화시스템, 한국항공우주, Lockheed Martin(LMT), RTX(RTX), General Dynamics(GD), Rheinmetall(RHM), BAE Systems(BAE), Leonardo(LDO), Thales(HO), Saab(SAAB), Elbit Systems(ESLT), Aselsan(ASELS))

## 대분류: 모빌리티·에너지전환

- **배터리** (LG에너지솔루션, 삼성SDI, SK온, 에코프로비엠, 포스코퓨처엠, 엘앤에프, CATL(300750.SZ), Panasonic Energy(6752.T), Ronbay(688005.SS), Easpring(300073.SZ))
- **로봇** (현대차, 레인보우로보틱스, Unitree(688836.SS), UBTech(9880.HK), Sanhua(002050.SZ), Tuopu(601689.SS), 현대모비스, Leaderdrive(688017.SS), 로보티즈, 에스비비테크, 두산로보틱스, 현대오토에버, Symbotic(SYM), Teradyne(TER))

## 대분류: 소비재

- **뷰티** (에이피알, 달바글로벌, 아모레퍼시픽, 브이티, 코스맥스, 한국콜마, 코스메카코리아, 실리콘투)
- **음식료** (삼양식품)
- **엔터** (하이브, JYP, 에스엠, 와이지엔터)

---
