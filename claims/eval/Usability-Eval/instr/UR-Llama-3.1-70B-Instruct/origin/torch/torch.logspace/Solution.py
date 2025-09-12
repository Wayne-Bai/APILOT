import torch

def log_space(base, start, end, steps):
    """
    Creates a one-dimensional tensor of size steps whose values are evenly spaced 
    from base start to base end, inclusive, on a logarithmic scale with base base.
    
    Parameters:
    base (float): The base of the logarithmic scale.
    start (float): The starting value.
    end (float): The ending value.
    steps (int): The number of steps.

    Returns:
    torch.Tensor: A one-dimensional tensor with evenly spaced values.
    """
    start_log = torch.log(start) / torch.log(base)
    end_log = torch.log(end) / torch.log(base)
    log_values = torch.arange(start_log, end_log + 1, (end_log - start_log) / (steps - 1))
    return base ** log_values

# Example usage:
base = 2
start = 2
end = 32
steps = 6
result = log_space(base, start, end, steps)
print(result)
