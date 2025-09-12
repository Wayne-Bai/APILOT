import numpy as np
from scipy.linalg import pinv

# Example Hermitian matrix
A = np.array([[1, 2+1j], [2-1j, 3]])

# Compute the pseudo-inverse
A_pseudo_inv = pinv(A)

print("Original Hermitian matrix:\n", A)
print("Pseudo-inverse of the Hermitian matrix:\n", A_pseudo_inv)
