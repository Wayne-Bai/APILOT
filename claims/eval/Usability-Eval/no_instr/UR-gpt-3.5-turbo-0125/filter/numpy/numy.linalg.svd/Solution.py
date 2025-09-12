
import numpy as np

# Create a 2D array for example
A = np.array([[4, 11, 14], [8, 7, -2]])

# Perform Singular Value Decomposition
U, S, V = np.linalg.svd(A)

print("Matrix U:")
print(U)

print("\nMatrix S:")
print(np.diag(S))

print("\nMatrix V:")
print(V)
