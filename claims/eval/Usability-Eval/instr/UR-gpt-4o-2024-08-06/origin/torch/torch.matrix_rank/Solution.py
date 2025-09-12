import torch

def compute_matrix_rank(matrix, tol=1e-10):
    """
    Computes the numerical rank of a matrix using its singular values.
    
    Parameters:
    - matrix: A 2-D tensor
    - tol: A threshold below which singular values are considered as zero
    
    Returns:
    - rank: The numerical rank of the matrix
    """
    # Compute singular values using SVD
    _, S, _ = torch.linalg.svd(matrix)
    
    # Count the number of singular values greater than the tolerance
    rank = torch.sum(S > tol).item()
    return rank

# Example usage:
matrix = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
rank = compute_matrix_rank(matrix)
print(f"The numerical rank of the matrix is: {rank}")
