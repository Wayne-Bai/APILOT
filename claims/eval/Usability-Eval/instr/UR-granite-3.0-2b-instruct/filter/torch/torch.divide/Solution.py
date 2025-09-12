import torch

def divide_tensors(input, other):
    assert input.shape == other.shape, "Input and other tensors must have the same shape"
    result = torch.div(input, other)
    return result
