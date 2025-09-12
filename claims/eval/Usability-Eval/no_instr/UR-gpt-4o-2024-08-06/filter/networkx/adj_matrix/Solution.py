import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()

# Add edges to the graph
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)])

# Obtain the adjacency matrix of the graph and convert it to a numpy matrix
adj_matrix = nx.to_numpy_array(G)

print(adj_matrix)
