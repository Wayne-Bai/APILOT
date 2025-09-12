
import torch

# Create a tensor
tensor = torch.randn(5, 5)

# Detach the tensor from the graph
tensor = tensor.detach()

print(tensor)
