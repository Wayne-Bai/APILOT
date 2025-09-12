import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()

# Add some nodes and edges to the graph
G.add_edges_from([(0, 1), (0, 2), (1, 2), (1, 3)])

# Get the adjacency matrix as a NumPy array
adj_matrix = nx.to_numpy_array(G)

# Print the adjacency matrix
print(adj_matrix)
