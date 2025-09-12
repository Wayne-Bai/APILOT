import networkx as nx
import numpy as np

# Example graph creation
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (1, 3), (3, 4)])

# Convert the graph to an adjacency matrix
adj_matrix = nx.to_numpy_matrix(G)

print(adj_matrix)
