import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3)])

# Create adjacency matrix
adj_matrix = nx.to_numpy_matrix(G)

print(adj_matrix)
