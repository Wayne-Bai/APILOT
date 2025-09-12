import torch

def create_tensor(start, end, steps):
    return torch.linspace(start, end, steps)

# Example usage:
start = 0
end = 10
steps = 5
tensor = create_tensor(start, end, steps)
print(tensor)
