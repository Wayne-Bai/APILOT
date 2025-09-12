import torch

def eigen_decomposition(A):
    # Check if the matrix is square
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square")

    # Compute the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = torch.symeig(A)

    return eigenvalues, eigenvectors
