import torch

def create_evenly_spaced_tensor(start, end, steps):
    return torch.linspace(start, end, steps)

# Example usage:
start = 0
end = 10
steps = 11
result_tensor = create_evenly_spaced_tensor(start, end, steps)
print(result_tensor)
