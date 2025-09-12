import torch

def divide_by_corresponding(input, other):
    """
    Divides each element of the input tensor by the corresponding element of other.

    Args:
        input (torch.Tensor): Input tensor.
        other (torch.Tensor): Other tensor with the same shape as input.

    Returns:
        torch.Tensor: Tensor obtained by dividing the input tensor by other.
    """
    return torch.abs(input) / torch.abs(other)

# Example usage:
input_tensor = torch.tensor([10, 20, 30])
other_tensor = torch.tensor([2, 4, 6])

result = divide_by_corresponding(input_tensor, other_tensor)
print(result)
