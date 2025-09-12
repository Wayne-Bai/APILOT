import networkx as nx
import numpy as np

# Assume you have a graph G
# If you don't have a graph, you can create one like this:
# G = nx.Graph()
# G.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 4), (4, 5)])

# Convert the graph to a NumPy matrix
adj_matrix = nx.to_numpy_matrix(G)

# Print the adjacency matrix
print(adj_matrix)
