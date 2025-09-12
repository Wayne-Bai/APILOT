
import torch

# Create a tensor
tensor = torch.randn(5, 3)

# Detach the tensor from the graph
detached_tensor = tensor.detach()

print(detached_tensor)
