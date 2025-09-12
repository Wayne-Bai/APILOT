import torch

def create_tensor(start, end, steps):
    return torch.linspace(start, end, steps)

# Example usage
tensor = create_tensor(1, 10, 5)
print(tensor)
