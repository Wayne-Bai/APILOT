import numpy as np
from scipy.linalg import pinvh

# Assuming 'A' is your Hermitian matrix
A = np.array([[1, 1j], [-1j, 1]])  # Example Hermitian matrix

# Compute the Moore-Penrose pseudo-inverse
A_pinv = pinvh(A)

print(A_pinv)
