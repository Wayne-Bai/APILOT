import torch

def fill_with_value(tensor, mask, value):
    tensor[mask] = value
    return tensor
