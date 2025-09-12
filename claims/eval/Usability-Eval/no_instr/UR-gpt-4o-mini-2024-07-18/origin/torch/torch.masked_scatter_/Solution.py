import torch

# Function to copy elements from source to self at positions where mask is True
def copy_elements_with_mask(source, mask):
    # Ensure the mask is a boolean tensor
    if not mask.dtype == torch.bool:
        raise ValueError("Mask tensor must be of boolean type.")
    
    # Create a tensor to hold the result, initializing with zeros or the appropriate shape
    result = torch.zeros_like(source)

    # Copy elements from source to result using the mask
    result[mask] = source[mask]

    return result

# Example usage
source_tensor = torch.tensor([1, 2, 3, 4, 5])
mask_tensor = torch.tensor([False, True, False, True, False], dtype=torch.bool)

result_tensor = copy_elements_with_mask(source_tensor, mask_tensor)
print(result_tensor)
