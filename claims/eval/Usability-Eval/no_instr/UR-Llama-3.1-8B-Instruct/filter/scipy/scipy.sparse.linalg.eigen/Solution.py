import numpy as np
from scipy.sparse.linalg import eigs

# Define a square matrix A
A = np.array([[3, 2], [4, 6]])

# Define the number of eigenvalues/eigenvectors to find
k = 2

# Find the k eigenvalues and eigenvectors of A
w, v = eigs(A, k=k, which='LM')

# Print the eigenvalues (w) and eigenvectors (v)
print("Eigenvalues: ", w)
print("Eigenvectors: \n", v)

