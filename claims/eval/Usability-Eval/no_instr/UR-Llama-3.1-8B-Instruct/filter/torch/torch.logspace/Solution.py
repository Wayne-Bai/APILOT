import torch
import numpy as np

def logspace(start, end, steps, base):
    """
    Creates a one-dimensional tensor of size `steps` whose values are evenly 
    spaced from `start` to `end`, inclusive, on a logarithmic scale with base `base`.

    Args:
        start (float): The starting value of the sequence.
        end (float): The ending value of the sequence.
        steps (int): The number of values to generate.
        base (float): The base of the logarithmic scale.

    Returns:
        torch.tensor: A one-dimensional tensor of size `steps` with values 
        evenly spaced from `start` to `end` on a logarithmic scale with base `base`.
    """
    # Generate evenly spaced values on a linear scale using numpy
    linear_values = np.linspace(start, end, steps)
    
    # Convert the linear values to the logarithmic scale using numpy's log function
    log_values = np.log(linear_values) / np.log(base)
    
    # Expand the log values to match the original linear scale
    expanded_log_values = base ** log_values
    
    # Convert the log values to a tensor and return
    return torch.tensor(expanded_log_values, dtype=torch.float32)

# Usage example
steps = 5
base = 2
start = 1
end = 8

tensor = logspace(start, end, steps, base)
print(tensor)
