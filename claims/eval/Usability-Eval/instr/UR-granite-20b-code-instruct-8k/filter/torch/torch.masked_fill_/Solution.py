import torch

def fill_tensor_with_value(tensor, value, mask):
    tensor[mask] = value
    return tensor
