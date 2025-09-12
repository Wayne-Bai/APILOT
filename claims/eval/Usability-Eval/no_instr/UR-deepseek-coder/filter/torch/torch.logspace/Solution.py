import torch

def logspace_tensor(start, end, steps, base=10):
    # Calculate the exponents for the logarithmic scale
    exponents = torch.linspace(start, end, steps)
    # Create the tensor with values on a logarithmic scale
    tensor = base ** exponents
    return tensor

# Example usage:
start = 1
end = 3
steps = 5
base = 2

result = logspace_tensor(start, end, steps, base)
print(result)
