import torch

def index_tensor(input_tensor, mask):
    """
    Returns a new 1-D tensor which indexes the input tensor
    according to the boolean mask.

    Args:
        input_tensor (torch.Tensor): The input tensor.
        mask (torch.BoolTensor): The boolean mask.

    Returns:
        torch.Tensor: The indexed tensor.
    """
    return input_tensor[mask]
