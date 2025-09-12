import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()

# Add nodes
G.add_nodes_from([1, 2, 3, 4, 5])

# Add edges
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (3, 5)])

# Get the adjacency matrix
adj_matrix = nx.to_numpy_array(G)

print(adj_matrix)
