import numpy as np
from scipy.linalg import pinv

# Example Hermitian matrix
A = np.array([[2, 2+1j], [2-1j, 3]])

# Compute the Moore-Penrose pseudo-inverse
pseudo_inverse = pinv(A)

print("Hermitian matrix A:")
print(A)
print("\nMoore-Penrose pseudo-inverse of A:")
print(pseudo_inverse)
