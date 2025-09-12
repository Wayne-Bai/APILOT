import torch

def fill_where_mask_true(tensor, mask, value):
    # Ensure the mask is broadcastable with the tensor
    assert tensor.shape == mask.shape, "Mask must be broadcastable with the tensor"
    
    # Create a new tensor filled with the specified value
    filled_tensor = torch.full_like(tensor, value)
    
    # Use the mask to select elements from the filled tensor and the original tensor
    result = torch.where(mask, filled_tensor, tensor)
    
    return result

# Example usage:
tensor = torch.tensor([[1, 2], [3, 4]])
mask = torch.tensor([[True, False], [False, True]])
value = 0

result = fill_where_mask_true(tensor, mask, value)
print(result)
