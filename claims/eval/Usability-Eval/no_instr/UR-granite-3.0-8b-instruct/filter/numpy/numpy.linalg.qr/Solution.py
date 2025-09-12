import numpy as np

# Assuming a is your matrix
a = np.array([[1, 2], [3, 4]])

# Compute the QR factorization
q, r = np.linalg.qr(a)

print("Q = \n", q)
print("R = \n", r)
