import torch

def fill_with_value(tensor, mask, value):
    """
    Fills elements of the tensor with value where mask is True.

    Args:
        tensor (torch.Tensor): The input tensor.
        mask (torch.Tensor): A mask where elements are True or False.
        value (float): The value to fill.

    Returns:
        torch.Tensor: The tensor with elements filled according to the mask.
    """
    return torch.where(mask, torch.full_like(tensor, value), tensor)

# Example usage:
tensor = torch.tensor([[1, 2], [3, 4]])
mask = torch.tensor([[True, False], [False, True]])
value = 10.0

filled_tensor = fill_with_value(tensor, mask, value)
print(filled_tensor)
