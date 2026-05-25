# 기업개요 1번 섹션 retrofit 핸드오프 (Cross-Session)

> **목적**: company-overview 1번 섹션을 삼성전자 v4.8 수준 디폴트 quality로 표준화
> **작성**: 2026-05-24 반도체 섹션 세션에서 신설 + T1 반도체 8개 완료
> **공유 위치**: `Scheduled\earnings\company-overview\_RETROFIT_HANDOFF.md` (모든 섹터 세션에서 읽기 가능)

---

## 1. 발동 문구 (다른 섹터 세션에서 사용)

### 가장 명확한 trigger:

```
company-overview/_RETROFIT_HANDOFF.md 읽고 {섹터명} 1번 섹션 retrofit 진행
```

예시:
- **빅테크 세션**: `_RETROFIT_HANDOFF.md 읽고 T1 빅테크 7개 retrofit 진행`
- **전력 인프라 세션**: `_RETROFIT_HANDOFF.md 읽고 T2 전력 인프라 7개 retrofit 진행`

### 메모리 자동 적용 확인:

위 발동 문구 호출 시 [기업 개요 모드] 스킬이 자동으로 `feedback_company_overview_section1_standard.md` 메모리를 참조한다. 별도 확인 불필요.

---

## 2. 표준 5가지 요약 (메모리 룰 핵심)

전체 룰은 메모리 `feedback_company_overview_section1_standard.md` 참조. 핵심:

(1) **Summary Box 6지표** — 매출 CAGR, OPM 평균/정점/저점 (연도 명시), 사이클 주기, 회수
(2) **손익 표 narrative annotation** — 각 연도 옆 사이클 변곡점 마커 (← 1차 슈퍼사이클, ← 다운사이클 저점 등). 표 자체가 사이클 history book
(3) **분류 결정 sub-logic 4단계** — (1) 매출 큰 사업부 기준 (2) secular 변수 sub-rule (3) Boundary case 처리 Primary + Secondary (4) 글로벌 피어 cross-reference
(4) **밸류에이션 다이얼** — 사업부 mix → method 연결. PER/PBR/EV/EBITDA 단순 나열 금지. 삼성전자 비교 1줄 필수
(5) **재평가 트리거 = 분류 변경 조건** — 실적 추적용 변수 (HBM 점유율·ASP 등)는 6번 섹션. 1번 트리거는 "분류 자체가 바뀔 조건" (예: HBM 비중 50%+ 도달 시 Primary cyclical → Secular 격상)

---

## 3. 진행 현황 (2026-05-24 기준)

### ✅ 완료 (10/24)

| 종목 | 섹터 | 새 분류 |
|---|---|---|
| 삼성전자 | T1 반도체 | Primary 사이클 + Secondary 지속성장 일부 (**reference 표준**) |
| ASML (v2.1) | T2 반도체 소부장 | Primary Secular Growth + Secondary WFE Capex 사이클 |
| SK하이닉스 (v4.9) | T1 반도체 | Primary 사이클 + Secondary AI HBM secular |
| MU (v4.9) | T1 반도체 | Primary 사이클 + Secondary AI HBM secular |
| INTC (v4.9) | T1 반도체 | Primary 구조적 Turnaround + Secondary Foundry 전환 |
| STX (v4.9) | T1 반도체 | Primary 사이클 + 구조적 전환 + Secondary AI 콜드 스토리지 |
| SNDK (v4.9) | T1 반도체 | Primary 사이클 + Secondary AI Enterprise SSD |
| WDC (v4.9) | T1 반도체 | Primary 사이클 + 구조적 전환 + Secondary AI Cloud Storage |
| AMD (v4.9) | T1 반도체 | Primary 고성장 + secular + Secondary 사이클 일부 |
| ARM (v4.9) | T1 반도체 | Primary 지속성장 + Secular (사이클 거의 부재) |

### ⏳ Pending (14/24)

**T1 미국 빅테크 (7개)** — 빅테크 세션 담당
- AAPL — Apple
- AMZN — Amazon
- GOOGL — Alphabet
- META — Meta
- MSFT — Microsoft
- TSLA — Tesla
- NVDA — Nvidia (반도체 섹터 겸함 — 빅테크 또는 반도체 어디서 진행해도 OK)

**T2 전력 인프라 (7개)** — 전력 인프라 세션 담당
- ABB — ABB Ltd
- GEV — GE Vernova
- HE — Hitachi Energy
- SU — Schneider Electric
- 효성중공업
- HD현대일렉트릭
- LS일렉트릭

### 📝 신규 작성 시 자동 적용 (메모리 룰만으로 충분)

이미지 Tier 1·2·3의 나머지 종목 (기업개요 미작성, 약 34개) — 향후 [기업 개요 모드] 호출 시 자동 표준 적용. 별도 retrofit 불요.

---

## 4. Sample Reference (작성 시 참고)

### A. Cyclical pure-play (메모리·HDD): SK하이닉스, MU, STX, SNDK, WDC
- 사이클 진폭 OPM ±50~80%pt
- 손익 표 annotation: ← 1차 슈퍼사이클, ← 다운사이클 저점, ← AI 회복 등
- secular 변수: HBM 비중·Cloud 비중·AI Enterprise SSD

### B. Multi-segment cyclical: 삼성전자 (디폴트 표준)
- 사업부 mix 추론 (DX vs DS 매출 비중 + OP 비중 = 사이클 분류 결정)
- valuation 다이얼: PBR + PER 혼합

### C. Structural turnaround: INTC
- 12년 매출 CAGR 마이너스 = 사이클 아닌 구조적 침체
- valuation: PBR + Sum-of-Parts + Catalysts 가중

### D. Secular growth (high growth): AMD, NVDA, ARM
- 사이클 진폭 작음 (±10~30%pt)
- valuation: PER + DCF + TAM expansion

### E. Secular growth (asset-light IP): ARM
- 사이클 거의 부재, OPM 40%+ 소프트웨어 수준
- valuation: PER 100배+ premium 정당화

### F. Secular + cyclical mix (장비): ASML
- WFE Capex 사이클 + EUV 독점 secular 중첩
- Boundary case 처리 룰 명시 적용

---

## 5. 작업 흐름 (종목당 ~5분)

(1) 기존 `.md`의 1번 섹션 읽기 (보통 line 1~80)
(2) 손익 데이터 + 산업 narrative 추출
(3) 표준 5가지 적용한 새 1번 섹션 작성 + Edit
(4) 다른 종목 retrofit 누적 후 batch `.html` 재생성 (단일 Python script로 10초)

### batch .html 재생성 script (재사용 가능)

`outputs/batch_html_t1_semi.py` 참조 (반도체 세션에서 작성). tickers list만 바꿔서 사용.

---

## 6. 메모리 발동 확인 방법

다른 세션에서 retrofit 시작 전:

```
메모리 확인:
- feedback_company_overview_section1_standard.md (표준 5가지 룰)
- feedback_sector_memory_structure.md (섹터별 세션 운영)
- 삼성전자_기업개요.md (디폴트 reference, 같은 폴더)
```

발동 문구 호출 시 위 3개가 자동 로드됨. 추가 안내 없이 진행 가능.

---

## 7. 본 핸드오프 파일 갱신 룰

각 섹터 retrofit 완료 시 본 파일의 "진행 현황" 섹션에 ✅ 추가. 모든 24개 종목 완료 후 본 파일 삭제 가능 (메모리 룰만 남기면 됨).
