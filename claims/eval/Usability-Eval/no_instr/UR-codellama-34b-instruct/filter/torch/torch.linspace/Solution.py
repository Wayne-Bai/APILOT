import torch

# Create a tensor of size steps
steps = torch.tensor(range(start, end+1))

# Evenly space the values from start to end
steps = steps / (end - start)

print(steps)
