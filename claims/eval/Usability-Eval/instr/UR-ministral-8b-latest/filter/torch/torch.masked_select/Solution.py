import torch

def index_tensor(input_tensor, mask):
    return input_tensor[mask]

# Example usage
input_tensor = torch.tensor([10, 20, 30, 40])
mask = torch.tensor([True, False, True, False])
output = index_tensor(input_tensor, mask)
print(output)  # Output will be: tensor([10, 30])
