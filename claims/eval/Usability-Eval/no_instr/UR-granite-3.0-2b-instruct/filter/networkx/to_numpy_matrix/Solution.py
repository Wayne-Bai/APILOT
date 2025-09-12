import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)

# Get the adjacency matrix
adj_matrix = nx.to_numpy(G.adjacency_matrix())

# Print the adjacency matrix
print(adj_matrix)
