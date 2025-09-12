import numpy as np
from scipy.linalg import eigh

# Assuming A to be a square matrix, we're finding its k smallest eigenvalues and eigenvectors

# Square matrix A
A = np.array([[...]])  # Fill the actual matrix here

# Number of eigenvalues and eigenvectors to find
k = ...  # Fill the actual number here

# Using eigh function from scipy.linalg to compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = eigh(A, eigvals=(0, k-1))  # eigvals set from 0 to k-1 for the k smallest eigenvalues

print("Eigenvalues: ", eigenvalues)
print("Eigenvectors: ", eigenvectors)
