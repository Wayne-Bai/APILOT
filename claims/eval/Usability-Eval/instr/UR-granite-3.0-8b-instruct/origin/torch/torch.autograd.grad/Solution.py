import torch

def sum_gradients(outputs, inputs):
    # Compute gradients of outputs with respect to inputs
    gradients = torch.autograd.grad(outputs, inputs, create_graph=True)

    # Sum the gradients
    sum_gradients = torch.sum(torch.stack(gradients), dim=0)

    return sum_gradients
