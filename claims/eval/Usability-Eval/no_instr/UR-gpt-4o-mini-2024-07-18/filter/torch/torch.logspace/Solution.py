import torch

def logspace_tensor(start, end, steps, base):
    return torch.logspace(start, end, steps, base=base)

# Example usage
start = 1
end = 10
steps = 5
base = 2
tensor = logspace_tensor(start, end, steps, base)
print(tensor)
