import numpy as np
from scipy.linalg import eig

# Define the matrix A
A = np.array([[4, 1], [5, 6]])

# Find k largest eigenvalues and eigenvectors
eigenvalues, eigenvectors = eig(A, k=2)
