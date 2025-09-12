import torch

def compute_gradient_sum(outputs, inputs):
    # compute gradients of the outputs with respect to inputs
    grads = torch.autograd.grad(outputs, inputs, create_graph=True)
    # compute sum of the gradients
    gradient_sum = sum([grad.sum() for grad in grads])
    return gradient_sum
