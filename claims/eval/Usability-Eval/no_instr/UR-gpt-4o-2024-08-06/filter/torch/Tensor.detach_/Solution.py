import torch

# Create a tensor that requires a gradient
tensor = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Perform some operations
result = tensor * 2

# Detach the tensor from the current computation graph
detached_tensor = result.detach()

# Check if the tensor is detached and a leaf
print("Is detached_tensor detached?", not detached_tensor.requires_grad)
print("Is detached_tensor a leaf?", detached_tensor.is_leaf)
