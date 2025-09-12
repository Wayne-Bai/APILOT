import torch

# Define inputs
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = torch.tensor([4.0, 5.0, 6.0], requires_grad=True)

# Define the forward function
def forward(x, y):
    out = x + y
    return out

# Compute the forward pass
out = forward(x, y)

# Define the backward pass
out.sum().backward()

# Get gradients of inputs
grad_x = x.grad
print('Gradient of x:', grad_x)
grad_y = y.grad
print('Gradient of y:', grad_y)

# Get the sum of gradients
sum_of_gradients = grad_x.sum() + grad_y.sum()
print('Sum of gradients:', sum_of_gradients)
