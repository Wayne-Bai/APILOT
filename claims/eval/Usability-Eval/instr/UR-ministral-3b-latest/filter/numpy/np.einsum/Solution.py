import numpy as np

# Define two matrices
A = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])

B = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Calculate the Einstein summation convention using NumPy
C = np.einsum('ij,ij->ij', A, A)
C = np.einsum('ij,ij->ij', C, B)

print(C)
