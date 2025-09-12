import torch

# Create a tensor of size (steps,) whose values are evenly spaced from base start to base end on a logarithmic scale with base base
start = 10
end = 20
base = 2
steps = 5
t = torch.linspace(start, end, steps, base=base)
print(t)
