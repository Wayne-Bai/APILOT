import numpy as np

# Let's take an example of a 2x2 Hermitian matrix
matrix = np.array([[1+2j, 3-4j], [3+4j, 1-2j]])

eigvals, eigvectors = np.linalg.eigh(matrix)

print("Eigenvalues: ", eigvals)
print("Eigenvectors: ", eigvectors)
