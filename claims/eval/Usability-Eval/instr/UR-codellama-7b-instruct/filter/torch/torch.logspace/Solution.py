import torch

def logspace(base: float, start: float, end: float, steps: int) -> torch.Tensor:
    """
    Returns a one-dimensional tensor of size steps whose values are evenly spaced from base start to base end, inclusive, on a logarithmic scale with base base.

    Args:
        base (float): The logarithmic base for the spacing.
        start (float): The starting value of the tensor.
        end (float): The ending value of the tensor.
        steps (int): The number of steps in the tensor.

    Returns:
        torch.Tensor: A one-dimensional tensor of size steps whose values are evenly spaced from base start to base end, inclusive, on a logarithmic scale with base base.
    """
    if steps < 1:
        raise ValueError("steps must be greater than or equal to 1")

    return torch.linspace(torch.log(start), torch.log(end), steps, base=base)
