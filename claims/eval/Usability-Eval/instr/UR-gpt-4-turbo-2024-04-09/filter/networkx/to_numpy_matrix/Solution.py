import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4)])

# Get the adjacency matrix as a NumPy matrix
A = nx.adjacency_matrix(G).toarray()

print(A)
