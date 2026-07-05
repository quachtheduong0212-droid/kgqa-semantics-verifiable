/**
 * API client for the KGQA backend.
 *
 * If the Flask backend is unreachable the client automatically falls back to
 * the mock data defined in mock_data.js and sets a global flag so the UI can
 * show a "Demo Mode" badge.
 */

const API_BASE = "http://localhost:5000";

/** True when we are serving mock data instead of live results. */
let isDemoMode = false;

/**
 * Check whether the backend is reachable. Called once at startup.
 * Sets `isDemoMode` accordingly.
 */
async function checkBackendStatus() {
  try {
    const res = await fetch(`${API_BASE}/api/graph-info`, {
      signal: AbortSignal.timeout(2000),
    });
    if (res.ok) {
      isDemoMode = false;
      return true;
    }
  } catch {
    /* backend not available */
  }
  isDemoMode = true;
  return false;
}

/* ------------------------------------------------------------------ */
/*  Public API functions                                               */
/* ------------------------------------------------------------------ */

/**
 * Query a single algorithm.
 * @param {string} question  Natural-language question.
 * @param {string} algorithm One of: bfs, dfs, dijkstra, astar.
 * @returns {Promise<Object>} Query result.
 */
async function fetchQuery(question, algorithm = "dijkstra") {
  if (isDemoMode) {
    return _mockQuery(question, algorithm);
  }

  const params = new URLSearchParams({ q: question, algorithm });
  const res = await fetch(`${API_BASE}/api/query?${params}`);
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.error || `Server error ${res.status}`);
  }
  return res.json();
}

/**
 * Compare all 4 algorithms on the same query.
 * @param {string} question Natural-language question.
 * @returns {Promise<Object>} Comparison result.
 */
async function fetchCompare(question) {
  if (isDemoMode) {
    return _mockCompare(question);
  }

  const params = new URLSearchParams({ q: question });
  const res = await fetch(`${API_BASE}/api/compare?${params}`);
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.error || `Server error ${res.status}`);
  }
  return res.json();
}

/**
 * Fetch immediate neighbors of a concept node.
 * @param {string} concept Node ID (e.g. "random_forests").
 * @returns {Promise<Object>} Neighbors list.
 */
async function fetchNeighbors(concept) {
  if (isDemoMode) {
    return _mockNeighbors(concept);
  }

  const params = new URLSearchParams({ concept });
  const res = await fetch(`${API_BASE}/api/neighbors?${params}`);
  if (!res.ok) {
    return { concept, label: concept, neighbors: [] };
  }
  return res.json();
}

/**
 * Fetch metadata about the loaded graph.
 * @returns {Promise<Object>} Graph info.
 */
async function fetchGraphInfo() {
  if (isDemoMode) {
    return MOCK_GRAPH_INFO;
  }

  const res = await fetch(`${API_BASE}/api/graph-info`);
  if (!res.ok) {
    return MOCK_GRAPH_INFO;
  }
  return res.json();
}

/* ------------------------------------------------------------------ */
/*  Mock helpers                                                       */
/* ------------------------------------------------------------------ */

function _normalizeKey(question) {
  return question
    .trim()
    .toLowerCase()
    .replace(/[?.!]/g, "");
}

function _mockQuery(question, algorithm) {
  const key = _normalizeKey(question);
  const result = MOCK_QUERY_RESULTS[key];
  if (!result) {
    throw new Error(
      "Could not parse the question. Try: 'How is Data Mining related to Random Forests?'"
    );
  }
  // Return a copy with the requested algorithm name (mock data is fixed).
  return Promise.resolve({ ...result, algorithm });
}

function _mockCompare(question) {
  const key = _normalizeKey(question);
  const result = MOCK_COMPARE_RESULTS[key];
  if (!result) {
    throw new Error(
      "Could not parse the question. Try: 'How is Data Mining related to Random Forests?'"
    );
  }
  return Promise.resolve(result);
}

function _mockNeighbors(concept) {
  const key = concept.trim().toLowerCase().replace(/\s+/g, "_");
  const result = MOCK_NEIGHBORS[key];
  if (!result) {
    return Promise.resolve({ concept: key, label: key, neighbors: [] });
  }
  return Promise.resolve(result);
}
