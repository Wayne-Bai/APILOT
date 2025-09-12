import numpy as np

# Function to calculate eigenvalues and eigenvectors of a symmetric matrix
def symmetric_eig(matrix):
    # Check if the matrix is symmetric
    if np.allclose(matrix, np.transpose(matrix)):
        # Calculate eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        return eigenvalues, eigenvectors
    else:
        raise ValueError("The matrix is not symmetric.")

# Example usage:
matrix = np.array([[1, 2+3j], [2-3j, 4]])
eigenvalues, eigenvectors = symmetric_eig(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
