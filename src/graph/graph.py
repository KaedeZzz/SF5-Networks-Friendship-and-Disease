import numpy as np


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


class SirGraph(Graph): # SIR Graph
    def __init__(self, num_nodes: int, directed=False):
        super().__init__(num_nodes, directed)
        self.state_keys = [self.S, self.I, self.R] = range(3)
        self.state = [self.S for _ in range(self.num_nodes)]

    def set_init_state(self, prob):
        for i in range(self.num_nodes):
            if np.random.binomial(n=1, p=prob, size=1) == 1.0:
                self.state[i] = self.I

    def advance(self, rate: float = 0.0) -> list[int]:
        if not 0.0 < rate < 1.0:
            raise ValueError('Infection rate must be between 0 and 1.')
        next_state = [self.S for _ in range(self.num_nodes)]
        for node in range(self.num_nodes):
            if self.state[node] == self.I:
                next_state[node] = self.R
                infection_list = np.random.binomial(n=1, p=rate, size=len(self.adj[node]))
                for friend in self.adj[node]:
                    if self.state[friend] == self.S and infection_list[friend]:
                        next_state[friend] = self.I
        return next_state

    def run(self, init_prob, rate):
        self.set_init_state(init_prob)
        time_scale = 0
        while self.I in self.state:
            self.advance(rate)
            time_scale += 1
        return self.state, time_scale
