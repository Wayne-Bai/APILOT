import numpy as np

# Define a complex Hermitian matrix (conjugate symmetric)
def create_matrix(n):
    matrix = np.array([[1 + 1j, 1 - 2j, 2 + 3j],
                       [1 + 2j, 4, 1 - 4j],
                       [2 - 3j, 1 + 4j, 5]])
    return matrix

# Define a real symmetric matrix
def create_real_symmetric_matrix(n):
    matrix = np.array([[1, 2, 3],
                       [2, 4, 5],
                       [3, 5, 6]])
    return matrix

# Function to return eigenvalues and eigenvectors of a matrix
def eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

# Create a matrix and get its eigenvalues and eigenvectors
matrix = create_matrix(3)
print("Eigenvalues of the complex Hermitian matrix:")
eigenvalues, eigenvectors = eigenvectors(matrix)
print("Eigenvalues:", eigenvalues)

print("\nEigenvectors of the complex Hermitian matrix:")
print(eigenvectors)

# Create a real symmetric matrix and get its eigenvalues and eigenvectors
matrix = create_real_symmetric_matrix(3)
print("\nEigenvalues of the real symmetric matrix:")
eigenvalues, eigenvectors = eigenvectors(matrix)
print("Eigenvalues:", eigenvalues)

print("\nEigenvectors of the real symmetric matrix:")
print(eigenvectors)
