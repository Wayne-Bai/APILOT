import torch

# Define a simple function to test, e.g., a polynomial
def simple_function(x):
    return x ** 3 + 2 * x ** 2 + x

# Create input tensor with requires_grad=True
x = torch.tensor(2.0, requires_grad=True)

# Compute output using the function
output = simple_function(x)

# Backward pass to compute gradients
output.backward()

# Store the analytical gradient
analytical_grad = x.grad.item()

# Compute gradients using small finite differences
epsilon = 1e-6  # Small perturbation
x_perturb = x.detach().clone()  # Clone the tensor for perturbation
x_perturb.requires_grad = False  # Perturb version should not require grad

# Applying finite difference method
finite_diff_grad = (simple_function(x_perturb + epsilon) - simple_function(x_perturb - epsilon)) / (2 * epsilon)

# Check the gradients (analytical vs finite differences) match
print("Analytical Gradient: ", analytical_grad)
print("Finite Differences Gradient: ", finite_diff_grad.item())

# Check if they are close in value
if torch.isclose(torch.tensor(analytical_grad), finite_diff_grad, atol=1e-5):
    print("The gradients match!")
else:
    print("The gradients do not match.")
