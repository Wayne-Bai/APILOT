import numpy as np

# Define the operands
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

# Evaluate the Einstein summation convention
C = np.einsum('ij,jk->ik', A, B)

print(C)
