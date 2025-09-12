import torch

def get_indexed_tensor(input_tensor, mask):
    # Check if the mask is a BoolTensor
    if not isinstance(mask, torch.BoolTensor):
        raise ValueError("Mask must be a BoolTensor")

    # Check if the input tensor and mask have the same size
    if input_tensor.size()!= mask.size():
        raise ValueError("Input tensor and mask must have the same size")

    # Use the mask to index the input tensor
    indexed_tensor = input_tensor[mask]

    # Reshape the indexed tensor to 1-D
    indexed_tensor = indexed_tensor.reshape(-1)

    return indexed_tensor

# Example usage:
input_tensor = torch.tensor([1, 2, 3, 4, 5])
mask = torch.tensor([True, False, True, False, True])

indexed_tensor = get_indexed_tensor(input_tensor, mask)
print(indexed_tensor)
