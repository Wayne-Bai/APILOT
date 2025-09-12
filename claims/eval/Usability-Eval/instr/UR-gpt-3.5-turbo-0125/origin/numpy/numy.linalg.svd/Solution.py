
import numpy as np

# Data for SVD
A = np.array([[1, 2], [3, 4], [5, 6]])

# Perform Singular Value Decomposition
U, S, Vt = np.linalg.svd(A)

print("U:")
print(U)
print("\nSingular Values:")
print(np.diag(S))
print("\nV transpose:")
print(Vt)
