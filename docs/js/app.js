/* Progressive enhancement: the full catalog remains readable without JavaScript. */
(() => {
  "use strict";
  const query = document.getElementById("q");
  const heroQuery = document.getElementById("hero-q");
  const category = document.getElementById("category");
  const status = document.getElementById("status");
  const grid = document.getElementById("grid");
  const pagination = document.getElementById("pagination");
  const pageSize = 12;
  let page = 1;
  const entries = Array.from(grid.querySelectorAll(".card"), (card) => ({
    card,
    text: [card.textContent, ...Array.from(card.querySelectorAll("a"), (a) => a.href)].join(" ").toLowerCase(),
  }));
  const buttons = Array.from(document.querySelectorAll("#category-buttons button"));

  function render() {
    const term = query.value.trim().toLowerCase();
    const matches = entries.filter(({ card, text }) =>
      (!category.value || card.dataset.category === category.value) && (!term || text.includes(term))
    );
    const pages = Math.max(1, Math.ceil(matches.length / pageSize));
    page = Math.min(page, pages);
    const shown = new Set(matches.slice((page - 1) * pageSize, page * pageSize));
    for (const entry of entries) entry.card.hidden = !shown.has(entry);
    for (const button of buttons) button.setAttribute("aria-pressed", String(button.dataset.category === category.value));
    const label = category.selectedOptions[0].textContent;
    status.textContent = !matches.length ? "没有匹配结果" : term ? `找到 ${matches.length} 个结果` : category.value ? label : "全部资源";
    document.getElementById("empty").hidden = matches.length > 0;
    pagination.hidden = pages <= 1;
    document.getElementById("page-status").textContent = `${page} / ${pages}`;
    document.getElementById("page-prev").disabled = page === 1;
    document.getElementById("page-next").disabled = page === pages;
  }
  function filter() { page = 1; heroQuery.value = query.value; render(); }
  function reset() { query.value = ""; category.value = ""; filter(); }
  query.addEventListener("input", filter);
  document.getElementById("hero-search").addEventListener("submit", (event) => {
    event.preventDefault();
    query.value = heroQuery.value;
    category.value = "";
    filter();
    document.getElementById("resources").scrollIntoView({ block: "start" });
    query.focus({ preventScroll: true });
  });
  const views = Array.from(document.querySelectorAll("button[data-view]"));
  for (const button of views) button.addEventListener("click", () => {
    grid.dataset.view = button.dataset.view;
    for (const view of views) view.setAttribute("aria-pressed", String(view === button));
  });
  category.addEventListener("change", filter);
  for (const button of buttons) button.addEventListener("click", () => {
    category.value = button.dataset.category;
    filter();
  });
  for (const link of document.querySelectorAll("[data-category-link]")) link.addEventListener("click", () => {
    query.value = "";
    category.value = link.dataset.categoryLink;
    filter();
  });
  document.getElementById("reset").addEventListener("click", reset);
  document.getElementById("empty-reset").addEventListener("click", () => { reset(); query.focus(); });
  for (const [id, delta] of [["page-prev", -1], ["page-next", 1]]) {
    document.getElementById(id).addEventListener("click", () => {
      page += delta;
      render();
      document.querySelector(".catalog-controls").scrollIntoView({ block: "start" });
      query.focus({ preventScroll: true });
    });
  }
  document.addEventListener("keydown", (event) => {
    if (event.key === "/" && !event.ctrlKey && !event.metaKey && !event.altKey &&
        !event.target.closest("input, textarea, select, [contenteditable]")) {
      event.preventDefault(); query.focus();
    }
  });
  document.getElementById("hero-search").hidden = false;
  document.getElementById("view-switch").hidden = false;
  document.getElementById("filters").hidden = false;
  document.getElementById("category-buttons").hidden = false;
  render();
})();
