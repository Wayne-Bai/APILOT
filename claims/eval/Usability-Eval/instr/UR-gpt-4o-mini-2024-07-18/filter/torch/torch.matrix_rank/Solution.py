import torch

def numerical_rank(matrix, epsilon=1e-10):
    # Compute the Singular Value Decomposition (SVD)
    U, S, Vh = torch.svd(matrix)
    
    # Count the significant singular values
    rank = (S > epsilon).sum().item()
    
    return rank

# Example usage
matrix = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
rank = numerical_rank(matrix)
print(f"The numerical rank of the matrix is: {rank}")
