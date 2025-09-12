import torch

# Example tensor
tensor = torch.randn(3, 3)

# Detaching the tensor from the computation graph
detached_tensor = tensor.detach()

print(tensor.detach())
print(detached_tensor)
