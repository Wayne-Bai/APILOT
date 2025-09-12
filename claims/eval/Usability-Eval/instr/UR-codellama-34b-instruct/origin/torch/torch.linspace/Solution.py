
import torch

# Define the start and end points of the range
start = 0.0
end = 1.0

# Define the number of steps in the range
steps = 100

# Create a one-dimensional tensor with evenly spaced values from start to end, inclusive
tensor = torch.linspace(start, end, steps)
