import numpy as np
import matplotlib.pyplot as plt
from src.graph_methods.graph_gen import random_graph
from src.graph_methods.graph_stats import count_edges


# Assignment 1.1: Generate random graph and do statistics of edge count

repeat = 300 # Number of generation of a random graph of same parameter
p_range = np.linspace(0.1,0.9, 9) # Range of probability of Bernoulli variable for edge generation
num_nodes = 100 # Number of nodes of network to be generated

for p in p_range:
    edge_counts = np.zeros(repeat)
    for count in range(repeat):
        network = random_graph(num_nodes=num_nodes, p=p)
        edge_counts[count] = count_edges(network)
    mean = np.mean(edge_counts)
    mean_theoretical = num_nodes * (num_nodes - 1) * p / 2
    std_theoretical = (num_nodes * (num_nodes - 1) * p * (1 - p) / 2) ** 0.5
    std = np.std(edge_counts)
    print("statistics for random graph of p={0:5.2f}:".format(p))
    print("theoretical mean: {0:5.2f}".format(mean_theoretical))
    print("generation mean: {0:5.2f}".format(mean))
    print("theoretical std: {0:5.2f}".format(std_theoretical))
    print("generation std: {0:5.2f}".format(std))
    print("\n")
    fig, ax = plt.subplots()
    ax.hist(edge_counts, bins=20)
    ax.set_title("p={0:5.2f}".format(p))
    ax.set_xlabel("edge counts")
    ax.set_ylabel("count")
    plt.show()

# Here we have obtained the histograms





