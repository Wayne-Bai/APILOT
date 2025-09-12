import numpy as np

# Using numpy's einsum function which provides a more generalized and efficient way to compute the Einstein summation convention

# Define two tensors
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Compute the Einstein summation convention
C = np.einsum('ij,ji->i', A, B)

# Print the result
print(C)
