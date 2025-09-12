
import numpy as np
from scipy.linalg import eigh

# Define the square matrix A
A = np.array([[1, 2, 3],
              [2, 4, 5],
              [3, 5, 6]])

# Find k eigenvalues and eigenvectors of A
k = 2
eigenvalues, eigenvectors = eigh(A, eigvals=(len(A) - k, len(A) - 1))

print("Eigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)
