import numpy as np
from scipy.linalg import pinv

# Example matrix
A = np.array([[1, 2], [3, 4], [5, 6]])

# Compute the pseudo-inverse of the matrix A
pseudo_inverse_A = pinv(A)

print("Original Matrix A:")
print(A)
print("\nPseudo-inverse of A:")
print(pseudo_inverse_A)
