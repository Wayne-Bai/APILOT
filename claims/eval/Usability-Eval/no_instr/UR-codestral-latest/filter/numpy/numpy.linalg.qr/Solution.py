import numpy as np

# Define the matrix
A = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])

# Compute the QR factorization
q, r = np.linalg.qr(A)

# Print the matrices
print("Q:")
print(q)
print("\nR:")
print(r)
