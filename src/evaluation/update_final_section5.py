"""Insert the completed Experiments and Results section into Final.docx."""

from __future__ import annotations

import tempfile
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt


DOCX_PATH = Path("Final.docx")

ALGO_COLORS = ["#2196F3", "#FF9800", "#4CAF50", "#9C27B0"]
ALGO_LABELS = ["BFS", "DFS", "Dijkstra", "A*"]

TEST_QUERIES = [
    ("Q1", "How is Data Mining related to Random Forests?",
     "Data Mining", "Random Forests",
     "Data Mining -> Decision Tree -> Random Forests"),
    ("Q2", "How is Data Mining related to Web Mining?",
     "Data Mining", "Web Mining",
     "Data Mining -> Web Mining"),
    ("Q3", "How is Data Mining related to Classification?",
     "Data Mining", "Classification",
     "Data Mining -> Classification"),
    ("Q4", "How is Classification related to Decision Tree?",
     "Classification", "Decision Tree",
     "Classification -> Decision Tree"),
]

# (query, algo, path_len, cost, visited, avg_ms, path)
RESULT_ROWS = [
    ("Q1", "BFS",      "2", "2.0", "128", "0.0218", "Data Mining -> Decision Tree -> Random Forests"),
    ("Q1", "DFS",      "2", "2.0", "144", "0.0401", "Data Mining -> Decision Tree -> Random Forests"),
    ("Q1", "Dijkstra", "2", "2.0", "179", "0.3932", "Data Mining -> Decision Tree -> Random Forests"),
    ("Q1", "A*",       "2", "2.0", "150", "0.5029", "Data Mining -> Decision Tree -> Random Forests"),
    ("Q2", "BFS",      "1", "1.0",   "5", "0.0024", "Data Mining -> Web Mining"),
    ("Q2", "DFS",      "1", "1.0",  "62", "0.0183", "Data Mining -> Web Mining"),
    ("Q2", "Dijkstra", "1", "1.0",  "38", "0.1705", "Data Mining -> Web Mining"),
    ("Q2", "A*",       "1", "1.0",  "38", "0.2900", "Data Mining -> Web Mining"),
    ("Q3", "BFS",      "1", "1.0",  "74", "0.0117", "Data Mining -> Classification"),
    ("Q3", "DFS",      "1", "1.0", "373", "0.1418", "Data Mining -> Classification"),
    ("Q3", "Dijkstra", "1", "1.0",   "3", "0.0365", "Data Mining -> Classification"),
    ("Q3", "A*",       "1", "1.0",   "3", "0.0697", "Data Mining -> Classification"),
    ("Q4", "BFS",      "1", "1.5",  "17", "0.0039", "Classification -> Decision Tree"),
    ("Q4", "DFS",      "1", "1.5", "237", "0.0892", "Classification -> Decision Tree"),
    ("Q4", "Dijkstra", "1", "1.5",  "39", "0.0974", "Classification -> Decision Tree"),
    ("Q4", "A*",       "1", "1.5",   "2", "0.0483", "Classification -> Decision Tree"),
]

# Averages over Q1, Q3, Q4, Q6
# visited:  BFS=(128+5+74+17)/4=56.00  DFS=(144+62+373+237)/4=204.00
#           Dijkstra=(179+38+3+39)/4=64.75  A*=(150+38+3+2)/4=48.25
# time(ms): BFS=0.0100  DFS=0.0724  Dijkstra=0.1744  A*=0.2277
# path_len: (2+1+1+1)/4=1.25   cost: (2.0+1.0+1.0+1.5)/4=1.38
SUMMARY_ROWS = [
    ("BFS",      "1.25", "1.38",  "56.00", "0.0100"),
    ("DFS",      "1.25", "1.38", "204.00", "0.0724"),
    ("Dijkstra", "1.25", "1.38",  "64.75", "0.1744"),
    ("A*",       "1.25", "1.38",  "48.25", "0.2277"),
]


# ── academic table style ────────────────────────────────────────────────────────

def _set_h_border(position: str, sz: str = "12", color: str = "000000") -> OxmlElement:
    """Create and return a border element for the given edge."""
    el = OxmlElement(f"w:{position}")
    el.set(qn("w:val"),   "single")
    el.set(qn("w:sz"),    sz)
    el.set(qn("w:space"), "0")
    el.set(qn("w:color"), color)
    return el


def _make_tbl_borders(top=True, bottom=True, inside_h=True,
                      thick="12", thin="6") -> OxmlElement:
    """Return a w:tblBorders element with only horizontal lines."""
    borders = OxmlElement("w:tblBorders")
    # suppress vertical lines
    for edge in ("left", "right", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "none")
        borders.append(el)
    if top:
        borders.append(_set_h_border("top",     sz=thick))
    if bottom:
        borders.append(_set_h_border("bottom",  sz=thick))
    if inside_h:
        borders.append(_set_h_border("insideH", sz=thin))
    return borders


def _apply_tbl_borders(tbl) -> None:
    tbl_pr = tbl._tbl.tblPr
    if tbl_pr is None:
        tbl_pr = OxmlElement("w:tblPr")
        tbl._tbl.insert(0, tbl_pr)
    # remove existing borders element if present
    for existing in tbl_pr.findall(qn("w:tblBorders")):
        tbl_pr.remove(existing)
    tbl_pr.append(_make_tbl_borders())


def _clear_cell_borders(cell) -> None:
    """Remove all cell-level borders so table-level borders take effect."""
    tc_pr = cell._tc.get_or_add_tcPr()
    for existing in tc_pr.findall(qn("w:tcBorders")):
        tc_pr.remove(existing)
    tc_borders = OxmlElement("w:tcBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "none")
        tc_borders.append(el)
    tc_pr.append(tc_borders)


def _set_cell_text(cell, text: str, bold: bool = False,
                   underline: bool = False, size_pt: int = 10) -> None:
    """Clear cell and write one run with the requested formatting."""
    for para in cell.paragraphs:
        for run in para.runs:
            run.text = ""
    para = cell.paragraphs[0]
    run = para.add_run(text)
    run.bold      = bold
    run.underline = underline
    run.font.size = Pt(size_pt)


def _add_header_separator(tbl) -> None:
    """Draw a thicker bottom border on every cell in the header row."""
    for cell in tbl.rows[0].cells:
        tc_pr = cell._tc.get_or_add_tcPr()
        for existing in tc_pr.findall(qn("w:tcBorders")):
            tc_pr.remove(existing)
        tc_borders = OxmlElement("w:tcBorders")
        # suppress sides
        for edge in ("left", "right"):
            el = OxmlElement(f"w:{edge}")
            el.set(qn("w:val"), "none")
            tc_borders.append(el)
        # thick bottom line under header
        tc_borders.append(_set_h_border("bottom", sz="12"))
        # no top line on header cells (table top border handles it)
        top_el = OxmlElement("w:top")
        top_el.set(qn("w:val"), "none")
        tc_borders.append(top_el)
        tc_pr.append(tc_borders)


def _rank_in_column(values: list[float | None],
                    lower_is_better: bool) -> dict[int, int]:
    """Return {row_index: rank} where rank 1 = best, 2 = second-best."""
    indexed = [(v, i) for i, v in enumerate(values) if v is not None]
    indexed.sort(key=lambda x: x[0], reverse=(not lower_is_better))
    return {i: rank + 1 for rank, (_, i) in enumerate(indexed)}


def make_academic_table(document: Document,
                        headers: list[str],
                        rows: list[tuple],
                        metric_cols: list[int] | None = None,
                        lower_is_better: bool = True,
                        group_size: int | None = None,
                        font_pt: int = 10) -> None:
    """
    Build an academic-style table:
      - horizontal rules only (top thick, header sep thick, bottom thick, inside thin)
      - no cell background colours
      - bold = best value per metric column (per group if group_size set)
      - underline = second-best value per metric column
    """
    n_cols = len(headers)
    tbl = document.add_table(rows=1, cols=n_cols)
    tbl.style = "TableNormal"
    _apply_tbl_borders(tbl)

    # header row
    for i, hdr in enumerate(headers):
        cell = tbl.rows[0].cells[i]
        _clear_cell_borders(cell)
        _set_cell_text(cell, hdr, bold=True, size_pt=font_pt)
    _add_header_separator(tbl)

    # data rows
    for row in rows:
        cells = tbl.add_row().cells
        for i, val in enumerate(row):
            _clear_cell_borders(cells[i])
            _set_cell_text(cells[i], val, size_pt=font_pt)

    # apply bottom border to last row
    last_row = tbl.rows[-1]
    for cell in last_row.cells:
        tc_pr = cell._tc.get_or_add_tcPr()
        tc_borders = OxmlElement("w:tcBorders")
        for edge in ("left", "right", "top"):
            el = OxmlElement(f"w:{edge}")
            el.set(qn("w:val"), "none")
            tc_borders.append(el)
        tc_borders.append(_set_h_border("bottom", sz="12"))
        tc_pr.append(tc_borders)

    # bold/underline best and second-best
    if metric_cols:
        data_rows = tbl.rows[1:]
        n = len(data_rows)
        groups = (
            [range(i, min(i + group_size, n)) for i in range(0, n, group_size)]
            if group_size else [range(n)]
        )
        for col in metric_cols:
            for grp in groups:
                vals = []
                for ri in grp:
                    try:
                        vals.append(float(data_rows[ri].cells[col].text))
                    except ValueError:
                        vals.append(None)
                ranks = _rank_in_column(vals, lower_is_better)
                for ri, v in zip(grp, vals):
                    if v is None:
                        continue
                    rank = ranks[ri - grp.start]
                    cell = data_rows[ri].cells[col]
                    text = cell.paragraphs[0].text
                    if rank == 1:
                        _set_cell_text(cell, text, bold=True,
                                       underline=False, size_pt=font_pt)
                    elif rank == 2:
                        _set_cell_text(cell, text, bold=False,
                                       underline=True, size_pt=font_pt)

    return tbl


# ── chart generation ────────────────────────────────────────────────────────────

def _extract_per_query_data():
    queries = ["Q1", "Q2", "Q3", "Q4"]
    visited = {a: [] for a in ALGO_LABELS}
    times   = {a: [] for a in ALGO_LABELS}
    for q in queries:
        rows_q = [r for r in RESULT_ROWS if r[0] == q]
        for row in rows_q:
            algo = row[1]
            visited[algo].append(int(row[4]))
            times[algo].append(float(row[5]))
    return queries, visited, times


def _apply_chart_style(ax, title: str, ylabel: str) -> None:
    ax.set_title(title, fontsize=10, fontweight="bold", pad=8)
    ax.set_ylabel(ylabel, fontsize=9)
    ax.grid(axis="y", linestyle="--", alpha=0.35, color="#aaaaaa")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#cccccc")
    ax.spines["bottom"].set_color("#cccccc")
    ax.tick_params(colors="#333333", labelsize=8)


def make_chart_visited(tmp_dir: str) -> str:
    queries, visited, _ = _extract_per_query_data()
    x = np.arange(len(queries))
    width = 0.19
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    fig.patch.set_facecolor("white")
    for i, (algo, color) in enumerate(zip(ALGO_LABELS, ALGO_COLORS)):
        bars = ax.bar(x + i * width, visited[algo], width, label=algo,
                      color=color, alpha=0.88, edgecolor="white", linewidth=0.6)
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, h + 1.5,
                    str(int(h)), ha="center", va="bottom", fontsize=6,
                    color="#333333")
    ax.set_xticks(x + width * 1.5)
    ax.set_xticklabels(queries, fontsize=9)
    ax.legend(fontsize=8, loc="upper right", framealpha=0.7,
              edgecolor="#cccccc")
    _apply_chart_style(ax, "Figure 1: Nodes Visited per Query", "Nodes Visited")
    plt.tight_layout()
    path = str(Path(tmp_dir) / "chart_visited.png")
    plt.savefig(path, dpi=160, facecolor="white")
    plt.close()
    return path


def make_chart_runtime(tmp_dir: str) -> str:
    queries, _, times = _extract_per_query_data()
    x = np.arange(len(queries))
    width = 0.19
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    fig.patch.set_facecolor("white")
    for i, (algo, color) in enumerate(zip(ALGO_LABELS, ALGO_COLORS)):
        bars = ax.bar(x + i * width, times[algo], width, label=algo,
                      color=color, alpha=0.88, edgecolor="white", linewidth=0.6)
        for bar in bars:
            h = bar.get_height()
            if h >= 0.01:
                ax.text(bar.get_x() + bar.get_width() / 2, h + 0.004,
                        f"{h:.3f}", ha="center", va="bottom", fontsize=5.5,
                        rotation=40, color="#333333")
    ax.set_xticks(x + width * 1.5)
    ax.set_xticklabels(queries, fontsize=9)
    ax.legend(fontsize=8, loc="upper right", framealpha=0.7,
              edgecolor="#cccccc")
    _apply_chart_style(ax, "Figure 2: Average Runtime per Query (ms)", "Avg. Time (ms)")
    plt.tight_layout()
    path = str(Path(tmp_dir) / "chart_runtime.png")
    plt.savefig(path, dpi=160, facecolor="white")
    plt.close()
    return path


def make_chart_summary(tmp_dir: str) -> str:
    algos    = [r[0] for r in SUMMARY_ROWS]
    visited  = [float(r[3]) for r in SUMMARY_ROWS]
    runtimes = [float(r[4]) for r in SUMMARY_ROWS]
    colors   = ALGO_COLORS

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.5, 3.0))
    fig.patch.set_facecolor("white")

    for ax, vals, xlabel, title in [
        (ax1, visited,  "Avg. Visited Nodes", "Avg. Nodes Visited"),
        (ax2, runtimes, "Avg. Time (ms)",      "Avg. Runtime (ms)"),
    ]:
        bars = ax.barh(algos, vals, color=colors, alpha=0.88,
                       edgecolor="white", linewidth=0.6)
        ax.invert_yaxis()
        ax.set_xlabel(xlabel, fontsize=9)
        ax.set_title(title, fontsize=9, fontweight="bold", pad=6)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_color("#cccccc")
        ax.spines["bottom"].set_color("#cccccc")
        ax.grid(axis="x", linestyle="--", alpha=0.35, color="#aaaaaa")
        ax.tick_params(colors="#333333", labelsize=8)
        for bar, v in zip(bars, vals):
            label = f"{v:.4f}" if v < 1 else f"{v:.2f}"
            ax.text(bar.get_width() + max(vals) * 0.02,
                    bar.get_y() + bar.get_height() / 2,
                    label, va="center", fontsize=8, color="#333333")

    fig.suptitle("Figure 3: Summary Comparison across All Queries",
                 fontsize=10, fontweight="bold", y=1.02)
    plt.tight_layout()
    path = str(Path(tmp_dir) / "chart_summary.png")
    plt.savefig(path, dpi=160, facecolor="white", bbox_inches="tight")
    plt.close()
    return path


# ── document building ───────────────────────────────────────────────────────────

def main() -> None:
    document = Document(DOCX_PATH)
    body = document._body._element

    start_paragraph = find_paragraph(document, "5. Experiments and Results")
    end_paragraph   = find_paragraph(document, "6. Discussion")
    remove_between(body, start_paragraph._element, end_paragraph._element)

    inserted: list = []

    def para(text: str = "", bold: bool = False, italic: bool = False,
             size_pt: int = 11) -> None:
        p = document.add_paragraph()
        run = p.add_run(text)
        run.bold      = bold
        run.italic    = italic
        run.font.size = Pt(size_pt)
        inserted.append(p._element)

    def tbl(headers, rows, metric_cols=None, lower_is_better=True,
            group_size=None, font_pt=10):
        t = make_academic_table(document, headers, rows, metric_cols,
                                lower_is_better, group_size, font_pt)
        inserted.append(t._element)

    def img(path: str, width_inches: float = 6.2) -> None:
        from docx.enum.text import WD_ALIGN_PARAGRAPH
        p = document.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(path, width=Inches(width_inches))
        inserted.append(p._element)

    with tempfile.TemporaryDirectory() as tmp:
        cv = make_chart_visited(tmp)
        cr = make_chart_runtime(tmp)
        cs = make_chart_summary(tmp)
        build_section(para, tbl, img, cv, cr, cs)

    insert_index = list(body).index(end_paragraph._element)
    for offset, element in enumerate(inserted):
        body.insert(insert_index + offset, element)

    document.save(DOCX_PATH)
    print(f"Updated {DOCX_PATH}")


def build_section(para, tbl, img, chart_visited, chart_runtime, chart_summary) -> None:
    para("5. Experiments and Results", bold=True)
    para(
        "This section evaluates the proposed KGQA prototype by running the "
        "same relationship questions through BFS, DFS, Dijkstra, and A*. The "
        "experiment focuses on retrieval behavior, path cost, search effort, "
        "and the explainability of the returned graph paths."
    )

    # 5.1
    para("5.1 Experimental Setup", bold=True)
    para(
        "The experiment was conducted on the pruned CSO subgraph stored in "
        "data/processed/subgraph_data_science.json. The graph contains 554 "
        "concept nodes and 1,448 directed typed edges (1,035 superTopicOf "
        "with weight 1.0 and 413 contributesTo with weight 1.5). "
        "The maximum recorded ontology depth is 5. Each algorithm was repeated "
        "20 times per query to obtain stable average runtimes."
    )
    tbl(
        ["Property", "Value"],
        [
            ("Raw data file",      "data/raw/CSO.3.5.csv"),
            ("Processed graph",    "data/processed/subgraph_data_science.json"),
            ("Root branch",        "data_mining"),
            ("Nodes",              "554"),
            ("Edges",              "1,448"),
            ("Maximum depth",      "5"),
            ("Depth distribution", "0:1, 1:38, 2:167, 3:205, 4:107, 5:36"),
            ("Edge types",         "1,035 superTopicOf + 413 contributesTo"),
            ("Edge weights",       "superTopicOf = 1.0, contributesTo = 1.5"),
            ("Environment",        "Python 3.11, NetworkX 3.6.1"),
            ("Repeated runs",      "20 runs per algorithm per query"),
        ],
    )

    # 5.2
    para("5.2 Test Queries", bold=True)
    para(
        "Four representative queries were selected to cover the three "
        "structurally distinct cases present in the graph: a two-hop "
        "superTopicOf path (Q1), a minimal one-hop superTopicOf path (Q3), "
        "a one-hop path with a high DFS node-visit count (Q4), and a one-hop "
        "contributesTo edge with weight 1.5 (Q6)."
    )
    tbl(
        ["ID", "Question", "Source", "Target", "Reference path"],
        TEST_QUERIES,
    )

    # 5.3
    para("5.3 Evaluation Metrics", bold=True)
    para(
        "Four quantitative metrics are reported: (1) Path length — number of "
        "edges in the returned path; (2) Total cost — sum of edge weights along "
        "the path; (3) Nodes visited — graph nodes explored before the target "
        "is reached; (4) Avg. runtime — mean execution time in milliseconds "
        "over 20 repeated runs. Arrows in table headers indicate the preferred "
        "direction (↓ lower is better)."
    )

    # 5.4
    para("5.4 Algorithm Comparison", bold=True)
    para(
        "All four algorithms found a valid path for every query. Bold values "
        "indicate the best result per metric within each query group; underlined "
        "values indicate the second-best. BFS is fastest overall. DFS is "
        "sensitive to successor ordering and visits many nodes on some queries. "
        "Dijkstra guarantees minimum-cost paths. A* reduces visited nodes "
        "versus Dijkstra, though heuristic overhead raises its runtime on this "
        "small graph."
    )
    tbl(
        ["Query", "Algorithm", "Path len ↓", "Cost ↓", "Visited ↓", "Avg. ms ↓", "Path"],
        RESULT_ROWS,
        metric_cols=[4, 5],
        lower_is_better=True,
        group_size=4,
    )
    para("Figure 1 shows nodes visited per query; Figure 2 shows runtime per query.",
         italic=True, size_pt=9)
    img(chart_visited)
    img(chart_runtime)

    # 5.5
    para("5.5 Summary", bold=True)
    para(
        "The table below aggregates averages across all seven queries. "
        "Bold = best; underlined = second-best per column."
    )
    tbl(
        ["Algorithm", "Avg. path len ↓", "Avg. cost ↓",
         "Avg. visited ↓", "Avg. ms ↓"],
        SUMMARY_ROWS,
        metric_cols=[2, 3, 4],
        lower_is_better=True,
    )
    para("Figure 3 compares average visited nodes and average runtime for all algorithms.",
         italic=True, size_pt=9)
    img(chart_summary)
    para(
        "BFS achieved the lowest mean runtime (0.0100 ms) and a low search "
        "effort (56.00 nodes on average). DFS explored the most nodes on "
        "average (204.00), driven by the 373-node traversal on Q4. Dijkstra "
        "maintained the minimum-cost guarantee at 64.75 visited nodes on "
        "average. A* achieved the smallest average node count (48.25) but its "
        "runtime (0.2277 ms) exceeded Dijkstra’s owing to heuristic overhead "
        "on this small graph."
    )

    # 5.6
    para("5.6 Case Studies", bold=True)
    para(
        "Case study 1 — ‘How is Data Mining related to Random Forests?’ "
        "All four algorithms returned the same two-hop path: "
        "Data Mining → Decision Tree → Random Forests. Both edges are "
        "superTopicOf relations (weight 1.0, total cost 2.0). The path is "
        "meaningful because Decision Tree is a well-established intermediate "
        "concept linking Data Mining to the ensemble method Random Forests."
    )
    para(
        "Case study 2 — ‘How is Classification related to Decision Tree?’ "
        "The returned path is the direct one-hop relation "
        "Classification → Decision Tree via a contributesTo edge (weight 1.5). "
        "This demonstrates that the weighted graph correctly distinguishes a "
        "contribution relation from a strict hierarchical superTopicOf edge, "
        "while still producing an explainable one-sentence answer."
    )
    para(
        "Overall, classical graph algorithms are sufficient for lightweight "
        "explainable KGQA on academic ontology subgraphs. BFS is the most "
        "efficient baseline; Dijkstra is preferred when weighted semantic "
        "distance matters; A* becomes advantageous on larger graphs where "
        "the depth heuristic yields a meaningful reduction in search space."
    )


# ── utilities ───────────────────────────────────────────────────────────────────

def find_paragraph(document: Document, text: str):
    for p in document.paragraphs:
        if p.text.strip() == text:
            return p
    raise ValueError(f"Paragraph not found: {text!r}")


def remove_between(body, start_el, end_el) -> None:
    children = list(body)
    start = children.index(start_el)
    end   = children.index(end_el)
    for el in children[start:end]:
        body.remove(el)


if __name__ == "__main__":
    main()
