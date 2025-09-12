import numpy as np
from scipy.linalg import eig

# Define the square matrix A
A = np.array([[1, 2], [3, 4]])

# Find the k largest eigenvalues and eigenvectors of A
k = 2 # number of eigenvalues to find
w, v = eig(A, k)

print("Eigenvalues:")
print(w)
print()
print("Eigenvectors:")
print(v)
