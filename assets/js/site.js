// Site enhancements: dark mode toggle, lazy loading, and accessibility helpers
(function() {
  function setDarkMode(on) {
    document.body.classList.toggle('dark-mode', on);
    document.querySelectorAll('header, nav, footer').forEach(el => el.classList.toggle('dark-mode', on));
  }

  function applySystemMode() {
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    setDarkMode(prefersDark);
  }

  function enableLazyLoading() {
    document.querySelectorAll('img:not([loading])').forEach(img => {
      img.setAttribute('loading', 'lazy');
      img.setAttribute('decoding', 'async');
    });
  }

  function init() {
    applySystemMode();
    if (window.matchMedia) {
      const media = window.matchMedia('(prefers-color-scheme: dark)');
      if (media.addEventListener) {
        media.addEventListener('change', applySystemMode);
      } else if (media.addListener) {
        media.addListener(applySystemMode);
      }
    }
    enableLazyLoading();
  }

  document.addEventListener('DOMContentLoaded', init);
})();
