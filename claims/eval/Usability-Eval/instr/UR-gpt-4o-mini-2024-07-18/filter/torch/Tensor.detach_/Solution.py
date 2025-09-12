import torch

# Create a tensor and enable gradient tracking
tensor = torch.randn(3, 3, requires_grad=True)

# Detach the tensor from the graph
detached_tensor = tensor.detach()

# Print the original and detached tensors
print("Original Tensor:", tensor)
print("Detached Tensor:", detached_tensor)
print("Is Detached Tensor a leaf?", detached_tensor.is_leaf)  # This should return True
