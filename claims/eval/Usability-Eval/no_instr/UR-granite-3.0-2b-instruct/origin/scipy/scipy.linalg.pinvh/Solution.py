import numpy as np
from scipy.linalg import pinv

# Define a Hermitian matrix
A = np.array([[1, 2j], [2j, 3]])

# Compute the pseudo-inverse of the matrix
A_pinv = pinv(A)

print("Pseudo-inverse of the matrix A:")
print(A_pinv)
