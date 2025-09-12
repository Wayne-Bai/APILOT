import networkx as nx
import numpy as np

# Assume G is a graph
G = nx.Graph()
# You can add edges to your graph using G.add_edge()

# Getting the adjacency matrix
adjacency_matrix = nx.to_numpy_matrix(G)

print("The adjacency matrix is:")
print(adjacency_matrix)
