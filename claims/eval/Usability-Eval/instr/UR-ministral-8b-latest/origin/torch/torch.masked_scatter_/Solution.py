import torch

def copy_elements_from_mask(source, mask):
    # Create a tensor to store the result
    result = torch.empty_like(source)
    # Copy elements from source into result where mask is True
    result[mask] = source[mask]
    return result

# Example usage
source = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)
mask = torch.tensor([True, False, True, False, True], dtype=torch.bool)
result = copy_elements_from_mask(source, mask)
print(result)  # Output: tensor([1., 3., 5.])
