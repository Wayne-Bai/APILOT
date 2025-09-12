import scipy.sparse.csgraph as csgraph
import numpy as np

# Define the adjacency matrix of a directed graph
# Example graph:
#   0 -> 1, 0 -> 2
#   1 -> 2
#   2 -> 1
adjacency_matrix = np.array([
    [0, 1, 1],
    [0, 0, 1],
    [0, 1, 0]
])

# Compute the Laplacian of the directed graph
laplacian_matrix = csgraph.laplacian(adjacency_matrix, normed=False, return_diag=False, use_out_degree=False)

print("Laplacian matrix:")
print(laplacian_matrix)
