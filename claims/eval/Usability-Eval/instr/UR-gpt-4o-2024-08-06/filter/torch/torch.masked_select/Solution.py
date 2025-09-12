import torch

def masked_select(input_tensor, mask):
    """
    Masks the input_tensor based on the boolean mask provided and returns a 1-D tensor.

    :param input_tensor: The tensor from which to select elements.
    :param mask: A boolean tensor indicating which elements to select.
    :return: A 1-D tensor with elements selected from input_tensor.
    """
    # Ensure the mask is a boolean tensor
    assert mask.dtype == torch.bool, "Mask must be a BoolTensor"

    # Use torch.masked_select to select elements from input_tensor based on mask
    selected_tensor = torch.masked_select(input_tensor, mask)
    
    return selected_tensor

# Example usage
input_tensor = torch.tensor([[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9]])
mask = torch.tensor([[True, False, True],
                     [False, True, False],
                     [True, False, False]])

selected_elements = masked_select(input_tensor, mask)
print(selected_elements)
