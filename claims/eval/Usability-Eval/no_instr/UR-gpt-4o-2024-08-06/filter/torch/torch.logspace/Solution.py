import torch

def logspace_with_base(start, end, steps, base):
    exponents = torch.linspace(start, end, steps)
    result = torch.pow(base, exponents)
    return result

# Example usage:
start = 0
end = 3
steps = 10
base = 2
logspace_tensor = logspace_with_base(start, end, steps, base)
print(logspace_tensor)
