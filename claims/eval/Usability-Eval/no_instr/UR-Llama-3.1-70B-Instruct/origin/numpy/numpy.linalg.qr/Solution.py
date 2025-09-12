import numpy as np

# Define a matrix 'a'
a = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])

# Compute the qr factorization of the matrix 'a'
q, r = np.linalg.qr(a)

# Print the original matrix 'a'
print("Original Matrix 'a':")
print(a)

# Print the orthonormal matrix 'q'
print("\nOrthonormal Matrix 'q':")
print(q)

# Print the upper-triangular matrix 'r'
print("\nUpper-Triangular Matrix 'r':")
print(r)

# Verify that qr equals the original matrix 'a'
# (up to numerical precision)
print("\nVerification that qr equals 'a':")
print(np.allclose(np.dot(q, r), a))
