import torch

def masked_select(tensor, mask):
    return tensor[mask]
