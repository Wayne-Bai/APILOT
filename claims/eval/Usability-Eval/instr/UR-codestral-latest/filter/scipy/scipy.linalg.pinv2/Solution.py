import numpy as np
from scipy.linalg import pinv

# Let's define a matrix
A = np.array([[1, 2], [3, 4]])

# Compute the Moore-Penrose pseudo-inverse of matrix A
A_pinv = pinv(A)

print("The Moore-Penrose pseudo-inverse of the matrix A is:")
print(A_pinv)
