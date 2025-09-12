import torch

# Create a tensor of size 3x3
A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Compute the eigenvalue decomposition
eig_vals, eig_vecs = torch.eig(A, eigenvectors=True)

# Print the eigenvalues and eigenvectors
print("Eigenvalues:")
print(eig_vals)
print("Eigenvectors:")
print(eig_vecs)
