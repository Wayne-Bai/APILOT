import numpy as np
from scipy.linalg import eigh

# Define the square matrix A
A = np.array([[1, 2], [3, 4]])

# Find the k eigenvalues and eigenvectors of the matrix A
k = 2
eigenvalues, eigenvectors = eigh(A, k=k)

# Print the eigenvalues and eigenvectors
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
