import scipy
import numpy as np

# Define the adjacency matrix of the directed graph
A = np.array([[0, 1, 0],
              [1, 0, 1],
              [0, 1, 0]])

# Compute the Laplacian matrix
L = scipy.sparse.csgraph.laplacian(A, normed=False)

print(L)
