import torch
import torch.nn as nn

# Input tensor
input_tensor = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# Boolean mask
mask = torch.tensor([True, False, True, True, False])

# Calculate the new input tensor based on the mask
new_tensor = mask[:]  # Copying the mask (rather than element-wise)

# The new tensor should have the value of the input tensor wherever the mask is True
for i in range(len(input_tensor)):
    if mask[i] == True:
        new_tensor[i] = input_tensor[i]

print(new_tensor)  # Resulting tensor based on the given mask
