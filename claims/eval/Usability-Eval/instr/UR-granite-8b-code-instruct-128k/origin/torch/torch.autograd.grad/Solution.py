import torch

def sum_of_gradients(outputs, inputs):
    gradients = torch.autograd.grad(outputs, inputs)
    return sum(gradients)
