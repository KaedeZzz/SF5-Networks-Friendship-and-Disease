import numpy as np

def bernoulli_sample(p: float) -> int:
    """
    Returns a sample from a bernoulli distribution.
    :param p: parameter (probability) of the distribution.
    :return: an integer of 0 or 1.
    """
    if p < 0 or p > 1:
        raise ValueError('Bernoulli probability must be between 0 and 1.')

    return 1 if np.random.rand() < p else 0


def sample_edge_count(num_nodes: int, p: float) -> int:
    """
    Sample an edge count for a given graph according to binomial distribution.
    :param num_nodes: number of nodes of the graph.
    :param p: probability of generation of an edge.
    :return: an integer of edge count.
    """

    if num_nodes <= 1:
        raise ValueError('Number of nodes must be greater than 1.')

    if p < 0 or p > 1:
        raise ValueError('Edge generation probability must be between 0 and 1.')

    n = num_nodes * (num_nodes - 1) / 2
    return np.random.binomial(n, p)


def geometric_sample(p: float) -> int:
    """
    Sample from a geometric distribution.
    :param p: Probability of success.
    :return: an integer of number of trials at first success.
    """

    if p < 0 or p > 1:
        raise ValueError('Geometric probability must be between 0 and 1.')

    rng = np.random.default_rng(12345)
    return rng.geometric(p=p) - 1