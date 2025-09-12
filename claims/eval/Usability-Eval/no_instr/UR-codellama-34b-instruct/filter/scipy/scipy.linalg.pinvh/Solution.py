import numpy as np
from scipy.linalg import pinv

# Define a Hermitian matrix
A = np.array([[1, 2], [2, 3]])

# Compute the pseudo-inverse of A
pinv_A = pinv(A)

print(pinv_A)
