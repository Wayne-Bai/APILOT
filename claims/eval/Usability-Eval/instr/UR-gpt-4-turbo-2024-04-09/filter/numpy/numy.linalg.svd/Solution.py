import numpy as np

# Example matrix
A = np.array([[1, 2], [3, 4], [5, 6]])

# Performing Singular Value Decomposition
U, s, Vt = np.linalg.svd(A)

print("U (left singular vectors):")
print(U)
print("s (singular values):")
print(s)
print("Vt (right singular vectors):")
print(Vt)
