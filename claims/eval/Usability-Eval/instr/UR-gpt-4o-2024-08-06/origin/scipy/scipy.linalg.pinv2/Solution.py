import numpy as np
from scipy.linalg import pinv

# Example matrix
A = np.array([[1, 2], [3, 4], [5, 6]])

# Compute the Moore-Penrose pseudo-inverse
A_pseudo_inv = pinv(A)

print("Original Matrix:")
print(A)
print("\nMoore-Penrose Pseudo-Inverse:")
print(A_pseudo_inv)
