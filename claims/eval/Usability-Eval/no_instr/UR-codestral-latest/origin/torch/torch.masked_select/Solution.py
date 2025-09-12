import torch

def index_tensor_with_mask(input_tensor, mask):
    return input_tensor[mask]
