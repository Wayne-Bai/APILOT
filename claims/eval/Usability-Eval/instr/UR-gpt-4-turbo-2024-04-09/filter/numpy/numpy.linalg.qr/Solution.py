import numpy as np

# Define the matrix a
a = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# Compute the QR factorization of the matrix a
q, r = np.linalg.qr(a)

print("Matrix Q (orthonormal):")
print(q)
print("Matrix R (upper triangular):")
print(r)
