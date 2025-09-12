import numpy as np
from scipy.linalg import pinv

# Example Hermitian matrix
A = np.array([[2, 2j], [-2j, 5]])

# Compute the pseudo-inverse of the Hermitian matrix
pseudo_inverse = pinv(A)

print("Original Hermitian Matrix:\n", A)
print("Pseudo-Inverse of the Hermitian Matrix:\n", pseudo_inverse)
