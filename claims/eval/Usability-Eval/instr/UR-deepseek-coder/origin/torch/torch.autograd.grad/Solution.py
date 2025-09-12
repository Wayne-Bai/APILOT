import torch

def sum_of_gradients(outputs, inputs):
    # Ensure the inputs require gradients
    inputs = [input.requires_grad_(True) for input in inputs]
    
    # Compute the gradients
    gradients = torch.autograd.grad(outputs, inputs, grad_outputs=torch.ones_like(outputs), create_graph=True)
    
    # Sum the gradients
    sum_grads = sum(grad.sum() for grad in gradients)
    
    return sum_grads
