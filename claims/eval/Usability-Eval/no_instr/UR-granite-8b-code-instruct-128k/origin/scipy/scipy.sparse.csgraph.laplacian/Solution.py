import scipy as sp
import numpy as np

# Define the adjacency matrix of the directed graph
A = np.array([[0, 1, 0],
              [0, 0, 1],
              [1, 0, 0]])

# Calculate the Laplacian matrix
L = np.diag(np.sum(A, axis=0)) - A

# Print the Laplacian matrix
print(L)
