
import torch

def masked_fill(input_tensor, mask, value):
    return torch.where(mask, value, input_tensor)

# Example usage
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
mask = torch.tensor([[True, False, True], [False, True, False]])
value = 0
output_tensor = masked_fill(input_tensor, mask, value)

print(output_tensor)
