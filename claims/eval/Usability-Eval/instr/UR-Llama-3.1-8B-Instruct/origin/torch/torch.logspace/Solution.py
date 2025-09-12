import torch

def logspace(start, end, steps, base):
    """
    Creates a one-dimensional tensor of size'steps' whose values are evenly spaced 
    from'start' to 'end', inclusive, on a logarithmic scale with base 'base'.

    Parameters:
    start (float): The starting point in the sequence.
    end (float): The end point in the sequence.
    steps (int): The number of values to generate.
    base (float): The base of the logarithmic scale.

    Returns:
    torch.Tensor: A one-dimensional tensor of size'steps' with values evenly spaced
                  on a logarithmic scale from'start' to 'end', inclusive.
    """
    # Calculate the logarithm of the start and end points
    log_start = torch.log(start) / torch.log(base)
    log_end = torch.log(end) / torch.log(base)

    # Calculate the step size
    step_size = (log_end - log_start) / (steps - 1)

    # Generate the tensor of evenly spaced values
    return torch.exp(torch.linspace(0, steps - 1, steps) * step_size) * base ** (log_start)


# Example usage:
tensor = logspace(2, 512, 10, 2)
print(tensor)
