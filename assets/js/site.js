// Site enhancements: dark mode toggle, lazy loading, and accessibility helpers
(function() {
  function setDarkMode(on) {
    document.body.classList.toggle('dark-mode', on);
    document.querySelectorAll('header, nav, footer').forEach(el => el.classList.toggle('dark-mode', on));
    localStorage.setItem('darkMode', on ? '1' : '0');
  }

  function ensureToggleButton() {
    if (document.getElementById('darkmode-toggle')) return;
    const btn = document.createElement('button');
    btn.id = 'darkmode-toggle';
    btn.type = 'button';
    btn.className = 'darkmode-toggle';
    btn.setAttribute('aria-label', 'Toggle dark mode');
    btn.textContent = 'Dark mode';

    const masthead = document.querySelector('.masthead__menu') || document.querySelector('header') || document.body;
    masthead.appendChild(btn);

    btn.addEventListener('click', () => {
      setDarkMode(!document.body.classList.contains('dark-mode'));
    });
  }

  function applySavedMode() {
    const saved = localStorage.getItem('darkMode');
    if (saved === '1') setDarkMode(true);
  }

  function enableLazyLoading() {
    document.querySelectorAll('img:not([loading])').forEach(img => {
      img.setAttribute('loading', 'lazy');
      img.setAttribute('decoding', 'async');
    });
  }

  function init() {
    applySavedMode();
    ensureToggleButton();
    enableLazyLoading();
  }

  document.addEventListener('DOMContentLoaded', init);
})();
