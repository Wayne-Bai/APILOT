
import numpy as np

# Example matrix
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Compute QR factorization
q, r = np.linalg.qr(a)

print("Q matrix:")
print(q)
print("R matrix:")
print(r)
