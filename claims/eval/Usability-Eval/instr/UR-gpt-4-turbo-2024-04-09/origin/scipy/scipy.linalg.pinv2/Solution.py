import scipy.linalg as la
import numpy as np

# Define a matrix
A = np.array([[1, 2], [3, 4]])

# Compute the pseudo-inverse of the matrix
A_pinv = la.pinv(A)

print("Matrix A:")
print(A)
print("Pseudo-inverse of A:")
print(A_pinv)
