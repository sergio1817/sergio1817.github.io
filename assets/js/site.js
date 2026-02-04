// Site enhancements: dark mode toggle, lazy loading, and accessibility helpers
(function() {
  function enableLazyLoading() {
    document.querySelectorAll('img:not([loading])').forEach(img => {
      img.setAttribute('loading', 'lazy');
      img.setAttribute('decoding', 'async');
    });
  }

  function init() {
    enableLazyLoading();
  }

  document.addEventListener('DOMContentLoaded', init);
})();
