import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()
G.add_edge(1, 2, weight=0.6)
G.add_edge(1, 3, weight=0.2)
G.add_edge(2, 3, weight=0.1)
G.add_edge(3, 4, weight=0.7)

# Get the adjacency matrix as a NumPy recarray
adj_matrix = nx.to_numpy_array(G)
adj_matrix = np.recarray.from_records(adj_matrix, dtype=[('source', int), ('target', int), ('weight', float)])

print(adj_matrix)
