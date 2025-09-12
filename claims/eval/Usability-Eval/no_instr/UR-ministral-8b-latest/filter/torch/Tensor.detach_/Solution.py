import torch

# Create a tensor that requires gradients
x = torch.tensor([1.0], requires_grad=True)

# Perform some operations on the tensor
y = (x + 2) ** 2

# Print the tensor to verify it is requiring gradients
print(y.requires_grad)

# Detach the tensor, making it a leaf
z = y.detach()

# Print the detached tensor to verify it's not requiring gradients
print(z.requires_grad)

# Print z to ensure it has been detached correctly
print(z)
