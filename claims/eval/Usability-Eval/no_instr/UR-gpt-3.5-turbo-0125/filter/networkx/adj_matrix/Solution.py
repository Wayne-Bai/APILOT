
import networkx as nx
import numpy as np

# Define a graph using networkx
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])

# Get adjacency matrix as a numpy matrix
adj_matrix = nx.to_numpy_matrix(G)

print(adj_matrix)
