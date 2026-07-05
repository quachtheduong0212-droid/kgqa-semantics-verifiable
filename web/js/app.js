/**
 * KGQA Concept Path Explorer — Main Application Logic
 *
 * Handles UI state, DOM rendering, and event binding. Uses the API client
 * from api.js (which itself falls back to mock_data.js when the backend is
 * offline).
 */

/* ------------------------------------------------------------------ */
/*  DOM references                                                     */
/* ------------------------------------------------------------------ */
const dom = {};

function cacheDom() {
  dom.queryInput = document.getElementById("query-input");
  dom.algoSelect = document.getElementById("algo-select");
  dom.searchBtn = document.getElementById("search-btn");
  dom.demoBadge = document.getElementById("demo-badge");
  dom.resultArea = document.getElementById("result-area");
  dom.loadingOverlay = document.getElementById("loading-overlay");
  dom.errorDisplay = document.getElementById("error-display");
  dom.pathChain = document.getElementById("path-chain");
  dom.pathExplanation = document.getElementById("path-explanation");
  dom.metricsGrid = document.getElementById("metrics-grid");
  dom.relatedConcepts = document.getElementById("related-concepts");
  dom.compareToggle = document.getElementById("compare-toggle");
  dom.comparisonSection = document.getElementById("comparison-section");
  dom.comparisonBody = document.getElementById("comparison-body");
  dom.graphStats = document.getElementById("graph-stats");
  dom.pathCard = document.getElementById("path-card");
}

/* ------------------------------------------------------------------ */
/*  State                                                              */
/* ------------------------------------------------------------------ */
let currentResult = null;
let compareVisible = false;

/* ------------------------------------------------------------------ */
/*  Initialisation                                                     */
/* ------------------------------------------------------------------ */
document.addEventListener("DOMContentLoaded", async () => {
  cacheDom();
  bindEvents();

  const backendOk = await checkBackendStatus();
  if (!backendOk) {
    dom.demoBadge.classList.add("visible");
  }

  // Load graph info for footer
  try {
    const info = await fetchGraphInfo();
    renderGraphStats(info);
  } catch {
    /* non-critical */
  }
});

/* ------------------------------------------------------------------ */
/*  Events                                                             */
/* ------------------------------------------------------------------ */
function bindEvents() {
  dom.searchBtn.addEventListener("click", handleSearch);
  dom.queryInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") handleSearch();
  });
  dom.compareToggle.addEventListener("click", handleCompareToggle);

  // Example query buttons
  document.querySelectorAll(".example-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      dom.queryInput.value = btn.dataset.query;
      handleSearch();
    });
  });
}

/* ------------------------------------------------------------------ */
/*  Search handler                                                     */
/* ------------------------------------------------------------------ */
async function handleSearch() {
  const question = dom.queryInput.value.trim();
  if (!question) {
    showError("Please enter a concept-relationship question.");
    return;
  }

  const algorithm = dom.algoSelect.value;

  hideError();
  hideResult();
  showLoading();

  try {
    const result = await fetchQuery(question, algorithm);
    currentResult = result;
    renderResult(result);

    // Also load neighbors for the target concept
    const target = result.target || result.path[result.path.length - 1];
    const neighbors = await fetchNeighbors(target);
    renderRelatedConcepts(neighbors);

    showResult();
  } catch (err) {
    showError(err.message);
  } finally {
    hideLoading();
  }
}

/* ------------------------------------------------------------------ */
/*  Render: path result                                                */
/* ------------------------------------------------------------------ */
function renderResult(result) {
  // -- Path chain --
  const labels = result.path_labels || result.path;
  dom.pathChain.innerHTML = "";
  labels.forEach((label, i) => {
    const node = document.createElement("span");
    node.className = "path-node";
    node.textContent = label;
    node.style.animationDelay = `${i * 0.08}s`;
    dom.pathChain.appendChild(node);

    if (i < labels.length - 1) {
      const arrow = document.createElement("span");
      arrow.className = "path-arrow";
      arrow.textContent = "→";
      arrow.style.animationDelay = `${i * 0.08 + 0.04}s`;
      dom.pathChain.appendChild(arrow);
    }
  });

  // -- Explanation --
  const sentences = result.answer.split(/\.\s*/g).filter((s) => s.trim());
  dom.pathExplanation.innerHTML = "";
  sentences.forEach((s) => {
    const span = document.createElement("span");
    span.className = "sentence";
    span.textContent = s.endsWith(".") ? s : s + ".";
    dom.pathExplanation.appendChild(span);
  });

  // -- Metrics --
  dom.metricsGrid.innerHTML = `
    <div class="metric-item">
      <div class="metric-label">Algorithm</div>
      <div class="metric-value">${(result.algorithm || "").toUpperCase()}</div>
    </div>
    <div class="metric-item">
      <div class="metric-label">Direction</div>
      <div class="metric-value direction">${result.direction || "forward"}</div>
    </div>
    <div class="metric-item">
      <div class="metric-label">Path Cost</div>
      <div class="metric-value cost">${formatNum(result.cost)}</div>
    </div>
    <div class="metric-item">
      <div class="metric-label">Nodes Visited</div>
      <div class="metric-value">${result.nodes_visited}</div>
    </div>
    <div class="metric-item">
      <div class="metric-label">Time</div>
      <div class="metric-value time">${formatNum(result.time_ms)} ms</div>
    </div>
    <div class="metric-item">
      <div class="metric-label">Path Length</div>
      <div class="metric-value">${(result.path || []).length} hops</div>
    </div>
  `;

  // Reset comparison when a new query is made
  compareVisible = false;
  dom.comparisonSection.classList.remove("visible");
  dom.compareToggle.classList.remove("active");
}

/* ------------------------------------------------------------------ */
/*  Render: related concepts                                           */
/* ------------------------------------------------------------------ */
function renderRelatedConcepts(data) {
  dom.relatedConcepts.innerHTML = "";
  if (!data || !data.neighbors || data.neighbors.length === 0) {
    dom.relatedConcepts.innerHTML =
      '<span style="color:var(--text-muted);font-size:0.82rem;">No neighbors found.</span>';
    return;
  }

  data.neighbors.forEach((n) => {
    const chip = document.createElement("button");
    chip.className = "concept-chip";

    const icon = n.direction === "parent" ? "↑" : n.direction === "child" ? "↓" : "→";
    chip.innerHTML = `<span class="edge-icon">${icon}</span> ${n.label}`;
    chip.title = `${n.edge_type} (${n.direction})`;

    // Clicking a related concept fills it into the query
    chip.addEventListener("click", () => {
      const currentSource = currentResult
        ? (currentResult.path_labels || currentResult.path)[0]
        : "";
      dom.queryInput.value = `How is ${currentSource} related to ${n.label}?`;
      handleSearch();
    });

    dom.relatedConcepts.appendChild(chip);
  });
}

/* ------------------------------------------------------------------ */
/*  Render: comparison table                                           */
/* ------------------------------------------------------------------ */
async function handleCompareToggle() {
  compareVisible = !compareVisible;
  dom.compareToggle.classList.toggle("active", compareVisible);

  if (!compareVisible) {
    dom.comparisonSection.classList.remove("visible");
    return;
  }

  const question = dom.queryInput.value.trim();
  if (!question) return;

  dom.comparisonSection.classList.add("visible");
  dom.comparisonBody.innerHTML = `
    <tr><td colspan="5" style="text-align:center;color:var(--text-muted);padding:1rem;">
      Loading comparison…
    </td></tr>`;

  try {
    const data = await fetchCompare(question);
    renderComparison(data.results);
  } catch (err) {
    dom.comparisonBody.innerHTML = `
      <tr><td colspan="5" style="color:var(--error-text);padding:1rem;">
        ${err.message}
      </td></tr>`;
  }
}

function renderComparison(results) {
  if (!results || results.length === 0) {
    dom.comparisonBody.innerHTML = `
      <tr><td colspan="5" style="text-align:center;color:var(--text-muted);">
        No results.
      </td></tr>`;
    return;
  }

  // Find best values for highlighting
  const minCost = Math.min(...results.map((r) => r.cost ?? Infinity));
  const minVisited = Math.min(...results.map((r) => r.nodes_visited ?? Infinity));
  const minTime = Math.min(...results.map((r) => r.time_ms ?? Infinity));

  dom.comparisonBody.innerHTML = results
    .map((r) => {
      const pathStr = (r.path_labels || r.path || []).join(" → ");
      const costClass = r.cost === minCost ? "best-value" : "";
      const visitedClass = r.nodes_visited === minVisited ? "best-value" : "";
      const timeClass = r.time_ms === minTime ? "best-value" : "";

      return `
        <tr>
          <td class="algo-name">${r.algorithm}</td>
          <td class="path-col" title="${pathStr}">${pathStr}</td>
          <td class="num-col ${costClass}">${formatNum(r.cost)}</td>
          <td class="num-col ${visitedClass}">${r.nodes_visited}</td>
          <td class="num-col ${timeClass}">${formatNum(r.time_ms)} ms</td>
        </tr>`;
    })
    .join("");
}

/* ------------------------------------------------------------------ */
/*  Render: graph stats footer                                         */
/* ------------------------------------------------------------------ */
function renderGraphStats(info) {
  if (!info) return;
  dom.graphStats.textContent = `${info.source} · ${info.num_nodes} nodes · ${info.num_edges} edges · root: ${info.root_concept}`;
}

/* ------------------------------------------------------------------ */
/*  UI helpers                                                         */
/* ------------------------------------------------------------------ */
function showLoading() {
  dom.loadingOverlay.classList.add("visible");
}

function hideLoading() {
  dom.loadingOverlay.classList.remove("visible");
}

function showResult() {
  dom.resultArea.classList.add("visible");
}

function hideResult() {
  dom.resultArea.classList.remove("visible");
}

function showError(msg) {
  dom.errorDisplay.textContent = msg;
  dom.errorDisplay.classList.add("visible");
  dom.resultArea.classList.remove("visible");
}

function hideError() {
  dom.errorDisplay.classList.remove("visible");
}

function formatNum(n) {
  if (n == null || n === Infinity) return "∞";
  if (Number.isInteger(n)) return n.toString();
  return n.toFixed(3);
}
