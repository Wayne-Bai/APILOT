
from scipy.linalg import inv
import numpy as np

# Generate a random Hermitian matrix
A = np.array([[1 + 1j, 2 - 3j], [2 + 3j, 5 - 2j]])

# Compute the (Moore-Penrose) pseudo-inverse of A
pinv_A = inv(A)

print(pinv_A)
