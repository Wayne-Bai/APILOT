import torch

def fill_tensor_with_mask(tensor, mask, value):
    # Check if mask is broadcastable with the tensor
    assert tensor.shape == mask.shape or tensor.shape[-len(mask.shape):] == mask.shape, "Mask shape must be broadcastable with the tensor shape."
    # Create a copy of the tensor to avoid in-place modification
    output = tensor.clone()
    # Fill the elements of the tensor with the value where mask is True
    output[mask] = value
    return output
