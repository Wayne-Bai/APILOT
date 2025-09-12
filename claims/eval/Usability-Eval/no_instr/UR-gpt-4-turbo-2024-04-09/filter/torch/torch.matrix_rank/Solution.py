import torch

def compute_numerical_rank(matrix, tol=None):
    # Compute the Singular Value Decomposition (SVD) of the matrix
    singular_values = torch.linalg.svdvals(matrix)
    
    # By default, tolerance is set to the maximum singular value multiplied by max(matrix size) times eps.
    if tol is None:
        tol = torch.max(singular_values) * max(matrix.size()) * torch.finfo(singular_values.dtype).eps
    
    # Count the number of singular values greater than the tolerance to determine the rank
    rank = torch.sum(singular_values > tol).item()
    
    return rank

# Example usage:
A = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 10.0]])
rank_of_A = compute_numerical_rank(A)
print('Rank of matrix A:', rank_of_A)
