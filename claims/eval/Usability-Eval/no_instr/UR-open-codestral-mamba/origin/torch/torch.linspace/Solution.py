import torch

def create_one_d_tensor(start, end, steps):
    return torch.linspace(start, end, steps)

# test the function
tensor = create_one_d_tensor(0, 10, 5)
print(tensor)
