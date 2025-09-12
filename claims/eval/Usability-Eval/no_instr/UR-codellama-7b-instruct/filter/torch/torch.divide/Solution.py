
import torch

# Define input and other tensors
input = torch.tensor([[1, 2], [3, 4]])
other = torch.tensor([[5, 6], [7, 8]])

# Divide each element of the input tensor by the corresponding element of other
output = input / other

print(output)
