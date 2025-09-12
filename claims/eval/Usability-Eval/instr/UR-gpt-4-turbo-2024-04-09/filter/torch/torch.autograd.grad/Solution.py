import torch

# Define the input tensor and requires gradient computation
input_tensor = torch.randn(3, requires_grad=True)

# Define the function for which the gradient is to be calculated
output = input_tensor ** 2 + 3 * input_tensor + 2

# Compute the gradients
output.sum().backward()

# Output the gradients with respect to the inputs
print(input_tensor.grad)
