import torch

def index_tensor_with_mask(tensor, mask):
    return tensor[mask]
