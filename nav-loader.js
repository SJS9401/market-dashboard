/* nav-loader.js — 모든 dashboard HTML이 공통으로 import.
 *
 * 동작:
 *   1. data-active 속성을 가진 nav 컨테이너 찾기 (.tab-bar 또는 .global-nav 모두 지원)
 *   2. nav-include.html을 fetch해서 innerHTML에 inject
 *   3. data-active 값과 같은 data-key anchor에 .active 클래스 부여
 *
 * 사용 (각 페이지):
 *   <div class="tab-bar" data-active="industry_battery"></div>
 *   또는 <div class="global-nav" data-active="leading_stocks"></div>
 *   <script src="nav-loader.js" defer></script>
 *
 * data-active 값:
 *   dashboard | market_cycle | leading_stocks | earnings | industry_semi | industry_battery
 */
(function () {
  // data-active 속성을 가진 첫 컨테이너 (클래스명 무관)
  const nav = document.querySelector('[data-active]');
  if (!nav) return;
  fetch('nav-include.html', { cache: 'no-store' })
    .then(r => {
      if (!r.ok) throw new Error('fetch failed: ' + r.status);
      return r.text();
    })
    .then(html => {
      nav.innerHTML = html;
      const active = nav.dataset.active;
      if (!active) return;
      const a = nav.querySelector('a[data-key="' + active + '"]');
      if (a) a.classList.add('active');
    })
    .catch(e => {
      console.error('[nav-loader] nav-include.html 로드 실패:', e);
      // fallback: 빈 nav 표시. 페이지 기능에는 영향 없음.
    });
})();
