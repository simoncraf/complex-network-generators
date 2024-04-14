import matplotlib.pyplot as plt
import networkx as nx

def save_graph(G: nx.Graph, filename: str = "graph", folder: str = "plots") -> None:
    """Saves the graph visualization as a PNG file.
    
    :param G: NetworkX graph
    :param filename: Name of the file
    :param folder: Folder to save the file
    """
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='#FF5733')
    plt.title("Graph Visualization")
    plt.savefig(f"{folder}/{filename}.png")
    plt.close()
    
def save_degree_distribution(G: nx.Graph, filename: str = "degree_distribution", folder: str = "plots") -> None:
    """Saves the degree distribution as a PNG file.
    
    :param G: NetworkX graph
    :param filename: Name of the file
    :param folder: Folder to save the file
    """
    degrees = [G.degree(n) for n in G.nodes()]
    plt.hist(degrees, bins='auto')
    plt.title("Degree Distribution")
    plt.ylabel("Frequency")
    plt.xlabel("Degree")
    plt.savefig(f"{folder}/{filename}.png")
    plt.close()