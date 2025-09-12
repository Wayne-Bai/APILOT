import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

# Generate the adjacency matrix as a NumPy recarray
adjacency_matrix = nx.to_numpy_recarray(G, dtype=[('weight', float)])
print(adjacency_matrix)
