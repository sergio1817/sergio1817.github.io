// Dark mode toggle script
(function() {
  function setDarkMode(on) {
    document.body.classList.toggle('dark-mode', on);
    document.querySelectorAll('header, nav, footer').forEach(el => el.classList.toggle('dark-mode', on));
    localStorage.setItem('darkMode', on ? '1' : '0');
  }
  function init() {
    const saved = localStorage.getItem('darkMode');
    if (saved === '1') setDarkMode(true);
    const btn = document.getElementById('darkmode-toggle');
    if (btn) {
      btn.onclick = () => setDarkMode(!document.body.classList.contains('dark-mode'));
    }
  }
  document.addEventListener('DOMContentLoaded', init);
})();