import numpy as np
from matplotlib import pyplot as plt
from src.graph import SirGraph as SIR
from src.graph_methods import random_graph
from src.io import load_graph, save_dir

path = save_dir / 'rg_n10000_d20_p.pkl'

if __name__ == '__main__':
    p_init = 0.05
    rate_ind_list = np.linspace(-2, -0.5, 5)
    transfer_rate_list = np.power(10, rate_ind_list)
    graph = load_graph(path)
    for rate in transfer_rate_list:
        sir = SIR(graph, p_init)
        transient_time = 0
        S_count, I_count, R_count = [], [], []
        while sir.has_infected():
            sir.advance(rate)
            transient_time += 1
            S_count.append(sir.state.count(sir.S))
            I_count.append(sir.state.count(sir.I))
            R_count.append(sir.state.count(sir.R))
        plt.plot(range(transient_time), S_count, color='blue', label='S')
        plt.plot(range(transient_time), I_count, color='red', label='I')
        plt.plot(range(transient_time), R_count, color='green', label='R')
        plt.xlabel('Simulation steps')
        plt.ylabel('Number of nodes')
        plt.show()