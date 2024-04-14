import networkx as nx
import random 

def generate_ba_network(n: int, m: int, initial_clique: int = 5) -> nx.Graph:
    """Generates a Barabasi-Albert network with n nodes, m edges to attach from a new node to existing nodes, and an initial clique of size initial_clique.
    
    :param n: Number of nodes in the network
    :param m: Number of edges to attach from a new node to existing nodes
    :param initial_clique: Size of the initial clique
    :return: A Barabasi-Albert network
    """
    G = nx.complete_graph(initial_clique)
    node_degrees = list(G.degree())

    for new_node in range(initial_clique, n):
        targets = _pick_nodes(node_degrees, m)
        G.add_node(new_node)
        for target in targets:
            G.add_edge(new_node, target)
        node_degrees.append((new_node, m))

    return G

def _pick_nodes(node_degrees: list[tuple[int, int]], m: int) -> list:
    """Picks m nodes from the list of nodes based on their degrees.
    
    :param node_degrees: List of tuples containing the node and its degree
    :param m: Number of nodes to pick
    :return: List of nodes
    """
    total_degree = sum(degree for _, degree in node_degrees)
    targets = []
    while len(targets) < m:
        rand_val = random.uniform(0, total_degree)
        cum_sum = 0
        for node, degree in node_degrees:
            cum_sum += degree
            if cum_sum > rand_val:
                if node not in targets:
                    targets.append(node)
                    total_degree -= degree
                    break
    
    return targets