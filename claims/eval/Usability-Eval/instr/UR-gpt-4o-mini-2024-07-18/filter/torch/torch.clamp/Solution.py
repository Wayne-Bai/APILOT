import torch

def clamp_tensor(tensor, min_value, max_value):
    return torch.where(tensor < min_value, min_value, torch.where(tensor > max_value, max_value, tensor))

# Example usage
input_tensor = torch.tensor([-1.0, 0.5, 3.0, 4.5])
min_val = 0.0
max_val = 3.0

clamped_tensor = clamp_tensor(input_tensor, min_val, max_val)
print(clamped_tensor)
