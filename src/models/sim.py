from src.graph import Graph

def non_infected_probs(graph: Graph, rate: float, init_probs: list) -> list:
    """
    Use iterated method to approximate the probability that a node never gets infected.
    :param graph: The graph.
    :param rate: Transition rate.
    :param init_probs: Probabilities to initialize.
    :return: A list of probabilities.
    """
    converged = False
    probs = init_probs

    while not converged:
        new_probs = []
        for i in range(len(probs)):
            neighbors = graph.neighbors(i)
            p = 1
            for neighbor in neighbors:
                p *= (1 - rate + probs[neighbor] * rate)
            new_probs.append(p)
        converged = True
        for i in range(len(probs)):
            if abs(probs[i] - new_probs[i]) > 0.01:
                converged = False
        if len(new_probs) != graph.num_nodes:
            raise ValueError('Number of nodes does not match graph')
        probs = new_probs

    return probs