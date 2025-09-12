import networkx as nx
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import laplacian

# Creating a directed graph
G = nx.DiGraph()

# Adding edges to the graph
G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 0)
G.add_edge(0, 2)
G.add_edge(1, 0)

# Converting the graph to an adjacency matrix
adj_matrix = nx.to_numpy_array(G)

# Creating a sparse matrix from the adjacency matrix
adj_sparse = csr_matrix(adj_matrix)

# Calculating the Laplacian of the graph
laplacian_matrix = laplacian(adj_sparse, symmetrize=False)

print(laplacian_matrix.toarray())
