import numpy as np
from scipy.linalg import pinv

# Example matrix
A = np.array([[1, 2], [3, 4], [5, 6]])

# Compute the Moore-Penrose pseudo-inverse
A_pinv = pinv(A)

print("Original Matrix:\n", A)
print("Pseudo-Inverse:\n", A_pinv)
