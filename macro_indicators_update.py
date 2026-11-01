#!/usr/bin/env python3
"""
경제지표 탭 데이터 수집 → data/macro_indicators.json
  * FRED API (환경변수 FRED_API_KEY, 없으면 fredgraph.csv 시도): 고용·소매판매·CPI·PCE·PPI 와 세부지표, 경기침체(USREC)
    - 실패한 시리즈는 이전 JSON 값을 그대로 유지 (data/macro_indicators.json 은 2026-10-15 브라우저 빌드로 시드됨)
  * OECD 경기선행지수(CLI): OECD SDMX API (미국·한국·중국·G20·일본·유로존)
  * ISM 제조업/서비스업: investing.com 차트 JSON (서버에서 403 이면 건너뜀 — 페이지가 브라우저에서 직접 받고 캐시는 보조)
  * S&P500 월말 종가 (yfinance ^GSPC, 1927~) — 역사 비교용 (실패 시 FRED SP500 10년)
GitHub Actions 에서 매일 실행. 순수 stdlib + (선택) yfinance.
"""
import json, os, sys, csv, io, time, re
import urllib.request, urllib.parse
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE if os.path.isdir(os.path.join(HERE, 'data')) else os.path.dirname(HERE)
OUT = os.path.join(ROOT, 'data', 'macro_indicators.json')
START = '1960-01-01'
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'}

# id: (label, unit, group, transform hint)
FRED = {
  # 고용
  'UNRATE':   ('실업률', '%', 'labor', 'level'),
  'PAYEMS':   ('비농업 고용', '천명', 'labor', 'diff'),
  'JTSJOL':   ('JOLTS 구인건수', '천건', 'labor', 'level'),
  'ICSA':     ('신규 실업수당 청구', '건', 'labor', 'level'),
  'CES0500000003': ('시간당 임금(민간)', '$', 'labor', 'yoy'),
  'U6RATE':   ('U-6 광의 실업률', '%', 'labor', 'level'),
  # 2026-11-01 세부지표 확장 (BT "전부 추가")
  'CCSA':     ('연속 실업수당 청구', '건', 'labor', 'level'),
  'CIVPART':  ('경제활동참가율', '%', 'labor', 'level'),
  'LNS12300060': ('25~54세 고용률', '%', 'labor', 'level'),
  'MANEMP':   ('제조업 고용', '천명', 'labor', 'diff'),
  'USCONS':   ('건설업 고용', '천명', 'labor', 'diff'),
  'USGOVT':   ('정부 고용', '천명', 'labor', 'diff'),
  'TEMPHELPS': ('임시직 고용', '천명', 'labor', 'diff'),
  'AWHAETP':  ('주당 근로시간(민간)', '시간', 'labor', 'level'),
  'JTSQUR':   ('JOLTS 자발적 퇴직률', '%', 'labor', 'level'),
  'JTSLDL':   ('JOLTS 해고', '천건', 'labor', 'level'),
  # 소매판매
  'RSAFS':    ('소매판매', '백만$', 'retail', 'yoy'),
  'RSFSXMV':  ('소매판매(자동차 제외)', '백만$', 'retail', 'yoy'),
  'RSXFS':    ('소매판매(음식서비스 제외)', '백만$', 'retail', 'yoy'),
  'RSMVPD':   ('소매: 자동차·부품', '백만$', 'retail', 'level'),
  'RSGASS':   ('소매: 주유소', '백만$', 'retail', 'level'),
  'RSBMGESD': ('소매: 건자재·원예', '백만$', 'retail', 'level'),
  'RSFSDP':   ('소매: 음식서비스', '백만$', 'retail', 'level'),
  # CPI
  'CPIAUCSL': ('CPI 헤드라인', 'idx', 'cpi', 'yoy'),
  'CPILFESL': ('CPI 근원', 'idx', 'cpi', 'yoy'),
  'CUSR0000SAH1': ('CPI 주거', 'idx', 'cpi', 'yoy'),
  'CPIENGSL': ('CPI 에너지', 'idx', 'cpi', 'yoy'),
  'CPIUFDSL': ('CPI 식품', 'idx', 'cpi', 'yoy'),
  'CUSR0000SASLE': ('CPI 서비스(에너지 제외)', 'idx', 'cpi', 'yoy'),
  'CUSR0000SACL1E': ('CPI 상품(식품·에너지 제외)', 'idx', 'cpi', 'yoy'),
  'CUSR0000SASL2RS': ('CPI 서비스(주거 임대료 제외)', 'idx', 'cpi', 'yoy'),
  'CUSR0000SEHC': ('CPI 자가주거비(OER)', 'idx', 'cpi', 'yoy'),
  'CUSR0000SETA01': ('CPI 신차', 'idx', 'cpi', 'yoy'),
  'CUSR0000SETA02': ('CPI 중고차', 'idx', 'cpi', 'yoy'),
  'CUSR0000SAM2': ('CPI 의료서비스', 'idx', 'cpi', 'yoy'),
  'CUSR0000SAS4': ('CPI 운송서비스', 'idx', 'cpi', 'yoy'),
  'CORESTICKM159SFRBATL': ('애틀랜타연준 끈적 근원CPI', '%', 'cpi', 'level'),
  # PCE
  'PCEPI':    ('PCE 헤드라인', 'idx', 'pce', 'yoy'),
  'PCEPILFE': ('PCE 근원', 'idx', 'pce', 'yoy'),
  'DGDSRG3M086SBEA': ('PCE 상품', 'idx', 'pce', 'yoy'),
  'DSERRG3M086SBEA': ('PCE 서비스', 'idx', 'pce', 'yoy'),
  'IA001260M': ('PCE 서비스(주거·에너지 제외)', 'idx', 'pce', 'yoy'),
  'PCETRIM12M159SFRBDAL': ('댈러스연준 절사평균 PCE', '%', 'pce', 'level'),
  # PPI
  'PPIFIS':   ('PPI 최종수요', 'idx', 'ppi', 'yoy'),
  'PPIFES':   ('PPI 최종수요 근원(식품·에너지 제외)', 'idx', 'ppi', 'yoy'),
  'PPIACO':   ('PPI 전체 원자재', 'idx', 'ppi', 'yoy'),
  'WPSFD4131': ('PPI 최종수요 서비스', 'idx', 'ppi', 'yoy'),
  # 기타
  'USREC':    ('NBER 경기침체', '0/1', 'misc', 'level'),
  'SP500':    ('S&P500 (FRED 10년)', 'pt', 'misc', 'level'),
}
MIN_PTS = {'UNRATE': 700, 'PAYEMS': 700, 'CPIAUCSL': 700, 'PCEPI': 600, 'PPIACO': 700, 'USREC': 700, 'RSAFS': 350}

ISM = {  # investing.com event id → (키, 라벨)
  173: ('mfg_pmi', 'ISM 제조업 PMI'), 174: ('mfg_prices', 'ISM 제조업 가격'), 1046: ('mfg_employment', 'ISM 제조업 고용'), 1483: ('mfg_neworders', 'ISM 제조업 신규주문'),
  176: ('svc_pmi', 'ISM 서비스업 PMI'), 1050: ('svc_neworders', 'ISM 서비스업 신규주문'), 1048: ('svc_employment', 'ISM 서비스업 고용'), 1049: ('svc_prices', 'ISM 서비스업 가격'),
}
OECD_URL = 'https://sdmx.oecd.org/public/rest/data/OECD.SDD.STES,DSD_STES@DF_CLI,/USA+KOR+CHN+G20+JPN+EA20.M.LI...AA...H?startPeriod=1990-01&format=csvfilewithlabels'

def log(*a): print(datetime.now().strftime('[%H:%M:%S]'), *a, flush=True)

def get(url, headers=None, retry=3, timeout=60):
    h = dict(UA); h.update(headers or {})
    for k in range(retry):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=timeout) as r:
                return r.read().decode('utf-8', errors='replace'), r.status
        except urllib.error.HTTPError as e:
            if e.code in (403, 404): return None, e.code
            log(f'  retry {k+1}: {e}'); time.sleep(3)
        except Exception as e:
            log(f'  retry {k+1}: {e}'); time.sleep(3)
    return None, 0

FRED_KEY = os.environ.get('FRED_API_KEY', '').strip()   # GitHub Secrets → FRED 공식 API (fredgraph.csv 는 GitHub 러너에서 타임아웃/차단)

def fred(sid):
    if FRED_KEY:
        raw, st = get(f'https://api.stlouisfed.org/fred/series/observations?series_id={sid}&api_key={FRED_KEY}&file_type=json&observation_start={START}', retry=2, timeout=40)
        if raw:
            try:
                out = [[o['date'], float(o['value'])] for o in json.loads(raw).get('observations', []) if o.get('value') not in ('.', '', None)]
                if out: return out
            except Exception as e: log(f'  {sid}: API parse error {e}')
        else: log(f'  {sid}: API HTTP {st}')
    end = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    raw, st = get(f'https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}&cosd={START}&coed={end}', retry=1, timeout=30)
    if not raw: return None
    out = []
    for rec in list(csv.reader(io.StringIO(raw)))[1:]:
        if len(rec) < 2 or rec[1].strip() in ('.', '', 'NA'): continue
        try: out.append([rec[0].strip(), float(rec[1])])
        except ValueError: pass
    return out or None

# 카드 대표 시리즈 — 최신 월 값이 "처음 발표된 날" (2026-11-01 BT: 최근 데이터 발표일 표시)
#   ALFRED 실시간(vintage) 조회: 그 관측월 값의 모든 버전 중 가장 이른 realtime_start = 최초 발표일.
REL_SIDS = ['UNRATE', 'PAYEMS', 'RSAFS', 'CPIAUCSL', 'PCEPI', 'PPIFIS']

def fred_first_release(sid, obs_date):
    if not FRED_KEY or not obs_date: return None
    raw, st = get(f'https://api.stlouisfed.org/fred/series/observations?series_id={sid}&api_key={FRED_KEY}&file_type=json'
                  f'&observation_start={obs_date}&observation_end={obs_date}&realtime_start=1990-01-01&realtime_end=9999-12-31', retry=2, timeout=40)
    if not raw: log(f'  {sid}: release HTTP {st}'); return None
    try:
        rs = [o['realtime_start'] for o in json.loads(raw).get('observations', []) if o.get('value') not in ('.', '', None)]
        return min(rs) if rs else None
    except Exception as e:
        log(f'  {sid}: release parse error {e}'); return None

# ── ISM 제조업 세부지수 (2026-11-01 BT) ─────────────────────────────────────
#   investing.com 에 재고·공급자납기 등이 없어 ISM 공식 보도자료(PR Newswire)에서 수집.
#   과거 2012-09~ 는 scripts/ism_mfg_detail_seed.csv (보도자료 전수 파싱, 다음달 보도자료의 '전월' 칸 = 수정치 우선).
#   매일: 최근 제조업 보도자료 2건의 "MANUFACTURING AT A GLANCE" 표 → 당월 값 + 전월 수정치 반영.
#   PR Newswire 실패 시 ismworld.org 월별 페이지로 폴백. 둘 다 실패하면 이전 JSON 유지.
ISMD_KEYS = ['pmi', 'new_orders', 'production', 'employment', 'supplier_deliveries', 'inventories',
             'customers_inventories', 'prices', 'backlog', 'export_orders', 'imports']
ISMD_PAT = [(r'^(manufacturing )?pmi', 'pmi'), (r'^new orders', 'new_orders'), (r'^production', 'production'),
            (r'^employment', 'employment'), (r'^supplier deliveries', 'supplier_deliveries'), (r'^inventories', 'inventories'),
            (r'^customers', 'customers_inventories'), (r'^prices', 'prices'), (r'^backlog', 'backlog'),
            (r'^new export', 'export_orders'), (r'^imports', 'imports')]
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

def _strip(h):
    import html as _h
    return re.sub(r'\s+', ' ', _h.unescape(re.sub(r'<[^>]+>', ' ', h))).strip()

def _ism_glance(page):
    """보도자료 HTML → (ym, {k:v}, pym, {k:v}) 또는 None"""
    tabs = re.findall(r'<table.*?</table>', page, flags=re.S | re.I)
    tab = next((t for t in tabs if re.search(r'AT A GLANCE', t, re.I)), None) or next((t for t in tabs if re.search(r'Series\s*Index', _strip(t), re.I)), None)
    if not tab: return None
    txt = _strip(tab) + ' ' + _strip(re.search(r'<title>(.*?)</title>', page, re.S | re.I).group(1) if re.search(r'<title>', page, re.I) else '')
    m = re.search(r'(' + '|'.join(MONTHS) + r')\s+(\d{4})', txt, re.I)
    if not m: return None
    y, mo = int(m.group(2)), MONTHS.index(m.group(1).lower()) + 1
    py, pm = (y, mo - 1) if mo > 1 else (y - 1, 12)
    cur, prv = {}, {}
    for row in re.findall(r'<tr.*?</tr>', tab, flags=re.S | re.I):
        cells = [_strip(c) for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', row, flags=re.S | re.I)]
        if len(cells) < 3: continue
        nm = re.sub(r"[®’']", '', cells[0].lower()).strip()
        k = next((k for pat, k in ISMD_PAT if re.match(pat, nm)), None)
        if not k: continue
        try: cur[k] = float(cells[1])
        except ValueError: pass
        try: prv[k] = float(cells[2])
        except ValueError: pass
    if len(cur) < 8: return None
    return f'{y}-{mo:02d}', cur, f'{py}-{pm:02d}', prv

def ism_detail(prev):
    base = {}
    seed = os.path.join(ROOT, 'scripts', 'ism_mfg_detail_seed.csv')
    if os.path.exists(seed):
        for r in csv.reader(open(seed, encoding='utf-8')):
            if not r or r[0].startswith('#') or r[0] == 'ym': continue
            base[r[0]] = {k: (float(v) if v not in ('', 'null') else None) for k, v in zip(ISMD_KEYS, r[1:])}
    for row in ((prev or {}).get('ism_detail') or {}).get('data', []):
        base[row[0]] = dict(zip(ISMD_KEYS, row[1:]))
    got = []
    raw, st = get('https://www.prnewswire.com/news/institute-for-supply-management/', retry=2, timeout=40)
    links = []
    if raw:
        for href, txt in re.findall(r'<a[^>]+href="([^"]*news-releases/[^"]+)"[^>]*>(.*?)</a>', raw, flags=re.S | re.I):
            t = _strip(txt)
            if re.search(r'Manufacturing PMI', t, re.I) and not re.search(r'Services', t, re.I):
                u = href if href.startswith('http') else 'https://www.prnewswire.com' + href
                u = u.split('?')[0]
                if u not in links: links.append(u)
    else: log(f'  ISM detail: PR Newswire list HTTP {st}')
    for u in links[:2][::-1]:          # 오래된 것부터 → 최신이 마지막에 덮어씀
        pg, st = get(u, retry=2, timeout=40)
        g = _ism_glance(pg) if pg else None
        if g: got.append(g)
        else: log(f'  ISM detail: parse fail {u[-60:]} ({st})')
        time.sleep(1)
    if not got:     # 폴백: ismworld 월별 페이지 (최근 2개월명)
        now = datetime.now(timezone.utc)
        for back in (2, 1):
            mo = (now.month - back - 1) % 12
            pg, st = get(f'https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/pmi/{MONTHS[mo]}/', retry=2, timeout=40)
            g = _ism_glance(pg) if pg else None
            if g: got.append(g)
            else: log(f'  ISM detail: ismworld {MONTHS[mo]} fail ({st})')
    for ym, cur, pym, prv in got:
        base[ym] = {**base.get(ym, {}), **cur}
        if prv: base[pym] = {**base.get(pym, {}), **prv}
        log(f'  ISM detail: {ym} {cur.get("pmi")} / revised {pym} {prv.get("pmi")}')
    if not base: return None
    rows = [[ym] + [base[ym].get(k) for k in ISMD_KEYS] for ym in sorted(base)]
    return {'keys': ISMD_KEYS, 'source': 'ISM Report On Business (PR Newswire / ismworld.org)', 'data': rows}

def oecd():
    raw, st = get(OECD_URL, headers={'Accept': 'text/csv'})
    if not raw: log('OECD fail', st); return None
    rows = list(csv.reader(io.StringIO(raw)))
    if not rows: return None
    h = rows[0]; ia, it, iv = h.index('REF_AREA'), h.index('TIME_PERIOD'), h.index('OBS_VALUE')
    out = {}
    for r in rows[1:]:
        try: out.setdefault(r[ia], []).append([r[it], round(float(r[iv]), 3)])
        except (ValueError, IndexError): pass
    for k in out: out[k].sort()
    return out

def ism():
    out = {}
    for eid, (key, label) in ISM.items():
        raw, st = get(f'https://sbcharts.investing.com/events_charts/us/{eid}.json', headers={'Referer': 'https://www.investing.com/economic-calendar/', 'Accept': 'application/json'}, retry=2, timeout=30)
        if not raw: log(f'  ISM {key}: HTTP {st} — skip'); continue
        try:
            j = json.loads(raw); data = []
            for d in j.get('data', []):
                ts, v = d[0], d[1]
                if v is None: continue
                data.append([datetime.fromtimestamp(ts / 1000, tz=timezone.utc).strftime('%Y-%m-%d'), float(v)])
            fc = {}
            for a in j.get('attr', []):
                if a.get('forecast') is not None: fc[datetime.fromtimestamp(a['timestamp'] / 1000, tz=timezone.utc).strftime('%Y-%m-%d')] = a['forecast']
            out[key] = {'label': label, 'data': data, 'forecast': fc}
            log(f'  ISM {key}: {len(data)} pts, last {data[-1] if data else None}')
        except Exception as e:
            log(f'  ISM {key}: parse error {e}')
        time.sleep(0.5)
    return out

def spx_monthly():
    try:
        import yfinance as yf
        h = yf.Ticker('^GSPC').history(period='max', interval='1mo', auto_adjust=False)
        out = [[str(idx.date())[:7], round(float(row['Close']), 2)] for idx, row in h.iterrows() if row['Close'] == row['Close']]
        if len(out) > 500: return out
        log('yfinance spx short', len(out))
    except Exception as e:
        log('yfinance spx fail', e)
    return None

def main():
    prev = {}
    if os.path.exists(OUT):
        try: prev = json.load(open(OUT, encoding='utf-8'))
        except Exception: prev = {}
    series = {}
    for sid, (label, unit, grp, tf) in FRED.items():
        d = fred(sid)
        if not d:
            log(f'{sid}: FAIL — keep previous');
            if sid in prev.get('series', {}): series[sid] = prev['series'][sid]
            continue
        if len(d) < MIN_PTS.get(sid, 50): log(f'  WARN {sid}: only {len(d)} pts')
        series[sid] = {'label': label, 'unit': unit, 'group': grp, 'tf': tf, 'data': d}
        log(f'{sid:16s} {len(d):5d} pts  {d[0][0]} ~ {d[-1][0]}  last={d[-1][1]}')
        time.sleep(0.3)
    # 최신 데이터 발표일
    release = {}
    for sid in REL_SIDS:
        if sid not in series: continue
        last = series[sid]['data'][-1][0]
        r = fred_first_release(sid, last)
        if not r and prev.get('release', {}).get(sid, {}).get('obs') == last: r = prev['release'][sid]['date']
        if r: release[sid] = {'obs': last, 'date': r}
        log(f'  release {sid:10s} {last} → {r}')
        time.sleep(0.3)
    # 침체 구간
    rec = []
    if 'USREC' in series:
        s = None
        for d, v in series['USREC']['data']:
            if v >= 1 and s is None: s = d
            if v < 1 and s is not None: rec.append([s, d]); s = None
        if s: rec.append([s, series['USREC']['data'][-1][0]])
    cli = oecd() or prev.get('oecd_cli')
    if cli: log('OECD CLI:', {k: (len(v), v[-1]) for k, v in cli.items()})
    ism_d = ism()
    if not ism_d: ism_d = prev.get('ism', {})
    else:
        for k, v in prev.get('ism', {}).items(): ism_d.setdefault(k, v)
    spx = spx_monthly() or prev.get('spx_monthly')
    try: ismd = ism_detail(prev) or prev.get('ism_detail')
    except Exception as e: log('ISM detail error', e); ismd = prev.get('ism_detail')
    if ismd: log('ISM detail rows', len(ismd['data']), ismd['data'][-1][:3])
    out = {
      'meta': {'updated': datetime.now(timezone.utc).isoformat(timespec='seconds'),
               'sources': 'FRED / OECD SDMX / investing.com(ISM) / yfinance(^GSPC)',
               'ism_cached_at': datetime.now(timezone.utc).isoformat(timespec='seconds') if ism_d else None},
      'series': series, 'release': release, 'recessions': rec, 'oecd_cli': cli, 'ism': ism_d, 'ism_detail': ismd, 'spx_monthly': spx,
    }
    # 데이터가 그대로면 파일을 건드리지 않음 (meta 제외 비교) → 불필요한 커밋 방지
    strip = lambda d: {k: v for k, v in d.items() if k != 'meta'}
    if prev and strip(prev) == strip(out):
        log('no data change — keep previous file'); return 0
    tmp = OUT + '.tmp'
    json.dump(out, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    os.replace(tmp, OUT)
    log('wrote', OUT, os.path.getsize(OUT) // 1024, 'KB')

if __name__ == '__main__':
    sys.exit(main())
