
import torch

# Create a tensor
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

# Detach the tensor from the computation graph
x_leaf = x.detach()

print(x_leaf)
