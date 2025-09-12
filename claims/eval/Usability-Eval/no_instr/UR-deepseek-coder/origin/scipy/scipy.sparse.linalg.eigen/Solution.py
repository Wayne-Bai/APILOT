import numpy as np
from scipy.linalg import eigh

# Example square matrix A
A = np.array([[4, 1, -1],
              [1, 2, 1],
              [-1, 1, 3]])

# Number of eigenvalues and eigenvectors to find
k = 2

# Find the k largest eigenvalues and corresponding eigenvectors
eigenvalues, eigenvectors = eigh(A, eigvals=(A.shape[0] - k, A.shape[0] - 1))

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
