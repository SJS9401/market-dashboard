#!/usr/bin/env python3
"""
수출 탭 — 과거 구간(K-stat 2000-01 ~ kstat_last) 수출 중량·단가 백필 (2026-11-01 BT: "판가 데이터가 9월치만 있다")
  * K-stat 중량 수집은 IP 차단(2026-10-15)으로 중단 → 관세청 tradedata.go.kr HS10 합산으로 대체.
  * 같은 HS10 묶음(2026 연계표)의 금액(wexp)과 중량(wgt)을 함께 저장 → 단가 = wexp / wgt (분자·분모 동일 코드 집합).
    HS 코드 개정으로 과거 연도에 코드가 일부 빠져도 단가는 왜곡되지 않는다.
  * 포괄률 = wexp / K-stat 금액. 0.6 미만·1.4 초과인 달은 대표성 부족으로 비움(None).
  * 이미 채워진 달은 건너뜀 → 중간 실패 시 재실행하면 이어서 채움. 순수 stdlib.
"""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kr_export_items_update as U

COV_LO, COV_HI = 0.6, 1.4
START_YEAR = int(os.environ.get('START_YEAR', '2000'))
SPAN = 2   # 한 요청 기간(년) — 250코드 × 24개월 = 6000행 < showPagingLine 20000

def main():
    items = json.load(open(U.ITEMS_PATH, encoding='utf-8'))
    hsmap = json.load(open(U.MAP_PATH, encoding='utf-8'))
    klast = items['meta'].get('kstat_last') or '2026-08'
    months, sub_months = items['months'], items['sub_months']
    midx = {m: i for i, m in enumerate(months)}; sidx = {m: i for i, m in enumerate(sub_months)}
    for ser in items['series'].values():
        for k in ('wgt', 'wexp'): ser[k] = (ser.get(k, []) + [None] * len(months))[:len(months)]
    for lst in items['subs'].values():
        for sb in lst:
            for k in ('wgt', 'wexp'): sb[k] = (sb.get(k, []) + [None] * len(sub_months))[:len(sub_months)]
    end_y = int(klast[:4])
    periods = []
    for y in range(START_YEAR, end_y + 1, SPAN):
        fr = f'{y}01'; to_y = min(y + SPAN - 1, end_y); to = f'{to_y}12' if to_y < end_y else klast.replace('-', '')
        periods.append((fr, to))
    stats = {'filled': 0, 'lowcov': 0, 'fail': 0}
    targets = [('item', iid, spec['hs10']) for iid, spec in hsmap['items'].items() if iid in items['series']]
    subs_by_id = {sb['id']: sb for lst in items['subs'].values() for sb in lst}
    targets += [('sub', sid, spec['hs10']) for sid, spec in hsmap['subs'].items() if spec['hs10'] and sid in subs_by_id]
    for kind, tid, codes in targets:
        obj = items['series'][tid] if kind == 'item' else subs_by_id[tid]
        idx = midx if kind == 'item' else sidx
        for fr, to in periods:
            need = [m for m in idx if fr[:4] <= m[:4] <= to[:4] and m <= klast and obj['wgt'][idx[m]] is None]
            if not need: continue
            try:
                acc = U.fetch_hs10(codes, fr, to)
            except Exception as e:
                U.log(f'  FAIL {tid} {fr}-{to}: {e}'); stats['fail'] += 1; continue
            for m in need:
                e, im, w = acc.get(m, (0.0, 0.0, 0.0))
                i = idx[m]; ref = obj['exp'][i]
                if w <= 0 or e <= 0: continue
                cov = U.M(e) / ref if ref else None
                if cov is None or not (COV_LO <= cov <= COV_HI):
                    stats['lowcov'] += 1; continue
                obj['wgt'][i] = U.T(w); obj['wexp'][i] = U.M(e); stats['filled'] += 1
            U.log(f'  {kind} {tid:12s} {fr}-{to} ok ({len(need)} months)')
        # 중간 저장 (긴 작업 중단 대비)
        json.dump(items, open(U.ITEMS_PATH, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    items['meta']['wgt_note'] = '중량: K-stat 구간은 관세청 HS10(2026 연계표) 합산 백필, 단가 = 같은 코드 금액(wexp)/중량. 포괄률 60~140% 밖인 달은 비움'
    json.dump(items, open(U.ITEMS_PATH, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    U.log('DONE', stats)

if __name__ == '__main__':
    main()
