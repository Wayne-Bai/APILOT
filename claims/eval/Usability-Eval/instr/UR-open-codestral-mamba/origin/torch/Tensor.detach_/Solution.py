import torch

# Create a tensor
tensor = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Perform some operations on the tensor
tensor = tensor * 2

# Detach the tensor from the computational graph
detached_tensor = tensor.detach()

# Now you can perform operations on the detached tensor without tracking gradients
detached_tensor.requires_grad
# Output: False
