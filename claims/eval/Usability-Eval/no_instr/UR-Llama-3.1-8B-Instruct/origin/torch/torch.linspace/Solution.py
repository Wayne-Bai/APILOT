import torch

# Define the start and end points
start = 0
end = 10

# Define the number of steps
steps = 6

# Create a 1D tensor of evenly spaced values from start to end, inclusive
tensor = torch.linspace(start, end, steps)

# Print the tensor
print(tensor)
