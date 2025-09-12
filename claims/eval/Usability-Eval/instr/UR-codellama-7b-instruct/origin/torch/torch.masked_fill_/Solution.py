
import torch

def fill_mask(self, mask):
    # Check if the mask is a valid tensor
    if not isinstance(mask, torch.Tensor):
        raise ValueError("Mask must be a torch.Tensor")
    
    # Check if the mask has the same shape as the underlying tensor
    if mask.shape != self.shape:
        raise ValueError("Mask must have the same shape as the underlying tensor")
    
    # Fill elements of self tensor with value where mask is True
    result = torch.where(mask, self, 0)
    return result
