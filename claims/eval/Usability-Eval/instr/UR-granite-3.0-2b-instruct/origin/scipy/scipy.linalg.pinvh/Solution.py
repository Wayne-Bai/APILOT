import numpy as np
from scipy.linalg import pinv

# Define a Hermitian matrix
matrix = np.array([[1, 2+1j, 3-1j], [2-1j, 4, 5+1j], [3+1j, 5-1j, 6]])

# Compute the pseudo-inverse
pseudo_inverse = pinv(matrix)

print("Pseudo-inverse of the Hermitian matrix:")
print(pseudo_inverse)
