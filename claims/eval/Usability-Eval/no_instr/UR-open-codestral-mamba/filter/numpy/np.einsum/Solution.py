import numpy as np

# Define the operands
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Evaluate the Einstein summation convention and obtain the result
result = np.einsum('ij,jk->ik', A, B)

result
