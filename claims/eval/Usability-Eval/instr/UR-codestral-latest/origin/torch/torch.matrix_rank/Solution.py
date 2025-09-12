import torch

def compute_rank(A):
    _, s, _ = torch.svd(A)
    rank = torch.sum(s > 1e-10)
    return rank.item()

# Usage
A = torch.randn(3, 4)
print(compute_rank(A))
