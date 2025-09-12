import torch

# Create two input tensors
input1 = torch.tensor([[1, 2], [3, 4]])
input2 = torch.tensor([[5, 6], [7, 8]])

# Divide each element of input1 by the corresponding element of input2
output = input1 / input2

print(output)
