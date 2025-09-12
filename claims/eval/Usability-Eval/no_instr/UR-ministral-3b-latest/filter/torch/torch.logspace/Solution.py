import torch

base = 2
start = 1
end = 10
steps = 5

tensor = torch.logspace(base, login(base), steps)
print(tensor)
