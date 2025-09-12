import numpy as np

# Define two example arrays
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Use Einstein summation convention to perform matrix multiplication
# 'ij,jk->ik' represents the multiplication logic
result = np.einsum('ij,jk->ik', A, B)

print("Result of Einstein summation (matrix multiplication):")
print(result)
