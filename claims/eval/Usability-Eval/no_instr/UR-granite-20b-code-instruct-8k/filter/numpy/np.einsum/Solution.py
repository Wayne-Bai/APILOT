import numpy as np

# Define the operands
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Define the subscript string
subscript = 'ij,jk->ik'

# Evaluate the Einstein summation convention
result = np.einsum(subscript, A, B)

print(result)
