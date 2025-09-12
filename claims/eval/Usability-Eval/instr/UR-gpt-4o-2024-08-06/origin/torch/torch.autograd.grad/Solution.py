import torch

# Define a simple function for which we want to compute gradients
def simple_function(x):
    return x ** 2 + 3 * x + 5

# Initialize a tensor with requires_grad=True to track computations
x = torch.tensor(2.0, requires_grad=True)

# Compute the output using the function
output = simple_function(x)

# Compute the gradients
output.backward()

# Get the gradient of the output with respect to the input
gradient_sum = x.grad

# Print the computed gradient
print(f"The computed gradient is: {gradient_sum}")
