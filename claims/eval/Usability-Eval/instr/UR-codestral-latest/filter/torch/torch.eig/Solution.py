import torch

def eigenvalue_decomposition(matrix):
    eigenvalues, eigenvectors = torch.eig(matrix, eigenvectors=True)
    return eigenvalues, eigenvectors
