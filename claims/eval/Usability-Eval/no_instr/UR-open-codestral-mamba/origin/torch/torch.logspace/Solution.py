import torch

def log_spaced_tensor(start, end, steps, base = 10):
    return torch.logspace(start, end, steps, base=base)

# Call function with example values
tensor = log_spaced_tensor(0, 10, 10) # Create a tensor with 10 values from 10^0 to 10^10, evenly spaced on a log scale.
print(tensor)
