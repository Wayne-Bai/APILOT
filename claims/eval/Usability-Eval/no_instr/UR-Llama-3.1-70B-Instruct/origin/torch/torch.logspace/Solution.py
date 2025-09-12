import torch

def log_space(base, start, end, steps):
    """
    Creates a one-dimensional tensor of size steps whose values are evenly spaced 
    from base start to base end, inclusive, on a logarithmic scale with base base.

    Args:
    base (float): The base of the logarithmic scale.
    start (float): The start value of the range (inclusive).
    end (float): The end value of the range (inclusive).
    steps (int): The number of steps.

    Returns:
    torch.Tensor: A one-dimensional tensor of size steps with values evenly spaced 
    on a logarithmic scale.
    """
    # Calculate the logarithmic values of start and end
    log_start = torch.log(torch.tensor(start)) / torch.log(torch.tensor(base))
    log_end = torch.log(torch.tensor(end)) / torch.log(torch.tensor(base))

    # Create a tensor with evenly spaced values on a linear scale
    linear_space = torch.linspace(log_start, log_end, steps)

    # Calculate the exponential of the linear values with base base
    log_space_values = base ** linear_space

    return log_space_values

# Example usage:
base = 2.0
start = 1.0
end = 16.0
steps = 5

log_space_values = log_space(base, start, end, steps)
print(log_space_values)
