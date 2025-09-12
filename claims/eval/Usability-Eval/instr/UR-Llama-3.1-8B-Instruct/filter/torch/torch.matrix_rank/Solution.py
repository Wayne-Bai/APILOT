import torch
import numpy as np
from torch import linalg

# Define a function to compute the numerical rank of a matrix
def numerical_rank(matrix, tol=1e-7):
    """
    Compute the numerical rank of a matrix.

    Args:
        matrix (Tensor): Input matrix.
        tol (float, optional): Tolerance for singular value decomposition. Defaults to 1e-7.

    Returns:
        int: The numerical rank of the matrix.
    """
    # Ensure the input matrix is a tensor
    if not isinstance(matrix, torch.Tensor):
        matrix = torch.tensor(matrix)

    # Perform singular value decomposition
    u, s, vh = linalg.svd(matrix)

    # Sort the singular values in descending order
    idx = s.argsort(descending=True)
    u = u[:, idx]
    s = s[idx]
    vh = vh[idx, :]

    # Compute the numerical rank
    rank = torch.sum(s > tol)

    return int(rank)

# Example usage:
matrix = np.random.rand(5, 5)
matrix_tensor = torch.tensor(matrix)

rank = numerical_rank(matrix_tensor)
print("Numerical rank of the matrix:", rank)
