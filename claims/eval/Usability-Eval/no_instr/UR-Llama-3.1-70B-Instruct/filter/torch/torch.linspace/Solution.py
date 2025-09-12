import torch

def create_tensor(steps, start, end):
    """
    Creates a one-dimensional tensor of size steps whose values are evenly spaced from start to end, inclusive.

    Args:
        steps (int): The size of the tensor.
        start (float): The starting value of the tensor.
        end (float): The ending value of the tensor.

    Returns:
        torch.Tensor: A one-dimensional tensor with evenly spaced values.
    """
    return torch.linspace(start, end, steps)

# Example usage:
print(create_tensor(5, 1.0, 2.0))
