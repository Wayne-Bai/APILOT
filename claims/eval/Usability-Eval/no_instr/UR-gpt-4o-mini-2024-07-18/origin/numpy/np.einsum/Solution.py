import numpy as np

# Define two example arrays (tensors) to evaluate using Einstein summation convention
A = np.array([[1, 2, 3], 
              [4, 5, 6]])

B = np.array([[7, 8], 
              [9, 10], 
              [11, 12]])

# Use np.einsum to perform the summation: for example, summing over the last axis of A and the first axis of B
result = np.einsum('ij,jk->ik', A, B)

print(result)
