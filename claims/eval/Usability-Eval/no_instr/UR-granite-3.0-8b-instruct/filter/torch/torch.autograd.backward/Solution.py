import torch

def sum_gradients(tensors):
    total_grad = torch.zeros_like(tensors[0])
    for tensor in tensors:
        total_grad += tensor.grad.sum()
    return total_grad
