import torch

def create_evenly_spaced_tensor(start, end, steps):
    step_size = (end - start) / (steps - 1)
    tensor = torch.arange(start, end + step_size, step_size)
    return tensor

# Example usage:
start = 0
end = 10
steps = 5
result = create_evenly_spaced_tensor(start, end, steps)
print(result)
