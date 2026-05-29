/* nav.js — mobile sidebar drawer + active link highlight */
(function () {
  const toggle = document.querySelector(".nav-toggle");
  const sidebar = document.querySelector(".sidebar");
  if (toggle && sidebar) {
    toggle.addEventListener("click", () => sidebar.classList.toggle("open"));
  }

  // Highlight the current page in the sidebar.
  const here = location.pathname.replace(/\/$/, "");
  document.querySelectorAll(".sidebar a").forEach((a) => {
    const href = (a.getAttribute("href") || "").replace(/\/$/, "");
    if (href && here.endsWith(href)) a.classList.add("active");
  });
})();
