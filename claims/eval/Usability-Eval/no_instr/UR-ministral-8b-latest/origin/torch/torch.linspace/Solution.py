import torch

# Set up the tensor parameters
end = 10
steps = 5

# Create a one-dimensional tensor with values evenly spaced from 0 to end
values = torch.linspace(0, end, steps=steps)

print(values)
