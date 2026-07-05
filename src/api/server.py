"""Flask web server for the Explainable KGQA prototype.

Wraps the existing KGQAEngine and exposes a REST API consumed by the
single-page frontend in ``web/``.

Usage::

    .venv/Scripts/python -m src.api.server
    .venv/Scripts/python -m src.api.server --graph data/processed/subgraph_ai.json
"""

import argparse
import os
import sys

# Ensure the project root is on sys.path so ``src.*`` imports work when
# running this file as ``python -m src.api.server`` from the project root.
_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from src.qa import KGQAEngine

# ------------------------------------------------------------------ #
#  Defaults                                                            #
# ------------------------------------------------------------------ #
DEFAULT_GRAPH = os.path.join(_PROJECT_ROOT, "data", "processed", "subgraph_data_science.json")
WEB_DIR = os.path.join(_PROJECT_ROOT, "web")

# ------------------------------------------------------------------ #
#  App factory                                                         #
# ------------------------------------------------------------------ #

def create_app(graph_path=None):
    """Create and configure the Flask application."""
    graph_path = graph_path or DEFAULT_GRAPH

    if not os.path.exists(graph_path):
        raise FileNotFoundError(
            f"Graph file not found: {graph_path}. "
            "Build a pruned graph first with src/graph_pruner.py."
        )

    engine = KGQAEngine.from_json(graph_path)
    graph = engine.graph

    app = Flask(__name__, static_folder=WEB_DIR, static_url_path="")
    CORS(app)

    # ----- Static frontend -----

    @app.route("/")
    def index():
        return send_from_directory(WEB_DIR, "index.html")

    # ----- API endpoints -----

    @app.route("/api/query")
    def api_query():
        question = request.args.get("q", "").strip()
        algorithm = request.args.get("algorithm", "dijkstra").strip().lower()

        if not question:
            return jsonify({"error": "Missing required parameter: q"}), 400

        try:
            result = engine.answer(question, algorithm)
        except ValueError as exc:
            return jsonify({"error": str(exc)}), 400

        # Enrich with path_labels and path_edges for the frontend.
        path = result.get("path") or []
        path_labels = [graph.nodes[n].get("label", n.replace("_", " ").title()) for n in path]
        path_edges = []
        for src, tgt in zip(path, path[1:]):
            edge = graph.get_edge_data(src, tgt, default={})
            path_edges.append({
                "from": src,
                "to": tgt,
                "type": edge.get("type", "relatedTo"),
                "weight": edge.get("weight", 1.0),
            })

        return jsonify({
            "question": result["question"],
            "source": result["source"],
            "target": result["target"],
            "algorithm": result["algorithm"],
            "direction": result["direction"],
            "answer": result["answer"],
            "path": path,
            "path_labels": path_labels,
            "path_edges": path_edges,
            "cost": result["cost"],
            "nodes_visited": result["nodes_visited"],
            "time_ms": result["time_ms"],
        })

    @app.route("/api/compare")
    def api_compare():
        question = request.args.get("q", "").strip()
        if not question:
            return jsonify({"error": "Missing required parameter: q"}), 400

        algorithms = ["bfs", "dfs", "dijkstra", "astar"]
        results = []

        # Parse once to detect errors early.
        try:
            parsed = engine.parser.parse(question)
        except ValueError as exc:
            return jsonify({"error": str(exc)}), 400

        source_display = parsed["source"]
        target_display = parsed["target"]

        for algo in algorithms:
            try:
                r = engine.answer(question, algo)
                path = r.get("path") or []
                path_labels = [
                    graph.nodes[n].get("label", n.replace("_", " ").title()) for n in path
                ]
                results.append({
                    "algorithm": algo,
                    "path": path,
                    "path_labels": path_labels,
                    "cost": r["cost"],
                    "nodes_visited": r["nodes_visited"],
                    "time_ms": r["time_ms"],
                    "direction": r["direction"],
                    "answer": r["answer"],
                })
            except ValueError:
                results.append({
                    "algorithm": algo,
                    "path": [],
                    "path_labels": [],
                    "cost": float("inf"),
                    "nodes_visited": 0,
                    "time_ms": 0,
                    "direction": "n/a",
                    "answer": "Error running this algorithm.",
                })

        return jsonify({
            "question": question,
            "source": source_display,
            "target": target_display,
            "results": results,
        })

    @app.route("/api/neighbors")
    def api_neighbors():
        concept = request.args.get("concept", "").strip().lower().replace(" ", "_")
        if not concept:
            return jsonify({"error": "Missing required parameter: concept"}), 400

        if concept not in graph:
            return jsonify({"concept": concept, "label": concept, "neighbors": []})

        label = graph.nodes[concept].get("label", concept.replace("_", " ").title())
        neighbors = []

        # Parents (predecessors)
        for pred in graph.predecessors(concept):
            edge = graph.get_edge_data(pred, concept, default={})
            neighbors.append({
                "id": pred,
                "label": graph.nodes[pred].get("label", pred.replace("_", " ").title()),
                "edge_type": edge.get("type", "relatedTo"),
                "direction": "parent",
            })

        # Children (successors)
        for succ in graph.successors(concept):
            edge = graph.get_edge_data(concept, succ, default={})
            direction = "child" if edge.get("type") == "superTopicOf" else "outgoing"
            neighbors.append({
                "id": succ,
                "label": graph.nodes[succ].get("label", succ.replace("_", " ").title()),
                "edge_type": edge.get("type", "relatedTo"),
                "direction": direction,
            })

        return jsonify({
            "concept": concept,
            "label": label,
            "neighbors": neighbors,
        })

    @app.route("/api/graph-info")
    def api_graph_info():
        edge_types = {}
        for _, _, data in graph.edges(data=True):
            t = data.get("type", "unknown")
            edge_types[t] = edge_types.get(t, 0) + 1

        # Try to find root concept from node attributes.
        root_concept = None
        for node, data in graph.nodes(data=True):
            if data.get("depth", -1) == 0:
                root_concept = node
                break

        return jsonify({
            "source": "CSO v3.5 (pruned subgraph)",
            "root_concept": root_concept,
            "num_nodes": graph.number_of_nodes(),
            "num_edges": graph.number_of_edges(),
            "edge_types": edge_types,
        })

    return app


# ------------------------------------------------------------------ #
#  CLI entry point                                                     #
# ------------------------------------------------------------------ #

def main():
    parser = argparse.ArgumentParser(description="Run the KGQA web UI server.")
    parser.add_argument(
        "--graph",
        default=DEFAULT_GRAPH,
        help="Path to a pruned graph JSON file.",
    )
    parser.add_argument("--port", type=int, default=5000, help="Port to run on.")
    parser.add_argument("--debug", action="store_true", help="Enable Flask debug mode.")
    args = parser.parse_args()

    app = create_app(args.graph)
    print(f"\n  Concept Path Explorer running at http://localhost:{args.port}\n")
    app.run(host="0.0.0.0", port=args.port, debug=args.debug)


if __name__ == "__main__":
    main()
