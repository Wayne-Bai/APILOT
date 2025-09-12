import torch

# Define the size of the tensor
steps = 10

# Define the start and end values
start = 0
end = 10

# Create a one-dimensional tensor with evenly spaced values from start to end
tensor = torch.linspace(start, end, steps)

print(tensor)
