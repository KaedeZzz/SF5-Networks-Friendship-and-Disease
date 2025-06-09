import numpy as np
from matplotlib import pyplot as plt
from src.graph import SirGraph as SIR
from src.graph_methods import random_graph
from src.io import load_graph, save_dir

path = save_dir / 'rg_n10000_d20_p.pkl'

if __name__ == '__main__':
    p_init = 0.05
    rate_ind_list = np.linspace(-2, -0.5, 50)
    transfer_rate_list = np.power(10, rate_ind_list)
    graph = load_graph(path)
    recovered_list = []
    for rate in transfer_rate_list:
        sir = SIR(graph, p_init)
        state, transient_time = sir.run(rate)
        print(f"At rate {rate}, {state.count(sir.R)} recovered after {transient_time} steps")
        recovered_list.append(state.count(sir.R))

    plt.plot(rate_ind_list, recovered_list)
    plt.xlabel('Transfer rate')
    plt.ylabel('Number of recovery')
    plt.vlines(x=-1.5, color='r', ymin=0, ymax=max(recovered_list))
    plt.show()