import torch

def logspace_tensor(start, end, steps, base=10):
    # Calculate the exponents for the logarithmic scale
    exponents = torch.linspace(start, end, steps)
    
    # Create the tensor with values on a logarithmic scale
    log_tensor = base ** exponents
    
    return log_tensor

# Example usage:
start = 1
end = 5
steps = 10
base = 2

result = logspace_tensor(start, end, steps, base)
print(result)
