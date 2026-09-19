/* All resources are already in the HTML; JavaScript only filters them. */
(() => {
  "use strict";
  const query = document.getElementById("q");
  const category = document.getElementById("category");
  const status = document.getElementById("status");
  const entries = Array.from(document.querySelectorAll(".card"), (card) => ({
    card,
    text: [card.textContent, ...Array.from(card.querySelectorAll("a"), (a) => a.href)].join(" ").toLowerCase(),
  }));
  function filter() {
    const term = query.value.trim().toLowerCase();
    let matches = 0;
    for (const { card, text } of entries) {
      card.hidden = Boolean((category.value && card.dataset.category !== category.value) || (term && !text.includes(term)));
      if (!card.hidden) matches += 1;
    }
    status.textContent = !matches ? "没有匹配结果，请换一个关键词或重置筛选。"
      : term || category.value ? `找到 ${matches} 个结果` : "完整目录";
  }
  query.addEventListener("input", filter);
  category.addEventListener("change", filter);
  document.getElementById("reset").addEventListener("click", () => {
    query.value = "";
    category.value = "";
    filter();
  });
  document.getElementById("filters").hidden = false;
  filter();
})();
