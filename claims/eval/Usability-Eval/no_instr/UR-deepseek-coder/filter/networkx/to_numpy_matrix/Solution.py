import networkx as nx
import numpy as np

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

# Get the adjacency matrix as a NumPy matrix
adj_matrix = nx.to_numpy_matrix(G)

print(adj_matrix)
