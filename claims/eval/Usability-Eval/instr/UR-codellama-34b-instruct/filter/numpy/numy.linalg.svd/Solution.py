
import numpy as np

# Define the matrix to be decomposed
A = np.array([[1, 2], [3, 4]])

# Perform the SVD decomposition
U, sigma, Vt = np.linalg.svd(A)

# Print the results
print("U:")
print(U)
print("sigma:")
print(sigma)
print("Vt:")
print(Vt)
