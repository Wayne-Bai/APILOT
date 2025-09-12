import torch

def copy_where_mask(self, source, mask):
    # Get the indices where the mask is True
    indices = torch.nonzero(mask)
    # Use the indices to copy the elements from the source tensor to self tensor
    self[indices] = source[indices]
    return self

# Example usage
source = torch.tensor([1, 2, 3, 4, 5])
mask = torch.tensor([True, False, True, False, True])
output = torch.zeros(5)
copy_where_mask(output, source, mask)
print(output)
