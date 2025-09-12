import torch

# Define some tensors with requires_grad=True
tensor1 = torch.randn(2, 2, requires_grad=True)
tensor2 = torch.randn(2, 2, requires_grad=True)

# Perform some operations on the tensors
output = tensor1 + tensor2

# Compute gradients
output.backward(torch.ones_like(output))

# Access gradients with respect to the graph leaves
grad_tensor1 = tensor1.grad
grad_tensor2 = tensor2.grad

# Compute the sum of gradients
sum_of_gradients = grad_tensor1 + grad_tensor2

print("Gradient of tensor1:\n", grad_tensor1)
print("Gradient of tensor2:\n", grad_tensor2)
print("Sum of gradients:\n", sum_of_gradients)
