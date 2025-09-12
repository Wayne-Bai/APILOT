
import torch

source = torch.tensor([[1, 2, 3], [4, 5, 6]])
mask = torch.tensor([[True, False, True], [False, True, False]])
self_tensor = torch.zeros_like(source)

self_tensor[mask] = source[mask]
print(self_tensor)
