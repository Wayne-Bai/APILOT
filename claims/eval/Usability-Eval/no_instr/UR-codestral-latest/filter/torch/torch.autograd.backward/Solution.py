import torch

# Declare the tensors with requires_grad=True to enable gradient calculation
tensors = [torch.tensor(data, requires_grad=True) for data in [[1.0, 2.0], [3.0, 4.0]]]

# Calculate a scalar loss function
loss = sum(tensor.sum() for tensor in tensors)

# Compute gradients
loss.backward()

# Calculate the sum of gradients with respect to graph leaves
grad_sum = sum(tensor.grad for tensor in tensors)

print("Sum of gradients with respect to graph leaves: ", grad_sum)
