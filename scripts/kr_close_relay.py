# -*- coding: utf-8 -*-
"""kr_close_relay.py v3 — 한국장 마감 릴레이 (KIS → data/kr_close_latest.json)
확정: 지수코드(0001/1001/2001/3003), 거래대금순 BLNG=3, ETF·ETN 제외 마스크 0000001100,
      투자자별 시장구분 KSP/KSQ(+0001/1001), 단위: 지수 거래대금 백만원 / 순위 거래대금 원 / 투자자 백만원
미확정(자가 발견): 선물(K2I)·코스닥150선물(KQI)의 업종구분 — 후보 순회 후 nonzero 채택, notes에 기록"""
import json, os, time, urllib.request, urllib.parse
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))
BASE = "https://openapi.koreainvestment.com:9443"
APPKEY = os.environ["KIS_APP_KEY"]
APPSECRET = os.environ["KIS_APP_SECRET"]
PROBE = os.environ.get("PROBE", "0") == "1"

INDEX_CODES = {"코스피": "0001", "코스닥": "1001", "코스피200": "2001", "코스닥150": "3003"}
TR_INDEX, TR_VOLRANK, TR_INVESTOR = "FHPUP02100000", "FHPST01710000", "FHPTJ04030000"

INVESTOR_TARGETS = {
    "코스피":        [("KSP", "0001")],
    "코스닥":        [("KSQ", "1001")],
    "선물(코스피200)": [("K2I", "0001"), ("K2I", "F001"), ("K2I", "2001"), ("K2I", "0002"), ("K2I", "K200")],
    "코스닥150선물":  [("KQI", "F001"), ("KQI", "1001"), ("KQI", "0001"), ("KQI", "3003")],
}
FIELDS = {"개인": "prsn", "외국인": "frgn", "기관계": "orgn", "금융투자": "scrt",
          "투신": "ivtr", "연기금등": "fund", "사모펀드": "pe_fund", "기타법인": "etc_corp"}

ETF_PREFIX = ("KODEX", "TIGER", "PLUS", "ACE", "SOL", "RISE", "KIWOOM", "KOSEF",
              "HANARO", "ARIRANG", "WON", "TIMEFOLIO", "에셋플러스", "KCGI")

def http(method, path, headers=None, body=None, params=None):
    url = BASE + path + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None,
                                 headers=headers or {}, method=method)
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())

