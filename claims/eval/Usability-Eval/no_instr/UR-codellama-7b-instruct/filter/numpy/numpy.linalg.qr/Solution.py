
import numpy as np

# Generate a random matrix
a = np.random.rand(3, 3)

# Compute the QR factorization of a using the Gram-Schmidt process
qr = np.linalg.qr(a)

# Extract the orthogonal matrix q and the upper-triangular matrix r
q, r = qr

print("Q:")
print(q)

print("\nR:")
print(r)
