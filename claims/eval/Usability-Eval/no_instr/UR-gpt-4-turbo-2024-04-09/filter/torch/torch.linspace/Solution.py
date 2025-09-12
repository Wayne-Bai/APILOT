import torch

def create_linear_space_tensor(start, end, steps):
    return torch.linspace(start, end, steps)

# Example usage
tensor = create_linear_space_tensor(0, 10, 11)
print(tensor)
