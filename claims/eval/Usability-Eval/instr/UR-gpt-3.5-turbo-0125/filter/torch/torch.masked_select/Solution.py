
import torch

def masked_select(input_tensor, mask):
    output_tensor = input_tensor[mask]
    return output_tensor

# Example usage
input_tensor = torch.tensor([1, 2, 3, 4, 5])
mask = torch.tensor([True, False, True, False, True])
output_tensor = masked_select(input_tensor, mask)
print(output_tensor)
