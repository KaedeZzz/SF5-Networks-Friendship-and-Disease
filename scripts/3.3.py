import numpy as np
from src.io import load_graph, save_dir
from src.models import non_infected_probs

path = save_dir / 'rg_n10000_d20_p.pkl'

if __name__ == '__main__':
    graph = load_graph(path)
    rate_ind_list = np.linspace(-2, -0.5, 5)
    transfer_rate_list = np.power(10, rate_ind_list)
    for rate in transfer_rate_list:
        init_probs = [np.random.rand() for _ in range(graph.num_nodes)]
        res = non_infected_probs(graph, rate, init_probs)
        print(f"For rate {rate}, estimated non-infected node count is {sum(res)}")