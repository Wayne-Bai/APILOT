import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import laplacian

# Create an adjacency matrix for a directed graph
# For example, a simple graph with 3 nodes:
# Node 0 -> Node 1, Node 1 -> Node 2, Node 2 -> Node 0
adj_matrix = np.array([
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
])

# Create a sparse matrix representation
sparse_matrix = csr_matrix(adj_matrix)

# Compute the Laplacian of the directed graph
lap_matrix = laplacian(sparse_matrix, normed=False)
print("Laplacian Matrix:")
print(lap_matrix.toarray())
