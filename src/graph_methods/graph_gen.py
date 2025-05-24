import numpy as np

from src.graph import Graph
from src.tools.mathtools import bernoulli_sample
from src.tools.mathtools import sample_edge_count


def random_graph(num_nodes: int, p: float, method: str= 'naive', directed: bool=False) -> Graph:
    """
    Random graph is a graph where generation of edges subject to a Bernoulli variable.

    :param num_nodes: the number of nodes in the graph.
    :param p: parameter of the Bernoulli variable; the probability of generating edges.
    :param method: the method to use for generating edges, either 'naive' or 'two-step'. If naive method is used, each pair of nodes will be attempted. If two-step is used, an edge count will be sampled, first, and then edge is generated uniformly.
    :param directed: whether the graph is directed or undirected.
    """

    if num_nodes <= 1:
        raise ValueError('Number of nodes must be greater than 1.')

    if p < 0 or p > 1:
        raise ValueError('Probability of edge generation must be between 0 and 1.')

    network = Graph(num_nodes, directed=directed)

    if method == 'naive':
        for i in range(num_nodes):
            for j in range(i):
                if bernoulli_sample(p=p) == 1:
                    network.add_edge(i, j)

    elif method == 'two-step':
        edge_count = sample_edge_count(num_nodes=num_nodes, p=p)
        attempts = 0
        while attempts < edge_count:
            i = np.random.randint(num_nodes)
            j = np.random.randint(num_nodes)
            if not (i == j or network.adj[i, j] == 1):
                network.add_edge(i, j)
                attempts += 1

    else:
        raise Exception("method {} is not implemented.".format(method))

    return network