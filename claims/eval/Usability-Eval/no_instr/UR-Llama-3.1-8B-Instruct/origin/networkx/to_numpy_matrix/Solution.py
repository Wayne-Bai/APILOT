import networkx as nx
import numpy as np

# Create a new empty graph
G = nx.Graph()

# Add edges to the graph
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)])

# Return the graph adjacency matrix as a NumPy matrix
adj_matrix = nx.to_numpy_array(G)

print(adj_matrix)
