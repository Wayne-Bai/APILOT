import torch

def create_tensor(start, end, steps):
    tensor = torch.linspace(start, end, steps)
    return tensor
