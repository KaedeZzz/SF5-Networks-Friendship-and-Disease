import numpy as np

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