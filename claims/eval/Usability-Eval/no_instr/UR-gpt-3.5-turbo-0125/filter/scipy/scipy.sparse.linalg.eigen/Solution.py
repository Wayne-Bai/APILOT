
import numpy as np
from scipy.linalg import eig

# Define the square matrix A
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Find k eigenvalues and eigenvectors
k = 2
eigenvalues, eigenvectors = eig(A)

# Get the first k eigenvalues and eigenvectors
k_eigenvalues = eigenvalues[:k]
k_eigenvectors = eigenvectors[:, :k]

print("Eigenvalues:")
print(k_eigenvalues)
print("\nEigenvectors:")
print(k_eigenvectors)
