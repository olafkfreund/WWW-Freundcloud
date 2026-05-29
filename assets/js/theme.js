/* theme.js — dark/light toggle with localStorage + system pref */
(function () {
  const KEY = "fc-theme";
  const root = document.documentElement;

  function apply(theme) {
    if (theme === "light") root.setAttribute("data-theme", "light");
    else root.removeAttribute("data-theme");
  }

  // Initial: stored pref, else system. (Dark is the default with no attribute.)
  const stored = localStorage.getItem(KEY);
  if (stored) {
    apply(stored);
  } else if (window.matchMedia("(prefers-color-scheme: light)").matches) {
    apply("light");
  }

  window.toggleTheme = function () {
    const isLight = root.getAttribute("data-theme") === "light";
    const next = isLight ? "dark" : "light";
    apply(next);
    localStorage.setItem(KEY, next);
  };
})();
