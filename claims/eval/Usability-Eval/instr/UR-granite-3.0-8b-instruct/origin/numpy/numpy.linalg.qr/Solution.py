import numpy as np

# Define the matrix a
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Compute the qr factorization
q, r = np.linalg.qr(a)

print("Q matrix:")
print(q)
print("\nR matrix:")
print(r)
