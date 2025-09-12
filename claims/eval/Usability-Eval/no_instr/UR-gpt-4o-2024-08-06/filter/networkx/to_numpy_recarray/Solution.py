import networkx as nx
import numpy as np

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

# Generate the adjacency matrix
adj_matrix = nx.to_numpy_array(G)

# Convert to a NumPy recarray
rec_array = np.rec.array(adj_matrix, dtype=[('value', float)])

print("Adjacency Matrix as RecArray:")
print(rec_array)
