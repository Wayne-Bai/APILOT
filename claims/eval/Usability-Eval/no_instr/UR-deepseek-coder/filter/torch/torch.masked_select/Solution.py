import torch

def mask_tensor(input_tensor, mask):
    return input_tensor[mask]

# Example usage:
input_tensor = torch.tensor([1, 2, 3, 4, 5])
mask = torch.tensor([True, False, True, False, True], dtype=torch.bool)

result = mask_tensor(input_tensor, mask)
print(result)  # Output: tensor([1, 3, 5])
