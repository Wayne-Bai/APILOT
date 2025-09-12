import torch

def fill_values(tensor, mask, value):
    """
    Fills elements of tensor with value where mask is True.
    The shapes of mask and tensor must be broadcastable.
    """
    return tensor.masked_fill(mask, value)
