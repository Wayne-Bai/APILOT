import torch

def sum_gradients(outputs, inputs):
    grads = torch.autograd.grad(outputs, inputs, create_graph=True)
    return sum(grad.flatten().sum().item() for grad in grads)
