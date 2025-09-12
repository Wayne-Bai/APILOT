
import torch

def copy_elements_with_mask(source, mask):
    result = torch.zeros_like(self)
    result[mask] = source[mask]
    return result
