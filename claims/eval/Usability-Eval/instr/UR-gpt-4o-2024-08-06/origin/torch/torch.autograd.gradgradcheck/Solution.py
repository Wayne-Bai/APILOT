import torch

# Define a simple function for which we want to check the gradients
def simple_function(x):
    return x ** 3 - 3 * x

# Function to perform finite difference approximation
def finite_difference_grad(func, x, eps=1e-6):
    x.requires_grad_(False)
    grad_approx = torch.zeros_like(x)
    for i in range(x.numel()):
        x_flat = x.view(-1)
        
        # Perturb positive
        x_flat[i] += eps
        f_pos = func(x).sum()
        
        # Perturb negative
        x_flat[i] -= 2 * eps
        f_neg = func(x).sum()

        # Restore original value
        x_flat[i] += eps

        # Finite difference approximation
        grad_approx.view(-1)[i] = (f_pos - f_neg) / (2 * eps)

    x.requires_grad_(True)
    return grad_approx

# Initialize tensor with requires_grad=True
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Compute analytical gradients using PyTorch
y = simple_function(x)
y.backward(torch.ones_like(x))
grad_analytical = x.grad

# Compute finite difference gradients
grad_approx = finite_difference_grad(simple_function, x)

# Compare the results
print("Analytical Gradients: ", grad_analytical)
print("Approximate Gradients: ", grad_approx)
