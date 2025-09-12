import torch

def copy_elements_where_mask_is_true(source, target, mask):
    """
    Copies elements from `source` tensor into `target` tensor at positions where `mask` is True.

    Parameters:
    source (torch.Tensor): The source tensor from which elements are to be copied.
    target (torch.Tensor): The target tensor into which elements are to be copied.
    mask (torch.Tensor): A boolean mask tensor indicating the positions where elements should be copied.

    Returns:
    torch.Tensor: The modified target tensor with copied elements from source.
    """
    # Ensure source, target and mask have compatible shapes
    if source.size() != target.size() or source.size() != mask.size():
        raise ValueError("Source, target, and mask tensors must have the same shape.")

    # Perform the in-place copy operation where mask is True
    target[mask] = source[mask]

    return target

# Example usage
source_tensor = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float)
target_tensor = torch.tensor([10, 20, 30, 40, 50], dtype=torch.float)
mask_tensor = torch.tensor([True, False, True, False, True], dtype=torch.bool)

# Copy elements where mask is True
result = copy_elements_where_mask_is_true(source_tensor, target_tensor, mask_tensor)
print(result)  # Output: tensor([ 1., 20.,  3., 40.,  5.])
