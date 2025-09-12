import torch

def sum_of_gradients(outputs, inputs):
    # Ensure inputs require grad
    inputs.requires_grad_(True)
    
    # Compute gradients of outputs with respect to inputs
    grads = torch.autograd.grad(outputs, inputs, grad_outputs=torch.ones_like(outputs), create_graph=True)
    
    # Sum the gradients
    gradients_sum = sum(grads)
    
    return gradients_sum

# Example usage:
# Define inputs and a simple function as outputs
x = torch.randn((2, 3), requires_grad=True)
outputs = x ** 2 + 3 * x + 2

# Call the function with outputs and inputs
gradient_sum = sum_of_gradients(outputs, x)
print(gradient_sum)
