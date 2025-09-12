
import torch

def numerical_rank(matrix):
    _, s, _ = torch.svd(matrix)
    rank = torch.sum(s > 1e-10).item()
    return rank

# Example usage
matrix = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
rank = numerical_rank(matrix)
print("Numerical rank of the matrix:", rank)
