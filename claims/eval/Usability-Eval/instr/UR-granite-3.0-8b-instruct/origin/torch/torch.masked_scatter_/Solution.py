import torch

def copy_elements_with_mask(source, mask, self_tensor):
    self_tensor[mask] = source[mask]
    return self_tensor
