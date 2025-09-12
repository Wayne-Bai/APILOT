import torch

def copy_elements_with_mask(source, mask, target):
    # Ensure that the mask is a boolean tensor
    if mask.dtype != torch.bool:
        mask = mask.bool()
    
    # Ensure that the source and target tensors have the same shape where the mask is True
    if source.shape != target.shape:
        raise ValueError("Source and target tensors must have the same shape.")
    
    # Copy elements from source to target where the mask is True
    target[mask] = source[mask]

# Example usage:
source = torch.tensor([1, 2, 3, 4])
mask = torch.tensor([True, False, True, False])
target = torch.tensor([0, 0, 0, 0])

copy_elements_with_mask(source, mask, target)
print(target)  # Output: tensor([1, 0, 3, 0])
