import numpy as np

# Define a matrix 'a'
a = np.array([[1, 2], [3, 4], [5, 6]])

# Use the 'qr' function to perform QR factorization
q, r = np.linalg.qr(a)

# Display the matrices
print("Q matrix:")
print(q)
print("R matrix:")
print(r)
