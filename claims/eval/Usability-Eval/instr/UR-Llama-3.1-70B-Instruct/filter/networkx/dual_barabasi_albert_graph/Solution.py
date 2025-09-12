import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def generate_dual_barabasi_albert_random_graph(n: int, m: int, **kwargs) -> nx.Graph:
    """
    Returns a random graph using dual Barabási–Albert preferential attachment model.

    Parameters:
    n (int): The number of nodes.
    m (int): Number of edges to attach from a new node to existing nodes

    Returns:
    G (nx.Graph): A graph with n nodes and m edges per node.
    """

    # Generate the graph
    G = nx.barabasi_albert_graph(n, m, **kwargs)

    return G

# Generate a random graph with 100 nodes and 5 edges per node
n = 100
m = 5

G = generate_dual_barabasi_albert_random_graph(n, m)

# Print the graph info
print("Graph Info:")
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, node_size=10, node_color='lightblue', edge_color='gray')
plt.show()
