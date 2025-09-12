import numpy as np
import scipy.linalg

# Define a matrix
matrix = np.array([[1, 2], [3, 4]])

# Compute the Moore-Penrose pseudo-inverse using scipy.linalg.pinv
pseudo_inverse = scipy.linalg.pinv(matrix)

print("Original Matrix:")
print(matrix)

print("Moore-Penrose Pseudo-Inverse:")
print(pseudo_inverse)
