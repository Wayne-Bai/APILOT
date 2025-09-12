
import torch

def clamp_elements(input_tensor, min_val, max_val):
    return torch.clamp(input_tensor, min=min_val, max=max_val)
