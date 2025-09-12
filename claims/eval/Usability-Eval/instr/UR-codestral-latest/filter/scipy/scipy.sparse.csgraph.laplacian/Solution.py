import networkx as nx
import numpy as np

# Create a directed graph
G = nx.DiGraph()

# Add edges with weight to the graph
G.add_edges_from([(1, 2, {'weight': 3}), (2, 3, {'weight': 7}), (3, 1, {'weight': 1})])

# Compute the degree matrix
degree_matrix = np.diag(np.sum(np.array(nx.adjacency_matrix(G).todense()), axis=1))

# Compute the Laplacian matrix
laplacian_matrix = degree_matrix - nx.adjacency_matrix(G).todense()

print(laplacian_matrix)
