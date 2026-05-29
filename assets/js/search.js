/* search.js — Cmd/Ctrl-K modal backed by Pagefind.
   Pagefind's bundle is generated at build time into /pagefind/ and loaded
   lazily the first time the modal opens. Degrades silently if absent
   (e.g. `jekyll serve` without a Pagefind run). */
(function () {
  const modal = document.querySelector(".search-modal");
  if (!modal) return;
  const openers = document.querySelectorAll("[data-search-open]");
  let pagefindUI = null;
  let loading = null;

  const BASE = (window.FC_BASEURL || "").replace(/\/$/, "");

  function ensurePagefind() {
    if (pagefindUI || loading) return loading;
    loading = new Promise((resolve) => {
      const css = document.createElement("link");
      css.rel = "stylesheet";
      css.href = BASE + "/pagefind/pagefind-ui.css";
      document.head.appendChild(css);

      const script = document.createElement("script");
      script.src = BASE + "/pagefind/pagefind-ui.js";
      script.onload = () => {
        /* global PagefindUI */
        pagefindUI = new PagefindUI({
          element: "#search-results",
          showImages: false,
          resetStyles: false,
          baseUrl: BASE || "/",
        });
        resolve(true);
      };
      script.onerror = () => resolve(false);
      document.body.appendChild(script);
    });
    return loading;
  }

  function open() {
    modal.classList.add("open");
    ensurePagefind().then((ok) => {
      const input = modal.querySelector(".pagefind-ui__search-input, .search-input");
      if (input) input.focus();
      if (!ok) {
        const r = document.querySelector("#search-results");
        if (r && !r.dataset.warned) {
          r.dataset.warned = "1";
          r.innerHTML =
            '<p class="text-muted" style="padding:1rem">Search index not built yet ' +
            '(run the production build).</p>';
        }
      }
    });
  }
  function close() {
    modal.classList.remove("open");
  }

  openers.forEach((b) => b.addEventListener("click", open));
  modal.addEventListener("click", (e) => {
    if (e.target === modal) close();
  });
  document.addEventListener("keydown", (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      modal.classList.contains("open") ? close() : open();
    } else if (e.key === "Escape") {
      close();
    }
  });
})();
