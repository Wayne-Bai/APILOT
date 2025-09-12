import torch

def compute_numerical_rank(matrix, tol=1e-10):
    """
    Computes the numerical rank of a given matrix.

    Parameters:
    matrix (torch.Tensor): The input matrix.
    tol (float): Tolerance level for considering singular values as zero.

    Returns:
    int: The numerical rank of the matrix.
    """
    # Compute the singular values of the matrix
    _, singular_values, _ = torch.linalg.svd(matrix, full_matrices=False)
    
    # Determine the number of singular values greater than the tolerance
    rank = torch.sum(singular_values > tol)
    
    return rank.item()

# Example usage:
matrix = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
rank = compute_numerical_rank(matrix)
print(f"The numerical rank of the matrix is: {rank}")
