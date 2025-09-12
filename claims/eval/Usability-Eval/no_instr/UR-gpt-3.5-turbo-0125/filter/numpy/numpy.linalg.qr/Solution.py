
import numpy as np

# Define a matrix 'a'
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Compute the QR factorization of matrix 'a'
q, r = np.linalg.qr(a)

print("Matrix Q (Orthonormal):")
print(q)
print("\nMatrix R (Upper Triangular):")
print(r)
