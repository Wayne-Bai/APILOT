import torch

# Create a tensor with requires_grad=True to track operations on it
tensor = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Perform some operations on the tensor
result = tensor * 2

# Detach the tensor from the computational graph
detached_tensor = result.detach()

# Print the detached tensor
print(detached_tensor)

# Ensure the detached tensor is a leaf
print(detached_tensor.is_leaf)  # Should print True
