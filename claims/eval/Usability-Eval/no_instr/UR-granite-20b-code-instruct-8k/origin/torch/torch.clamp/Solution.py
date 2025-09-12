
import torch

def clamp_tensor(input, min, max):
    return torch.clamp(input, min, max)
