import numpy as np
from matplotlib import pyplot as plt
from src.graph_methods import random_graph, get_degree_dist, get_friends_degree

graph = random_graph(num_nodes=1000, deg=10, method='geometric')


degree, friends_degree = get_friends_degree(graph, return_both=True)

plt.hist((degree, friends_degree), bins=40, density=True, color=['b', 'g'], histtype='bar')
plt.show()

print("Mean degree of nodes: {0:.2f}".format(np.mean(degree)))
print("Standard deviation of degree of nodes: {0:.2f}".format(np.std(degree)))

print("Mean degree of friends: {0:.2f}".format(np.mean(friends_degree)))
print("Standard deviation of degree of nodes: {0:.2f}".format(np.std(friends_degree)))

diff_dist = np.array(friends_degree) - np.array(degree)

plt.hist(diff_dist, bins=40, density=True, color='b')
plt.show()

print("Mean of difference: {0:.2f}".format(np.mean(diff_dist)))
print("Standard deviation of difference: {0:.2f}".format(np.std(diff_dist)))