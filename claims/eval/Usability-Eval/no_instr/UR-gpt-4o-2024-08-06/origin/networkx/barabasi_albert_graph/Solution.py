import networkx as nx
import matplotlib.pyplot as plt

def generate_barabasi_albert_graph(n, m):
    """
    Generates a random graph using the Barabási–Albert preferential attachment model.

    :param n: Number of nodes
    :param m: Number of edges to attach from a new node to existing nodes
    :return: A Barabási–Albert graph
    """
    BA_graph = nx.barabasi_albert_graph(n, m)
    return BA_graph

# Parameters for the Barabási–Albert graph
num_nodes = 100  # Total number of nodes
num_edges_to_attach = 2  # Number of edges to attach from a new node

# Generate the graph
ba_graph = generate_barabasi_albert_graph(num_nodes, num_edges_to_attach)

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(ba_graph, with_labels=False, node_size=20)
plt.title(f'Barabási–Albert graph with {num_nodes} nodes and {num_edges_to_attach} edges per new node')
plt.show()
