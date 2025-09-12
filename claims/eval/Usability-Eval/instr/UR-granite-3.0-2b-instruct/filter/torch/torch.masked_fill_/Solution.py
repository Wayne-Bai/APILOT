import torch

def fill_tensor_with_mask(self, mask):
    # Ensure mask is a tensor
    if not isinstance(mask, torch.Tensor):
        raise ValueError("Mask must be a torch tensor")

    # Ensure mask has the correct shape
    if self.shape != mask.shape:
        raise ValueError("Mask shape must be broadcastable with the underlying tensor shape")

    # Fill elements of self tensor where mask is True
    self[mask] = self.value
