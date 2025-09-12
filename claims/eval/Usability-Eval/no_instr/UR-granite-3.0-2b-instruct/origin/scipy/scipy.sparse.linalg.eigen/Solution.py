import numpy as np
from scipy.linalg import eigh

# Define the square matrix A
A = np.array([[4, 1], [1, 2]])

# Find the k smallest eigenvalues and eigenvectors
k = 2
eigenvalues, eigenvectors = eigh(A, k)

print("Eigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)
