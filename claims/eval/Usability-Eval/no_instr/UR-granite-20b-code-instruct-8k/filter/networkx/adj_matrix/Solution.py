import networkx as nx
import numpy as np

# Create an instance of graph
G = nx.Graph()

# Add edges to graph
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])

# Get adjacency matrix of graph
A = nx.adjacency_matrix(G)

# Convert adjacency matrix to numpy matrix
A_np = np.matrix(A.todense())

print(A_np)
