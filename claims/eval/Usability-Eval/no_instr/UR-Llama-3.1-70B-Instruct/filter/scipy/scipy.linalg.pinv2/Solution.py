import scipy.linalg as la
import numpy as np

# Create a matrix
A = np.array([[1, 2], [3, 4]])

# Compute the Moore-Penrose pseudo-inverse of A
A_inv = la.pinv(A)

print("Original Matrix:")
print(A)

print("\nPseudo-Inverse of the Matrix:")
print(A_inv)
