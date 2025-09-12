
import numpy as np

# Create a sample matrix
A = np.array([[1, 2], [3, 4]])

# Compute the pseudo-inverse of matrix A using SVD method
U, S, VT = np.linalg.svd(A)
pseudo_inv = np.dot(VT.T, np.dot(np.linalg.inv(np.diag(S)), U.T))

print("Pseudo-inverse of matrix A:")
print(pseudo_inv)
