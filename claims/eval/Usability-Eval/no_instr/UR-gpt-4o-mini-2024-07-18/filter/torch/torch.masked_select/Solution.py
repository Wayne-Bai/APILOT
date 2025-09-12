import torch

def index_tensor_with_mask(input_tensor, mask):
    # Ensure the mask is a Boolean tensor
    if not isinstance(mask, torch.BoolTensor):
        raise ValueError("Mask must be a BoolTensor")

    # Use the mask to index the input tensor
    return input_tensor[mask]

# Example usage
input_tensor = torch.tensor([10, 20, 30, 40, 50])
mask = torch.tensor([True, False, True, False, True], dtype=torch.bool)

result = index_tensor_with_mask(input_tensor, mask)
print(result)  # Output: tensor([10, 30, 50])
