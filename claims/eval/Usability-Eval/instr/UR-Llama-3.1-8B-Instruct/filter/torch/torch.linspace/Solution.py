import torch

def create_evenly_spaced_tensor(start, end, steps):
    """
    Creates a one-dimensional tensor of size steps whose values are evenly spaced 
    from start to end, inclusive.

    Args:
    start (float): The starting value of the tensor.
    end (float): The ending value of the tensor.
    steps (int): The number of steps in the tensor.

    Returns:
    tensor: A one-dimensional tensor of size steps with values evenly spaced from start to end.
    """
    
    # Calculate the spacing between each value in the tensor
    spacing = (end - start) / (steps - 1)
    
    # Use torch.arange to create the tensor with evenly spaced values
    tensor = torch.arange(start, end + spacing, spacing)
    
    return tensor

# Example usage
tensor = create_evenly_spaced_tensor(0, 10, 11)
print(tensor)
