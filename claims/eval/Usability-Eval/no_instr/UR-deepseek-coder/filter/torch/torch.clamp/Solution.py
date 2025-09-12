import torch

def clamp_elements(input_tensor, min_value, max_value):
    return torch.clamp(input_tensor, min=min_value, max=max_value)

# Example usage:
input_tensor = torch.tensor([1, -2, 3, -4, 5])
min_value = -1
max_value = 3

clamped_tensor = clamp_elements(input_tensor, min_value, max_value)
print(clamped_tensor)
