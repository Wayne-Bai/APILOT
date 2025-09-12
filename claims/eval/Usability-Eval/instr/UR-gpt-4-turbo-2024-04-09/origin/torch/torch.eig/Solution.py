import torch

def compute_eigen_decomposition(matrix):
    if matrix.size(0) != matrix.size(1):
        raise ValueError("Input must be a square matrix.")
    eigenvalues, eigenvectors = torch.linalg.eig(matrix)
    return eigenvalues, eigenvectors

# Example usage:
A = torch.tensor([[2.0, 0.0], [0.0, 3.0]], dtype=torch.float64)
eigenvalues, eigenvectors = compute_eigen_decomposition(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
