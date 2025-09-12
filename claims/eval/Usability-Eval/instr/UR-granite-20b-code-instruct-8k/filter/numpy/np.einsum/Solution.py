import numpy as np

# Define the operands
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Compute the Einstein summation convention
result = np.einsum('ij,jk->ik', A, B)

# Print the result
print(result)
