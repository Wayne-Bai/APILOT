import networkx as nx
import numpy as np

# Create a simple graph
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)

# Get the adjacency matrix
adj_matrix = nx.to_numpy_matrix(G)

# Print the adjacency matrix
print(adj_matrix)
