import numpy as np

# Define the matrix 'a'
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Compute the QR factorization
q, r = np.linalg.qr(a)

# Print the results
print("Q:\n", q)
print("R:\n", r)
