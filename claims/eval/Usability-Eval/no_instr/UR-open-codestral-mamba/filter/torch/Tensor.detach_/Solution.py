import torch

# Create a tensor
tensor = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Perform some operation
new_tensor = tensor * 2

# Detach the tensor
detached_tensor = new_tensor.detach()

# Print the detached tensor
print(detached_tensor)
