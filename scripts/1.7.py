import numpy as np
import matplotlib.pyplot as plt
from src.graph_methods.graph_gen import random_graph
from src.graph_methods.graph_stats import get_reachable


if __name__ == '__main__':
    n: int = 4096
    p_list: np.array = np.linspace(10**-5, 10**-3, 20)
    repeat: int = 20

    p_crit: float = 1 / (n - 1)
    reach_list: list[float] = []

    print("p_crit = 1/(n - 1) = {0:.8f}".format(p_crit))

    for p in p_list:
        reach: float = 0.0
        for _ in range(repeat):
            network = random_graph(n, p, method='two-step')
            reach += len(get_reachable(network))
        reach /= repeat
        print("Average number of reachable nodes for p = {0:.8f}: {1:.2f}".format(p, reach))
        reach_list.append(reach)

    plt.plot(p_list, np.log(np.array(reach_list)))
    plt.vlines(x=p_crit, ymin=0, ymax=np.max(np.log(np.array(reach_list))), colors='r', label='p_crit')
    plt.legend()
    plt.show()
