import numpy as np

# Creating a complex Hermitian matrix (conjugate symmetric)
# The matrix can be of any size, but we'll create a 3x3 matrix for simplicity
matrix = np.array([[1 + 2j, 3 - 4j, 5 + 6j],
                   [3 + 4j, 7 - 8j, 9 + 10j],
                   [5 - 6j, 9 + 10j, 11 - 12j]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Print eigenvalues
print("Eigenvalues: ", eigenvalues)

# Print eigenvectors
print("Eigenvectors: ", eigenvectors)

# Creating a real symmetric matrix
matrix_symmetric = np.array([[1, 2, 3],
                             [2, 4, 5],
                             [3, 5, 6]])
matrix_symmetric_T = np.transpose(matrix_symmetric)
np.testing.assert_array_almost_equal(matrix_symmetric, matrix_symmetric_T)

# Compute eigenvalues and eigenvectors of real symmetric matrix
eigenvalues_symmetric, eigenvectors_symmetric = np.linalg.eig(matrix_symmetric)

# Print eigenvalues
print("Eigenvalues of Real Symmetric Matrix: ", eigenvalues_symmetric)

# Print eigenvectors
print("Eigenvectors of Real Symmetric Matrix: ", eigenvectors_symmetric)
