import torch
import numpy as np

class CustomTensor(torch.nn.Module):
    def __init__(self, tensor):
        super(CustomTensor, self).__init__()
        self.tensor = tensor

    def apply_mask(self, mask, value):
        if not torch.broadcast_tensors(mask.shape, self.tensor.shape):
            raise ValueError("The shape of mask must be broadcastable with the shape of the tensor.")

        mask = torch.tensor(mask, dtype=torch.bool)
        self.tensor[mask] = value

tensor = torch.tensor([1, 2, 3, 4, 5])
mask = [True, False, True, True, False]
value = 10

custom_tensor = CustomTensor(tensor)
custom_tensor.apply_mask(mask, value)
print(custom_tensor.tensor)
