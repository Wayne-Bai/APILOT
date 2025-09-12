import numpy as np
from scipy.linalg import pinv as pseudo_inverse

# Example matrix
A = np.array([[1, 2], [3, 4]])

# Compute the (Moore-Penrose) pseudo-inverse of A
pseudo_inv_A = pseudo_inverse(A)

print(pseudo_inv_A)
