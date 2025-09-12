
import networkx as nx
import numpy as np

# Create a graph (example)
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])

# Get the adjacency matrix
adj_matrix = nx.to_numpy_array(G, dtype=int)

# Convert adjacency matrix to NumPy recarray
adj_recarray = np.rec.fromrecords(adj_matrix)

print(adj_recarray)
