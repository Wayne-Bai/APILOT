import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()

# Add edges
edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
G.add_edges_from(edges)

# Compute the adjacency matrix
adjacency_matrix = nx.adjacency_matrix(G).todense().A

# Convert to NumPy recarray
numba = np.ndarray(adjacency_matrix, dtype=adj_matrix)

# Output the adjacency matrix
adjacency_matrix_rec = np.rec.fromarrays([numba.nonzero()[0], numba.nonzero()[1]], dtype=['i4', 'i4'])

# Print the adjacency matrix
print(adjacency_matrix_rec)
