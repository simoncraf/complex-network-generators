import networkx as nx
import random
from algorithms import (
    generate_ba_network,
    generate_er_network, 
    generate_sw_network
)
from loguru import logger
from tqdm import tqdm
from utils import save_degree_distribution, save_graph

N = (50, 100, 1000, 10000)
M = (1, 2, 3, 4, 5, 10)

def er_experiment():
    for n in tqdm(N, desc=f"Running Erdos-Renyi Experiment for N={N}"):
        for _ in range(3):
            max_p = 20/(n-1)
            prob = random.uniform(0,max_p)
            logger.info(f"Generating ER network with N={n} and p={prob}")
            g_er = generate_er_network(n, prob)
            nx.write_graphml(g_er, f"graphs/graph_er_{n}_{round(prob,5)}.graphml")
            save_graph(g_er, filename=f"graph_er_{n}_{round(prob,5)}")
            save_degree_distribution(g_er, filename=f"degree_distribution_er_{n}_{round(prob,5)}")
            
def ba_experiment():
    for n in tqdm((1000, 10000), desc=f"Running Barabasi-Albert Experiment for N=(1000, 10000) and M={M}"):
        for m in M:
            logger.info(f"Generating BA network with N={n} and M={m}")
            g_ba = generate_ba_network(n, m)
            nx.write_graphml(g_ba, f"graphs/graph_ba_{n}_{m}.graphml")
            save_graph(g_ba, filename=f"graph_ba_{n}_{m}")
            save_degree_distribution(g_ba, filename=f"degree_distribution_ba_{n}_{m}")

if __name__ == '__main__':
    er_experiment()
    ba_experiment()