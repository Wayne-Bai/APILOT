import torch

# Create example tensors and make them require gradients
x = torch.tensor(2.0, requires_grad=True)
y = torch.tensor(3.0, requires_grad=True)

# Define an example function of x and y
z = x ** 2 + y ** 3

# Compute gradients with respect to both x and y graph leaves
z.backward()

# Sum of gradients for each leaf
total_gradient_sum = x.grad + y.grad

# Output the sum of gradients
print("Sum of gradients:", total_gradient_sum.item())
