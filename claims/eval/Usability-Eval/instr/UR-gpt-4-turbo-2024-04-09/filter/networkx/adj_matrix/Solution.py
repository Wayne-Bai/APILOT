import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4)])

# Get adjacency matrix as a numpy array
adjacency_matrix = nx.to_numpy_array(G)
print(adjacency_matrix)
