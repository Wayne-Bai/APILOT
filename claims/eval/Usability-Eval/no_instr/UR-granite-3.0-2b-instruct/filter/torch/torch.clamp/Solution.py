import torch

def clamp_tensor(tensor, min_val, max_val):
    return torch.clamp(tensor, min=min_val, max=max_val)
