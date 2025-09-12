import torch

def fill_tensor_with_mask(tensor, mask, value):
    """
    Fills elements of the tensor with the specified value where mask is True.
    
    Parameters:
    tensor (torch.Tensor): The tensor to be filled.
    mask (torch.Tensor): A boolean tensor where True indicates the positions to fill.
    value: The value to fill at the positions specified by the mask.

    Returns:
    torch.Tensor: The modified tensor.
    """
    tensor[mask] = value
    return tensor

# Example usage
tensor = torch.zeros((5, 5))
mask = torch.tensor([[True, False, False, True, False],
                     [False, False, False, False, False],
                     [False, True, False, False, False],
                     [False, False, False, False, False],
                     [False, False, True, False, True]])

value = 1.0
result_tensor = fill_tensor_with_mask(tensor, mask, value)
print(result_tensor)
