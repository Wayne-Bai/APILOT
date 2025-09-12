
import numpy as np

# Define the operands
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# Define the Einstein summation convention expression
# Example expression: C[i,j] = A[i,k] * B[k,j]
C = np.einsum('ik,kj->ij', A, B)

print(C)
