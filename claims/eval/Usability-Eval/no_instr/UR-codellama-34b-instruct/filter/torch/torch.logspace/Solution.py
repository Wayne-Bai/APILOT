import torch

# Define the base, start, and end points
base = 10
start = 1
end = 1000
steps = 10

# Create an empty tensor of size steps
tensor = torch.empty(steps)

# Fill in the values of the tensor using a logarithmic scale
for i in range(steps):
    tensor[i] = base ** (start + (end - start) * i / (steps - 1))

print(tensor)
