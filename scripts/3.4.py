import numpy as np
from matplotlib import pyplot as plt

from src.io import load_graph, save_dir
from src.models import outbreak_cluster_size

path = save_dir / 'rg_n10000_d20_p.pkl'

if __name__ == '__main__':
    graph = load_graph(path)
    rate_ind_list = np.linspace(-2, -1, 20)
    transfer_rate_list = np.power(10, rate_ind_list)
    coeff_of_var_list = []
    for i, rate in enumerate(transfer_rate_list):
        dist = outbreak_cluster_size(graph, rate, repeat=50)
        mean = np.mean(dist)
        std = np.std(dist)
        coeff_of_var_list.append(std/mean)
        print(f"sample collected from simulation with rate {i + 1}, {len(transfer_rate_list)} in total")
    plt.plot(rate_ind_list, coeff_of_var_list)
    plt.show()