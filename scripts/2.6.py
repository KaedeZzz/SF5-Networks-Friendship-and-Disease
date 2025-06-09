import numpy as np
import matplotlib.pyplot as plt
from src.graph_methods.graph_gen import random_graph
from src.graph_methods.graph_stats import get_reachable


if __name__ == '__main__':
    n: int = 1000
    deg_list = [np.linspace(1.01, 2, 20), np.linspace(0.01, 2, 20)]
    method_list = ['geometric', 'poisson']
    crit_deg = [1.5, 1]
    repeat = 50

    for i in range(len(method_list)):
        reach_list: list[float] = []
        deg_space = deg_list[i]
        for deg in deg_space:
            reach: float = 0.0
            for _ in range(repeat):
                network = random_graph(num_nodes=n, deg=deg, method=method_list[i])
                reach += len(get_reachable(network))
            reach /= repeat
            print("Average number of reachable nodes for degree = {0:.8f} and method: {1:.2f}".format(deg, reach))
            reach_list.append(reach)

        plt.plot(deg_space, np.array(reach_list))
        plt.vlines(x=crit_deg[i], ymin=0, ymax=np.max(np.array(reach_list)), colors='r', label='deg_crit')
        plt.legend()
        plt.show()
