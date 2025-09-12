# Import necessary libraries
import torch
import torch.nn.functional as F

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Create a boolean mask tensor
mask = torch.tensor([True, False, True, False], dtype=torch.bool)

# Use torch.masked_select to create a new tensor based on the mask
tensor_selected = torch.masked_select(input_tensor, mask)

print("Input Tensor:")
print(input_tensor)

print("\nBoolean Mask:")
print(mask)

print("\nSelected Tensor:")
print(tensor_selected)
