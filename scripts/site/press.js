(() => {
  const input = document.getElementById('press-q');
  const tiles = [...document.querySelectorAll('.press-tile')];
  const live = document.getElementById('press-live');
  const empty = document.getElementById('press-empty');
  const fold = value => value.toLowerCase().normalize('NFD').replace(/\p{M}/gu, '').replace(/ł/g, 'l');
  input.closest('label').hidden = false;

  function filter({ followAnchor = false, writeURL = false } = {}) {
    const url = new URL(location.href);
    let target;
    if (followAnchor) {
      try { target = document.getElementById(decodeURIComponent(url.hash.slice(1))); }
      catch { /* A malformed fragment has no target. */ }
      if (target?.matches('.press-moved')) {
        const destination = new URL(target.querySelector('a').href);
        destination.search = url.search;
        location.replace(destination);
        return;
      }
    }
    const words = fold(input.value).trim().split(/\s+/).filter(Boolean);
    const matches = tile => words.every(word => tile.dataset.q.includes(word));
    if (tiles.includes(target) && !matches(target)) {
      input.value = '';
      words.length = 0;
      writeURL = true;
    }
    let count = 0;
    for (const tile of tiles) {
      tile.parentElement.hidden = !matches(tile);
      if (!tile.parentElement.hidden) count++;
    }
    empty.hidden = count !== 0;
    live.textContent = words.length ? `${count} ${count === 1 ? 'result' : 'results'}` : '';
    if (writeURL) {
      if (input.value.trim()) url.searchParams.set('q', input.value.trim());
      else url.searchParams.delete('q');
      if (url.href !== location.href) history.replaceState(history.state, '', url);
    }
    if (target) requestAnimationFrame(() => target.scrollIntoView());
  }

  function readURL() {
    input.value = new URLSearchParams(location.search).get('q') || '';
    filter({ followAnchor: true });
  }
  function clear() {
    input.value = '';
    filter({ writeURL: true });
    input.focus();
  }
  input.addEventListener('input', () => filter({ writeURL: true }));
  input.addEventListener('keydown', event => {
    if (event.key === 'Escape') { event.preventDefault(); clear(); }
  });
  empty.querySelector('button').addEventListener('click', clear);
  addEventListener('hashchange', readURL);
  addEventListener('popstate', readURL);
  readURL();

  const topbar = document.querySelector('.topbar');
  const button = document.getElementById('sbtn');
  const siteQuery = document.getElementById('q');
  const open = value => {
    topbar.classList.toggle('searching', value);
    button.setAttribute('aria-expanded', String(value));
    if (value) siteQuery.focus();
    else button.focus();
  };
  button.hidden = false;
  button.addEventListener('click', () => open(!topbar.classList.contains('searching')));
  document.addEventListener('keydown', event => {
    if (event.defaultPrevented) return;
    if (event.key === 'Escape' && topbar.classList.contains('searching') && button.offsetWidth) open(false);
    if (event.key === '/' && !event.ctrlKey && !event.metaKey && !event.altKey &&
        !event.target.closest('input, textarea, select, [contenteditable]')) {
      event.preventDefault();
      open(true);
      siteQuery.select();
    }
  });
})();
