import torch

def create_evenly_spaced_tensor(start, end, steps):
    return torch.arange(start, end + (end - start) / (steps - 1), step=(end - start) / (steps - 1))

# Example usage
start = 0
end = 10
steps = 5
tensor = create_evenly_spaced_tensor(start, end, steps)
print(tensor)
