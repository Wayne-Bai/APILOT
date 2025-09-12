import numpy as np
from scipy.linalg import pinv

# Assuming 'A' is your Hermitian matrix
A = np.array([[1, 2+3j], [2-3j, 4]])

# Compute the Moore-Penrose pseudo-inverse of the Hermitian matrix
A_pinv = pinv(A)

print(A_pinv)
