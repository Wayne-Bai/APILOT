import numpy as np

# Example matrix 'a'
a = np.array([[12, -51, 4],
              [6, 167, -68],
              [-4, 24, -41]])

# Compute the QR factorization
q, r = np.linalg.qr(a)

print("Q matrix (orthonormal):")
print(q)
print("\nR matrix (upper triangular):")
print(r)
