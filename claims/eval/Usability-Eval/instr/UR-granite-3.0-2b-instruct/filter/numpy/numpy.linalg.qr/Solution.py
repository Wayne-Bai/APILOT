import numpy as np

# Define the matrix
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Compute the QR factorization
Q, R = np.linalg.qr(a)

# Print the results
print("Q:\n", Q)
print("R:\n", R)
