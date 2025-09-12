import torch

# Create a tensor
tensor = torch.tensor([1.0, 2.0, 3.0])

# Print the tensor
print("Original Tensor:")
print(tensor)

# Detach the tensor from the computation graph
detached_tensor = tensor.detach()

# Print the detached tensor
print("\nDetached Tensor:")
print(detached_tensor)
