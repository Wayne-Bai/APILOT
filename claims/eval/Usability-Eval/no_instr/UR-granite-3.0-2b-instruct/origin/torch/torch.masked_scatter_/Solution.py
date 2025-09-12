import torch

def copy_elements(source, mask, self_tensor):
    # Ensure the source and mask tensors have the same shape
    assert source.shape == mask.shape, "Source and mask tensors must have the same shape"

    # Create a boolean mask for the self tensor
    self_mask = mask.clone()

    # Copy elements from source to self tensor where the mask is True
    self_tensor[self_mask] = source[self_mask]

    return self_tensor
