
import torch

# Define a Tensor
tensor = torch.randn(5, 3)

# Define a Mask (Tensor)
mask = torch.tensor([[True, False, True],
                     [False, True, False],
                     [True, False, True]])

# Copies elements from source into self tensor at positions where the mask is True
torch.where(mask, tensor)
