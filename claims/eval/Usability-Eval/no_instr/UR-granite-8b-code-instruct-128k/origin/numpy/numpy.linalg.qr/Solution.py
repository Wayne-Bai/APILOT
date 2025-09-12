import numpy as np

# Define the matrix a
a = np.array([[1, 2], [3, 4]])

# Compute the qr factorization of a
q, r = np.linalg.qr(a)

# Print the orthonormal matrix q and the upper-triangular matrix r
print("Orthonormal matrix q:")
print(q)
print("Upper-triangular matrix r:")
print(r)