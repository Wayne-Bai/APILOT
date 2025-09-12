import torch

def log_space_tensor(start, end, steps, base):
    return torch.linspace(start, end, steps).pow(base)

# Example usage
start = 1
end = 100
steps = 10
base = 10
tensor = log_space_tensor(start, end, steps, base)
print(tensor)
