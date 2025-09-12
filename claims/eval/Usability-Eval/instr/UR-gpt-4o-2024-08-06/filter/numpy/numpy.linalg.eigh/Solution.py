import numpy as np

# Example of a Hermitian matrix
# For a real symmetric matrix, all elements would be real.
A = np.array([[1, 2j], [-2j, 3]])

# Calculate the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eigh(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)
