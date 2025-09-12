import torch

# define the function for clamping tensors
def clamp_tensor(tensor, min_val, max_val):
    return torch.clamp(tensor, min_val, max_val)

# example usage
tensor = torch.tensor([-1, 0, 1, 2, 3, 4, 5])
min_val = 0
max_val = 3

clamped_tensor = clamp_tensor(tensor, min_val, max_val)
print(clamped_tensor)
