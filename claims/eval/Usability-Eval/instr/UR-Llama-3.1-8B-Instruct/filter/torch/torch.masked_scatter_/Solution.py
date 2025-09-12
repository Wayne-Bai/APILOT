import torch

def update_tensor(tensor, source, mask):
    """
    Copies elements from source into tensor at positions where the mask is True.
    
    Args:
        tensor (torch.Tensor): The tensor to update.
        source (torch.Tensor): The source tensor.
        mask (torch.BoolTensor): A boolean mask indicating where to copy elements.
        
    Returns:
        torch.Tensor: The updated tensor.
    """
    # Get the device of the tensor to update
    device = tensor.device
    
    # Move the source tensor to the same device as the tensor to update
    source = source.to(device)
    
    # Move the mask to the same device as the tensor to update
    mask = mask.to(device)
    
    # Create a mask for each element in the tensor
    masked_tensor = tensor.masked_fill(~mask, float('-inf'))
    
    # Use masked_fill to copy elements from source into masked_tensor
    masked_tensor = masked_tensor.masked_fill_(mask, source.masked_fill(~mask, 0))
    
    return masked_tensor

# Create tensors
tensor = torch.tensor([1, 2, 3, 4, 5])
source = torch.tensor([10, 20, 30, 40, 50])
mask = torch.tensor([True, False, True, False, True])

# Update the tensor
updated_tensor = update_tensor(tensor, source, mask)
print(updated_tensor)
