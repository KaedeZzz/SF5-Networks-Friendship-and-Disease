import numpy as np
from src.graph import graph

def count_edges(network, method='naive') -> int:
    """
    Count the number of edges in a network.
    :param network: the network
    :param method: 'naive' lists all edges by visiting all node pairs.
    :return: An integer of count. Returns -1 if no proper method is selected.
    """
    if method == 'naive':
        return len(network.edge_list())
    else:
        raise Exception('Method {} not supported.'.format(method))


def get_reachable(network: graph, starting_node: int = 1) -> list:
    """
    Get a list of nodes reachable from a starting node using a naive search-along-graph method.
    :param network: the graph to count.
    :param starting_node: staring node to count from. Default set to 1 as assignment 1.7.
    :return: A list of indices of all reachable nodes.
    """

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
