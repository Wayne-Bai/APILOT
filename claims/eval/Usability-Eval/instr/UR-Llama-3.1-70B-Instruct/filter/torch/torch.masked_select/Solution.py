import torch

def get_masked_indices(tensor, mask):
    """
    Returns a new 1-D tensor which indexes the input tensor according to the boolean mask.

    Args:
        tensor (torch.Tensor): Input tensor.
        mask (torch.BoolTensor): Boolean mask.

    Returns:
        torch.Tensor: A new 1-D tensor with indices of the input tensor where the mask is True.
    """
    # Ensure the tensor and mask have the same shape
    assert tensor.shape == mask.shape, "Tensor and mask must have the same shape"

    # Get the indices where the mask is True
    masked_indices = torch.nonzero(mask, as_tuple=False).squeeze(-1)

    return masked_indices

# Example usage:
tensor = torch.tensor([1, 2, 3, 4, 5])
mask = torch.tensor([True, False, True, True, False])

masked_indices = get_masked_indices(tensor, mask)
print(masked_indices)  # Output: tensor([0, 2, 3])
