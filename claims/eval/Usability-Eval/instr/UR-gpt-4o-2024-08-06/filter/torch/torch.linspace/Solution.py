import torch

def create_linspace_tensor(start, end, steps):
    # Generate linearly spaced tensor using torch.linspace
    return torch.linspace(start, end, steps)

# Example usage:
start = 0
end = 10
steps = 5
linspace_tensor = create_linspace_tensor(start, end, steps)
print(linspace_tensor)
