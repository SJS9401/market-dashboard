/* deploy:2026-05-02-22:20 force CDN invalidate v2 */
const DATA_PATHS = {
  watchlist: 'earnings/watchlist.md',
  calendar: 'earnings/earnings_calendar.md',  // 2026-10-08: 원본 = Documents\Claude\earnings\earnings_calendar.md (배포 미러)
  manifest: 'earnings/manifest.json'
};

let state = {
  currentQuarter: '2026-Q1',
  watchlist: { T1: [], groups: [] },
  calendar: {},
  signals: {},
  manifest: { preview: [], review: [], 'in-depth': [], followup: [], company: [], analysis: [], theme: [], 'theme-review': [] }
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
  renderThemeReviews();
  renderSectors();
}

function parseWatchlist(md) {
  // 2026-11-14: 우선순위(T1/T2/T3) → "섹터 T1(집중)" + 산업 대분류 그룹 ("## 대분류: 테크" 등)
  //   T1 줄은 "- **섹터** [대분류] (종목…)" 형식으로 원래 대분류를 남긴다
  const result = { T1: [], groups: [] };
  // 2026-11-14: 반기 공시 종목 목록 (헤더 노트 "> **반기 공시 종목** (...): A, B")
  const hm = md.match(/^>[ \t]*\*\*반기 공시 종목\*\*[^\n]*:[ \t]*([^\n]*)$/m);
  result.halfYear = hm ? hm[1].split(',').map(x => x.trim()).filter(Boolean) : [];
  const am = md.match(/^>[ \t]*\*\*연간 공시 종목\*\*[^\n]*:[ \t]*([^\n]*)$/m);
  result.annual = am ? am[1].split(',').map(x => x.trim()).filter(Boolean) : [];
  let current = null;  // 'T1' | group 객체
  const lines = md.split('\n');
  for (const line of lines) {
    let gm;
    if (/^##\s+섹터\s*T1/.test(line)) current = 'T1';
    else if ((gm = line.match(/^##\s+대분류\s*[:：]\s*(.+?)\s*$/))) {
      current = { name: gm[1], sectors: [] };
      result.groups.push(current);
    }
    else if (/^##\s/.test(line)) current = null;
    else if (current && /^\s*-\s+\*\*/.test(line)) {
      // 섹터명: **섹터** [대분류]? 다음 (...) 안의 종목 리스트 추출
      const m = line.match(/^\s*-\s+\*\*([^*]+)\*\*\s*(?:\[([^\]]+)\]\s*)?\((.+)\)\s*$/);
      if (m) {
        const sector = m[1].trim();
        const category = current === 'T1' ? (m[2] ? m[2].trim() : '') : current.name;
        m[2] = m[3];  // 아래 종목 파싱은 m[2] = 종목 리스트 기준
        // 5/18 변경: 종목 안의 괄호에 ticker + industry 들어갈 수 있음 (예: "Tesla(TSLA, industry=자동차)")
        // 괄호 안 콤마는 분리 안 하도록 negative lookahead split 사용
        const stocks = m[2].split(/,(?![^()]*\))/).map(s => s.trim()).filter(Boolean);
        const stockObjs = stocks.map(s => {
          // 종목명(inner) 형식이면 분리. inner는 콤마로 split → [ticker, industry=primary|secondary, ...]
          // 5/18 변경: industry는 파이프(|)로 multi 표현 — 첫째 primary, 나머지 secondary
          //   예: industry=광고|클라우드 → primary 광고, secondary 클라우드
          const tm = s.match(/^(.+?)\s*\(([^)]+)\)\s*$/);
          if (tm) {
            const name = tm[1].trim();
            const innerParts = tm[2].split(',').map(x => x.trim()).filter(Boolean);
            const ticker = innerParts[0] || '';
            let industriesRaw = null;
            for (const part of innerParts.slice(1)) {
              const im = part.match(/^industry\s*=\s*(.+)$/i);
              if (im) industriesRaw = im[1].trim();
              else if (!industriesRaw) industriesRaw = part;
            }
            const industries = industriesRaw
              ? industriesRaw.split('|').map(x => x.trim()).filter(Boolean)
              : null;
            return {
              name, ticker,
              industry: industries ? industries[0] : null,  // primary (backward compat)
              industries  // array, multi 케이스용
            };
          }
          return { name: s, ticker: '', industry: null, industries: null };
        });
        const secObj = { sector, category, stocks: stockObjs };
        if (current === 'T1') result.T1.push(secObj); else current.sectors.push(secObj);
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
  const iso = dateStr.match(/(\d{4})-(\d{2})-\d{2}/);  // 노션 동기화 행은 보통 [YYYY-Qn] override가 있어 여기 안 옴
  if (iso) {
    const y = parseInt(iso[1]), mo = parseInt(iso[2]);
    if (mo <= 3) return (y - 1) + '-Q4';
    return y + '-Q' + (Math.floor((mo - 1) / 3));
  }
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
  // 2026-11-03: 노션 동기화 형식 "YYYY-MM-DD" / "~YYYY-MM-DD"(추정) → "YY/MM/DD" / "~YY/MM/DD"
  const iso = rawDate.match(/^(~)?(\d{4})-(\d{2})-(\d{2})/);
  if (iso) return (iso[1] || '') + iso[2].slice(2) + '/' + iso[3] + '/' + iso[4];
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

const SUFFIX = { preview: '프리뷰', review: '리뷰', 'in-depth': '인뎁스', followup: '팔로업', company: '기업분석', theme: '테마분석' };
const MODE_LABELS = { preview: '프리뷰', review: '리뷰', 'in-depth': '인뎁스', followup: '요약' };

function getModeFile(stock, mode) {
  // stock: {name, ticker, sector}. ticker 있으면 ticker 사용 (미국 기업 산출물 명명 규칙).
  // sector는 renderSectorCard에서 inject (산업기초 매칭용).
  const key = stock.ticker || stock.name;
  // industry-basic: 산업 단위 산출물 ({industry}_산업기초.html) — 산업/기업 분석 세션의 industry-basic 스킬
  // 폴더는 earnings/earnings-theme/ (산업/기업 세션이 테마와 같은 폴더에 둠)
  // 5/18 변경: stock.industry 우선 (mixed 그룹 = 미국 빅테크 7종목이 다른 산업기초 가리킴)
  //   - Nvidia (industry=반도체) → 반도체_산업기초.html
  //   - Apple (industry=소비재) → 소비재_산업기초.html
  //   - 다른 섹터는 그루핑 = 산업이라 sector fallback
  if (mode === 'industry-basic') {
    const industryName = stock.industry || stock.sector;
    if (!industryName) return null;
    const expected = industryName + '_산업기초.html';
    return (state.manifest.theme || []).includes(expected) ? expected : null;
  }
  // company: 분기 무관 단일 파일 ({종목}_기업개요.html) — company-overview 스킬 v4.8 산출물
  // 폴더는 earnings/company-overview/, 파일은 _기업개요 suffix
  if (mode === 'company') {
    const expected = key + '_기업개요.html';
    return (state.manifest.company || []).includes(expected) ? expected : null;
  }
  // analysis: 분기 무관, 테마별 파일 ({종목}_{테마}_기업분석.html) — company-analysis 스킬 산출물
  // 폴더는 earnings/company-analysis/. 한 종목이 multi-theme 보유 가능
  // 현재: prefix 매칭으로 첫 파일 반환 (1개면 직접, multi면 첫 번째). 향후 dropdown UX 추가
  if (mode === 'analysis') {
    const list = state.manifest.analysis || [];
    const prefix = key + '_';
    const matched = list.filter(f => f.startsWith(prefix) && f.endsWith('_기업분석.html'));
    return matched.length > 0 ? matched[0] : null;
  }
  // theme: Phase 2에서 multi-theme dropdown 구현 예정. 지금은 산출물 없으면 dim
  if (mode === 'theme') {
    // Phase 2: 테마 산출물 본문 fetch 후 관련 종목 list parse → 매칭
    return null;  // Phase 1 — disabled
  }
  // 분기 mode (preview/review/in-depth/followup)
  // followup은 다음 분기 파일을 이번 분기 페이지에서 찾음
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

function buildHtmlPath(mode, file) {
  // company-overview 스킬 산출물은 별도 폴더 (earnings/company-overview/)
  if (mode === 'company') return 'earnings/company-overview/' + file;
  // company-analysis 스킬 산출물도 별도 폴더 (earnings/company-analysis/)
  if (mode === 'analysis') return 'earnings/company-analysis/' + file;
  // industry-basic은 산업/기업 세션이 earnings-theme 폴더에 둠
  if (mode === 'industry-basic') return 'earnings/earnings-theme/' + file;
  // theme-review는 별도 폴더 (earnings/theme-review/)
  if (mode === 'theme-review') return 'earnings/theme-review/' + file;
  return 'earnings/earnings-' + mode + '/' + file;
}

// 2026-11-14: T1 + 대분류 그룹의 모든 섹터
function allSectors() {
  const wl = state.watchlist;
  return (wl.T1 || []).concat(...(wl.groups || []).map(g => g.sectors));
}

function renderWatchlistSummary() {
  const wl = state.watchlist;
  const lines = [];
  const line = (badgeCls, label, sectors) => {
    const sectorNames = sectors.map(s => s.sector).join(' · ');
    const stockCount = sectors.reduce((sum, s) => sum + s.stocks.length, 0);
    lines.push('<div class="tier-line"><span class="tier-badge ' + badgeCls + '">' + label + '</span>' + sectorNames + ' <span style="color:var(--text-dim);">(' + sectors.length + '개 섹터, ' + stockCount + '개 종목)</span></div>');
  };
  if ((wl.T1 || []).length) line('tier-T1', 'T1', wl.T1);
  for (const g of (wl.groups || [])) if (g.sectors.length) line('tier-grp', g.name, g.sectors);
  $('watchlistSummary').innerHTML = lines.join('') || '<div class="loading">no data</div>';
}

function renderProgress() {
  let totalStocks = 0, r = 0;
  for (const sec of allSectors()) {
    for (const stock of sec.stocks) {
      totalStocks++;
      if (getModeFile(stock, 'review')) r++;
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

// 5/18 신규 — multi-industry 종목 (예: Alphabet=광고|클라우드)의 [산업기초] 버튼
// click = primary 산업기초 직접 열림. hover = dropdown으로 secondary 산업기초 접근.
function renderIndustryBasicDropdown(stock, label) {
  const themeList = state.manifest.theme || [];
  const inds = stock.industries;
  const primaryFile = inds[0] + '_산업기초.html';
  const primaryActive = themeList.includes(primaryFile);

  const wrapper = el('div', { class: 'mode-btn-wrapper' });
  // 메인 버튼 (primary 직접 link)
  if (primaryActive) {
    wrapper.appendChild(el('a', {
      class: 'mode-btn mode-btn-multi',
      href: buildHtmlPath('industry-basic', primaryFile),
      target: '_blank',
      title: label + ' (' + inds.length + '): ' + inds.join(', ')
    }, label + ' ▾'));
  } else {
    wrapper.appendChild(el('span', {
      class: 'mode-btn mode-btn-multi disabled',
      title: label + ' (' + inds.length + '): ' + inds.join(', ') + ' — primary 미작성'
    }, label + ' ▾'));
  }
  // dropdown — 모든 industry option 표시 (primary 포함)
  const dropdown = el('div', { class: 'mode-btn-dropdown' });
  for (const ind of inds) {
    const file = ind + '_산업기초.html';
    if (themeList.includes(file)) {
      dropdown.appendChild(el('a', {
        class: 'dropdown-item',
        href: buildHtmlPath('industry-basic', file),
        target: '_blank'
      }, ind));
    } else {
      dropdown.appendChild(el('span', {
        class: 'dropdown-item disabled',
        title: ind + ' — 미작성'
      }, ind + ' (미작성)'));
    }
  }
  wrapper.appendChild(dropdown);
  return wrapper;
}

// 2026-11-14: 실적 리뷰 파일 결정 — 반기·연간 공시 종목의 업데이트 분기는 직전 손익 리뷰에 덧붙인 경우만 연결
//   updateQuarter = 그 분기에 손익이 없는 분기 (반기: Q1·Q3, 연간: Q1~Q3)
function resolveReview(stock, cycle) {
  const qn = parseInt(state.currentQuarter.slice(-1));
  const updateQuarter = (cycle === '반기' && qn % 2 === 1) || (cycle === '연간' && qn !== 4);
  const own = getModeFile(stock, 'review');
  if (own || !updateQuarter) return { file: own, suffix: '', updateQuarter };
  // 직전 손익 리뷰 (반기: 직전 분기, 연간: 직전 Q4) md의 "> 분기 업데이트: 3Q26 ..." 줄에 현재 분기가 있어야 켠다
  let baseQ = getPreviousQuarter(state.currentQuarter);
  if (cycle === '연간') baseQ = (parseInt(state.currentQuarter.slice(0, 4)) - 1) + '-Q4';
  const baseFile = baseQ + '_' + (stock.ticker || stock.name) + '_' + SUFFIX.review + '.html';
  const upd = (state.halfUpdates || {})[baseFile] || '';
  if ((state.manifest.review || []).includes(baseFile) && upd.includes(displayQuarter(state.currentQuarter))) {
    return { file: baseFile, suffix: '(' + displayQuarter(baseQ).slice(0, 2) + ')', updateQuarter };
  }
  return { file: null, suffix: '', updateQuarter };
}

// 캘린더 날짜 → Date. ISO("~2026-11-19") 우선, 구 형식 "M/D"는 분기 연도 기준 (Q4 화면의 1~3월은 익년)
function parseCalDate(raw) {
  if (!raw) return null;
  const iso = raw.match(/(\d{4})-(\d{2})-(\d{2})/);
  if (iso) return new Date(+iso[1], +iso[2] - 1, +iso[3]);
  const m = raw.match(/^~?(\d{1,2})\/(\d{1,2})/);
  if (!m) return null;
  let y = parseInt(state.currentQuarter.slice(0, 4));
  if (state.currentQuarter.endsWith('Q4') && +m[1] <= 3) y += 1;
  return new Date(y, +m[1] - 1, +m[2]);
}

function renderReleaseStatus(cal, rv) {
  const noun = rv.updateQuarter ? '덧붙임' : '리뷰';
  const d = parseCalDate(cal && cal.date);
  if (!d) return el('span', { class: 'st-badge st-none', title: '캘린더에 이번 분기 발표일 없음 — 노션 확인' }, '미정');
  const estimated = /^~/.test(cal.date);
  const today = new Date(); today.setHours(0, 0, 0, 0);
  const days = Math.round((d - today) / 86400000);
  if (days > 0) return el('span', { class: 'st-badge st-upcoming', title: estimated ? '추정 발표일' : '확정 발표일' }, 'D-' + days + (estimated ? '?' : ''));
  if (rv.file) return el('span', { class: 'st-badge st-done', title: '발표 후 ' + noun + ' 반영됨' }, noun + ' 완료');
  if (days === 0) return el('span', { class: 'st-badge st-today', title: '오늘 발표' }, '오늘 발표');
  return el('span', { class: 'st-badge st-missing', title: '발표 ' + (-days) + '일 경과' + (estimated ? ' (추정일 — 실제 발표 여부 확인)' : '') + ', ' + noun + ' 없음' }, noun + ' 대기');
}

function renderStockRow(stock) {
  const calByQuarter = state.calendar[stock.name];
  const cal = calByQuarter ? calByQuarter[state.currentQuarter] : null;
  const sig = state.signals[stock.name];
  const tr = el('tr', { class: 'stock-row' });
  const ticker = stock.ticker || (cal && cal.ticker) || (sig && sig.ticker) || '';
  // 5/18 변경: 팔로업 컬럼 제거 (3 컬럼 = 종목명·발표일·리포트)
  // td 1: 종목명(티커)
  const nameTd = el('td', { class: 'col-name' }, [
    el('span', { class: 'stock-name' }, stock.name),
    ticker ? el('span', { class: 'ticker' }, ' (' + ticker + ')') : null
  ]);
  tr.appendChild(nameTd);
  // td 2 (2026-11-14): 공시 주기 — 분기 / 반기 / 연간. 반기·연간은 1·3분기에 손익이 없어 섹터 리뷰 전 확인용
  const cycle = (state.watchlist.annual || []).includes(stock.name) ? '연간'
    : (state.watchlist.halfYear || []).includes(stock.name) ? '반기' : '분기';
  const cycleTitle = cycle === '분기' ? '분기마다 손익 공시'
    : cycle === '반기' ? '손익은 반기(1H→Q2·2H→Q4 리뷰)만 — 1·3분기는 수주·매출 업데이트를 직전 반기 리뷰에 덧붙임'
    : '손익은 연간(Q4 리뷰)만';
  tr.appendChild(el('td', { class: 'col-cycle' }, el('span', { class: 'cycle-badge cycle-' + cycle, title: cycleTitle }, cycle)));
  // td 3: 발표일 (YY/MM/DD)
  tr.appendChild(el('td', { class: 'col-date' }, (cal && cal.date) ? formatDate(cal.date, state.currentQuarter) : '발표일 미정'));
  // td 4 (2026-11-14): 발표 여부 — 발표 전 D-n / 발표 후 리뷰 완료 / 발표 후 리뷰 대기(놓침 방지 경고)
  const rv = resolveReview(stock, cycle);
  tr.appendChild(el('td', { class: 'col-status' }, renderReleaseStatus(cal, rv)));
  // td 3: 리포트 버튼 4개
  const buttons = el('div', { class: 'mode-buttons' });
  // 2026-10-30: 프리뷰·인뎁스 모드 폐지 → 버튼 제거 (실적은 리뷰 v11 하나)
  // 2026-11-14: 산업기초 → 기업개요 → 실적 리뷰. 테마분석은 종목 행에서 빼고 "테마 리뷰" 칸에서만 연결
  for (const pair of [['industry-basic', '산업기초'], ['company', '기업개요'], ['review', '실적 리뷰']]) {
    const mode = pair[0], label = pair[1];
    // 5/18 추가: industry-basic + multi-industry (예: Alphabet=광고|클라우드) → dropdown UX
    if (mode === 'industry-basic' && stock.industries && stock.industries.length > 1) {
      buttons.appendChild(renderIndustryBasicDropdown(stock, label));
      continue;
    }
    let file = mode === 'review' ? rv.file : getModeFile(stock, mode);
    const shownLabel = mode === 'review' ? label + rv.suffix : label;
    if (file) {
      buttons.appendChild(el('a', { class: 'mode-btn', href: buildHtmlPath(mode, file), target: '_blank', title: shownLabel + ': ' + file }, shownLabel));
    } else {
      buttons.appendChild(el('span', { class: 'mode-btn disabled', title: label + ': 미작성' }, label));
    }
  }
  tr.appendChild(el('td', { class: 'col-report' }, [buttons]));
  return tr;
}

function renderSectorCard(sectorObj, tier) {
  // tier: 'T1' (집중 칸) | 'grp' (대분류 그룹). T1 카드는 원래 대분류를 배지로 함께 표시
  const card = el('div', { class: 'sector-card ' + tier.toLowerCase() });
  const metaBits = ['종목 ' + sectorObj.stocks.length + '개'];
  if (tier === 'T1') metaBits.push('T1');
  if (sectorObj.category) metaBits.push(sectorObj.category);
  card.appendChild(el('div', { class: 'sector-header' }, [
    el('div', { class: 'sector-name' }, sectorObj.sector),
    el('div', { class: 'sector-meta' }, metaBits.join(' · '))
  ]));
  let rCount = 0;
  for (const stock of sectorObj.stocks) {
    if (getModeFile(stock, 'review')) rCount++;
  }
  card.appendChild(el('div', { class: 'sector-meta', style: 'margin-bottom: 0.4rem;' },
    '리뷰 ' + rCount + '/' + sectorObj.stocks.length));
  // 종목 테이블 (table 사용 — 컬럼 vertical line 카드 전체에 이어짐)
  const table = el('table', { class: 'stock-table' });
  const thead = el('thead');
  thead.appendChild(el('tr', null, [
    el('th', { class: 'col-name' }, '종목명'),
    el('th', { class: 'col-cycle' }, '공시 주기'),
    el('th', { class: 'col-date' }, '발표일'),
    el('th', { class: 'col-status' }, '발표 여부'),
    el('th', { class: 'col-report' }, '리포트')
  ]));
  table.appendChild(thead);
  // 2026-11-01 변경: 발표일순 → 서브섹터(세부 테마)순 정렬
  //   watchlist "섹터 리뷰 단위" 표 순서 → 각 서브섹터 안에서 핵심 → 확장 순. 표에 없는 종목은 맨 뒤(원래 순서 유지)
  //   한 종목이 여러 서브섹터에 있으면 표에서 처음 나오는 서브섹터 기준 (예: SpaceX → 하이퍼스케일러)
  const subRank = getSubsectorRank();
  const ranked = sectorObj.stocks.map((s, i) => ({ s, i, r: subRank[s.name] }));
  ranked.sort((a, b) => {
    const ra = a.r ? a.r.order : 1e9, rb = b.r ? b.r.order : 1e9;
    return (ra - rb) || (a.i - b.i);
  });
  const groupNames = new Set(ranked.map(x => x.r ? x.r.sub : '기타'));
  const showGroups = groupNames.size > 1;
  const tbody = el('tbody');
  let lastGroup = null;
  // 5/18 변경: stock 객체에 sector inject (산업기초 버튼 매칭용)
  for (const { s: stock, r } of ranked) {
    const group = r ? r.sub : '기타';
    if (showGroups && group !== lastGroup) {
      const td = el('td', { class: 'sub-group', colspan: '5' }, group);
      tbody.appendChild(el('tr', { class: 'sub-group-row' }, [td]));
      lastGroup = group;
    }
    stock.sector = sectorObj.sector;
    tbody.appendChild(renderStockRow(stock));
  }
  table.appendChild(tbody);
  card.appendChild(table);
  return card;
}

function renderSectors() {
  // 2026-11-14: Tier 1(집중 칸) + 산업 대분류 섹션 (대분류끼리 합산·델타 비교는 하지 않음)
  const t1 = $('t1Sectors'), box = $('groupSections');
  const wl = state.watchlist;
  t1.innerHTML = '';
  for (const sec of (wl.T1 || [])) t1.appendChild(renderSectorCard(sec, 'T1'));
  if (!(wl.T1 || []).length) t1.appendChild(el('div', { class: 'empty-state' }, '집중 섹터 없음 — watchlist.md "섹터 T1" 칸에 섹터를 옮기면 여기에 표시됩니다.'));
  if (!box) return;
  box.innerHTML = '';
  for (const g of (wl.groups || [])) {
    box.appendChild(el('h2', null, g.name));
    const inT1 = (wl.T1 || []).filter(s => s.category === g.name).map(s => s.sector);
    if (inT1.length) box.appendChild(el('div', { class: 'sr-pending', style: 'margin:-0.4rem 0 0.6rem;' }, 'T1에 배치: ' + inT1.join(' · ')));
    const grid = el('div', { class: 'sector-grid' });
    for (const sec of g.sectors) grid.appendChild(renderSectorCard(sec, 'grp'));
    if (g.sectors.length) box.appendChild(grid);
  }
}

// 5/18 신규 — 테마 리뷰 카드 렌더링
// 위치: 워치리스트 박스 / 진행률 카드 다음, Tier 1 카드 전
// 데이터: manifest['theme-review']에서 파일명 parse → 테마별 그룹핑 → 분기별 link
// 파일 패턴: {테마}_테마리뷰_{분기}.html (예: 에이전트AI_테마리뷰_1Q26.html)
function renderThemeReviews() {
  const container = $('themeReviews');
  if (!container) return;
  container.innerHTML = '';
  const list = state.manifest['theme-review'] || [];
  // 2026-11-14: 테마분석(earnings-theme/{테마}_테마분석.html)도 이 칸에서만 연결 — 종목 행 버튼에서 제거
  const analysisFiles = (state.manifest.theme || []).filter(f => /_테마분석\.html$/.test(f));
  if (list.length === 0 && analysisFiles.length === 0) {
    container.appendChild(el('div', { class: 'empty-state' },
      '아직 작성된 테마 분석·리뷰가 없습니다. 새 모멘텀이 나오면 테마 분석 후 [테마 리뷰 모드] {테마}로 리뷰 작성.'));
    return;
  }
  // 테마별 그룹핑 (테마 분석만 있고 리뷰가 아직 없는 테마도 카드로 표시)
  const themeMap = {};
  const analysisOf = {};
  analysisFiles.forEach(f => {
    const t = f.replace(/_테마분석\.html$/, '');
    analysisOf[t] = f;
    if (!themeMap[t]) themeMap[t] = [];
  });
  // 2026-11-01: 종료 리포트 = {테마}_테마리뷰_{분기}_종료.html → "종료" 배지, 활성 테마 먼저 정렬
  list.forEach(file => {
    const m = file.match(/^(.+)_테마리뷰_(.+?)(_종료)?\.html$/);
    if (m) {
      const theme = m[1], quarter = m[2], ended = !!m[3];
      if (!themeMap[theme]) themeMap[theme] = [];
      themeMap[theme].push({ quarter, file, ended });
    }
  });
  const isEnded = (t) => themeMap[t].some(r => r.ended);
  const themeNames = Object.keys(themeMap).sort((a, b) => (isEnded(a) - isEnded(b)) || a.localeCompare(b));
  for (const theme of themeNames) {
    const reviews = themeMap[theme].slice().sort((a, b) => b.quarter.localeCompare(a.quarter));
    const ended = reviews.find(r => r.ended);
    const card = el('div', { class: 'theme-card' + (ended ? ' theme-ended' : '') });
    card.appendChild(el('div', { class: 'theme-name' }, theme));
    if (ended) {
      const badges = el('div', { class: 'sr-badges' });
      badges.appendChild(el('span', { class: 'sr-badge delta-꺾임' }, '종료 ' + ended.quarter));
      card.appendChild(badges);
    }
    card.appendChild(el('div', { class: 'theme-meta' }, '분기 리뷰: ' + reviews.length + '회' + (ended ? '' : (reviews.length ? ' · 진행 중' : ' · 리뷰 전'))));
    const links = el('div', { class: 'theme-reviews' });
    if (analysisOf[theme]) {
      links.appendChild(el('a', {
        class: 'theme-review-link',
        href: 'earnings/earnings-theme/' + analysisOf[theme],
        target: '_blank',
        title: analysisOf[theme]
      }, '테마 분석'));
    }
    for (const r of reviews) {
      links.appendChild(el('a', {
        class: 'theme-review-link',
        href: buildHtmlPath('theme-review', r.file),
        target: '_blank',
        title: r.file
      }, r.quarter));
    }
    card.appendChild(links);
    container.appendChild(card);
  }
}

// 2026-11-01 신규 — 섹터 리뷰 (서브섹터 단위 상시 레이어)
// 데이터: watchlist.md "## 섹터 리뷰 단위 (서브섹터)" 표 → 서브섹터별 living doc
//   earnings/sector-review/{서브섹터}_섹터리뷰.md 의 상단 상태 블록(> 키: 값)을 읽어 카드 표시
//   (분기 무관 영구 문서라 manifest 없이 파일명으로 직접 조회)
function parseSubsectors(md) {
  const rows = [];
  let inSection = false;
  for (const line of md.split('\n')) {
    if (/^##\s/.test(line)) { inSection = /섹터 리뷰 단위/.test(line); continue; }
    if (!inSection || !/^\|/.test(line) || /^\|\s*-/.test(line)) continue;
    const cells = line.split('|').slice(1, -1).map(c => c.trim());
    if (cells.length < 4 || cells[0] === '섹터') continue;
    const split = s => (s && s !== '-') ? s.split(',').map(x => x.trim()).filter(Boolean) : [];
    rows.push({ sector: cells[0], sub: cells[1], core: split(cells[2]), ext: split(cells[3]) });
  }
  return rows;
}

// 종목명 → { order, sub } (서브섹터 표 순서 기반 정렬 키). 첫 등장 서브섹터 우선
function getSubsectorRank() {
  if (state._subRank) return state._subRank;
  const rank = {};
  (state.subsectors || []).forEach((row, gi) => {
    row.core.concat(row.ext).forEach((name, si) => {
      if (!(name in rank)) rank[name] = { order: gi * 100 + si, sub: row.sub };
    });
  });
  state._subRank = rank;
  return rank;
}

function parseSectorReviewStatus(md) {
  const get = (key) => {
    const m = md.match(new RegExp('^>\\s*' + key + '\\s*:\\s*(.+)$', 'm'));
    return m ? m[1].trim() : null;
  };
  const deltaLine = get('섹터 델타') || '';
  const dm = deltaLine.match(/^([^|]+?)\s*\|\s*내러티브\s*:\s*(.+)$/);
  return {
    quarter: get('최신 분기'),
    delta: dm ? dm[1].trim() : (deltaLine || null),
    narrative: dm ? dm[2].trim() : null,
    signal: get('모멘텀 신호'),
    theme: get('활성 테마'),
    positioning: get('포지셔닝'),  // 2026-11-14: ⑦ 글로벌 PM 포지셔닝 결론 압축
    members: get('편입 종목')
  };
}

async function fetchQuiet(path) {
  try { const r = await fetch(path, { cache: 'no-cache' }); return r.ok ? await r.text() : null; }
  catch (e) { return null; }
}

async function renderSectorReviews() {
  const container = $('sectorReviews');
  const pendingBox = $('sectorReviewsPending');
  if (!container) return;
  const subs = state.subsectors || [];
  if (subs.length === 0) {
    container.innerHTML = '';
    container.appendChild(el('div', { class: 'empty-state' }, 'watchlist.md에 "섹터 리뷰 단위 (서브섹터)" 표가 없습니다.'));
    return;
  }
  const base = 'earnings/sector-review/';
  const results = await Promise.all(subs.map(async (s) => {
    const md = await fetchQuiet(base + encodeURIComponent(s.sub + '_섹터리뷰') + '.md');
    return { s, status: md ? parseSectorReviewStatus(md) : null };
  }));
  container.innerHTML = '';
  const pending = [];
  for (const { s, status } of results) {
    if (!status) { pending.push(s.sub); continue; }
    const card = el('div', { class: 'theme-card sr-card' });
    card.appendChild(el('div', { class: 'theme-name' }, s.sub));
    const metaParts = [s.sector];
    if (status.quarter) metaParts.push('최신 ' + displayQuarter(status.quarter));
    metaParts.push(status.members ? status.members : ('핵심 ' + s.core.join(', ')));
    card.appendChild(el('div', { class: 'theme-meta' }, metaParts.join(' · ')));
    const badges = el('div', { class: 'sr-badges' });
    if (status.delta) badges.appendChild(el('span', { class: 'sr-badge delta-' + status.delta }, '델타 ' + status.delta));
    if (status.narrative) badges.appendChild(el('span', { class: 'sr-badge' }, '내러티브 ' + status.narrative));
    card.appendChild(badges);
    if (status.signal && !/^없음/.test(status.signal)) {
      card.appendChild(el('div', { class: 'sr-signal', html: '모멘텀 신호: <b>' + status.signal.replace(/</g, '&lt;') + '</b>' }));
    }
    if (status.theme && !/^없음/.test(status.theme)) {
      card.appendChild(el('div', { class: 'sr-signal' }, '활성 테마: ' + status.theme));
    }
    if (status.positioning) {
      card.appendChild(el('div', { class: 'sr-signal sr-pm', html: 'PM: <b>' + status.positioning.replace(/</g, '&lt;') + '</b>' }));
    }
    const links = el('div', { class: 'theme-reviews' });
    links.appendChild(el('a', {
      class: 'theme-review-link',
      href: base + encodeURIComponent(s.sub + '_섹터리뷰') + '.html',
      target: '_blank'
    }, '섹터 리뷰 열기'));
    card.appendChild(links);
    container.appendChild(card);
  }
  if (container.children.length === 0) {
    container.appendChild(el('div', { class: 'empty-state' },
      '아직 작성된 섹터 리뷰가 없습니다. 핵심 종목 리뷰 후 [섹터 리뷰 모드] {서브섹터}로 첫 리뷰 작성.'));
  }
  if (pendingBox) pendingBox.textContent = pending.length ? ('미작성: ' + pending.join(' · ')) : '';
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

// 2026-11-14: 반기 공시 종목 리뷰 md에서 "> 분기 업데이트:" 줄을 읽어 둔다 (파일명 → 줄 내용)
async function loadHalfYearUpdates() {
  state.halfUpdates = {};
  const names = (state.watchlist.halfYear || []).concat(state.watchlist.annual || []);
  if (!names.length) return;
  const keys = [];
  for (const sec of allSectors()) for (const s of sec.stocks) if (names.includes(s.name)) keys.push(s.ticker || s.name);
  const files = (state.manifest.review || []).filter(f => keys.some(k => f.endsWith('_' + k + '_' + SUFFIX.review + '.html')));
  await Promise.all(files.map(async (f) => {
    const md = await fetchQuiet(buildHtmlPath('review', f).replace(/\.html$/, '.md'));
    const m = md && md.match(/^>\s*분기 업데이트\s*:\s*(.+)$/m);
    state.halfUpdates[f] = m ? m[1] : '';
  }));
}

async function init() {
  const wlText = await fetchText(DATA_PATHS.watchlist);
  if (wlText) {
    state.watchlist = parseWatchlist(wlText);
    state.subsectors = parseSubsectors(wlText);
  }
  else $('watchlistSummary').innerHTML = '<div class="error-box">watchlist.md load failed.</div>';
  renderSectorReviews();  // 비동기 — 다른 렌더를 막지 않음
  const calText = await fetchText(DATA_PATHS.calendar);
  if (calText) {
    const parsed = parseCalendar(calText);
    state.calendar = parsed.calendar;
    state.signals = parsed.signals;
  }
  const manifest = await fetchJson(DATA_PATHS.manifest);
  if (manifest) state.manifest = manifest;
  await loadHalfYearUpdates();
  state.currentQuarter = getCurrentQuarter();
  $('currentQuarterLabel').textContent = displayQuarter(state.currentQuarter);
  populateQuarterSelector();
  renderWatchlistSummary();
  renderProgress();
  renderThemeReviews();
  renderSectors();
  setupSearch();
  setupQuarterSelector();
  $('lastUpdate').textContent = new Date().toLocaleString('ko-KR');
}

document.addEventListener('DOMContentLoaded', init);
