import numpy as np
import networkx as nx

# Create a sample adjacency matrix
adj_matrix = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

# Create a NetworkX graph from the adjacency matrix
G = nx.Graph(adj_matrix)

print(G.edges())
