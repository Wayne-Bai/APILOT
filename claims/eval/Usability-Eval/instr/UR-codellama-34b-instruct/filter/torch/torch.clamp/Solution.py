
import torch

def clamp(input, min, max):
    return torch.clamp(input, min, max)
