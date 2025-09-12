import numpy as np
from scipy.linalg import pinv

# Example Hermitian matrix
hermitian_matrix = np.array([[1, 2 + 1j], [2 - 1j, 3]])

# Compute the Moore-Penrose pseudo-inverse
pseudo_inverse = pinv(hermitian_matrix)

print("Hermitian Matrix:")
print(hermitian_matrix)
print("\nMoore-Penrose Pseudo-Inverse:")
print(pseudo_inverse)
