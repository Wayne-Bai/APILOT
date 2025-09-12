import torch

def create_indexed_tensor(input_tensor, mask):
    indexed_tensor = input_tensor[mask]
    return indexed_tensor
