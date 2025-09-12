import torch

def eigenvalue_decomposition(matrix):
    # Check if the input is a square matrix
    if matrix.size(0) != matrix.size(1):
        raise ValueError("Input matrix must be square.")

    # Compute the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = torch.linalg.eig(matrix)

    return eigenvalues, eigenvectors

# Example usage:
matrix = torch.tensor([[1, 2], [3, 4]])
eigenvalues, eigenvectors = eigenvalue_decomposition(matrix)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
