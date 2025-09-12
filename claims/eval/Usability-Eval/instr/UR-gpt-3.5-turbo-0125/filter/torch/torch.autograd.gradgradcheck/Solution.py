
import torch

# Create the input tensor with requires_grad=True
inputs = torch.randn(3, 4, requires_grad=True)

# Create the grad_outputs tensor with requires_grad=True
grad_outputs = torch.randn(3, 4, requires_grad=True)

# Define the function for which gradients need to be computed
def my_function(x):
    return x ** 2 + 2 * x + 1

# Compute the analytical gradients
outputs = my_function(inputs)
torch.autograd.grad(outputs, inputs, grad_outputs=grad_outputs, create_graph=True)

# Compute the gradients of gradients using small finite differences
grads = torch.autograd.grad(outputs, inputs, grad_outputs=grad_outputs)
for i in range(len(inputs)):
    grad_input = grads[i]
    grad_grad_output = torch.autograd.grad(grad_input, inputs, grad_outputs=grad_outputs, retain_graph=True)
    print("Gradients of gradients for input ", i, ":", grad_grad_output)

