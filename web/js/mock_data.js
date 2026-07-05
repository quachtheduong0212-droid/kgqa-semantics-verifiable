/**
 * Mock data for demo mode.
 *
 * When the Flask backend is not reachable the frontend falls back to these
 * objects so the UI can still be demonstrated and developed independently.
 */

const MOCK_QUERY_RESULTS = {
  "how is data mining related to random forests": {
    question: "How is Data Mining related to Random Forests?",
    source: "data_mining",
    target: "random_forests",
    algorithm: "dijkstra",
    direction: "forward",
    answer:
      "Data Mining is a broader topic that includes Decision Tree. Decision Tree is a broader topic that includes Random Forests.",
    path: ["data_mining", "decision_tree", "random_forests"],
    path_labels: ["Data Mining", "Decision Tree", "Random Forests"],
    path_edges: [
      { from: "data_mining", to: "decision_tree", type: "superTopicOf", weight: 1.0 },
      { from: "decision_tree", to: "random_forests", type: "superTopicOf", weight: 1.0 },
    ],
    cost: 2.0,
    nodes_visited: 12,
    time_ms: 0.142,
  },
  "how is machine learning related to deep learning": {
    question: "How is Machine Learning related to Deep Learning?",
    source: "machine_learning",
    target: "deep_learning",
    algorithm: "dijkstra",
    direction: "forward",
    answer:
      "Machine Learning is a broader topic that includes Neural Networks. Neural Networks is a broader topic that includes Deep Learning.",
    path: ["machine_learning", "neural_networks", "deep_learning"],
    path_labels: ["Machine Learning", "Neural Networks", "Deep Learning"],
    path_edges: [
      { from: "machine_learning", to: "neural_networks", type: "superTopicOf", weight: 1.0 },
      { from: "neural_networks", to: "deep_learning", type: "superTopicOf", weight: 1.0 },
    ],
    cost: 2.0,
    nodes_visited: 15,
    time_ms: 0.189,
  },
  "how is data mining related to classification": {
    question: "How is Data Mining related to Classification?",
    source: "data_mining",
    target: "classification",
    algorithm: "dijkstra",
    direction: "forward",
    answer: "Data Mining is a broader topic that includes Classification.",
    path: ["data_mining", "classification"],
    path_labels: ["Data Mining", "Classification"],
    path_edges: [
      { from: "data_mining", to: "classification", type: "superTopicOf", weight: 1.0 },
    ],
    cost: 1.0,
    nodes_visited: 5,
    time_ms: 0.067,
  },
};

const MOCK_COMPARE_RESULTS = {
  "how is data mining related to random forests": {
    question: "How is Data Mining related to Random Forests?",
    source: "data_mining",
    target: "random_forests",
    results: [
      {
        algorithm: "bfs",
        path: ["data_mining", "decision_tree", "random_forests"],
        path_labels: ["Data Mining", "Decision Tree", "Random Forests"],
        cost: 2.0,
        nodes_visited: 8,
        time_ms: 0.098,
        direction: "forward",
        answer:
          "Data Mining is a broader topic that includes Decision Tree. Decision Tree is a broader topic that includes Random Forests.",
      },
      {
        algorithm: "dfs",
        path: [
          "data_mining",
          "knowledge_discovery",
          "pattern_recognition",
          "decision_tree",
          "random_forests",
        ],
        path_labels: [
          "Data Mining",
          "Knowledge Discovery",
          "Pattern Recognition",
          "Decision Tree",
          "Random Forests",
        ],
        cost: 4.5,
        nodes_visited: 23,
        time_ms: 0.112,
        direction: "forward",
        answer:
          "Data Mining is a broader topic that includes Knowledge Discovery. Knowledge Discovery contributes to Pattern Recognition. Pattern Recognition is a broader topic that includes Decision Tree. Decision Tree is a broader topic that includes Random Forests.",
      },
      {
        algorithm: "dijkstra",
        path: ["data_mining", "decision_tree", "random_forests"],
        path_labels: ["Data Mining", "Decision Tree", "Random Forests"],
        cost: 2.0,
        nodes_visited: 12,
        time_ms: 0.142,
        direction: "forward",
        answer:
          "Data Mining is a broader topic that includes Decision Tree. Decision Tree is a broader topic that includes Random Forests.",
      },
      {
        algorithm: "astar",
        path: ["data_mining", "decision_tree", "random_forests"],
        path_labels: ["Data Mining", "Decision Tree", "Random Forests"],
        cost: 2.0,
        nodes_visited: 7,
        time_ms: 0.203,
        direction: "forward",
        answer:
          "Data Mining is a broader topic that includes Decision Tree. Decision Tree is a broader topic that includes Random Forests.",
      },
    ],
  },
  "how is machine learning related to deep learning": {
    question: "How is Machine Learning related to Deep Learning?",
    source: "machine_learning",
    target: "deep_learning",
    results: [
      {
        algorithm: "bfs",
        path: ["machine_learning", "neural_networks", "deep_learning"],
        path_labels: ["Machine Learning", "Neural Networks", "Deep Learning"],
        cost: 2.0,
        nodes_visited: 10,
        time_ms: 0.105,
        direction: "forward",
        answer:
          "Machine Learning is a broader topic that includes Neural Networks. Neural Networks is a broader topic that includes Deep Learning.",
      },
      {
        algorithm: "dfs",
        path: [
          "machine_learning",
          "supervised_learning",
          "neural_networks",
          "deep_learning",
        ],
        path_labels: [
          "Machine Learning",
          "Supervised Learning",
          "Neural Networks",
          "Deep Learning",
        ],
        cost: 3.0,
        nodes_visited: 18,
        time_ms: 0.131,
        direction: "forward",
        answer:
          "Machine Learning is a broader topic that includes Supervised Learning. Supervised Learning is a broader topic that includes Neural Networks. Neural Networks is a broader topic that includes Deep Learning.",
      },
      {
        algorithm: "dijkstra",
        path: ["machine_learning", "neural_networks", "deep_learning"],
        path_labels: ["Machine Learning", "Neural Networks", "Deep Learning"],
        cost: 2.0,
        nodes_visited: 15,
        time_ms: 0.189,
        direction: "forward",
        answer:
          "Machine Learning is a broader topic that includes Neural Networks. Neural Networks is a broader topic that includes Deep Learning.",
      },
      {
        algorithm: "astar",
        path: ["machine_learning", "neural_networks", "deep_learning"],
        path_labels: ["Machine Learning", "Neural Networks", "Deep Learning"],
        cost: 2.0,
        nodes_visited: 9,
        time_ms: 0.215,
        direction: "forward",
        answer:
          "Machine Learning is a broader topic that includes Neural Networks. Neural Networks is a broader topic that includes Deep Learning.",
      },
    ],
  },
};

const MOCK_NEIGHBORS = {
  random_forests: {
    concept: "random_forests",
    label: "Random Forests",
    neighbors: [
      { id: "decision_tree", label: "Decision Tree", edge_type: "superTopicOf", direction: "parent" },
      { id: "ensemble_methods", label: "Ensemble Methods", edge_type: "contributesTo", direction: "outgoing" },
      { id: "classification", label: "Classification", edge_type: "contributesTo", direction: "outgoing" },
      { id: "bagging", label: "Bagging", edge_type: "superTopicOf", direction: "child" },
    ],
  },
  decision_tree: {
    concept: "decision_tree",
    label: "Decision Tree",
    neighbors: [
      { id: "data_mining", label: "Data Mining", edge_type: "superTopicOf", direction: "parent" },
      { id: "random_forests", label: "Random Forests", edge_type: "superTopicOf", direction: "child" },
      { id: "classification", label: "Classification", edge_type: "contributesTo", direction: "outgoing" },
      { id: "regression", label: "Regression", edge_type: "contributesTo", direction: "outgoing" },
    ],
  },
  data_mining: {
    concept: "data_mining",
    label: "Data Mining",
    neighbors: [
      { id: "decision_tree", label: "Decision Tree", edge_type: "superTopicOf", direction: "child" },
      { id: "classification", label: "Classification", edge_type: "superTopicOf", direction: "child" },
      { id: "clustering", label: "Clustering", edge_type: "superTopicOf", direction: "child" },
      { id: "association_rules", label: "Association Rules", edge_type: "superTopicOf", direction: "child" },
      { id: "knowledge_discovery", label: "Knowledge Discovery", edge_type: "superTopicOf", direction: "child" },
      { id: "feature_selection", label: "Feature Selection", edge_type: "superTopicOf", direction: "child" },
    ],
  },
  deep_learning: {
    concept: "deep_learning",
    label: "Deep Learning",
    neighbors: [
      { id: "neural_networks", label: "Neural Networks", edge_type: "superTopicOf", direction: "parent" },
      { id: "convolutional_neural_networks", label: "Convolutional Neural Networks", edge_type: "superTopicOf", direction: "child" },
      { id: "recurrent_neural_networks", label: "Recurrent Neural Networks", edge_type: "superTopicOf", direction: "child" },
      { id: "transfer_learning", label: "Transfer Learning", edge_type: "contributesTo", direction: "outgoing" },
    ],
  },
  neural_networks: {
    concept: "neural_networks",
    label: "Neural Networks",
    neighbors: [
      { id: "machine_learning", label: "Machine Learning", edge_type: "superTopicOf", direction: "parent" },
      { id: "deep_learning", label: "Deep Learning", edge_type: "superTopicOf", direction: "child" },
      { id: "backpropagation", label: "Backpropagation", edge_type: "superTopicOf", direction: "child" },
    ],
  },
  machine_learning: {
    concept: "machine_learning",
    label: "Machine Learning",
    neighbors: [
      { id: "neural_networks", label: "Neural Networks", edge_type: "superTopicOf", direction: "child" },
      { id: "supervised_learning", label: "Supervised Learning", edge_type: "superTopicOf", direction: "child" },
      { id: "unsupervised_learning", label: "Unsupervised Learning", edge_type: "superTopicOf", direction: "child" },
      { id: "reinforcement_learning", label: "Reinforcement Learning", edge_type: "superTopicOf", direction: "child" },
      { id: "feature_engineering", label: "Feature Engineering", edge_type: "contributesTo", direction: "outgoing" },
    ],
  },
};

const MOCK_GRAPH_INFO = {
  source: "CSO v3.5 (pruned subgraph)",
  root_concept: "data_mining",
  num_nodes: 142,
  num_edges: 198,
  edge_types: { superTopicOf: 165, contributesTo: 33 },
};
