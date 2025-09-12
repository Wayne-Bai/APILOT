import numpy as np

# Input matrix
A = np.array([[1, 2, 3],
              [0, 4, 5],
              [0, 0, 2]])

# Compute qr factorization
Q, R = np.linalg.qr(A)
print("Q:\n", Q)
print("R:\n", R)
