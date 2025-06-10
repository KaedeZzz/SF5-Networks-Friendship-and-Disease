import numpy as np
from matplotlib import pyplot as plt

from src.io import load_graph, save_dir
from src.graph import SirGraph
from src.graph_methods import friend_infect_vec

paths = [save_dir / 'rg_n10000_d20_g.pkl', save_dir / 'rg_n10000_d20_p.pkl']
keys = ['geometric', 'poisson']

if __name__ == '__main__':
    for j in range(2):
        graph = load_graph(paths[j])
        rate = 10 ** -1.6
        sir = SirGraph(graph, prob=0.05)
        p_infect_vec = sir.infected_estimate(rate)
        p_friend_infect_vec = friend_infect_vec(graph=graph,
                                                infect_vec=p_infect_vec)
        print(f"Mean of probability of infection vector: {np.mean(p_infect_vec)}")
        print(f"Mean of probability of infection of friend vector: {np.mean(p_friend_infect_vec)}")
        print(f"Standard deviation of probability of infection vector: {np.std(p_infect_vec)}")
        print(f"Standard deviation of probability of infection of friend vector: {np.std(p_friend_infect_vec)}")