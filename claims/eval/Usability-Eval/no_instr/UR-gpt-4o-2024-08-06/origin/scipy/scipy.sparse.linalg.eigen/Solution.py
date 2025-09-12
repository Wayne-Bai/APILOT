import numpy as np
from scipy.linalg import eig

# Define your square matrix A
A = np.array([[4, 2, 2],
              [2, 3, 1],
              [2, 1, 3]])

# Number of eigenvalues and eigenvectors to find
k = 2  # for example, find 2 eigenvalues and eigenvectors

# Calculate all eigenvalues and eigenvectors
eigenvalues, eigenvectors = eig(A)

# Sort the eigenvalues and corresponding eigenvectors
# Pick the indices of the k largest eigenvalues
indices = np.argsort(np.abs(eigenvalues))[-k:]

# Select k largest eigenvalues and corresponding eigenvectors
k_eigenvalues = eigenvalues[indices]
k_eigenvectors = eigenvectors[:, indices]

print("Eigenvalues:")
print(k_eigenvalues)
print("Eigenvectors:")
print(k_eigenvectors)
