import numpy as np
from scipy.linalg import pinv

# Define a matrix
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Compute the Moore-Penrose pseudo-inverse
A_pinv = pinv(A)

print("The Moore-Penrose pseudo-inverse of the matrix A is:")
print(A_pinv)
