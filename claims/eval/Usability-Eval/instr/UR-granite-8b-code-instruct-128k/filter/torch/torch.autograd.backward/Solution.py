
import torch

def compute_grad_sum(tensors):
    grad_sum = 0
    for tensor in tensors:
        grad_sum += torch.sum(tensor.grad)
    return grad_sum
