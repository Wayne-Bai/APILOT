import torch

def clamp_tensor(input_tensor, min_value, max_value):
    return torch.clamp(input_tensor, min=min_value, max=max_value)

# Example usage
tensor = torch.rand((5, 5)) * 10  # Random tensor with values from 0 to 10
min_val = 3
max_val = 7
clamped_tensor = clamp_tensor(tensor, min_val, max_val)
print("Original Tensor:\n", tensor)
print("Clamped Tensor:\n", clamped_tensor)
