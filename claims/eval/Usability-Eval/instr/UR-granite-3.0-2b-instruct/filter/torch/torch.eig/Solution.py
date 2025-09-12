import torch

def compute_eigen_decomposition(matrix):
    # Check if the matrix is square
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square to compute eigenvalue decomposition.")

    # Compute the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = torch.eig(matrix)

    return eigenvalues, eigenvectors
