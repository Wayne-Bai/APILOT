import networkx as nx
import numpy as np

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4)])

# Get the adjacency matrix as a NumPy array
adjacency_matrix = nx.to_numpy_array(G)

print(adjacency_matrix)
