import torch

# Create a tensor and enable gradient tracking
tensor = torch.randn(3, 3, requires_grad=True)

# Detach the tensor from the graph
detached_tensor = tensor.detach()

# Print the tensors
print("Original tensor:")
print(tensor)
print("Detached tensor (leaf):")
print(detached_tensor)
