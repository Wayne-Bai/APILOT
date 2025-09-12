import torch

def copy_elements_with_mask(source, mask):
    # Ensure source and mask are of the same shape
    if source.shape != mask.shape:
        raise ValueError("Source and mask must have the same shape.")
    
    # Create a destination tensor initialized with zeros or any other preferred value
    destination = torch.zeros_like(source)

    # Copy elements from source to destination where mask is True
    destination[mask] = source[mask]

    return destination

# Example usage
source = torch.tensor([1, 2, 3, 4, 5])
mask = torch.tensor([True, False, True, False, True])
result = copy_elements_with_mask(source, mask)
print(result)
