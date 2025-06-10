import numpy as np
from src.tools import check_rate

class Graph(object):
    def __init__(self, num_nodes: int, directed=False):
        """
        :param num_nodes: the number of nodes in the graph.
        :param directed: whether the graph is directed or undirected.
        """
        if num_nodes < 1:
            raise ValueError('Number of nodes must be greater than 1.')

        self.num_nodes = num_nodes # Number of nodes in the graph
        # Initialise adjacency matrix as a list of lists, where each list
        # is a list of neighbors of a node
        self.adj = [list() for _ in range(self.num_nodes)]
        self.directed = directed

    def add_edge(self, i: int, j: int) -> None:
        """
        Add an edge between nodes i and j. Direction of the edge dependent on whether the graph is directed; if the graph is undirected, the edge would be bidirectional.
        :param i: index of the source node.
        :param j: index of the target node.
        """
        if i not in range(self.num_nodes) or j not in range(self.num_nodes):
            raise ValueError('Index out of range.')

        self.adj[i].append(j)
        if not self.directed:
            self.adj[j].append(i)

    def neighbors(self, i: int) -> np.array:
        """
        Search for indices of all adjacent nodes of a node.
        :param i: index of the source node.
        :return: A list of node indices.
        """
        if i not in range(self.num_nodes):
            raise ValueError('Index out of range.')

        return self.adj[i]


class SirGraph(object):
    # SIR Graph
    """
    S: susceptible node
    I: infectious
    R: recovered
    """
    table = {
        0: 'Susceptible',
        1: 'Infectious',
        2: 'Recovered',
    }

    def __init__(self, graph: Graph, prob: float = 0.0):
        self.graph = graph
        self.num_nodes = graph.num_nodes
        self.directed = graph.directed
        self.adj = self.graph.adj
        self.prob = prob
        self.state_keys = [self.S,
                           self.I,
                           self.R,
                           self.V] = range(4)

        self.state = [self.S for _ in range(self.num_nodes)]
        self.i_list = []
        if 0.0 < prob < 1.0: # Optional, initialize infection state
            self.set_init_state(prob)

    def set_init_state(self, prob: float):
        """
        Randomly set the initial state of infection;
        some node being infectious, the rest being susceptible.

        :param prob: Initial probability of infection.
        :return: None
        """
        if not 0.0 < prob < 1.0:
            raise ValueError('Initial probability must be between 0 and 1.')
        self.state = [self.S for _ in range(self.num_nodes)]
        self.i_list = []
        rng = np.random.default_rng()
        binom = rng.binomial(n=1, p=prob, size=self.num_nodes)
        for i in range(self.num_nodes):
            if binom[i] == 1:
                self.state[i] = self.I
                self.i_list.append(i)

    def has_infected(self) -> bool:
        """
        Return True if any node is infected.
        :return: Boolean.
        """
        return self.I in self.state

    def advance(self, rate: float) -> None:
        """
        Advance the simulation of infection by one step, and update the state.
        :param rate: Probability of transition (probability that an infectious node
         infects neighbors)
        :return: None.
        """
        check_rate(rate)
        next_state = self.state
        for node in self.i_list:
            if self.state[node] != self.I:
                raise ValueError("Unmatched state and infectious state.")
            self.i_list.remove(node)
            next_state[node] = self.R
            infection_list = np.random.binomial(n=1, p=rate, size=len(self.adj[node]))
            for i, friend in enumerate(self.adj[node]):
                if self.state[friend] == self.S and infection_list[i]:
                    next_state[friend] = self.I
                    self.i_list.append(friend)
        self.state = next_state

    def run(self, rate):
        """
        Run the simulation of infection until it reaches steady state.
        :param rate: Probability of transition (probability that an infectious node
         infects neighbors)
        :return: A pair of (final state, time taken to reach steady state).
        """
        check_rate(rate)
        transient_time = 0
        while self.I in self.state:
            self.advance(rate)
            transient_time += 1
            # print(f"Run {transient_time}, Infectious: {self.state.count(self.I)}, Recovered: {self.state.count(self.R)}")
        return self.state, transient_time

    def infected_estimate(self, rate, repeat=200):
        recovered_list = [0 for _ in range(self.num_nodes)]
        for _ in range(repeat):
            self.set_init_state(self.prob)
            res_state, _ = self.run(rate)
            for i, item in enumerate(res_state):
                inc = 1 if item == self.R else 0
                recovered_list[i] += inc
            if len(recovered_list) > self.num_nodes:
                raise ValueError("Length of recovered list exceeds number of nodes.")
        for i in range(self.num_nodes):
            recovered_list[i] /= repeat
        return recovered_list

    def vaccinate(self, vac_rate):
        rng = np.random.default_rng()
        binom = rng.binomial(n=1, p=vac_rate, size=self.num_nodes)
        for i in range(self.num_nodes):
            if binom[i] == 1:
                self.state[i] = self.V
