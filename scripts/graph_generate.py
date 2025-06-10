from src.graph import Graph
from src.graph_methods import random_graph
from src.io import save_graph, load_graph

if __name__ == '__main__':
    num_nodes = 10_000
    deg = 20
    method = 'geometric'
    graph = random_graph(num_nodes=num_nodes,
                         deg=deg,
                         method=method)
    filename = 'rg_n' + str(num_nodes) + '_d' + str(deg) + '_' + method[0] + '.pkl'
    save_graph(graph=graph, filename=filename)
    loaded_graph = load_graph(filename)

