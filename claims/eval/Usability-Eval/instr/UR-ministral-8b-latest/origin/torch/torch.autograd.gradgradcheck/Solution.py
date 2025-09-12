import torch

# Define a function for which you want to calculate second-order derivatives
def my_function(x):
    return x**3 + 4*x**2 + 6*x - 1

# Create a tensor with requires_grad=True
x = torch.tensor([2.0], requires_grad=True)

# Compute the first derivatives using requires_grad=True
y = my_function(x)
grad_outputs = torch.ones_like(y)
y.backward(gradient=grad_outputs)

# First derivative
first_derivative = x.grad

# Create a tensor with suitable support for second derivative computation
x.grad.requires_grad_( True )  # Re-enable requires_grad for x.grad

# Compute the second derivatives using analytical computations and finite differences
# Analytical second derivative
def analytical_second_derivative(func, input_tensor, grad, tolerance=1e-8):
    h = tolerance
    grad_unnorm = torch.autograd.grad(
        func, input_tensor, grad_outputs=grad, create_graph=True, only_inputs=True, retain_graph=True, grad_checkpointing=False)
    grad_unnorm = torch.autograd.grad(grad, input_tensor, grad_outputs=grad_unnorm, create_graph=True, only_inputs=True, retain_graph=True, grad_checkpointing=False)
    grad_unnorm = grad_unnorm[0]
    return grad_unnorm * grad_unnorm / h

analytic_second_derivative = analytical_second_derivative(my_function, x, grad_outputs)

# Finite difference second derivative
def finite_difference_second_derivative(func, x, step=1e-5):
    x_plus = torch.autograd.Variable(x.data, requires_grad=True) + step
    x_minus = torch.autograd.Variable(x.data, requires_grad=True) - step

    y_plus_clear = func(x_plus)
    y_minus_clear = func(x_minus)

    approximate_grad = (y_plus_clear - y_minus_clear) / (2 * step)
    return torch.autograd.grad(approximate_grad, [x_minus] + [x_plus])[0][0]

finite_second_derivative = finite_difference_second_derivative(my_function, x)

# Print the results
print("First Derivative (Analytical):", first_derivative)
print("Second Derivative (Analytical):", analytic_second_derivative)
print("Second Derivative (Finite Difference):", finite_second_derivative)

# Check agreement
print("Do the second derivatives agree?", torch.allclose(analytic_second_derivative, finite_second_derivative))
