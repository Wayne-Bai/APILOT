
import numpy as np

# Create a random matrix
A = np.random.rand(5, 5)

# Compute the QR factorization
Q, R = np.linalg.qr(A)

print("Matrix Q (orthonormal):")
print(Q)
print("\nMatrix R (upper triangular):")
print(R)
