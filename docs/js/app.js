/* All resources and category links remain readable without JavaScript. */
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
  const normalize = text => text.normalize("NFKC").toLowerCase();
  const entries = Array.from(grid.querySelectorAll(".card"), card => ({
    card,
    text: normalize([card.textContent, ...Array.from(card.querySelectorAll("a"), a => a.href)].join(" ")),
  }));
  const buttons = Array.from(document.querySelectorAll("#category-buttons button"));
  const views = Array.from(document.querySelectorAll("button[data-view]"));

  function saveURL(mode = "replace") {
    const url = new URL(location.href);
    for (const [key, value] of Object.entries({q: query.value.trim(), category: category.value, page: page > 1 ? String(page) : "", view: grid.dataset.view === "list" ? "list" : ""})) {
      if (value) url.searchParams.set(key, value);
      else url.searchParams.delete(key);
    }
    if (url.href !== location.href) history[mode === "push" ? "pushState" : "replaceState"](null, "", url);
  }

  function render(mode = "replace") {
    const terms = normalize(query.value.trim()).split(/\s+/u).filter(Boolean);
    const matches = entries.filter(({ card, text }) =>
      (!category.value || card.dataset.category === category.value) && terms.every(term => text.includes(term))
    );
    const pages = Math.max(1, Math.ceil(matches.length / pageSize));
    page = Math.min(page, pages);
    const shown = new Set(matches.slice((page - 1) * pageSize, page * pageSize));
    for (const entry of entries) entry.card.hidden = !shown.has(entry);
    for (const button of buttons) button.setAttribute("aria-pressed", String(button.dataset.category === category.value));
    for (const button of views) button.setAttribute("aria-pressed", String(button.dataset.view === grid.dataset.view));
    if (heroQuery) heroQuery.value = query.value;
    status.textContent = !matches.length ? "没有匹配结果" : terms.length ? `找到 ${matches.length} 个结果` : category.value ? category.selectedOptions[0].textContent : (grid.dataset.label || "全部资源");
    document.getElementById("empty").hidden = matches.length > 0;
    pagination.hidden = pages <= 1;
    document.getElementById("page-status").textContent = `${page} / ${pages}`;
    document.getElementById("page-prev").disabled = page === 1;
    document.getElementById("page-next").disabled = page === pages;
    document.getElementById("share-status").textContent = "";
    document.getElementById("share-url").hidden = true;
    saveURL(mode);
  }

  function restoreURL() {
    const params = new URLSearchParams(location.search);
    query.value = params.get("q") || "";
    category.value = Array.from(category.options).some(option => option.value === params.get("category")) ? params.get("category") : "";
    const requestedPage = Number(params.get("page"));
    page = Number.isSafeInteger(requestedPage) && requestedPage > 0 ? requestedPage : 1;
    grid.dataset.view = params.get("view") === "list" ? "list" : "grid";
    render();
  }
  function filter(mode = "replace") { page = 1; render(mode); }
  function reset() { query.value = ""; category.value = ""; filter("push"); }
  query.addEventListener("input", () => filter());
  document.getElementById("hero-search")?.addEventListener("submit", event => {
    event.preventDefault(); query.value = heroQuery.value; category.value = ""; filter("push");
    document.getElementById("resources").scrollIntoView({ block: "start" });
    query.focus({ preventScroll: true });
  });
  for (const button of views) button.addEventListener("click", () => {
    grid.dataset.view = button.dataset.view; render("push");
  });
  category.addEventListener("change", () => filter("push"));
  for (const button of buttons) button.addEventListener("click", () => {
    category.value = button.dataset.category; filter("push");
  });
  document.getElementById("reset").addEventListener("click", reset);
  document.getElementById("empty-reset").addEventListener("click", () => { reset(); query.focus(); });
  for (const [id, delta] of [["page-prev", -1], ["page-next", 1]]) {
    document.getElementById(id).addEventListener("click", () => {
      page += delta; render("push");
      document.querySelector(".catalog-controls").scrollIntoView({ block: "start" });
      query.focus({ preventScroll: true });
    });
  }
  document.getElementById("share").addEventListener("click", async () => {
    const url = new URL(location.href); url.hash = "resources";
    const message = document.getElementById("share-status");
    try {
      await navigator.clipboard.writeText(url.href);
      message.textContent = "已复制当前筛选链接。";
    } catch {
      const input = document.getElementById("share-url");
      input.value = url.href; input.hidden = false; input.focus(); input.select();
      message.textContent = "自动复制失败，请手动复制下方链接。";
    }
  });
  window.addEventListener("popstate", restoreURL);
  document.addEventListener("keydown", event => {
    if (event.key === "/" && !event.ctrlKey && !event.metaKey && !event.altKey &&
        !event.target.closest("input, textarea, select, [contenteditable]")) {
      event.preventDefault(); query.focus();
    }
  });
  for (const id of ["hero-search", "view-switch", "filters", "category-buttons", "share"]) {
    const element = document.getElementById(id);
    if (element) element.hidden = false;
  }
  restoreURL();
})();
