import torch

# Creating a tensor
x = torch.tensor([[1, 2], [3, 4]])

# Creating a mask
mask = torch.tensor([[True, False], [False, True]])

# Fill elements where the mask is True
x.masked_fill_(mask, value=999)

print(x)
