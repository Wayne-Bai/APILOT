
import torch

def fill_with_mask(self, mask):
    """Fills elements of self tensor with value where mask is True.
    The shape of mask must be broadcastable with the shape of the underlying tensor.
    """
    if not isinstance(mask, torch.Tensor):
        raise TypeError("Mask must be a torch.Tensor.")
    if len(self.shape) != len(mask.shape):
        raise ValueError("Shape of mask must be broadcastable with the shape of the underlying tensor.")
    
    # Create a copy of the tensor with the same shape as self
    filled = self.clone()
    
    # Loop over the elements in the mask and fill them into the new tensor
    for i, (m, s) in enumerate(zip(mask, self)):
        if m:
            filled[i] = s
    
    return filled
