
import numpy as np
from scipy.linalg import eig

# Define the matrix A
A = np.array([[1, 2], [3, 4]])

# Find the k eigenvalues and eigenvectors of A
k = 2
eigenvalues, eigenvectors = eig(A, k=k)

# Print the results
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
