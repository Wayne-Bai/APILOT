import numpy as np
from scipy.linalg import pinv

# Example matrix
A = np.array([[1, 2], [3, 4], [5, 6]])

# Compute the Moore-Penrose pseudo-inverse
A_pseudo_inverse = pinv(A)

print("Original Matrix A:")
print(A)
print("\nMoore-Penrose Pseudo-Inverse of A:")
print(A_pseudo_inverse)
