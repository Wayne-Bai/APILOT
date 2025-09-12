import numpy as np
from scipy.linalg import eig

# Define the square matrix A
A = np.array([[1, 2], [3, 4]])

# Find k eigenvalues and eigenvectors
k = 2
eigenvalues, eigenvectors = eig(A, k)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
