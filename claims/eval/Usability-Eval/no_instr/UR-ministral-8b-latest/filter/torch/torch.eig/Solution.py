import torch

# Function to compute the eigenvalue decomposition of a square matrix
def eigenvalue_decomposition(matrix):
    # Check if the matrix is square
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("The input matrix must be square")

    # Compute the eigenvalue decomposition
    eigen_values, eigen_vectors = torch.eig(matrix, eigenvectors=True)

    # Return the eigenvalues and eigenvectors
    return eigen_values, eigen_vectors

# Example usage
matrix = torch.tensor([[4, -2], [-2, 4]])
eigen_values, eigen_vectors = eigenvalue_decomposition(matrix)

# Print the eigenvalues and eigenvectors
print("Eigenvalues:\n", eigen_values)
print("Eigenvectors:\n", eigen_vectors)
