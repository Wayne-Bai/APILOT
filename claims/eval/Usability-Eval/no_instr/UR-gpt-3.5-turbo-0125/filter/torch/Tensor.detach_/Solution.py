
import torch

# Create a tensor
x = torch.tensor([1, 2, 3, 4, 5])

# Detach the tensor from the computation graph
x_detached = x.detach()

print("Original Tensor:")
print(x)
print("\nDetached Tensor:")
print(x_detached)
