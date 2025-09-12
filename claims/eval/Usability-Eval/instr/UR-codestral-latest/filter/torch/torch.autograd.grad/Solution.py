import torch

# Initialize a random input tensor and set requires_grad to True
input_tensor = torch.randn(1, requires_grad=True)

# Define a function for which to compute the gradients
def func(x):
    return 2*x**2 + 3*x + 1

# Forward pass
output_tensor = func(input_tensor)

# Compute gradient
output_tensor.backward()

# The gradient of the output with respect to the input is stored in input_tensor.grad
grad_sum = torch.sum(input_tensor.grad)

print(f"The sum of gradients is: {grad_sum}")
