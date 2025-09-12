import numpy as np

# Define a complex Hermitian matrix
matrix = np.array([[1+2j, 3+4j], [3-4j, 5+6j]])

# Find the eigenvalues and eigenvectors of the matrix
eigenvalues, eigenvectors = np.linalg.eig(matrix)

print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)
