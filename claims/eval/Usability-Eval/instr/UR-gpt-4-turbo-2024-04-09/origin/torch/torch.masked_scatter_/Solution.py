import torch

# Define the tensor to be modified, the source tensor, and the mask
self_tensor = torch.tensor([10, 20, 30, 40], dtype=torch.float32)
source_tensor = torch.tensor([1, 2, 3, 4], dtype=torch.float32)
mask = torch.tensor([False, True, False, True])

# Use masked_scatter to copy elements from source to self tensor at mask positions
result = self_tensor.masked_scatter(mask, source_tensor[mask])

print("Original tensor:", self_tensor)
print("Source tensor:", source_tensor)
print("Mask:", mask)
print("Result tensor:", result)
