import torch

def numerical_rank(matrix):
    matrix = torch.cast(matrix, torch.float32)
    u, s, vh = torch.svd(matrix)
    s = torch.diag(s)
    numerical_rank = torch.sum(s > 1e-10)
    return numerical_rank

# Example usage:
matrix = torch.randn(10, 10)
print("Numerical rank of the matrix:", numerical_rank(matrix))
