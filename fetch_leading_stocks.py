"""
한국 주도주 + KOSPI OHLC 일봉 데이터 수집 스크립트
yfinance 필요: pip install yfinance
실행: python fetch_leading_stocks.py
출력: leading_stocks_data.json (create_leading_stocks.py가 읽는 형식)
"""

import json
import os
import subprocess
import sys
from datetime import datetime

try:
    import yfinance as yf
except ImportError:
    print("yfinance가 설치되어 있지 않습니다. 자동 설치합니다...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "yfinance"])
    import yfinance as yf
    print("yfinance 설치 완료!\n")

# ===== 종목 정의 =====
# stock_id는 create_leading_stocks.py의 LEADING_STOCKS와 일치해야 함
# 같은 티커의 다른 시기 종목은 동일 stock_id 사용 (데이터는 캐싱)
STOCKS = [
    # (id, 이름, Yahoo ticker, 주도 시기, 해당 사이클)
    ("spc_samlib",      "SPC삼립",       "005610.KS", "1993",     "kr_imf_1997"),
    ("sk_telecom",      "SK텔레콤",      "017670.KS", "1999",     "kr_it_1998"),
    ("coway",           "코웨이",        "021240.KS", "2002",     "kr_card_2001"),
    ("hyundai_elev",    "현대엘리베이터", "017800.KS", "2004",     "kr_china_2003"),
    ("hyundai_mipo",    "현대미포조선",   "010620.KQ", "2007",     "kr_china_2003"),
    ("kia",             "기아",          "000270.KS", "2010",     "kr_gfc_2007"),
    ("hanmi_science",   "한미사이언스",   "008930.KS", "2015",     "kr_semi_2016"),
    ("amorepacific",    "아모레퍼시픽",   "090430.KS", "2015",     "kr_sideways_2011"),
    ("celltrion",       "셀트리온",      "068270.KS", "2017",     "kr_semi_2016"),
    ("sk_hynix",        "SK하이닉스",    "000660.KS", "2018",     "kr_semi_2016"),
    ("seegene",         "씨젠",          "096530.KQ", "2020",     "kr_covid_2020"),
    ("hmm",             "HMM",           "011200.KS", "2020",     "kr_covid_2020"),
    ("ecopro",          "에코프로",      "086520.KQ", "2020",     "kr_covid_2020"),
    ("hanmi_semi",      "한미반도체",     "042700.KQ", "2023",     "kr_sideways_2023"),
    ("alteogen",        "알테오젠",      "196170.KQ", "2024",     "kr_sideways_2023"),
    ("hanwha_ocean",    "한화오션",      "042660.KS", "2025",     "kr_ai_2025"),
    ("doosan_enerbil",  "두산에너빌리티", "034020.KS", "2025",     "kr_ai_2025"),
    ("samsung_elec",    "삼성전자",      "005930.KS", "2026",     "kr_ai_2025"),
    # 신규 종목 (1986~2009 사이클)
    ("hyundai_const",   "현대건설",      "000720.KS", "1988",     "kr_troika_1986"),
    ("daishin_sec",     "대신증권",      "003540.KS", "1988",     "kr_troika_1986"),
    ("kepco",           "한국전력",      "015760.KS", "1993",     "kr_bluechip_1990"),
    ("posco",           "POSCO홀딩스",   "005490.KS", "1994",     "kr_bluechip_1990"),
    ("hyundai_motor",   "현대차",        "005380.KS", "1994",     "kr_bluechip_1990"),
    ("lg_chem",         "LG화학",        "051910.KS", "2010",     "kr_chahwajeong_2009"),
    ("s_oil",           "S-Oil",         "010950.KS", "2010",     "kr_chahwajeong_2009"),
]

# KOSPI 인덱스
INDEX = ("kospi", "KOSPI", "^KS11")

def fetch_ohlc(ticker_symbol, name):
    """일봉 OHLC 전체 기간 다운로드 → [YYYYMMDD, O, H, L, C, vol_eok] 배열.

    - auto_adjust=False : raw price 사용 (키움 HTS 와 동일)
    - vol_eok = volume × close ÷ 1e8 (거래대금 억원)
    """
    print(f"  Fetching {name} ({ticker_symbol})...", end=" ", flush=True)
    try:
        tk = yf.Ticker(ticker_symbol)
        df = tk.history(period="max", interval="1d", auto_adjust=False)
        if df.empty:
            print("NO DATA")
            return None

        # NaN 행 제거
        df = df.dropna(subset=["Open", "High", "Low", "Close"])

        records = []
        for idx, row in df.iterrows():
            date_str = idx.strftime("%Y%m%d")
            # KRW 주가는 정수로 충분 (파일 크기 절감)
            o = int(round(row["Open"]))
            h = int(round(row["High"]))
            l = int(round(row["Low"]))
            c = int(round(row["Close"]))
            v = float(row["Volume"]) if row["Volume"] == row["Volume"] else 0.0
            # 거래대금(억) 변환: vol_eok = v × c ÷ 1e8
            vol_eok = round(v * c / 1e8, 2) if c > 0 else 0.0
            records.append([date_str, o, h, l, c, vol_eok])

        print(f"OK — {len(records)} days ({records[0][0]} ~ {records[-1][0]})")
        return records
    except Exception as e:
        print(f"ERROR: {e}")
        return None

def main():
    print("=" * 60)
    print("한국 주도주 OHLC 데이터 수집")
    print("=" * 60)

    result = {
        "generated": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "stocks": {},
        "meta": {}
    }

    # 1. KOSPI 인덱스
    print("\n[1] KOSPI 인덱스")
    kospi_data = fetch_ohlc(INDEX[2], INDEX[1])
    if kospi_data:
        result["stocks"]["kospi"] = kospi_data
        result["meta"]["kospi"] = {
            "name": "KOSPI",
            "ticker": INDEX[2],
            "start": kospi_data[0][0],
            "end": kospi_data[-1][0],
            "count": len(kospi_data)
        }

    # 2. 개별 종목 — 같은 티커는 한 번만 수집
    print("\n[2] 주도주 종목")
    fetched_tickers = {}  # ticker → data (캐시)

    for stock_id, name, ticker, era, cycle in STOCKS:
        if ticker not in fetched_tickers:
            data = fetch_ohlc(ticker, name)
            fetched_tickers[ticker] = data
        else:
            data = fetched_tickers[ticker]
            print(f"  {name} ({ticker}) — cached from previous fetch")

        if data:
            result["stocks"][stock_id] = data
            result["meta"][stock_id] = {
                "name": name,
                "ticker": ticker,
                "era": era,
                "cycle": cycle,
                "start": data[0][0],
                "end": data[-1][0],
                "count": len(data)
            }

    # 3. 저장 (권한 오류 시 다른 이름으로 저장)
    output_path = "leading_stocks_data.json"
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False)
    except PermissionError:
        output_path = "leading_stocks_data_new.json"
        print(f"\n기존 파일 잠김 — {output_path}로 저장합니다.")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False)

    file_size = os.path.getsize(output_path)
    print(f"\n{'=' * 60}")
    print(f"저장 완료: {output_path} ({file_size / 1024 / 1024:.1f} MB)")
    print(f"종목 수: {len(result['stocks'])}")
    print(f"\n데이터 가용 범위:")
    for sid, meta in result["meta"].items():
        print(f"  {meta['name']:12s} | {meta['start']} ~ {meta['end']} | {meta['count']:,} days")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n오류 발생: {e}")
        import traceback
        traceback.print_exc()

    print()
    input("완료. Enter 키를 누르면 종료됩니다...")
