import numpy as np
from scipy.linalg import pinv

# Example matrix
A = np.array([[1, 2, 3], [4, 5, 6]])

# Compute the pine Inverse of matrix
pinv_result = pinv(A)

print("Pseudo-Inverse of A:")
print(pinv_result)
