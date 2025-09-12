import torch

def fill_where_mask_true(tensor, mask, value):
    # Ensure the mask is broadcastable with the tensor
    mask = mask.expand_as(tensor)
    
    # Fill the tensor where the mask is True with the specified value
    tensor[mask] = value
    
    return tensor

# Example usage:
tensor = torch.tensor([[1, 2], [3, 4]])
mask = torch.tensor([[True, False], [False, True]])
value = 0

result = fill_where_mask_true(tensor, mask, value)
print(result)
