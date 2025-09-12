import torch

def copy_elements(source, mask, self_tensor):
    self_tensor[mask] = source[mask]
    return self_tensor

# Test the function
source = torch.tensor([1, 2, 3, 4, 5])
mask = torch.tensor([True, False, True, False, True])
self_tensor = torch.zeros(5)

result = copy_elements(source, mask, self_tensor)
print(result)
