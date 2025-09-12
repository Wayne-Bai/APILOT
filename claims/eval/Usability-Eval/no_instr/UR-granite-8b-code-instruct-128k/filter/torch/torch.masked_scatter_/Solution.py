
import torch

def copy_elements_from_source(source, mask):
    self = torch.zeros_like(source)
    self[mask] = source[mask]
    return self
