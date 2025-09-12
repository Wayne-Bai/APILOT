import torch

def function(x):
    """ Define some arbitrary differentiable function """
    return torch.sin(x) * torch.log(x + 2)

def analytical_second_derivative(x):
    """ Compute the second derivative analytically for the given function """
    return torch.cos(x) / (x + 2) - torch.sin(x) / (x + 2)**2 - 2 * torch.sin(x) / (x + 2)**3

def finite_difference_second_derivative(x, eps=1e-5):
    """ Compute the second derivative using finite differences for the given function """
    x.requires_grad = True
    y = function(x)
    y.backward(create_graph=True)
    grad = x.grad

    x_p = x + eps
    grad_p = torch.autograd.grad(function(x_p), x_p, create_graph=True)[0]

    x_m = x - eps
    grad_m = torch.autograd.grad(function(x_m), x_m, create_graph=True)[0]

    second_derivative = (grad_p - grad_m) / (2 * eps)
    return second_derivative

# Select a tensor value for x
x = torch.tensor(1.0, requires_grad=True)

# Compute second derivatives
analytical = analytical_second_derivative(x)
finite_diff = finite_difference_second_derivative(x)

print('Analytical Second Derivative:', analytical)
print('Finite Differences Second Derivative:', finite_diff)
