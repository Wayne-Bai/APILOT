import torch

def clamp_tensor(input_tensor, min_val, max_val):
    return torch.clamp(input_tensor, min=min_val, max=max_val)

# Example usage
input_tensor = torch.tensor([-2.0, -1.0, 0.0, 1.0, 2.0])
min_val = -1.0
max_val = 1.0
clamped_tensor = clamp_tensor(input_tensor, min_val, max_val)
print(clamped_tensor)
