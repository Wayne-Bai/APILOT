
import torch

# Create tensors
a = torch.tensor([1.0, 2.0], requires_grad=True)
b = torch.tensor([3.0, 4.0], requires_grad=True)

# Perform some operations
c = a * b
loss = c.sum()

# Compute gradients
loss.backward()

# Sum the gradients of given tensors
sum_gradients = torch.autograd.grad(loss, [a, b], retain_graph=True)

print("Sum of gradients with respect to 'a':", sum_gradients[0])
print("Sum of gradients with respect to 'b':", sum_gradients[1])
