import networkx as nx
import numpy as np

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Get the adjacency matrix
adj_matrix = nx.to_numpy_array(G)

# Convert the adjacency matrix to a NumPy recarray
dtype = [('node1', int), ('node2', int), ('weight', float)]
recarray = np.array([(i, j, adj_matrix[i, j]) for i in range(adj_matrix.shape[0]) for j in range(adj_matrix.shape[1]) if adj_matrix[i, j] != 0], dtype=dtype)

print(recarray)
