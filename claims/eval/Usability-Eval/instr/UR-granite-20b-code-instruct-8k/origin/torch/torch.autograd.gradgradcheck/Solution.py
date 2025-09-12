import torch

# Define the function for which we want to check the gradients
def my_function(x):
    return x**2

# Define the input tensor for which we want to check the gradients
x = torch.tensor([1.0], requires_grad=True)

# Compute the gradients of the function wrt to the input tensor
y = my_function(x)
y.backward()

# Compute the gradients of the gradients using small finite differences
grad_finite_diff = torch.grad(y, x, grad_outputs=torch.ones_like(y), create_graph=True)[0]

# Compute the analytical gradients
grad_analytical = 2 * x

# Check if the gradients are equal
print((grad_finite_diff - grad_analytical).abs().max())
