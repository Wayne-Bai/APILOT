import torch

def create_linspace_tensor(start, end, steps):
    # Use torch.linspace to create a tensor with evenly spaced values
    tensor = torch.linspace(start, end, steps)
    return tensor

# Example usage
start_value = 0
end_value = 10
steps = 5
linspace_tensor = create_linspace_tensor(start_value, end_value, steps)
print(linspace_tensor)
