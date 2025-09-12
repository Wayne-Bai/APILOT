import torch

def index_tensor(input_tensor, mask):
    # Ensure the input tensor and mask have the same shape
    if input_tensor.shape != mask.shape:
        raise ValueError("Input tensor and mask must have the same shape")

    # Create a BoolTensor that flattens the mask
    flat_mask = mask.flatten()

    # Create a 1-D tensor with the original indexing
    flattened_indices = torch.arange(input_tensor.numel()).view(flattened_indices.size(0), 1)

    # Combine mask and indices
    result_indices = flattened_indices[flat_mask]

    # Flatten the result to 1-D tensor
    result_tensor = input_tensor.view(-1)[result_indices]

    # Reshape to the original shape
    result_tensor = result_tensor.view(-1)

    return result_tensor
