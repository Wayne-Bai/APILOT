import torch

# Create a tensor and a mask
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mask = torch.tensor([[True, False, True], [False, True, False], [True, False, True]])

# Use torch.where() to fill elements of x based on the mask
y = torch.where(mask, x, torch.tensor(0))

print(y)
