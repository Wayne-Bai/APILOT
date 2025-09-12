import torch

def logspace(start, end, steps, base):
    # Compute the exponent values evenly spaced
    exponent_values = torch.linspace(start, end, steps)
    
    # Calculate the log space values based on the base
    logspace_values = base ** exponent_values
    
    return logspace_values

# Example of creating a tensor with base 10, from 1 to 3, with 5 steps
log_tensor = logspace(1, 3, 5, 10)
print(log_tensor)
