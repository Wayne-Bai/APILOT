import torch

def logspace(start, end, steps, base=10.0):
    return torch.logspace(start, end, steps, base)
