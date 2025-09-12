import torch

def index_tensor_with_mask(input_tensor, mask):
    if mask.dtype != torch.bool:
        raise ValueError("Mask must be of type torch.bool")
    return input_tensor[mask]

# Example usage
input_tensor = torch.tensor([1, 2, 3, 4, 5])
mask = torch.tensor([True, False, True, False, True], dtype=torch.bool)
result = index_tensor_with_mask(input_tensor, mask)
print(result)
