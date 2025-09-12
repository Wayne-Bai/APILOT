import numpy as np

# Define a matrix a (in this example, a 3x3 matrix)
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 10]])

# Perform QR factorization of the matrix a
q, r = np.linalg.qr(a)

# Print the orthogonal matrix q and the upper triangular matrix r
print("Orthogonal matrix q:")
print(q)
print("\nUpper triangular matrix r:")
print(r)
