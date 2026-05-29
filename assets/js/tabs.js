/* tabs.js — GitBook-style tab groups */
(function () {
  document.querySelectorAll(".tabs").forEach((group) => {
    const buttons = group.querySelectorAll(".tab-buttons button");
    const panels = group.querySelectorAll(".tab-panel");
    buttons.forEach((btn, i) => {
      btn.addEventListener("click", () => {
        buttons.forEach((b) => b.classList.remove("active"));
        panels.forEach((p) => p.classList.remove("active"));
        btn.classList.add("active");
        if (panels[i]) panels[i].classList.add("active");
      });
    });
  });
})();
