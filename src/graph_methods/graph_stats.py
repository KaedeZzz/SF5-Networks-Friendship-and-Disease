import numpy as np
from src.graph import Graph

def count_edges(graph: Graph, method='naive') -> int:
    """
    Count the number of edges in a network.
    :param graph: the network
    :param method: 'naive' lists all edges by visiting all node pairs.
    :return: An integer of count. Returns -1 if no proper method is selected.
    """
    if method == 'naive':
        return len(graph.adj)
    else:
        raise Exception(f'Method {method} not supported.')


def get_reachable(network: Graph, starting_node: int = 1) -> list[int]:
    """
    Get a list of nodes reachable from a starting node using a naive search-along-graph method.
    :param network: the graph to count.
    :param starting_node: staring node to count from. Default set to 1 as assignment 1.7.
    :return: A list of indices of all reachable nodes.
    """

    if starting_node < 0 or starting_node >= network.num_nodes:
        raise ValueError('Invalid starting node index.')

    to_visit = [starting_node]
    visited = []
    while to_visit:
        node = to_visit.pop(0)
        visited.append(node)
        if network.neighbors(node) is None:
            continue
        for neighbor in network.neighbors(node):
            if neighbor not in visited and neighbor not in to_visit:
                to_visit.append(neighbor)
    return visited


def get_degree_dist(graph: Graph) -> list[int]:
    """
    Get degree distribution of a graph as a list.
    :param graph: the graph to count.
    :return: a list of degrees of each node.
    """

    degree_dist: list[int] = []
    for i in range(graph.num_nodes):
        degree_dist.append(len(graph.neighbors(i)))
    if len(degree_dist) != graph.num_nodes:
        raise ValueError('Length of degree distribution does not match graph.')
    return degree_dist


def get_friends_degree(graph: Graph, method = 'sample', repeat = 2000, return_both = False) -> list[float] | tuple[list[float], list[float]]:
    """
    Get distributions of average of friends' degrees of a graph as a list.
    :param graph: The graph to count.
    :param method: 'Sample' estimated degree by sampling nodes, and 'iterate' lists all edges by visiting all node pairs.
    :param repeat: Number of times to repeat the estimate.
    :return: A list of average of friends' degrees of each node.
    """

    degree_dist: list[float] = []
    second_dist: list[float] = []

    if method == 'sample':
        count = 0
        while True:
            i = np.random.randint(graph.num_nodes)
            if len(graph.neighbors(i)) == 0:
                continue
            if return_both:
                second_dist.append(len(graph.neighbors(i)))
            j = np.random.randint(len(graph.neighbors(i)))
            friend = graph.neighbors(i)[j]
            degree_dist.append(len(graph.neighbors(friend)))
            count += 1
            if count >= repeat:
                break

    elif method == 'iterate':
        for i in range(graph.num_nodes):
            count: float = 0
            if len(graph.neighbors(i)) == 0:
                break
            for j in graph.neighbors(i):
                count += len(graph.neighbors(j))
            count /= len(graph.neighbors(i))
            degree_dist.append(count)

    if return_both:
        return second_dist, degree_dist
    return degree_dist


def friend_infect_vec(graph: Graph, infect_vec: list) -> list:
    """
    Estimate probability of infection from friend vector given probability of infection vector.
    :param graph: The graph.
    :param infect_vec: Probability of infection vector.
    :return: A list representing the vector.
    """
    res_vec = []
    degrees = get_degree_dist(graph)
    for i in range(graph.num_nodes):
        if degrees[i] == 0:
            continue
        total = 0
        for j in graph.neighbors(i):
            total += infect_vec[j]
        total /= degrees[i]
        res_vec.append(total)
    return res_vec