import torch

def sum_of_gradients(tensors):
    grad_sum = torch.sum(torch.stack([tensor.grad for tensor in tensors]))
    return grad_sum
