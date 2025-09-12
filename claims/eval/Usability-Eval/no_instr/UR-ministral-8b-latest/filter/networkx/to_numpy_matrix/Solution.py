import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()

# Add nodes
G.add_nodes_from([1, 2, 3, 4])

# Add edges
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Convert graph to adjacency matrix
adj_matrix = nx.to_numpy_array(G)

print(adj_matrix)
