import torch

def clamp_elements(tensor, min_val, max_val):
    return torch.clamp(tensor, min=min_val, max=max_val)

# Example usage:
input_tensor = torch.tensor([2.0, 5.5, 8.0, -1.0, 10.0])
min_val = 0.0
max_val = 10.0

clamped_tensor = clamp_elements(input_tensor, min_val, max_val)
print(clamped_tensor)
