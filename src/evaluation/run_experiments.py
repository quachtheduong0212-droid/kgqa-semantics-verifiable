"""Run algorithm comparisons for the paper's experiments section."""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from pathlib import Path

import networkx as nx

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from src.qa import KGQAEngine


DEFAULT_GRAPH = Path("data/processed/subgraph_data_science.json")
ALGORITHMS = ("bfs", "dfs", "dijkstra", "astar")
QUESTIONS = (
    "How is Data Mining related to Random Forests?",
    "How is Data Mining related to Text Mining?",
    "How is Data Mining related to Web Mining?",
    "How is Data Mining related to Classification?",
    "How is Classification related to Support Vector Machines?",
    "How is Classification related to Decision Tree?",
    "How is Clustering related to K-Means Clustering Method?",
)


def main() -> None:
    args = parse_args()
    graph = load_graph(args.graph)
    engine = KGQAEngine(graph)

    print(f"Graph: {args.graph}")
    print(f"Nodes: {graph.number_of_nodes()}")
    print(f"Edges: {graph.number_of_edges()}")
    print(f"Runs per algorithm/query: {args.runs}")
    print()

    for query_index, question in enumerate(QUESTIONS, start=1):
        print(f"Query {query_index}: {question}")
        for algorithm in ALGORITHMS:
            runs = [engine.answer(question, algorithm) for _ in range(args.runs)]
            first = runs[0]
            time_values = [run["time_ms"] for run in runs]
            path = first["path"] or []
            path_length = max(len(path) - 1, 0)
            avg_time = statistics.mean(time_values)

            print(
                f"{algorithm.upper():8} | "
                f"path_len={path_length:<2} | "
                f"cost={first['cost']:<5} | "
                f"visited={first['nodes_visited']:<4} | "
                f"avg_ms={avg_time:.4f} | "
                f"direction={first['direction']:<7} | "
                f"path={first['path_text']}"
            )
        print()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run KGQA algorithm experiments.")
    parser.add_argument("--graph", default=DEFAULT_GRAPH, type=Path)
    parser.add_argument("--runs", default=20, type=int)
    return parser.parse_args()


def load_graph(path: Path) -> nx.DiGraph:
    with path.open("r", encoding="utf-8") as file:
        return nx.node_link_graph(json.load(file))


if __name__ == "__main__":
    main()
