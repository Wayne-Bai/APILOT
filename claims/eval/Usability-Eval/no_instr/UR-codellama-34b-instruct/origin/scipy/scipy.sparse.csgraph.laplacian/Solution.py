import numpy as np
from scipy.linalg import laplacian

# Define the adjacency matrix of the directed graph
A = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])

# Compute the Laplacian matrix using SciPy's laplacian function
L = laplacian(A)

# Print the resulting Laplacian matrix
print(L)
