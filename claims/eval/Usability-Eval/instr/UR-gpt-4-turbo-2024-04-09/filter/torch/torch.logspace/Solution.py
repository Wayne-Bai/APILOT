import torch

def logspace_tensor(start, end, steps, base=10):
    exponent_tensor = torch.linspace(start, end, steps)
    return base ** exponent_tensor

# Example usage
tensor = logspace_tensor(1, 3, 10)
print(tensor)
