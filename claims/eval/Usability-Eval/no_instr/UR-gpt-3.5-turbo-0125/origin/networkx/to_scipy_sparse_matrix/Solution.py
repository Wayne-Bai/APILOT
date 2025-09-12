
import networkx as nx
import numpy as np
from scipy.sparse import csr_matrix

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

# Convert graph adjacency matrix to a SciPy sparse matrix
adj_matrix = nx.to_scipy_sparse_matrix(G, format='csr')

print(adj_matrix)
