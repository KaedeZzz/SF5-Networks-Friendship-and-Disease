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
        self.adj = np.zeros((num_nodes, num_nodes)) # Initialise adjacency matrix with no edges in the graph
        self.directed = directed

    def add_edge(self, i: int, j: int) -> None:
        """
        Add an edge between nodes i and j. Direction of the edge dependent on whether the graph is directed; if the graph is undirected, the edge would be bidirectional.
        :param i: index of the source node.
        :param j: index of the target node.
        """
        if i not in range(self.num_nodes) or j not in range(self.num_nodes):
            raise ValueError('Index out of range.')

        if not self.directed:
            # If graph is not directed, adjacency matrix is symmetric and two entries need to be added for one edge
            self.adj[i, j] = 1
            self.adj[j, i] = 1
        else:
            self.adj[i, j] = 1

    def neighbors(self, i: int) -> np.array:
        """
        Search for indices of all adjacent nodes of a node.
        :param i: index of the source node.
        :return: A list of node indices.
        """
        if i not in range(self.num_nodes):
            raise ValueError('Index out of range.')

        return np.where(self.adj[i, :] == 1)[0]

    def edge_list(self) -> list:
        """
        List indices of all source and target nodes of all edges of the graph.
        :return: A list of tuples of indices in the form of (source, target).
        """
        return [(i, j) for i in range(self.num_nodes) for j in self.neighbors(i) if i < j]
