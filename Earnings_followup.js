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
  manifest: { preview: [], review: [], 'in-depth': [] }
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
  for (const mode of ['preview', 'review', 'in-depth']) {
    for (const file of (manifest[mode] || [])) {
      const m = file.match(/^(\d{4}-Q\d)_/);
      if (m) set.add(m[1]);
    }
  }
  return Array.from(set);
}

function buildQuarterList() {
  const set = new Set(extractQuartersFromManifest(state.manifest));
  set.add(getCurrentQuarter());
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
    else if (currentTier && /^\s*-\s+/.test(line)) {
      const m = line.match(/-\s+\*?\*?([\u{AC00}-\u{D7AF}\w\s]+?)\*?\*?\s*\(([^)]+)\)/u);
      if (m) {
        const sector = m[1].trim();
        const stocks = m[2].split(',').map(s => s.trim()).filter(Boolean);
        const looksLikeStocks = stocks.every(s => s.length < 30 && !/[:%]/.test(s));
        if (looksLikeStocks) {
          result[currentTier].push({ sector, stocks: stocks.map(name => ({ name, ticker: '' })) });
        }
      }
    }
  }
  return result;
}

function parseCalendar(md) {
  const result = { calendar: {}, signals: {} };
  const lines = md.split('\n');
  let inSignalSection = false;
  let inEarningsSection = false;
  let inTable = false;
  const SIGNAL_HDR = '추적';  // 추적
  const EARN_HDR = '실적';    // 실적
  const ARCH_HDR = '아카이브'; // 아카이브
  const DATE_COL = '날짜';    // 날짜
  const TICKER_COL = '티커';  // 티커
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
        result.calendar[name] = { date, ticker, sector, note };
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

const SUFFIX = { preview: '프리뷰', review: '리뷰', 'in-depth': '인댄스' };

function getModeFile(stockName, mode) {
  const expected = state.currentQuarter + '_' + stockName + '_' + SUFFIX[mode] + '.html';
  const list = state.manifest[mode] || [];
  return list.includes(expected) ? expected : null;
}

function getProgressStage(stockName) {
  if (getModeFile(stockName, 'in-depth')) return 3;
  if (getModeFile(stockName, 'review')) return 2;
  if (getModeFile(stockName, 'preview')) return 1;
  return 0;
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
        if (getModeFile(stock.name, 'preview')) p++;
        if (getModeFile(stock.name, 'review')) r++;
      }
    }
  }
  $('statP').textContent = p + '/' + totalStocks;
  $('statR').textContent = r + '/' + totalStocks;
}

function renderProgressCircles(stage) {
  const container = el('span', { class: 'progress-circles' });
  for (let i = 1; i <= 3; i++) {
    container.appendChild(el('span', { class: i <= stage ? 'circle' : 'circle empty' }));
  }
  return container;
}

function renderStockRow(stock) {
  const cal = state.calendar[stock.name];
  const sig = state.signals[stock.name];
  const stage = getProgressStage(stock.name);
  const stockRow = el('div', { class: 'stock-row' });
  const ticker = (cal && cal.ticker) || (sig && sig.ticker) || '';
  const followup = sig ? sig.signal : '';
  const nameRow = el('div', { class: 'stock-name-row' }, [
    el('span', { class: 'stock-name' }, stock.name),
    ticker ? el('span', { class: 'ticker' }, '(' + ticker + ')') : null,
    followup ? el('span', { class: 'stock-followup' }, '— ' + followup) : null
  ]);
  stockRow.appendChild(nameRow);
  const middleCol = el('div', null, [
    cal && cal.date ? el('div', { class: 'dday-cell' }, cal.date) : el('div', { class: 'dday-cell' }, '발표일 미정'),
    renderProgressCircles(stage)
  ]);
  stockRow.appendChild(middleCol);
  const buttons = el('div', { class: 'mode-buttons' });
  let hasAny = false;
  for (const pair of [['preview', 'P'], ['review', 'R'], ['in-depth', 'I']]) {
    const mode = pair[0], label = pair[1];
    const file = getModeFile(stock.name, mode);
    if (file) {
      buttons.appendChild(el('a', { class: 'mode-btn', href: buildHtmlPath(mode, file), target: '_blank', title: label + ': ' + file }, label));
      hasAny = true;
    }
  }
  if (!hasAny) buttons.appendChild(el('span', { class: 'sector-meta', style: 'opacity:0.5;' }, '미작성'));
  stockRow.appendChild(buttons);
  return stockRow;
}

function renderSectorCard(sectorObj, tier) {
  const card = el('div', { class: 'sector-card ' + tier.toLowerCase() });
  card.appendChild(el('div', { class: 'sector-header' }, [
    el('div', { class: 'sector-name' }, sectorObj.sector),
    el('div', { class: 'sector-meta' }, '종목 ' + sectorObj.stocks.length + '개 · ' + tier)
  ]));
  let pCount = 0, rCount = 0;
  for (const stock of sectorObj.stocks) {
    if (getModeFile(stock.name, 'preview')) pCount++;
    if (getModeFile(stock.name, 'review')) rCount++;
  }
  card.appendChild(el('div', { class: 'sector-meta', style: 'margin-bottom: 0.4rem;' },
    '진행: P ' + pCount + '/' + sectorObj.stocks.length + ' · R ' + rCount + '/' + sectorObj.stocks.length));
  const stockList = el('div', { class: 'stock-list' });
  for (const stock of sectorObj.stocks) stockList.appendChild(renderStockRow(stock));
  card.appendChild(stockList);
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
