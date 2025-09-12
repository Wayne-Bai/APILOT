import networkx as nx
import numpy as np

# Create a new directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edges_from([(1, 2), (2, 3), (1, 3), (3, 1), (2, 1)])

# Get the adjacency matrix as a numpy matrix
adj_matrix = nx.to_numpy_array(G)

print("Adjacency Matrix:")
print(adj_matrix)
