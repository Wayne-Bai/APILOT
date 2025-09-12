import torch

# Define the starting and ending points of the range
start = torch.tensor(1)
end = torch.tensor(100)

# Calculate the difference between the start and end points
diff = end - start

# Create a tensor with evenly spaced values from start to end on a logarithmic scale
logspace = torch.logspace(start, end, steps=diff.item())
