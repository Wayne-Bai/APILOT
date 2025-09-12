
import torch

def clamp(input, min=None, max=None):
    """
    Clamps all elements in input into the range [min, max].

    Args:
        input (torch.Tensor): The input tensor to be clamped.
        min (float or torch.Tensor, optional): The minimum value to clamp to. Defaults to None.
        max (float or torch.Tensor, optional): The maximum value to clamp to. Defaults to None.

    Returns:
        torch.Tensor: The clamped tensor.
    """
    if min is not None and max is not None:
        return input.clamp(min=min, max=max)
    elif min is not None:
        return input.clamp(min=min)
    elif max is not None:
        return input.clamp(max=max)
    else:
        raise ValueError("At least one of 'min' or 'max' must be specified")
