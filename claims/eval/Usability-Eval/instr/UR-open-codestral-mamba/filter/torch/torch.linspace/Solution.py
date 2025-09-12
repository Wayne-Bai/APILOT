import torch

def create_tensor(start, end, steps):
    return torch.linspace(start, end, steps)

# Testing the function
create_tensor(0, 10, 6)
