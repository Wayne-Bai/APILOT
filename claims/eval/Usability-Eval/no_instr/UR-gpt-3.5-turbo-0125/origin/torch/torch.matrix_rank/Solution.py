
import torch

def numerical_rank(matrix):
    u, s, v = torch.svd(matrix)
    threshold = s.max() * max(matrix.size()) * torch.finfo(s.dtype).eps
    rank = torch.sum(s > threshold)
    
    return rank

# Example usage
matrix = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=torch.float)
rank = numerical_rank(matrix)
print("Numerical rank of the matrix:", rank.item())
