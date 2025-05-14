import numpy as np

def bernoulli_sample(p: float) -> int:
    """
    Returns a sample from a bernoulli distribution.
    :param p: parameter (probability) of the distribution.
    :return: an integer of 0 or 1.
    """
    return 1 if np.random.rand() < p else 0


def sample_edge_count(num_nodes: int, p: float) -> int:
    """
    Sample an edge count for a given graph according to binomial distribution.
    :param num_nodes: number of nodes of the graph.
    :param p: probability of generation of an edge.
    :return: an integer of edge count.
    """

    n = num_nodes * (num_nodes - 1) / 2
    return np.random.binomial(n, p)