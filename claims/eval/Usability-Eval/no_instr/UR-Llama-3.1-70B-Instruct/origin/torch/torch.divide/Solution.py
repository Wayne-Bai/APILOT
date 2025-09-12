import torch

def divide_tensors(input, other):
    """
    Divides each element of the input by the corresponding element of other.

    Args:
        input (torch.Tensor): The input tensor.
        other (torch.Tensor): The other tensor.

    Returns:
        torch.Tensor: The result of the division operation.
    """
    if input.shape!= other.shape:
        raise ValueError("Input and other must have the same shape")

    # Check for zero division
    if (other == 0).any():
        raise ZeroDivisionError("Cannot divide by zero")

    return input / other

# Example usage:
input_tensor = torch.tensor([1, 2, 3, 4, 5])
other_tensor = torch.tensor([1, 2, 3, 4, 5])

result = divide_tensors(input_tensor, other_tensor)
print(result)
