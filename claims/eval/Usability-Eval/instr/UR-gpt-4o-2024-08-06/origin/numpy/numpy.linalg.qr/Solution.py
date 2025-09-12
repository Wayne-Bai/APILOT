import numpy as np

# Example matrix to factor
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Compute the QR factorization
Q, R = np.linalg.qr(A)

print("Matrix A:")
print(A)
print("\nOrthogonal matrix Q:")
print(Q)
print("\nUpper triangular matrix R:")
print(R)
