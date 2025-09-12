import torch

steps = 10
start = -2
end = 2

tensor = torch.arange(start, end + 1, step=1)
print(tensor)
