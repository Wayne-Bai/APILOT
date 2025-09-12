import torch

# Create a tensor with requires_grad=True
x = torch.tensor(3.0, requires_grad=True)

# Compute a function of x
y = x * x

# Compute the analytical gradient
y.grad = 2.0 * x

# Compute the gradient using small finite differences
h = 1e-5
x_plus = x + h
y_plus = x_plus * x_plus
x_minus = x - h
y_minus = x_minus * x_minus

gradient_fd = (y_plus - y_minus) / (2.0 * h)

# Print the analytical and finite difference gradients
print("Analytical gradient:", y.grad)
print("Finite difference gradient:", gradient_fd)
