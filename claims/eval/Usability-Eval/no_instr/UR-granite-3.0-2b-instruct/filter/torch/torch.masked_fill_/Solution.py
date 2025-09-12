import torch

def fill_tensor_with_mask(self, mask):
    # Create a boolean mask where True indicates where to fill the tensor
    mask = mask.to(self.device)
    mask = mask.unsqueeze(1)  # Add an extra dimension for broadcasting

    # Fill the tensor with the mask value
    self[mask] = self.fill_value
