import numpy as np
from scipy.linalg import pinv

# Example Hermitian matrix
A = np.array([[1, 2 + 1j], [2 - 1j, 3]])

# Compute the Moore-Penrose pseudo-inverse
A_pinv = pinv(A)

print("Original Matrix:\n", A)
print("Pseudo-inverse of the Matrix:\n", A_pinv)
