
import networkx as nx
import numpy as np
from scipy.sparse import csr_matrix

# Create a sample graph using networkx
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])

# Get the adjacency matrix of the graph as a NumPy array
adj_matrix = nx.adjacency_matrix(G).toarray()

# Convert the adjacency matrix to a SciPy sparse matrix
sparse_adj_matrix = csr_matrix(adj_matrix)

print(sparse_adj_matrix)
