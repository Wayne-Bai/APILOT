import numpy as np

# Example operands
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Einstein summation convention on the operands
result = np.einsum('ij,jk->ik', A, B)

print(result)
