import numpy as np
from scipy.sparse import csgraph

# Sample adjacency matrix of a directed graph
adjacency_matrix = np.array([
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 0]
], dtype=float)

# Using csgraph to compute the Laplacian matrix of the directed graph
laplacian_matrix = csgraph.laplacian(adjacency_matrix, normed=False, return_diag=False)

print("Laplacian matrix of the directed graph:")
print(laplacian_matrix)
