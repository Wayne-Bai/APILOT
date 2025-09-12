import torch

x = torch.randn(3, 4)
mask = torch.tensor([True, False, True], dtype=torch.bool)
result = torch.masked_select(x, mask)
print(result)
