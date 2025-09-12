import torch

def create_one_dimensional_tensor(start, end, steps):
    return torch.linspace(start, end, steps)
