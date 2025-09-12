import torch

variable = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mask = torch.tensor([[True, False, True], [True, False, True], [False, True, False]])
result = torch.where(mask, value, variable)
print(result)
