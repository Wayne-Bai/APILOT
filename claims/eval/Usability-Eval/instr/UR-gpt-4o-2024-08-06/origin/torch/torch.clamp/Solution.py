import torch

def clamp_tensor(input_tensor, min_value, max_value):
    return torch.clamp(input_tensor, min=min_value, max=max_value)

# Example usage
input_tensor = torch.tensor([1.0, -1.0, 3.0, 4.0, -5.0])
clamped_tensor = clamp_tensor(input_tensor, min_value=-2.0, max_value=2.0)
print(clamped_tensor)
