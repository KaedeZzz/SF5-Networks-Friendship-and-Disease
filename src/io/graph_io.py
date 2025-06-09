import pickle
from pathlib import Path
from src.graph import Graph

base_dir = Path(__file__).parent.parent.parent
save_dir = base_dir / 'saved_graphs'

def save_graph(graph: Graph, filename: str) -> None:
    path = base_dir / 'saved_graphs' / filename
    with open(path, 'wb') as f:
        pickle.dump(graph.adj, f)

def load_graph(filename: str) -> Graph:
    path = base_dir / 'saved_graphs' / filename
    with open(path, 'rb') as f:
        adj = pickle.load(f)
    num_nodes = len(adj)
    graph = Graph(num_nodes)
    graph.adj = adj
    return graph