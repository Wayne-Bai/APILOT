import torch

# Create a random input tensor
x = torch.randn(20, 16, 50, 50)

# Apply Group Normalization
y = torch.nn.functional.group_norm(x, num_groups=16, channels_axis=1)

# Print the output tensor
print(y)
