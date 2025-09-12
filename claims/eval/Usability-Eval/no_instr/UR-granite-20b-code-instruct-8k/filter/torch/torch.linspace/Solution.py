import torch

def generate_evenly_spaced_tensor(start, end, steps):
    tensor = torch.linspace(start, end, steps)
    return tensor
