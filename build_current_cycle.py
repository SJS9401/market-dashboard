#!/usr/bin/env python3
"""
build_current_cycle.py — Current_cycle.html 데일리 자동 빌드

입력:
  - data/kospi_historical.json (1985-01-04 ~ 2026-04-24 정적 historical)
  - data/yahoo_dashboard.json   (^KS11 candles, daily GitHub Actions로 갱신)
  - Current_cycle_template.html (placeholder가 있는 base HTML)

처리:
  - historical + yahoo merge → 3사이클 (3저호황/중국 중후장대/현재) 데이터 추출
  - 각 사이클 MDD 시계열 계산
  - 현재 cycle_day, matched 시점 등 메타 정보 산출
  - 템플릿의 __DATA_PLACEHOLDER__ / __TODAY__ / __YAHOO_LAST__ 치환

출력:
  - Current_cycle.html (배포본)

스케줄 (.github/workflows/current_cycle_update.yml):
  - 매일 KST 06:45 (UTC 21:45) — yahoo_dashboard_update 직후
  - workflow_dispatch (수동)

운영 메모:
  - 사이클 정의가 바뀌면 CYCLES dict 수정
  - 키움 CSV가 업데이트되면 kospi_historical.json 재생성 (별도 작업)
"""

import json
import os
import sys
from datetime import datetime, timezone, timedelta, date

# ─────────────────────────────────────────────────────────────────────
# 설정
# ─────────────────────────────────────────────────────────────────────

ROOT = os.path.dirname(os.path.abspath(__file__))
HIST_PATH = os.path.join(ROOT, 'data', 'kospi_historical.json')
YAHOO_PATH = os.path.join(ROOT, 'data', 'yahoo_dashboard.json')
DOTCOM_PATH = os.path.join(ROOT, 'data', 'dotcom_historical.json')
TEMPLATE_PATH = os.path.join(ROOT, 'Current_cycle_template.html')
OUTPUT_PATH = os.path.join(ROOT, 'Current_cycle.html')

# 닷컴 vs AI 카드 정렬 (KB증권 그림 53/54 기준)
DOTCOM_AI_ANCHORS = {
    'first':  {'dotcom_sym': 'CSCO', 'ai_sym': 'NVDA',
               'dotcom_anchor': date(1995, 1, 3), 'dotcom_end': date(2001, 12, 31),
               'ai_anchor':     date(2021, 7, 1),
               'label': '1차 주도주', 'dotcom_color': '#9ca3af', 'ai_color': '#f87171'},
    'second': {'dotcom_sym': 'QCOM', 'ai_sym': 'MU',
               'dotcom_anchor': date(1995, 1, 3), 'dotcom_end': date(2001, 12, 31),
               'ai_anchor':     date(2021, 7, 1),
               'label': '2차 주도주', 'dotcom_color': '#fbbf24', 'ai_color': '#ef4444'},
}

CYCLES = {
    '3jeo': {
        'anchor': date(1985, 5, 20),
        'end': date(1989, 12, 8),
        'label': '3저호황 (1985.05 저점)',
        'color': '#60a5fa',
    },
    'china': {
        'anchor': date(2003, 3, 17),
        'end': date(2008, 7, 8),
        'label': '중국 중후장대 (2003.03 저점)',
        'color': '#34d399',
    },
    'now': {
        'anchor': date(2025, 4, 9),
        'end': None,  # 진행 중 — 최신 데이터까지
        'label': '현재 (2025.04 저점)',
        'color': '#f87171',
    },
}

KST = timezone(timedelta(hours=9))


# ─────────────────────────────────────────────────────────────────────
# 데이터 로드 & merge
# ─────────────────────────────────────────────────────────────────────

def load_kospi_data():
    """historical + yahoo merge → {date: close} dict 반환."""
    data = {}

    # 1) Historical (정적, 1985-01-04 ~ 2026-04-24)
    if not os.path.exists(HIST_PATH):
        sys.exit(f"[ERROR] historical 데이터 없음: {HIST_PATH}")
    with open(HIST_PATH, encoding='utf-8') as f:
        hist = json.load(f)
    for row in hist['data']:
        d = datetime.strptime(row[0], '%Y-%m-%d').date()
        data[d] = round(float(row[1]), 2)
    hist_last = max(data.keys())
    print(f"  [historical] {len(data):,}일 ({min(data.keys())} ~ {hist_last})")

    # 2) Yahoo cache (^KS11 candles, hist_last 이후만 보충)
    if not os.path.exists(YAHOO_PATH):
        print(f"  [WARN] yahoo cache 없음: {YAHOO_PATH} — historical만 사용")
    else:
        with open(YAHOO_PATH, encoding='utf-8') as f:
            yh = json.load(f)
        candles = yh.get('data', {}).get('^KS11', {}).get('candles', [])
        added = 0
        yahoo_last = None
        for c in candles:
            d = datetime.strptime(c['time'], '%Y-%m-%d').date()
            if d > hist_last:
                data[d] = round(float(c['close']), 2)
                added += 1
                if yahoo_last is None or d > yahoo_last:
                    yahoo_last = d
        print(f"  [yahoo cache] {added}일 보충 (~{yahoo_last})")

    return data, hist_last, max(data.keys())


# ─────────────────────────────────────────────────────────────────────
# 사이클 시리즈 + MDD 계산
# ─────────────────────────────────────────────────────────────────────

def build_series(data, anchor, end):
    """anchor ~ end (inclusive) 구간 [{days, date, close}, ...]."""
    if end is None:
        end = max(data.keys())
    sorted_dates = sorted(d for d in data.keys() if anchor <= d <= end)
    return [
        {'days': (d - anchor).days, 'date': d.strftime('%Y-%m-%d'), 'close': data[d]}
        for d in sorted_dates
    ]


def calc_mdd(series):
    """MDD 시계열 [{days, date, mdd}, ...] — 시작점부터 누적."""
    rmax = 0.0
    out = []
    for x in series:
        if x['close'] > rmax:
            rmax = x['close']
        dd = (x['close'] / rmax - 1.0) * 100.0
        out.append({'days': x['days'], 'date': x['date'], 'mdd': round(dd, 2)})
    return out


def get_peak(series):
    p = max(series, key=lambda x: x['close'])
    return {'days': p['days'], 'date': p['date'], 'close': p['close']}


# ─────────────────────────────────────────────────────────────────────
# 닷컴 vs AI 데이터 빌드
# ─────────────────────────────────────────────────────────────────────

def load_dotcom():
    """dotcom_historical.json → {symbol: [[date, close], ...]} 반환. 없으면 None."""
    if not os.path.exists(DOTCOM_PATH):
        print(f"  [INFO] dotcom historical 없음 ({DOTCOM_PATH}) — 닷컴 vs AI 카드 skip")
        return None
    with open(DOTCOM_PATH, encoding='utf-8') as f:
        d = json.load(f)
    return d.get('data', {})


def load_ai_yahoo(yahoo_data, sym, anchor):
    """yahoo_dashboard.json 의 sym candle → [[date, close], ...] (anchor 이후만)."""
    candles = yahoo_data.get('data', {}).get(sym, {}).get('candles', [])
    out = []
    for c in candles:
        d = datetime.strptime(c['time'], '%Y-%m-%d').date()
        if d >= anchor:
            out.append([d.strftime('%Y-%m-%d'), round(float(c['close']), 4)])
    return out


def build_pair_series(rows, anchor, end=None):
    """[[date, close], ...] → [{days, date, close}, ...] (anchor 이후만)."""
    out = []
    for r in rows:
        d = datetime.strptime(r[0], '%Y-%m-%d').date()
        if d < anchor:
            continue
        if end and d > end:
            continue
        out.append({'days': (d - anchor).days, 'date': r[0], 'close': r[1]})
    return out


def build_dotcom_ai_payload(yahoo_data):
    """닷컴 vs AI 카드 2개의 payload 생성. dotcom 데이터 없으면 None."""
    dotcom = load_dotcom()
    if dotcom is None:
        return None

    result = {}
    for key, cfg in DOTCOM_AI_ANCHORS.items():
        dot_rows = dotcom.get(cfg['dotcom_sym'])
        if not dot_rows:
            print(f"  [WARN] {cfg['dotcom_sym']} 데이터 없음 — {key} skip")
            continue
        ai_rows = load_ai_yahoo(yahoo_data, cfg['ai_sym'], cfg['ai_anchor'])
        if not ai_rows:
            print(f"  [WARN] {cfg['ai_sym']} yahoo 데이터 없음 — {key} skip")
            continue

        dot_series = build_pair_series(dot_rows, cfg['dotcom_anchor'], cfg['dotcom_end'])
        ai_series  = build_pair_series(ai_rows,  cfg['ai_anchor'])

        result[key] = {
            'label': cfg['label'],
            'dotcom_sym': cfg['dotcom_sym'],
            'dotcom_anchor': cfg['dotcom_anchor'].strftime('%Y-%m-%d'),
            'dotcom_end': cfg['dotcom_end'].strftime('%Y-%m-%d'),
            'dotcom_color': cfg['dotcom_color'],
            'dotcom_series': dot_series,
            'ai_sym': cfg['ai_sym'],
            'ai_anchor': cfg['ai_anchor'].strftime('%Y-%m-%d'),
            'ai_end': ai_series[-1]['date'] if ai_series else None,
            'ai_color': cfg['ai_color'],
            'ai_series': ai_series,
        }
        print(f"  [{key}] {cfg['dotcom_sym']} {len(dot_series)}일 ({dot_series[0]['date']}~{dot_series[-1]['date']}) "
              f"vs {cfg['ai_sym']} {len(ai_series)}일 ({ai_series[0]['date']}~{ai_series[-1]['date']})")

    return result if result else None


# ─────────────────────────────────────────────────────────────────────
# 메인 빌드
# ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print(f"build_current_cycle.py — {datetime.now(KST).strftime('%Y-%m-%d %H:%M KST')}")
    print("=" * 60)

    # 1) 데이터 로드
    data, hist_last, latest = load_kospi_data()

    # 1b) yahoo cache full load (NVDA, MU 용)
    yahoo_data = {}
    if os.path.exists(YAHOO_PATH):
        with open(YAHOO_PATH, encoding='utf-8') as f:
            yahoo_data = json.load(f)

    # 2) 사이클 시리즈 + MDD
    series = {}
    mdd_data = {}
    for key, cfg in CYCLES.items():
        s = build_series(data, cfg['anchor'], cfg['end'])
        if not s:
            sys.exit(f"[ERROR] {key} 사이클 빈 데이터 — anchor={cfg['anchor']}")
        series[key] = s
        mdd_data[key] = calc_mdd(s)
        worst = min(mdd_data[key], key=lambda x: x['mdd'])
        print(f"  [{key}] {len(s):,}일 ({s[0]['date']}~{s[-1]['date']}) "
              f"정점: {get_peak(s)['close']}pt @ {get_peak(s)['date']} · "
              f"worst MDD: {worst['mdd']:.2f}% @ {worst['date']}")

    # 3) 메타 정보
    cd = series['now'][-1]['days']
    today_kst = datetime.now(KST).date()

    def matched(key):
        return min(series[key], key=lambda x: abs(x['days'] - cd))

    meta = {
        'today': today_kst.strftime('%Y-%m-%d'),
        'cycle_day_today': cd,
        'cycles': {
            '3jeo': {
                'anchor': CYCLES['3jeo']['anchor'].strftime('%Y-%m-%d'),
                'end': CYCLES['3jeo']['end'].strftime('%Y-%m-%d'),
                'label': CYCLES['3jeo']['label'],
                'color': CYCLES['3jeo']['color'],
                'base': series['3jeo'][0]['close'],
                'peak': get_peak(series['3jeo']),
            },
            'china': {
                'anchor': CYCLES['china']['anchor'].strftime('%Y-%m-%d'),
                'end': CYCLES['china']['end'].strftime('%Y-%m-%d'),
                'label': CYCLES['china']['label'],
                'color': CYCLES['china']['color'],
                'base': series['china'][0]['close'],
                'peak': get_peak(series['china']),
            },
            'now': {
                'anchor': CYCLES['now']['anchor'].strftime('%Y-%m-%d'),
                'end': series['now'][-1]['date'],
                'label': CYCLES['now']['label'],
                'color': CYCLES['now']['color'],
                'base': series['now'][0]['close'],
                'peak': series['now'][-1],  # 진행 중 — 최근 종가가 peak
            },
        },
        'matched': {
            '3jeo': matched('3jeo'),
            'china': matched('china'),
        },
    }

    # 4) 닷컴 vs AI 카드 데이터
    print("\n[닷컴 vs AI 카드]")
    dotcom_ai = build_dotcom_ai_payload(yahoo_data)

    payload = {
        'series_3jeo': series['3jeo'],
        'series_china': series['china'],
        'series_now': series['now'],
        'mdd_3jeo': mdd_data['3jeo'],
        'mdd_china': mdd_data['china'],
        'mdd_now': mdd_data['now'],
        'dotcom_ai': dotcom_ai,
        'meta': meta,
    }

    # 4) 템플릿 치환
    if not os.path.exists(TEMPLATE_PATH):
        sys.exit(f"[ERROR] 템플릿 없음: {TEMPLATE_PATH}")
    with open(TEMPLATE_PATH, encoding='utf-8') as f:
        html = f.read()

    payload_str = json.dumps(payload, ensure_ascii=False, separators=(',', ':'))
    html = html.replace('__DATA_PLACEHOLDER__', payload_str)
    html = html.replace('__TODAY__', today_kst.strftime('%Y-%m-%d'))
    html = html.replace('__YAHOO_LAST__', series['now'][-1]['date'])

    if '__DATA_PLACEHOLDER__' in html or '__TODAY__' in html or '__YAHOO_LAST__' in html:
        sys.exit("[ERROR] placeholder 치환 누락")

    # 5) Atomic write
    tmp = OUTPUT_PATH + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        f.write(html)
    os.replace(tmp, OUTPUT_PATH)

    print(f"\n[OK] Built: {OUTPUT_PATH}")
    print(f"     size: {os.path.getsize(OUTPUT_PATH):,} bytes")
    print(f"     today (KST): {today_kst}, cycle_day: {cd}")
    print(f"     현재 코스피: {series['now'][-1]['close']}pt @ {series['now'][-1]['date']}")


if __name__ == '__main__':
    main()
