#!/usr/bin/env python3
"""
수출 탭 자동 갱신 — 관세청 tradedata.go.kr 로 K-stat 과거치(data/kr_export_items.json) 이후 달을 채운다.
  * 품목: scripts/kr_export_mti_map.json 의 HS10 목록을 합산 (산업부 20대 주력품목 정의와 동일 → 발표치와 일치)
  * 국가: 국가별 실적(ETS_MNK_1020000D) → data/kr_export_country.json
  * 잠정치: 10일 단위 잠정치(총액 + 10개 품목) → kr_export_items.json['provisional']
  * 중량(wgt, 톤): 관세청 구간(kstat_last 이후)만 채움. K-stat 과거 구간 중량은 별도 재수집 필요 (2026-10-15 BT 요청: 단가 = 금액/중량)
순수 stdlib. GitHub Actions 에서 매일 실행, 변경 있을 때만 커밋.
"""
import json, os, sys, time, re
import urllib.request, urllib.parse
from datetime import datetime, timezone, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE if os.path.isdir(os.path.join(HERE, 'data')) else os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'data')
ITEMS_PATH = os.path.join(DATA, 'kr_export_items.json')
CTRY_PATH = os.path.join(DATA, 'kr_export_country.json')
MAP_PATH = os.path.join(ROOT, 'scripts', 'kr_export_mti_map.json')

TRADE_URL = 'https://tradedata.go.kr/cts/hmpg/retrieveTrade.do'
TENT_URL = 'https://tradedata.go.kr/cts/hmpg/retrieveTentativeValues.do'
HEADERS = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0 (market-dashboard kr_export_items_update)',
           'Referer': 'https://tradedata.go.kr/cts/index.do', 'X-Requested-With': 'XMLHttpRequest'}
KST = timezone(timedelta(hours=9))
CHUNK = 250          # HS10 코드 묶음 크기 (POST 본문 길이 안전선)
SLEEP = 0.4

def log(*a):
    print(datetime.now(KST).strftime('[%H:%M:%S]'), *a, flush=True)

def post(url, params, retries=3):
    body = urllib.parse.urlencode(params).encode()
    for k in range(retries):
        try:
            req = urllib.request.Request(url, data=body, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode('utf-8'))
        except Exception as e:
            log(f'  retry {k+1}: {e}')
            time.sleep(2 + 2 * k)
    raise RuntimeError('tradedata fetch failed')

def num(s):
    try: return float(str(s).replace(',', '').strip() or 0)
    except ValueError: return 0.0

def ym_add(ym, n):
    y, m = int(ym[:4]), int(ym[5:7]); m += n
    while m > 12: y += 1; m -= 12
    while m < 1: y -= 1; m += 12
    return f'{y:04d}-{m:02d}'

def fetch_hs10(codes, fr, to):
    """HS10 코드 목록의 월별 합계 {ym: (exp_usd, imp_usd, exp_kg)}"""
    acc = {}
    for i in range(0, len(codes), CHUNK):
        chunk = codes[i:i + CHUNK]
        j = post(TRADE_URL, {'tradeKind': 'ETS_MNK_1020000A', 'priodKind': 'MON', 'priodFr': fr, 'priodTo': to,
                             'statsBase': 'acptDd', 'ttwgTpcd': '1', 'selectPaging': '1', 'showPagingLine': '20000',
                             'sortColumn': '', 'sortOrder': '', 'hsSgnGrpCol': 'HS10_SGN', 'hsSgnWhrCol': 'HS10_SGN',
                             'hsSgn': ','.join(chunk), 'subHsSgn': 'N'})
        for it in j.get('items', []):
            t = str(it.get('priodTitle', '')).strip()
            if not re.match(r'^\d{4}\.\d{2}$', t): continue
            ym = t.replace('.', '-')
            e, im, w = acc.get(ym, (0.0, 0.0, 0.0))
            acc[ym] = (e + num(it.get('expUsdAmt')) * 1000, im + num(it.get('impUsdAmt')) * 1000, w + num(it.get('expTtwg')))   # 관세청 금액은 천달러 단위
        time.sleep(SLEEP)
    return acc

def fetch_country(fr, to):
    j = post(TRADE_URL, {'tradeKind': 'ETS_MNK_1020000D', 'priodKind': 'MON', 'priodFr': fr, 'priodTo': to,
                         'statsBase': 'acptDd', 'ttwgTpcd': '1000', 'selectPaging': '1', 'showPagingLine': '20000',
                         'sortColumn': '', 'sortOrder': '', 'cntyNm': ''})
    out = {}
    for it in j.get('items', []):
        t = str(it.get('priodTitle', '')).strip()
        if not re.match(r'^\d{4}\.\d{2}$', t): continue
        ym = t.replace('.', '-'); cd = str(it.get('cntyCd', '')).strip()
        if not cd: continue
        out.setdefault(ym, {})[cd] = (num(it.get('expUsdAmt')) * 1000, num(it.get('impUsdAmt')) * 1000)   # 천달러 → 달러
    return out

def fetch_provisional(fr, to):
    """10일 단위 잠정치: {period: {cutoff: {'total':usd_k, 'items':{name:usd_k}}}}"""
    NAMES = ['반도체', '철강제품', '승용차', '석유제품', '무선통신기기', '선박', '자동차부품', '컴퓨터주변기기', '정밀기기', '가전제품']
    out = {}
    for pd, cutoff in (('1', '1-10'), ('2', '1-20'), ('3', '1-31')):
        j = post(TENT_URL, {'statsKind': 'ETS_MNK_1050000A', 'imexTpcd': 'E', 'priodKind': 'MON', 'priodFr': fr, 'priodTo': to,
                            'priodDate': pd, 'showPagingLine': '500', 'sortColumn': '', 'sortOrder': ''})
        for it in j.get('items', []):
            pm = str(it.get('priodMon', '')).strip()
            if len(pm) != 6: continue
            tot = num(it.get('itemUsdAmt00'))
            if tot <= 0: continue
            ym = pm[:4] + '-' + pm[4:]
            out.setdefault(ym, {})[cutoff] = {'total': tot, 'items': {NAMES[k]: num(it.get(f'itemUsdAmt{k+1:02d}')) for k in range(10)},
                                              'priod_dt': str(it.get('priodDt', '')).strip()}
        time.sleep(SLEEP)
    return out

M = lambda v: round(v / 1e6, 1)      # 달러 → 백만달러
T = lambda w: round(w / 1e3, 1)      # kg → 톤

def main():
    items = json.load(open(ITEMS_PATH, encoding='utf-8'))
    ctry = json.load(open(CTRY_PATH, encoding='utf-8'))
    hsmap = json.load(open(MAP_PATH, encoding='utf-8'))
    now = datetime.now(KST)
    last_done = f'{now.year:04d}-{now.month:02d}'           # 이번 달은 미완
    last_done = ym_add(last_done, -1)
    changed = False

    # ── 0. K-stat 과거치 이후 달은 매번 다시 받는다 (관세청 정정분 반영 + 이전 실행 오류 자가 복구) ──
    def truncate_after(obj, key_months, last_keep):
        keep = [i for i, m in enumerate(obj[key_months]) if m <= last_keep]
        n = len(keep)
        if n == len(obj[key_months]): return False
        obj[key_months] = obj[key_months][:n]
        for sid, ser in obj['series'].items():
            for k in ('exp', 'imp', 'wgt'):
                if k in ser: ser[k] = ser[k][:n]
        return True
    k_items = items['meta'].get('kstat_last') or '2026-08'
    k_ctry = ctry['meta'].setdefault('kstat_last', '2026-08')
    if truncate_after(items, 'months', k_items): changed = True
    if truncate_after(ctry, 'months', k_ctry): changed = True
    ns = len([m for m in items['sub_months'] if m <= k_items])
    if ns != len(items['sub_months']):
        items['sub_months'] = items['sub_months'][:ns]
        for lst in items['subs'].values():
            for sb in lst:
                sb['exp'] = sb['exp'][:ns]
                if 'wgt' in sb: sb['wgt'] = sb['wgt'][:ns]
        changed = True
    # ── 0b. 중량(wgt, 톤) 배열 보장 — 과거치(K-stat 구간)는 아직 없음 → None 으로 채움 (2026-10-15 신설) ──
    for ser in items['series'].values():
        if len(ser.setdefault('wgt', [])) != len(items['months']):
            ser['wgt'] = (ser['wgt'] + [None] * len(items['months']))[:len(items['months'])]; changed = True
    for lst in items['subs'].values():
        for sb in lst:
            if len(sb.setdefault('wgt', [])) != len(items['sub_months']):
                sb['wgt'] = (sb['wgt'] + [None] * len(items['sub_months']))[:len(items['sub_months'])]; changed = True

    # ── 1. 품목 월 확정치 (K-stat 과거치 이후) ──
    fr = ym_add(items['months'][-1], 1)
    if fr <= last_done:
        log(f'items: fetch {fr} ~ {last_done}')
        probe = fetch_hs10(hsmap['items']['semi']['hs10'][:10], fr.replace('-', ''), last_done.replace('-', ''))
        new_months = sorted(m for m in probe if m >= fr)
        if new_months:
            log('  months available:', new_months)
            per_item = {}
            for iid, spec in hsmap['items'].items():
                per_item[iid] = fetch_hs10(spec['hs10'], fr.replace('-', ''), last_done.replace('-', ''))
                log(f'  {iid:10s} {len(spec["hs10"]):5d} codes  ' + ' '.join(f'{m}:{M(per_item[iid].get(m,(0,0,0))[0]):,.0f}' for m in new_months))
            per_sub = {}
            for sid, spec in hsmap['subs'].items():
                per_sub[sid] = fetch_hs10(spec['hs10'], fr.replace('-', ''), last_done.replace('-', '')) if spec['hs10'] else {}
            for m in new_months:
                items['months'].append(m)
                tot_e = tot_i = 0.0
                for iid in items['series']:
                    if iid == 'total': continue
                    e, im, w = per_item[iid].get(m, (0.0, 0.0, 0.0))
                    items['series'][iid]['exp'].append(M(e)); items['series'][iid]['imp'].append(M(im))
                    items['series'][iid]['wgt'].append(T(w))          # 수출 중량(톤) — 관세청 kg 합산
                # 총액은 국가별 총계(전 품목)로 — 아래 국가 단계에서 채움. 임시로 품목합. (총액 중량은 국가별 통계에 없음 → None)
                items['series']['total']['exp'].append(None); items['series']['total']['imp'].append(None); items['series']['total']['wgt'].append(None)
                items['sub_months'].append(m)
                for parent, lst in items['subs'].items():
                    for s in lst:
                        e = per_sub.get(s['id'], {}).get(m)
                        s['exp'].append(M(e[0]) if e else None)
                        s['wgt'].append(T(e[2]) if e else None)
            items['meta']['last_month'] = new_months[-1]
            changed = True
    else:
        log('items: up to date', items['months'][-1])

    # ── 2. 국가별 ──
    fr_c = ym_add(ctry['months'][-1], 1)
    if fr_c <= last_done:
        log(f'country: fetch {fr_c} ~ {last_done}')
        cdata = fetch_country(fr_c.replace('-', ''), last_done.replace('-', ''))
        for m in sorted(k for k in cdata if k >= fr_c):
            rows = cdata[m]
            ctry['months'].append(m)
            tot_e = sum(v[0] for v in rows.values()); tot_i = sum(v[1] for v in rows.values())
            for c in ctry['countries']:
                cid = c['id']; ser = ctry['series'][cid]
                if cid == 'ALL': e, im = tot_e, tot_i
                elif 'members' in c:
                    e = sum(rows[x][0] for x in c['members'] if x in rows); im = sum(rows[x][1] for x in c['members'] if x in rows)
                else:
                    e, im = rows.get(cid, (None, None))
                ser['exp'].append(M(e) if e is not None else None); ser['imp'].append(M(im) if im is not None else None)
            # 품목 total 비어 있으면 국가 총계로 채움
            if m in items['months']:
                k = items['months'].index(m)
                if items['series']['total']['exp'][k] is None:
                    items['series']['total']['exp'][k] = M(tot_e); items['series']['total']['imp'][k] = M(tot_i)
            ctry['meta']['last_month'] = m
            changed = True
    else:
        log('country: up to date', ctry['months'][-1])
    # total 이 비어 있는 달은 국가 총계로 채움
    for k, m in enumerate(items['months']):
        if items['series']['total']['exp'][k] is None:
            rows = fetch_country(m.replace('-', ''), m.replace('-', '')).get(m, {})
            if rows:
                items['series']['total']['exp'][k] = M(sum(v[0] for v in rows.values()))
                items['series']['total']['imp'][k] = M(sum(v[1] for v in rows.values()))
                changed = True

    # ── 3. 잠정치 (최근 3개월) ──
    cur = f'{now.year:04d}-{now.month:02d}'
    pfr = ym_add(cur, -2)
    prov = fetch_provisional(pfr.replace('-', ''), cur.replace('-', ''))
    prov.update(fetch_provisional(ym_add(pfr, -12).replace('-', ''), ym_add(cur, -12).replace('-', '')))   # 전년 동월 (YoY 계산용)
    if prov and prov != items.get('provisional'):
        items['provisional'] = prov
        changed = True
        log('provisional:', {k: list(v.keys()) for k, v in prov.items()})

    if not changed:
        log('no change'); return 0
    items['meta']['generated_at'] = datetime.now(timezone.utc).isoformat(timespec='seconds')
    ctry['meta']['generated_at'] = items['meta']['generated_at']
    for path, obj in ((ITEMS_PATH, items), (CTRY_PATH, ctry)):
        tmp = path + '.tmp'
        json.dump(obj, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
        os.replace(tmp, path)
        log('wrote', path, os.path.getsize(path) // 1024, 'KB')
    return 0

if __name__ == '__main__':
    sys.exit(main())
