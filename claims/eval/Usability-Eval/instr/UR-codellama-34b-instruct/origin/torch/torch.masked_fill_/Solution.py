
import torch

def masked_fill(tensor, mask):
    """Fills elements of self tensor with value where mask is True."""
    # Check if the shapes of the tensor and mask are broadcastable
    assert torch.broadcastable(tensor.shape, mask.shape), "Shapes of tensor and mask must be broadcastable"
    
    # Create a new tensor with the same shape as the input tensor
    result = tensor.new_empty(tensor.shape)
    
    # Iterate over the elements of the tensor and fill them with the corresponding value from the mask
    for i, (val, m) in enumerate(zip(tensor, mask)):
        if m:
            result[i] = val
        else:
            result[i] = 0.0
    
    return result
