import torch

# Define the parameters
steps = 10  # Number of elements in the tensor
start = 0   # Starting value of the tensor
end = 1     # Ending value of the tensor

# Create a one-dimensional tensor of size steps whose values are evenly spaced from start to end, inclusive.
tensor = torch.arange(start, end + 1, steps)

print(tensor)
