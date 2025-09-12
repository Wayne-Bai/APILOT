import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()

# Add nodes
G.add_nodes_from([1, 2, 3, 4])

# Add edges
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

# Convert adjacency matrix to NumPy recarray
A = nx.to_numpy_array(G)
adj_matrix = np.asrecarray(A, dtype=[('nodes', int)])

adj_matrix
