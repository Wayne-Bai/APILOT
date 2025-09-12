import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()

# Add edges
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)

# Get the adjacency matrix
adj_matrix = nx.to_numpy_array(G)

# Convert the adjacency matrix to a NumPy recarray
adj_matrix_recarray = np.recarray(shape=adj_matrix.shape, dtype=[('row', int), ('col', int), ('weight', float)], buffer=adj_matrix.data)

# Set the row and column indices
adj_matrix_recarray.row = np.arange(adj_matrix.shape[0])
adj_matrix_recarray.col = np.arange(adj_matrix.shape[1])

adj_matrix_recarray
