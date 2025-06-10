import numpy as np
from matplotlib import pyplot as plt

from src.io import load_graph, save_dir
from src.graph import SirGraph
from src.graph_methods import get_degree_dist

paths = [save_dir / 'rg_n10000_d20_g.pkl', save_dir / 'rg_n10000_d20_p.pkl']
keys = ['geometric', 'poisson']

if __name__ == '__main__':
    for j in range(2):
        graph = load_graph(paths[j])
        rate_ind_list = np.linspace(-2, -1, 5)
        transfer_rate_list = np.power(10, rate_ind_list)
        for i, rate in enumerate(transfer_rate_list):
            sir = SirGraph(graph, prob=0.05)
            infected_p = sir.infected_estimate(rate)
            fig, ax = plt.subplots(1, 2)
            ax[0].hist(infected_p, bins=20)
            ax[1].hist(get_degree_dist(graph), bins=20)
            plt.title(keys[j])
            plt.show()
