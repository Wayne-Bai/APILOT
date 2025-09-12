import numpy as np

# Define a matrix
a = np.array([[3, 2, 1],
              [2, -1, 0],
              [1, 0, -1]])

# Compute the QR factorization
Q, R = np.linalg.qr(a)

# Print the results
print("Q:")
print(Q)
print("R:")
print(R)
