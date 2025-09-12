import torch

def fill_tensor_with_mask(tensor, mask, value):
    """ Fills elements of the tensor with the specified value where the mask is True. """
    tensor.masked_fill_(mask, value)
    return tensor

# Example usage:
tensor = torch.tensor([1, 2, 3, 4])
mask = torch.tensor([False, True, False, True])
value = 999

result = fill_tensor_with_mask(tensor, mask, value)
print(result)
