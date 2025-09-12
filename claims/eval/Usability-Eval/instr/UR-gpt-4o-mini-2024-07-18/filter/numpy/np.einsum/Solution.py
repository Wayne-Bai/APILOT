import numpy as np

# Example arrays
A = np.random.rand(3, 4)  # 3x4 matrix
B = np.random.rand(4, 2)  # 4x2 matrix

# Evaluate the Einstein summation convention for matrix multiplication
result = np.einsum('ij,jk->ik', A, B)

print(result)
