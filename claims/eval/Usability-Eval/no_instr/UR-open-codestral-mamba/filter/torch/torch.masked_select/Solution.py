import torch

def index_tensor_based_on_mask(tensor, mask):
    return tensor[mask]

# Example usage:
input_tensor = torch.tensor([1, 2, 3, 4, 5])
mask_tensor = torch.tensor([True, False, True, False, True], dtype=torch.bool)

output_tensor = index_tensor_based_on_mask(input_tensor, mask_tensor)
print(output_tensor)
