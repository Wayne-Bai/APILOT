import numpy as np
from scipy.linalg import pseudoinverse

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Matrix A:")
print(A)
print("Pseudo-Inverse of Matrix A:")
print(pseudoinverse(A))
