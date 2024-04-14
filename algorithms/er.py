import networkx as nx
import random

def generate_er_network(N: int, p: float) -> nx.Graph:
    """Generates an Erdos-Renyi network with N nodes and probability p of connecting two nodes.
    
    :param N: Number of nodes in the network
    :param p: Probability of connecting two nodes
    :return: An Erdos-Renyi network 
    """
    G = nx.Graph()
    for i in range(N):
        for j in range(i + 1, N):
            if random.random() < p:
                G.add_edge(i, j)
    return G
