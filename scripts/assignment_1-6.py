import numpy as np
import timeit

from matplotlib import pyplot as plt

from src.graph_methods.graph_gen import random_graph

power_list = np.array([6, 7, 8, 9, 10])
n_list = np.power(2, power_list)
repeat = 100

naive_time_list = []
two_step_time_list = []

for n in n_list:
    p = 10 / (n - 1)
    naive_time = timeit.timeit(lambda: random_graph(num_nodes=n, p=p, method='naive'), number=repeat)
    two_step_time = timeit.timeit(lambda: random_graph(num_nodes=n, p=p, method='two-step'), number=repeat)
    naive_time_list.append(naive_time)
    two_step_time_list.append(two_step_time)
    print("time for {0:d} naive generations for n={1:d}: {2:.2f} sec".format(repeat, n, naive_time))
    print("time for {0:d} two-step generations for n={1:d}: {2:.2f} sec".format(repeat, n, two_step_time))

fig, ax = plt.subplots(1, 2)
ax[0].plot(power_list, np.log(np.array(naive_time_list)), color='blue', label='naive')
ax[1].plot(power_list, np.log(np.array(two_step_time_list)), color='red', label='two-step')

ax.legend()
plt.show()