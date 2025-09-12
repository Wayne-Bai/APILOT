import torch

def copy_elements(source, mask, self):
    self[mask] = source[mask]
    return self

# Example usage:
source = torch.Tensor([1.0, 2.0, 3.0, 4.0])
mask = torch.BooleanTensor([True, False, True, False])
self = torch.zeros_like(source)
result = copy_elements(source, mask, self)
print(result)
