import networkx as nx
import numpy as np

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])

# Get the adjacency matrix as a numpy matrix
adjacency_matrix = nx.to_numpy_array(G)

print(adjacency_matrix)
