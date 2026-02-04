// Site enhancements: dark mode toggle, lazy loading, and accessibility helpers
(function() {
  function setDarkMode(on) {
    document.body.classList.toggle('dark-mode', on);
    document.querySelectorAll('header, nav, footer').forEach(el => el.classList.toggle('dark-mode', on));
  }

  function applySystemMode() {
    if (localStorage.getItem('theme')) return;
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    setDarkMode(prefersDark);
  }

  function applySavedMode() {
    const saved = localStorage.getItem('theme');
    if (saved === 'dark') return setDarkMode(true);
    if (saved === 'light') return setDarkMode(false);
    applySystemMode();
  }

  function ensureToggleButton() {
    let btn = document.getElementById('darkmode-toggle');
    if (!btn) {
      btn = document.createElement('button');
      btn.id = 'darkmode-toggle';
      btn.type = 'button';
      btn.className = 'darkmode-toggle';
      btn.setAttribute('aria-label', 'Toggle dark mode');
      btn.textContent = 'Toggle dark mode';
      document.body.appendChild(btn);
    }
    if (btn.dataset.bound === '1') return;
    btn.dataset.bound = '1';

    btn.addEventListener('click', () => {
      const isDark = document.body.classList.contains('dark-mode');
      const next = !isDark;
      setDarkMode(next);
      localStorage.setItem('theme', next ? 'dark' : 'light');
    });
  }

  function enableLazyLoading() {
    document.querySelectorAll('img:not([loading])').forEach(img => {
      img.setAttribute('loading', 'lazy');
      img.setAttribute('decoding', 'async');
    });
  }

  function init() {
    applySavedMode();
    if (window.matchMedia) {
      const media = window.matchMedia('(prefers-color-scheme: dark)');
      if (media.addEventListener) {
        media.addEventListener('change', applySystemMode);
      } else if (media.addListener) {
        media.addListener(applySystemMode);
      }
    }
    ensureToggleButton();
    enableLazyLoading();
  }

  document.addEventListener('DOMContentLoaded', init);
})();
