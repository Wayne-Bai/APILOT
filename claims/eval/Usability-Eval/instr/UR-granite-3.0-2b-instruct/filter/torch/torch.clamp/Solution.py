import torch

def clamp(tensor, min, max):
    return torch.clamp(tensor, min, max)
