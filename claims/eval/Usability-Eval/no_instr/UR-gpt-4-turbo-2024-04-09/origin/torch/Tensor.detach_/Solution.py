import torch

# Create a tensor involved in computation graph
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = x * 2

# Detach the tensor from the graph
detached_tensor = y.detach()

# Print the detached tensor
print("Detached Tensor:", detached_tensor)
