import torch

def index_tensor(input_tensor, mask):
    # Ensure the mask is a BoolTensor
    mask = mask.bool()

    # Use the mask to index the input tensor
    indexed_tensor = input_tensor[mask]

    return indexed_tensor
