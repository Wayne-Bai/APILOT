import numpy as np

# Define a matrix for which we will compute the QR factorization
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 10]], dtype=float)

# Compute the QR factorization using the QR decomposition
Q, R = np.linalg.qr(A)

# Print the original matrix A
print("Original Matrix A:")
print(A)

# Print the Q matrix
print("\nQ matrix:")
print(Q)

# Print the R matrix
print("\nR matrix:")
print(R)
