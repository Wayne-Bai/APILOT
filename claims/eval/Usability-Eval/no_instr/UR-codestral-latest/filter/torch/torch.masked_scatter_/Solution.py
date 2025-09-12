import torch

# Create a main tensor
main_tensor = torch.tensor([1, 2, 3, 4, 5])

# Create a source tensor
source_tensor = torch.tensor([9, 8, 7, 6, 5])

# Create a mask
mask = torch.tensor([True, False, True, False, True])

# Copy elements from source into main where the mask is True
main_tensor[mask] = source_tensor[mask]

print(main_tensor)
