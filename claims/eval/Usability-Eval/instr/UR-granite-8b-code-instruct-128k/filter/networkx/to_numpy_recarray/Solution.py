import networkx as nx
import numpy as np

# Create a simple graph with 4 nodes
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# Generate the adjacency matrix as a NumPy recarray
adj_matrix = nx.to_numpy_recarray(G)

# Print the adjacency matrix
print(adj_matrix)
