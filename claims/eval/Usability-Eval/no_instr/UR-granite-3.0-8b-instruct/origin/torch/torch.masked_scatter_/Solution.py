import torch

def copy_elements(source, mask, self_tensor):
    self_tensor[mask] = source[mask]
