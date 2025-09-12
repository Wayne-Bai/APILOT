
import numpy as np

# Define a Hermitian matrix
A = np.array([[4, 1 + 2j, 3 - 1j],
              [1 - 2j, 5, 2],
              [3 + 1j, 2, 6]])

# Compute the pseudo-inverse of the Hermitian matrix using numpy
A_inv = np.linalg.pinv(A)

print("Pseudo-Inverse of the Hermitian matrix:")
print(A_inv)
