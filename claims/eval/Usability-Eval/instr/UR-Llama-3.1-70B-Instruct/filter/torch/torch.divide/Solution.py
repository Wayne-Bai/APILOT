# Import torch
import torch

def divide_tensors(input, other):
    """
    Divides each element of the input tensor by the corresponding element of another tensor.

    Args:
        input (torch.Tensor): The input tensor to be divided.
        other (torch.Tensor): The tensor by which we divide the input tensor.

    Returns:
        torch.Tensor: The result of the element-wise division.
    """
    # Check if the input and other tensors have the same shape
    if input.shape!= other.shape:
        raise ValueError("Input and other tensors must have the same shape.")

    # Divide each element of the input tensor by the corresponding element of the other tensor
    result = torch.div(input, other)

    return result

# Create two example tensors
input_tensor = torch.tensor([10, 20, 30], dtype=torch.float32)
other_tensor = torch.tensor([2, 4, 6], dtype=torch.float32)

# Divide the input tensor by the other tensor
result = divide_tensors(input_tensor, other_tensor)

# Print the result
print(result)
