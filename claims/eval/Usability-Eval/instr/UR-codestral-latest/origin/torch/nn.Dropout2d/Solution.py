import torch

def zero_out_channels(tensor, p):
    # Define the shape of the mask
    mask_shape = (tensor.size(0), 1, 1, 1)

    # Generate a mask with the same shape as the tensor,
    # where each channel will be zeroed out independently
    # with probability p
    mask = torch.bernoulli((1 - p) * torch.ones(mask_shape)).expand_as(tensor)

    # Use the mask to zero out the channels
    tensor = tensor * mask

    return tensor
