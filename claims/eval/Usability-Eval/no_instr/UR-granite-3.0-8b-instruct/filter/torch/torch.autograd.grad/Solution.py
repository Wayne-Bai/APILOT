import torch

def compute_gradient_sum(outputs, inputs):
    # Compute gradients of outputs with respect to inputs
    gradients = torch.autograd.grad(outputs, inputs, create_graph=True)

    # Sum the gradients
    gradient_sum = sum(gradients)

    return gradient_sum
