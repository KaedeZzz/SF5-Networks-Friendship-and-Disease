from matplotlib import pyplot as plt

from src.graph_methods import random_graph, get_degree_dist
from src.tools import geometric_sample, poisson_sample


if __name__ == "__main__":
        graph_geo = random_graph(num_nodes=1000, deg=10, method='geometric')
        graph_poi = random_graph(num_nodes=1000, deg=10, method='poisson')


        plt.hist((get_degree_dist(graph_geo), [geometric_sample(1 / 10) for _ in range(100000)]),
                color=['b', 'g'], density=True, bins=20, histtype='bar')
        plt.show()

        plt.hist((get_degree_dist(graph_poi), [poisson_sample(10) for _ in range(100000)]),
                color=['b', 'g'], density=True, bins=20, histtype='bar')
        plt.show()