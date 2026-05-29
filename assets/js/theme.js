/* theme.js — dark/light toggle with localStorage + system pref */
(function () {
  const KEY = "fc-theme";
  const root = document.documentElement;

  function apply(theme) {
    if (theme === "light") root.setAttribute("data-theme", "light");
    else root.removeAttribute("data-theme");
  }

  // Terminal dark is the brand default; only an explicit choice flips to light.
  const stored = localStorage.getItem(KEY);
  if (stored) apply(stored);

  window.toggleTheme = function () {
    const isLight = root.getAttribute("data-theme") === "light";
    const next = isLight ? "dark" : "light";
    apply(next);
    localStorage.setItem(KEY, next);
  };
})();
