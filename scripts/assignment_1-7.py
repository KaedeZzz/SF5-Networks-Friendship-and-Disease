import numpy as np
import matplotlib.pyplot as plt
from src.graph_methods.graph_gen import random_graph
from src.graph_methods.graph_stats import get_reachable

n = 4096
p_list = np.linspace(10**-5, 10**-3, 20)
repeat = 20

p_crit = 1 / (n - 1)
reach_list = []

print("p_crit = 1/(n - 1) = {0:.8f}".format(p_crit))

for p in p_list:
    reach = 0
    for _ in range(repeat):
        network = random_graph(n, p, method='two-step')
        reach += len(get_reachable(network))
    reach /= repeat
    print("Average number of reachable nodes for p = {0:.8f}: {1:.2f}".format(p, reach))
    reach_list.append(reach)

plt.plot(p_list, np.log(np.array(reach_list)))
plt.vlines(x=p_crit, ymin=0, ymax=np.max(np.log(np.array(reach_list))), colors='r', label='p_crit')
plt.title("log-average count of reachable node vs. generation probability")
plt.legend()
plt.show()
