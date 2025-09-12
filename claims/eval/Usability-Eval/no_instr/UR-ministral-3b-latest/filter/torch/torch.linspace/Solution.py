import torch

def create_evenly_spaced_tensor(steps, start, end):
    return torch.linspace(start, end, steps)

# Example usage:
tensor = create_evenly_spaced_tensor(10, -2, 2)
print(tensor)
