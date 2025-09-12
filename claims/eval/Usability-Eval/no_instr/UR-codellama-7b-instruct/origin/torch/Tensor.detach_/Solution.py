
import torch

# Create a tensor object
tensor = torch.ones(10)

# Detach the tensor from the graph
detached_tensor = tensor.detach()

print(detached_tensor)
