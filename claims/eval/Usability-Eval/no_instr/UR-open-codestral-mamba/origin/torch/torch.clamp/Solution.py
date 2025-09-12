import torch

def clamp_tensor(tensor, min_val, max_val):
    return torch.clamp(tensor, min_val, max_val)

# Test the function
x = torch.tensor([-2, -1, 0, 1, 2])
print(clamp_tensor(x, 0, 1))  # should print tensor([0., 0., 0., 1., 1.])
