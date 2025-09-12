import torch

def copy_elements(source, mask, target):
    target[mask] = source[mask]
    return target

# Example usage
source = torch.tensor([1, 2, 3, 4, 5])
mask = torch.tensor([True, False, True, False, True], dtype=torch.bool)
target = torch.zeros_like(source)
print(copy_elements(source, mask, target))
