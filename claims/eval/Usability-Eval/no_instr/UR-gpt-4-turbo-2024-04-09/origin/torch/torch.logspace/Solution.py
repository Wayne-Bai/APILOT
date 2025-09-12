import torch

def log_space_tensor(start, end, steps, base=10):
    # Create a tensor with values from start to end spaced evenly on a logarithmic scale
    values = torch.logspace(start=torch.log10(torch.tensor(start, dtype=torch.float)),
                            end=torch.log10(torch.tensor(end, dtype=torch.float)),
                            steps=steps, base=base)
    return values

# Example usage
start = 1
end = 1000
steps = 10
base = 10

result = log_space_tensor(start, end, steps, base)
print(result)
