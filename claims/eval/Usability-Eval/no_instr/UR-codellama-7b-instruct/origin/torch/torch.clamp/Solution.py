
import torch

# Define the range for which to clamp
min_value = -10
max_value = 10

# Create a random tensor with values in the range (-10, 10)
x = torch.randint(-10, 10, (3, 3))

# Clamp all elements in the tensor to the specified range
y = torch.clamp(x, min_value, max_value)
