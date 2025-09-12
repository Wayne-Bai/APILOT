import torch

def log_space(start, end, steps):
    return torch.logspace(start, end, steps, base=10)

# Example usage:
start = 1
end = 2
steps = 5

tensor = log_space(start, end, steps)
print(tensor)
