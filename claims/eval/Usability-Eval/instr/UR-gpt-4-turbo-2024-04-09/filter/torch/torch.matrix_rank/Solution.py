import torch

def numerical_rank(matrix, tol=1e-5):
    # Perform Singular Value Decomposition (SVD) to extract the singular values
    singular_values = torch.linalg.svdvals(matrix)
    # Count the number of singular values greater than the specified tolerance
    rank = torch.sum(singular_values > tol).item()
    return rank

# Example usage
A = torch.tensor([[1, 2, 3], [2, 3, 4], [3, 5, 6]], dtype=torch.float32)
rank = numerical_rank(A)
print("Rank of the matrix:", rank)
