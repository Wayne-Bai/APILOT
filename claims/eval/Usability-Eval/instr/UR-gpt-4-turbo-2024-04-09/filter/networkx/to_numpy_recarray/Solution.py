import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4)])

# Generate the adjacency matrix
adj_matrix = nx.to_numpy_array(G)

# Convert the array to a structured array (similar to recarray)
dtype = [('weight', float)]
structured_adj_matrix = np.array(adj_matrix, dtype=dtype)

# Now, let's make it a record array
rec_adj_matrix = np.core.records.fromarrays(structured_adj_matrix.transpose(), dtype=dtype)

# Test output
print(rec_adj_matrix)
