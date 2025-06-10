import numpy as np
from matplotlib import pyplot as plt

from src.graph import SirGraph
from src.io import load_graph, save_dir
from src.models import outbreak_cluster_size

path = save_dir / 'rg_n10000_d20_p.pkl'

if __name__ == '__main__':
    graph = load_graph(path)
    rate_ind_list = np.linspace(-2, -1, 20)
    transfer_rate_list = np.power(10, rate_ind_list)
    for vac_rate in [0, 0.2, 0.4]:
        res_list = []
        for rate in transfer_rate_list:
            sir = SirGraph(graph)
            sir.vaccinate(vac_rate)
            vac_list = [0 for _ in range(graph.num_nodes)]
            for i in range(graph.num_nodes):
                vac_list[i] = 1 if sir.state[i] == sir.V else 0
            res = outbreak_cluster_size(graph, rate, vac_list=vac_list)
            res_list.append(np.mean(res))
            print(f'vac rate: {vac_rate:.2f} transfer rate: {rate:.3f} cluster size: {np.mean(res):.2f}')
        plt.plot(rate_ind_list, res_list)
    plt.show()
