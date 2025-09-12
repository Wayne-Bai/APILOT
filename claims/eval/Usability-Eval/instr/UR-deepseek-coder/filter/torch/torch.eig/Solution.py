import torch

def eigenvalue_decomposition(matrix):
    # Ensure the input is a square matrix
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")
    
    # Compute the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = torch.linalg.eig(matrix)
    
    return eigenvalues, eigenvectors

# Example usage:
# matrix = torch.tensor([[4.0, 1.0], [1.0, 3.0]])
# eigenvalues, eigenvectors = eigenvalue_decomposition(matrix)
# print("Eigenvalues:", eigenvalues)
# print("Eigenvectors:", eigenvectors)
