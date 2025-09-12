import torch

def create_one_dimensional_tensor(steps, start, end):
    """
    Creates a one-dimensional tensor of size steps whose values are evenly spaced from start to end, inclusive.

    Args:
        steps (int): The size of the tensor.
        start (float): The starting value of the tensor.
        end (float): The ending value of the tensor.

    Returns:
        torch.Tensor: A one-dimensional tensor with evenly spaced values.
    """
    return torch.arange(start, end + (end - start) / (steps - 1), (end - start) / (steps - 1))

# Example usage
steps = 5
start = 0.0
end = 1.0
tensor = create_one_dimensional_tensor(steps, start, end)
print(tensor)
