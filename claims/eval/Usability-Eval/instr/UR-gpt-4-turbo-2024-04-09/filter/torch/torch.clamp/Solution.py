import torch

def clamp_tensor_values(tensor, min_value, max_value):
    clamped_tensor = torch.clamp(tensor, min=min_value, max=max_value)
    return clamped_tensor

# Example uses
input_tensor = torch.tensor([0.5, -1.5, 2.0, 0.7, -0.2, 3.5])
clamped_output = clamp_tensor_values(input_tensor, min_value=-1.0, max_value=2.0)
print(clamped_output)
