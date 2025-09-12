import torch

# Define the tensors as leaves
x = torch.tensor(1.0, requires_grad=True)
y = torch.tensor(2.0, requires_grad=True)

# Define a function of x and y
z = x * y + x**2

# Compute the gradients of z with respect to x and y
z.backward()

# Get the sum of gradients of the leaves
gradient_sum = x.grad + y.grad
print("Sum of gradients:", gradient_sum)
