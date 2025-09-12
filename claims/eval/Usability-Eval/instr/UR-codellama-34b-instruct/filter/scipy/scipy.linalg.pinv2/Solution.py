import numpy as np
from scipy import linalg

# Define a matrix A
A = np.array([[1, 2], [3, 4]])

# Compute the pseudo-inverse of A using pinv()
pinv_A = linalg.pinv(A)

print(pinv_A)
