import torch

def compute_numerical_rank(matrix):
    # Convert the matrix to a tensor if it's a list or numpy array
    matrix_tensor = torch.tensor(matrix)

    # Compute the singular values using SVD
    u, s, v = torch.svd(matrix_tensor)

    # The numerical rank is the number of non-zero singular values
    rank = torch.sum(s > 0).item()

    return rank

# Example usage
matrix = [[1, 2], [3, 4]]
numerical_rank = compute_numerical_rank(matrix)
print(f"Numerical Rank: {numerical_rank}")
