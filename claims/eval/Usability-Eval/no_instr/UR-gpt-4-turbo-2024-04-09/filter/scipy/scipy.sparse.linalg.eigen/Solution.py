import numpy as np
from scipy.linalg import eigh

# Example square matrix A
A = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 6]])

# Number of eigenvalues and eigenvectors to find
k = 2

# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = eigh(A)

# Since eigh returns them in ascending order, we take the last k (the largest)
eigenvalues_k = eigenvalues[-k:]
eigenvectors_k = eigenvectors[:, -k:]

print("Eigenvalues:", eigenvalues_k)
print("Eigenvectors:", eigenvectors_k)
