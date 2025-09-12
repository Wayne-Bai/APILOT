import torch

def log_scale_tensor(start, end, steps, base):
    if start < 0 or end < 0 or steps < 1:
        raise ValueError("Log scale requires start, end, and steps to be positive")
    if base <= 0 or base == 1:
        raise ValueError("Base has to be positive and not equal to 1")
    # Generate a one-dimensional tensor of size steps
    tensor = torch.logspace(start, end, steps, base=base)
    return tensor
