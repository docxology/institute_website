const search = document.querySelector("#atlas-search");
const section = document.querySelector("#atlas-section");
const rows = [...document.querySelectorAll(".atlas-row")];
const count = document.querySelector("#atlas-count");

function applyAtlasFilters() {
  const query = (search?.value || "").trim().toLowerCase();
  const selected = section?.value || "";
  let visible = 0;

  for (const row of rows) {
    const matchesQuery = !query || row.dataset.search.includes(query);
    const matchesSection = !selected || row.dataset.section === selected;
    const show = matchesQuery && matchesSection;
    row.hidden = !show;
    if (show) visible += 1;
  }

  if (count) {
    count.textContent = `${visible} page${visible === 1 ? "" : "s"} shown`;
  }
}

search?.addEventListener("input", applyAtlasFilters);
section?.addEventListener("change", applyAtlasFilters);
applyAtlasFilters();
