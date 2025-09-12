import torch

def create_tensor(start, end, steps):
    return torch.linspace(start, end, steps)

# usage:
# print(create_tensor(0, 10, 5))
