import torch

def clamp_tensor(input_tensor, min_value, max_value):
    """
    Clamps all elements in input into the range [ min, max ].
    
    Args:
    input_tensor (torch.Tensor): Input tensor to clamp.
    min_value (int or float): Minimum value of the range.
    max_value (int or float): Maximum value of the range.
    
    Returns:
    torch.Tensor: Clamped tensor.
    """
    
    clamped_tensor = torch.clamp(input_tensor, min=min_value, max=max_value)
    
    return clamped_tensor

# Example usage
input_tensor = torch.tensor([-2.0, 3.0, 5.0, 7.0])
min_value = 0.0
max_value = 6.0

clamped_tensor = clamp_tensor(input_tensor, min_value, max_value)

print("Input Tensor: ", input_tensor)
print("Clamped Tensor: ", clamped_tensor)
