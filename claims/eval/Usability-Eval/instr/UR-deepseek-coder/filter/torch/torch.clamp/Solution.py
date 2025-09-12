import torch

def clamp_elements(input_tensor, min_value, max_value):
    return torch.max(torch.min(input_tensor, torch.tensor(max_value)), torch.tensor(min_value))

# Example usage:
input_tensor = torch.tensor([1.2, -0.5, 3.7, -2.1])
min_value = -1.0
max_value = 2.0

clamped_tensor = clamp_elements(input_tensor, min_value, max_value)
print(clamped_tensor)
