import torch

def copy_elements_with_mask(source, mask, target):
    # Ensure the mask is a boolean tensor
    mask = mask.bool()
    
    # Copy elements from source to target where mask is True
    target[mask] = source[mask]
    
    return target

# Example usage:
source = torch.tensor([1, 2, 3, 4, 5])
mask = torch.tensor([True, False, True, False, True])
target = torch.zeros_like(source)

result = copy_elements_with_mask(source, mask, target)
print(result)  # Output: tensor([1, 0, 3, 0, 5])
