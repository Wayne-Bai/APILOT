# Import necessary libraries
import torch

# Create a tensor
tensor = torch.randn(3, 3, requires_grad=True)

# Print the tensor's requires_grad attribute
print("Before detach():", tensor.requires_grad)

# Detach the tensor from the graph
detached_tensor = tensor.detach()

# Print the detached tensor's requires_grad attribute
print("After detach():", detached_tensor.requires_grad)
