import numpy as np

# Let's assume we have a 3x4 matrix
# In real scenarios, you would replace this with your own data
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Perform Singular Value Decomposition (SVD)
U, s, Vh = np.linalg.svd(A)

print("Matrix A:")
print(A)
print("\nMatrix U (Left Singular Vectors):")
print(U)

print("\nSingular values:")
print(s)

print("\nMatrix Vh (Right Singular Vectors) Transpose:")
print(Vh)

# You can also get the Matrix V by Transpose of Vh
V = Vh.T

print("\nMatrix V (Right Singular Vectors):")
print(V)

# Let's verify if A can be reconstructed from U and V
# The product of U, Diagonal matrix s and Vh should equal A
reconstructed_A = np.dot(U, np.dot(np.diag(s), Vh))
print("\nReconstructed Matrix A:")
print(reconstructed_A)
