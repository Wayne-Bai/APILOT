import torch

def fill_with_value(tensor, mask, value):
    tensor.masked_fill_(mask, value)
    return tensor
