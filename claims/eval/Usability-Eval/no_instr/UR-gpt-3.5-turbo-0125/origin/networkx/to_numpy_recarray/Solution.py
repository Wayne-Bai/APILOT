
import numpy as np
import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3)])

# Convert graph to adjacency matrix as a NumPy recarray
adj_matrix = nx.to_numpy_recarray(G, dtype=[('weight', np.float)])
print(adj_matrix)
