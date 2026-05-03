/* deploy:2026-05-02-22:20 force CDN invalidate v2 */
const DATA_PATHS = {
  watchlist: 'earnings/watchlist.md',
  calendar: 'earnings_calendar.md',
  manifest: 'earnings/manifest.json'
};

let state = {
  currentQuarter: '2026-Q1',
  watchlist: { T1: [], T2: [], T3: [] },
  calendar: {},
  signals: {},
  manifest: { preview: [], review: [], 'in-depth': [], followup: [] }
};

function $(id) { return document.getElementById(id); }
function el(tag, attrs, children) {
  const e = document.createElement(tag);
  if (attrs) for (const k in attrs) {
    if (k === 'class') e.className = attrs[k];
    else if (k === 'html') e.innerHTML = attrs[k];
    else if (k.startsWith('on')) e.addEventListener(k.slice(2), attrs[k]);
    else e.setAttribute(k, attrs[k]);
  }
  if (children) (Array.isArray(children) ? children : [children]).forEach(c => {
    if (typeof c === 'string') e.appendChild(document.createTextNode(c));
    else if (c) e.appendChild(c);
  });
  return e;
}

async function fetchText(path) {
  try { const r = await fetch(path); if (!r.ok) throw new Error(r.status); return await r.text(); }
  catch (e) { console.error('Fetch failed:', path, e); return null; }
}
async function fetchJson(path) {
  try { const r = await fetch(path); if (!r.ok) throw new Error(r.status); return await r.json(); }
  catch (e) { console.error('Fetch JSON failed:', path, e); return null; }
}

function displayQuarter(internal) {
  const m = internal.match(/^(\d{4})-Q(\d)$/);
  if (m) return m[2] + 'Q' + m[1].slice(2);
  return internal;
}

function getCurrentQuarter() {
  // 분기 발표 마감 + 5일 cutoff 기준 기본 분기 결정
  // 1Q 마감 5/15 → 5/20부터 2Q, 2Q 마감 8/15 → 8/20부터 3Q,
  // 3Q 마감 11/15 → 11/20부터 4Q, 4Q 마감 익년 2/15 → 익년 2/20부터 1Q
  const now = new Date();
  const y = now.getFullYear();
  const md = (now.getMonth() + 1) * 100 + now.getDate();  // MMDD
  if (md < 220) return (y - 1) + '-Q4';
  if (md < 520) return y + '-Q1';
  if (md < 820) return y + '-Q2';
  if (md < 1120) return y + '-Q3';
  return y + '-Q4';
}

function extractQuartersFromManifest(manifest) {
  const set = new Set();
  for (const mode of ['preview', 'review', 'in-depth', 'followup']) {
    for (const file of (manifest[mode] || [])) {
      const m = file.match(/^(\d{4}-Q\d)_/);
      if (m) set.add(m[1]);
    }
  }
  return Array.from(set);
}

function getNextQuarter(quarter) {
  const m = quarter.match(/^(\d{4})-Q(\d)$/);
  if (!m) return null;
  let y = parseInt(m[1]), q = parseInt(m[2]);
  q += 1;
  if (q > 4) { q = 1; y += 1; }
  return y + '-Q' + q;
}

function extractFollowupQuarters(manifest) {
  // review 또는 in-depth 산출물이 있는 분기의 다음 분기를 자동 생성
  // (리뷰/인뎁스 작성 시점부터 다음 분기 마일스톤이 시작되므로)
  const set = new Set();
  for (const mode of ['review', 'in-depth']) {
    for (const file of (manifest[mode] || [])) {
      const m = file.match(/^(\d{4}-Q\d)_/);
      if (m) {
        const next = getNextQuarter(m[1]);
        if (next) set.add(next);
      }
    }
  }
  return set;
}

function buildQuarterList() {
  const set = new Set(extractQuartersFromManifest(state.manifest));
  set.add(getCurrentQuarter());
  for (const q of extractFollowupQuarters(state.manifest)) set.add(q);
  return Array.from(set).sort().reverse();
}

function populateQuarterSelector() {
  const sel = $('quarterSelect');
  const quarters = buildQuarterList();
  sel.innerHTML = '';
  for (const q of quarters) {
    const opt = el('option', { value: q }, displayQuarter(q));
    if (q === state.currentQuarter) opt.selected = true;
    sel.appendChild(opt);
  }
  updateQuarterButtons();
}

function updateQuarterButtons() {
  const quarters = buildQuarterList();
  const idx = quarters.indexOf(state.currentQuarter);
  const next = $('nextQuarter');
  const prev = $('prevQuarter');
  next.disabled = (idx <= 0);
  prev.disabled = (idx >= quarters.length - 1);
  next.style.opacity = next.disabled ? '0.4' : '1';
  prev.style.opacity = prev.disabled ? '0.4' : '1';
  next.style.cursor = next.disabled ? 'not-allowed' : 'pointer';
  prev.style.cursor = prev.disabled ? 'not-allowed' : 'pointer';
}

function changeQuarter(newQ) {
  state.currentQuarter = newQ;
  $('quarterSelect').value = newQ;
  $('currentQuarterLabel').textContent = displayQuarter(newQ);
  updateQuarterButtons();
  renderProgress();
  renderSectors();
}

function parseWatchlist(md) {
  const result = { T1: [], T2: [], T3: [] };
  let currentTier = null;
  const lines = md.split('\n');
  const T1 = '섹터';  // 섹터
  for (const line of lines) {
    if (line.match(new RegExp('^##\\s+' + T1 + '\\s*T1'))) currentTier = 'T1';
    else if (line.match(new RegExp('^##\\s+' + T1 + '\\s*T2'))) currentTier = 'T2';
    else if (line.match(new RegExp('^##\\s+' + T1 + '\\s*T3'))) currentTier = 'T3';
    else if (/^##\s/.test(line)) currentTier = null;
    else if (currentTier && /^\s*-\s+\*\*/.test(line)) {
      // 섹터명: **섹터** 다음 (...) 안의 종목 리스트 추출
      const m = line.match(/^\s*-\s+\*\*([^*]+)\*\*\s*\((.+)\)\s*$/);
      if (m) {
        const sector = m[1].trim();
        // 종목 분리: 콤마로 자르되 종목 안의 ticker 괄호와 충돌 방지
        // "삼성전자, SK하이닉스, Micron(MU)" → ['삼성전자','SK하이닉스','Micron(MU)']
        const stocks = m[2].split(',').map(s => s.trim()).filter(Boolean);
        const stockObjs = stocks.map(s => {
          // 종목명(ticker) 형식이면 분리
          const tm = s.match(/^(.+?)\s*\(([^)]+)\)\s*$/);
          if (tm) return { name: tm[1].trim(), ticker: tm[2].trim() };
          return { name: s, ticker: '' };
        });
        result[currentTier].push({ sector, stocks: stockObjs });
      }
    }
  }
  return result;
}

// 발표일 → 캘린더 분기 매핑
// default: 4~6월 발표 → 1Q (직전 회계 분기 결과), 7~9월 → 2Q, 10~12월 → 3Q, 익년 1~3월 → 4Q
// override: 캘린더 entry 비고에 [YYYY-Qn] 패턴 명시 시 그 분기로 매핑 (마이크론 등 회계 어긋난 종목)
function mapDateToQuarter(dateStr, currentYear, note) {
  // 비고 override 우선 — 마이크론 3/18 → [2026-Q1] 같은 케이스
  if (note) {
    const override = note.match(/\[(\d{4}-Q\d)\]/);
    if (override) return override[1];
  }
  const m = dateStr.match(/(\d{1,2})\//);
  let month;
  if (m) {
    month = parseInt(m[1]);
  } else {
    const m2 = dateStr.match(/(\d{1,2})월/);
    if (!m2) return null;
    month = parseInt(m2[1]);
  }
  if (month >= 1 && month <= 3) return (currentYear - 1) + '-Q4';
  if (month >= 4 && month <= 6) return currentYear + '-Q1';
  if (month >= 7 && month <= 9) return currentYear + '-Q2';
  if (month >= 10 && month <= 12) return currentYear + '-Q3';
  return null;
}

// 발표일 표시 양식: "M/D" → "YY/MM/DD" (currentQuarter year 기준)
function formatDate(rawDate, currentQuarter) {
  if (!rawDate) return '';
  const yearMatch = currentQuarter && currentQuarter.match(/^(\d{4})/);
  const year = yearMatch ? yearMatch[1] : '26';
  const yy = year.slice(2);
  const m = rawDate.match(/^(\d{1,2})\/(\d{1,2})/);
  if (!m) return rawDate;  // "(5월중)" 같은 경우 원본
  return yy + '/' + String(m[1]).padStart(2, '0') + '/' + String(m[2]).padStart(2, '0');
}

function parseCalendar(md) {
  const result = { calendar: {}, signals: {} };
  const lines = md.split('\n');
  let inSignalSection = false;
  let inEarningsSection = false;
  let inTable = false;
  const SIGNAL_HDR = '추적';
  const EARN_HDR = '실적';
  const ARCH_HDR = '아카이브';
  const DATE_COL = '날짜';
  const TICKER_COL = '티커';
  // currentYear 추정 — manifest 또는 default 2026
  const currentYear = 2026;
  for (const line of lines) {
    if (/^##\s/.test(line)) {
      inSignalSection = line.indexOf(SIGNAL_HDR) >= 0;
      inEarningsSection = (line.indexOf(EARN_HDR) >= 0) || (line.indexOf(ARCH_HDR) >= 0);
      inTable = false;
    }
    if (inEarningsSection && line.match(new RegExp('^\\|\\s*' + DATE_COL + '\\s*\\|'))) inTable = 'earnings';
    else if (inSignalSection && line.match(new RegExp('^\\|\\s*' + TICKER_COL + '\\s*\\|'))) inTable = 'signal';
    else if (inTable && /^\|/.test(line) && !/^\|\s*-+/.test(line)) {
      const cells = line.split('|').map(c => c.trim()).filter(c => c !== '');
      if (cells.length < 3) continue;
      if (inTable === 'earnings') {
        const date = cells[0];
        const nameTickerRaw = cells[1];
        const sector = cells[2];
        const note = cells[3] || '';
        const tickerMatch = nameTickerRaw.match(/^(.+?)\s*\(([^)]+)\)\s*$/);
        const name = tickerMatch ? tickerMatch[1].trim() : nameTickerRaw.trim();
        const ticker = tickerMatch ? tickerMatch[2].trim() : '';
        // 분기 추정 후 종목별 분기-entry 저장
        const quarter = mapDateToQuarter(date, currentYear, note);
        if (!quarter) continue;
        if (!result.calendar[name]) result.calendar[name] = {};
        result.calendar[name][quarter] = { date, ticker, sector, note };
      } else if (inTable === 'signal') {
        const ticker = cells[0] === '—' ? '' : cells[0];
        const name = cells[1];
        const signal = cells[2];
        if (name && signal) result.signals[name] = { ticker, signal };
      }
    }
    if (/^\s*$/.test(line) || /^##/.test(line)) inTable = false;
  }
  return result;
}

const SUFFIX = { preview: '프리뷰', review: '리뷰', 'in-depth': '인뎁스', followup: '팔로업' };
const MODE_LABELS = { preview: '프리뷰', review: '리뷰', 'in-depth': '인뎁스', followup: '요약' };

function getModeFile(stock, mode) {
  // stock: {name, ticker}. ticker 있으면 ticker 사용 (미국 기업 산출물 명명 규칙).
  // followup은 다음 분기 파일을 이번 분기 페이지에서 찾음 (BT가 이번 분기 페이지에서 보길 원함)
  const key = stock.ticker || stock.name;
  let quarter = state.currentQuarter;
  if (mode === 'followup') {
    quarter = getNextQuarter(state.currentQuarter);
    if (!quarter) return null;
  }
  const expected = quarter + '_' + key + '_' + SUFFIX[mode] + '.html';
  const list = state.manifest[mode] || [];
  return list.includes(expected) ? expected : null;
}

function getProgressStage(stock) {
  if (getModeFile(stock, 'in-depth')) return 3;
  if (getModeFile(stock, 'review')) return 2;
  if (getModeFile(stock, 'preview')) return 1;
  return 0;
}

function getPreviousQuarter(quarter) {
  const m = quarter.match(/^(\d{4})-Q(\d)$/);
  if (!m) return null;
  let y = parseInt(m[1]), q = parseInt(m[2]);
  q -= 1;
  if (q < 1) { q = 4; y -= 1; }
  return y + '-Q' + q;
}

function hasPriorReview(stock, currentQuarter) {
  // 시그널 키워드는 다음 분기 페이지에서 표시:
  // 직전 분기에 review 또는 in-depth 산출물 있으면 시그널 표시
  // (예: 1Q26 review 작성 → 2Q26 페이지에서 SK하이닉스 시그널 표시)
  const prev = getPreviousQuarter(currentQuarter);
  if (!prev) return false;
  const key = stock.ticker || stock.name;
  const reviewFile = prev + '_' + key + '_' + SUFFIX.review + '.html';
  const indepthFile = prev + '_' + key + '_' + SUFFIX['in-depth'] + '.html';
  return (state.manifest.review || []).includes(reviewFile) ||
         (state.manifest['in-depth'] || []).includes(indepthFile);
}

function buildHtmlPath(mode, file) { return 'earnings/earnings-' + mode + '/' + file; }

function renderWatchlistSummary() {
  const wl = state.watchlist;
  const lines = [];
  for (const tier of ['T1', 'T2', 'T3']) {
    const sectors = wl[tier];
    if (sectors.length === 0) continue;
    const sectorNames = sectors.map(s => s.sector).join(' · ');
    const stockCount = sectors.reduce((sum, s) => sum + s.stocks.length, 0);
    lines.push('<div class="tier-line"><span class="tier-badge tier-' + tier + '">' + tier + '</span>' + sectorNames + ' <span style="color:var(--text-dim);">(' + sectors.length + '개 섹터, ' + stockCount + '개 종목)</span></div>');
  }
  $('watchlistSummary').innerHTML = lines.join('') || '<div class="loading">no data</div>';
}

function renderProgress() {
  let totalStocks = 0, p = 0, r = 0;
  for (const tier of ['T1', 'T2', 'T3']) {
    for (const sec of state.watchlist[tier]) {
      for (const stock of sec.stocks) {
        totalStocks++;
        if (getModeFile(stock, 'preview')) p++;
        if (getModeFile(stock, 'review')) r++;
      }
    }
  }
  const pct = totalStocks > 0 ? Math.round((r / totalStocks) * 100) : 0;
  $('statR').textContent = r + '/' + totalStocks + ' (' + pct + '%)';
}

function renderProgressCircles(stage) {
  const container = el('span', { class: 'progress-circles' });
  for (let i = 1; i <= 3; i++) {
    container.appendChild(el('span', { class: i <= stage ? 'circle' : 'circle empty' }));
  }
  return container;
}

function renderStockRow(stock) {
  const calByQuarter = state.calendar[stock.name];
  const cal = calByQuarter ? calByQuarter[state.currentQuarter] : null;
  const sig = state.signals[stock.name];
  const tr = el('tr', { class: 'stock-row' });
  const ticker = stock.ticker || (cal && cal.ticker) || (sig && sig.ticker) || '';
  const followup = (sig && hasPriorReview(stock, state.currentQuarter)) ? sig.signal : '';
  // td 1: 종목명(티커)
  const nameTd = el('td', { class: 'col-name' }, [
    el('span', { class: 'stock-name' }, stock.name),
    ticker ? el('span', { class: 'ticker' }, ' (' + ticker + ')') : null
  ]);
  tr.appendChild(nameTd);
  // td 2: 팔로업 키워드
  tr.appendChild(el('td', { class: 'col-followup' }, followup));
  // td 3: 발표일 (YY/MM/DD)
  tr.appendChild(el('td', { class: 'col-date' }, (cal && cal.date) ? formatDate(cal.date, state.currentQuarter) : '발표일 미정'));
  // td 4: 리포트 4개 버튼
  const buttons = el('div', { class: 'mode-buttons' });
  for (const pair of [['preview', '프리뷰'], ['review', '리뷰'], ['in-depth', '인뎁스'], ['followup', '요약']]) {
    const mode = pair[0], label = pair[1];
    const file = getModeFile(stock, mode);
    if (file) {
      buttons.appendChild(el('a', { class: 'mode-btn', href: buildHtmlPath(mode, file), target: '_blank', title: label + ': ' + file }, label));
    } else {
      buttons.appendChild(el('span', { class: 'mode-btn disabled', title: label + ': 미작성' }, label));
    }
  }
  tr.appendChild(el('td', { class: 'col-report' }, [buttons]));
  return tr;
}

function renderSectorCard(sectorObj, tier) {
  const card = el('div', { class: 'sector-card ' + tier.toLowerCase() });
  card.appendChild(el('div', { class: 'sector-header' }, [
    el('div', { class: 'sector-name' }, sectorObj.sector),
    el('div', { class: 'sector-meta' }, '종목 ' + sectorObj.stocks.length + '개 · ' + tier)
  ]));
  let pCount = 0, rCount = 0;
  for (const stock of sectorObj.stocks) {
    if (getModeFile(stock, 'preview')) pCount++;
    if (getModeFile(stock, 'review')) rCount++;
  }
  card.appendChild(el('div', { class: 'sector-meta', style: 'margin-bottom: 0.4rem;' },
    '진행: P ' + pCount + '/' + sectorObj.stocks.length + ' · R ' + rCount + '/' + sectorObj.stocks.length));
  // 종목 테이블 (table 사용 — 컬럼 vertical line 카드 전체에 이어짐)
  const table = el('table', { class: 'stock-table' });
  const thead = el('thead');
  thead.appendChild(el('tr', null, [
    el('th', { class: 'col-name' }, '종목명'),
    el('th', { class: 'col-followup' }, '팔로업 키워드'),
    el('th', { class: 'col-date' }, '발표일'),
    el('th', { class: 'col-report' }, '리포트')
  ]));
  table.appendChild(thead);
  // 발표일 오름차순 정렬 (currentQuarter 기준), 발표일 없는 종목은 마지막
  const sortedStocks = sectorObj.stocks.slice().sort((a, b) => {
    const calA = state.calendar[a.name] && state.calendar[a.name][state.currentQuarter];
    const calB = state.calendar[b.name] && state.calendar[b.name][state.currentQuarter];
    const dateA = calA && calA.date ? calA.date : 'zz';  // 'zz' → 마지막 정렬
    const dateB = calB && calB.date ? calB.date : 'zz';
    // M/D 형식이라 단순 lexical sort 안 됨 — 월·일 분리 비교
    const parseDate = (d) => {
      const m = d.match(/^(\d{1,2})\/(\d{1,2})/);
      if (!m) return [99, 99];
      return [parseInt(m[1]), parseInt(m[2])];
    };
    const [mA, dA] = parseDate(dateA);
    const [mB, dB] = parseDate(dateB);
    if (mA !== mB) return mA - mB;
    return dA - dB;
  });
  const tbody = el('tbody');
  for (const stock of sortedStocks) tbody.appendChild(renderStockRow(stock));
  table.appendChild(tbody);
  card.appendChild(table);
  return card;
}

function renderSectors() {
  const t1 = $('t1Sectors'), t2 = $('t2Sectors'), t3 = $('t3Sectors');
  t1.innerHTML = ''; t2.innerHTML = ''; t3.innerHTML = '';
  for (const sec of state.watchlist.T1) t1.appendChild(renderSectorCard(sec, 'T1'));
  for (const sec of state.watchlist.T2) t2.appendChild(renderSectorCard(sec, 'T2'));
  for (const sec of state.watchlist.T3) t3.appendChild(renderSectorCard(sec, 'T3'));
  if (state.watchlist.T1.length === 0) t1.innerHTML = '<div class="loading">no data</div>';
  if (state.watchlist.T2.length === 0) t2.innerHTML = '<div class="loading">no data</div>';
  if (state.watchlist.T3.length === 0) t3.innerHTML = '<div class="loading">no data</div>';
}

function setupSearch() {
  $('searchInput').addEventListener('input', function(e) {
    const q = e.target.value.toLowerCase().trim();
    document.querySelectorAll('.sector-card').forEach(function(card) {
      const text = card.textContent.toLowerCase();
      card.style.display = (q === '' || text.includes(q)) ? '' : 'none';
    });
  });
}

function setupQuarterSelector() {
  $('quarterSelect').addEventListener('change', function(e) { changeQuarter(e.target.value); });
  $('prevQuarter').addEventListener('click', function() {
    const quarters = buildQuarterList();
    const idx = quarters.indexOf(state.currentQuarter);
    if (idx >= 0 && idx < quarters.length - 1) changeQuarter(quarters[idx + 1]);
  });
  $('nextQuarter').addEventListener('click', function() {
    const quarters = buildQuarterList();
    const idx = quarters.indexOf(state.currentQuarter);
    if (idx > 0) changeQuarter(quarters[idx - 1]);
  });
}

async function init() {
  const wlText = await fetchText(DATA_PATHS.watchlist);
  if (wlText) state.watchlist = parseWatchlist(wlText);
  else $('watchlistSummary').innerHTML = '<div class="error-box">watchlist.md load failed.</div>';
  const calText = await fetchText(DATA_PATHS.calendar);
  if (calText) {
    const parsed = parseCalendar(calText);
    state.calendar = parsed.calendar;
    state.signals = parsed.signals;
  }
  const manifest = await fetchJson(DATA_PATHS.manifest);
  if (manifest) state.manifest = manifest;
  state.currentQuarter = getCurrentQuarter();
  $('currentQuarterLabel').textContent = displayQuarter(state.currentQuarter);
  populateQuarterSelector();
  renderWatchlistSummary();
  renderProgress();
  renderSectors();
  setupSearch();
  setupQuarterSelector();
  $('lastUpdate').textContent = new Date().toLocaleString('ko-KR');
}

document.addEventListener('DOMContentLoaded', init);
