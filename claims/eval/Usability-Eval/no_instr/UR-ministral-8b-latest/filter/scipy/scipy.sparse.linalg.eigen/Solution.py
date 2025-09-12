import numpy as np
from scipy.linalg import eigh

# Define the square matrix A
A = np.array([[4, 1],
              [1, 2]])

# Number of eigenvalues and eigenvectors to calculate
k = 2

# Compute the k eigenvalues and eigenvectors
eigenvalues, eigenvectors = eigh(A, k=k)

print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)
