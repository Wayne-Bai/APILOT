import torch

def logspace(start, end, steps):
    base = 10  # Logarithmic base
    factors = torch.tensor([10 ** ((end - start) / (steps - 1) * (i - 1)) for i in range(1, steps + 1)])
    return torch.tensor([base ** factors[i] for i in range(steps)])

# Example usage
start = 1e-2
end = 1e3
steps = 100
log_tensor = logspace(start, end, steps)
print(log_tensor)
