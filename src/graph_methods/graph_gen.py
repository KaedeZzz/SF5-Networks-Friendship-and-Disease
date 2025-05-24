import numpy as np

from src.graph import Graph
from src.tools import *

def edge_list_from_degrees(num_nodes: int, deg: float, dist: str) -> np.ndarray:
    """
    Generates a list of edges by matching each node with the degree distribution.
    :param num_nodes: number of nodes of the graph.
    :param deg: mean degree of each node.
    :param dist: the type of degree distribution to use.
    :return: a list of dimension (something, 2) representing all pairs of edges of the graph.
    """

    if dist == 'geometric':
        p_geom = 1 / deg
        samples = [geometric_sample(p=p_geom) for _ in range(num_nodes)]
    else:
        raise Exception(f'Distribution {dist} not supported.')

    index = np.array([i for i in range(num_nodes) for _ in range(samples[i])])
    index = np.random.permutation(index)
    if len(index) % 2 == 1:
        index = index[:-1]
    index = np.reshape(index, (-1, 2))

    return index


def random_graph(num_nodes: int, p: float = 0.0, deg: float = 0.0, method: str = 'naive', directed: bool = False) -> Graph:
    """
    Random graph is a graph where generation of edges subject to a Bernoulli variable.

    :param num_nodes: the number of nodes in the graph.
    :param p: parameter of the Bernoulli variable; the probability of generating edges. Used with 'naive' and 'two-step' methods.
    :param deg: mean degree of nodes of the graph. Used with 'geometric' method.
    :param method: the method to use for generating edges, either 'naive' or 'two-step'. If naive method is used, each pair of nodes will be attempted. If two-step is used, an edge count will be sampled, first, and then edge is generated uniformly.
    :param directed: whether the graph is directed or undirected.
    """

    if num_nodes <= 1:
        raise ValueError('Number of nodes must be greater than 1.')

    if p < 0 or p > 1:
        raise ValueError('Probability of edge generation must be between 0 and 1.')


    graph = Graph(num_nodes, directed=directed)

    if method == 'naive':
        for i in range(num_nodes):
            for j in range(i):
                if bernoulli_sample(p=p) == 1:
                    graph.add_edge(i, j)

    elif method == 'two-step':
        edge_count = sample_edge_count(num_nodes=num_nodes, p=p)
        attempts = 0
        while attempts < edge_count:
            i = np.random.randint(num_nodes)
            j = np.random.randint(num_nodes)
            if not (i == j or graph.adj[i, j] == 1):
                graph.add_edge(i, j)
                attempts += 1

    elif method == 'geometric':
        edge_list = edge_list_from_degrees(num_nodes, deg, 'geometric')
        for edge in edge_list:
            graph.add_edge(*edge)

    else:
        raise Exception(f'Method {method} is not supported.')

    return graph