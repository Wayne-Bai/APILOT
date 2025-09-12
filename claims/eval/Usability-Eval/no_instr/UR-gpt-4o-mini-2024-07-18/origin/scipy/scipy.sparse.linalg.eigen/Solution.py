import numpy as np
from scipy.linalg import eigh  # Using `eigh` for symmetric/hermitian matrices

# Example square matrix A
A = np.array([[1, 2], 
              [2, 3]])

# Number of eigenvalues and eigenvectors to find
k = 1  # Adjust 'k' as needed

# Finding the k eigenvalues and eigenvectors
eigenvalues, eigenvectors = eigh(A, eigvals=(A.shape[0] - k, A.shape[0] - 1))

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
