import torch
import numpy as np

def create_logarithmical_tensor(steps, base, start, end):
    # Use numpy to create a list of evenly spaced values on a logarithmic scale
    log_values = np.linspace(np.log(start), np.log(end), steps - 1, dtype=np.float64)
    # Exponentiate to get back from log to regular scale
    values = np.exp(log_values)

    # Create a PyTorch tensor from the numpy array
    tensor = torch.tensor(values)

    return tensor

# Example usage
steps = 10
base = 2.0
start = 1.0
end = 10.0

tensor = create_logarithmical_tensor(steps, base, start, end)
print(tensor)
