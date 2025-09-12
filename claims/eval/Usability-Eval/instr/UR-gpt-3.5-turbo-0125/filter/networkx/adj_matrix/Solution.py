
import networkx as nx
import numpy as np

# Create a sample graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (2, 3)])

# Generate the adjacency matrix
adj_matrix = nx.adjacency_matrix(G).todense()

print(adj_matrix)
