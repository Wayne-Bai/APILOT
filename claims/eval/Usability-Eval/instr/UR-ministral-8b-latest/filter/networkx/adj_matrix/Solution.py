import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()

# Add nodes and edges
G.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 3)])

# Get adjacency matrix
adj_matrix = nx.adjacency_matrix(G).toarray()

print(adj_matrix)
