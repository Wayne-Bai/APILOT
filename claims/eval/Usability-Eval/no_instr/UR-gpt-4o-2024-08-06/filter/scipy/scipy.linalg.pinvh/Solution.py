import numpy as np
from scipy.linalg import pinvh

# Example of a Hermitian matrix
A = np.array([[2, 2+1j], [2-1j, 3]])

# Ensure it's Hermitian
A = (A + A.conj().T) / 2

# Compute the Moore-Penrose pseudo-inverse
A_pseudo_inverse = pinvh(A)

print("Hermitian matrix A:")
print(A)

print("\nPseudo-inverse of A:")
print(A_pseudo_inverse)
