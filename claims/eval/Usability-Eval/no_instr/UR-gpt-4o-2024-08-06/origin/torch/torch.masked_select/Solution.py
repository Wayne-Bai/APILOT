import torch

# Create a sample input tensor
input_tensor = torch.tensor([10, 20, 30, 40, 50])

# Create a boolean mask
mask = torch.tensor([True, False, True, False, True], dtype=torch.bool)

# Use the mask to index the input tensor
masked_tensor = input_tensor[mask]

# Print the resulting tensor
print(masked_tensor)
