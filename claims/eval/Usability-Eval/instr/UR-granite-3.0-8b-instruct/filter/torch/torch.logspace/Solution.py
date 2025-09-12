import torch

def logspace(start, end, steps, base=10.0):
    return torch.logspace(start, end, steps, base=base)

# Example usage:
start = 1.0
end = 1000.0
steps = 10
base = 10.0

tensor = logspace(start, end, steps, base)
print(tensor)
