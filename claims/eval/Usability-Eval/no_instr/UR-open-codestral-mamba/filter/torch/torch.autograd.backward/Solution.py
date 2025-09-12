import torch

# Assume we have three tensors
x = torch.tensor([[1., 2.], [3., 4.]], requires_grad=True)
y = torch.tensor([[2., 3.], [4., 5.]], requires_grad=True)
z = torch.tensor([[3., 4.], [5., 6.]], requires_grad=True)

# Perform some operations
a = x * y
b = a + z

# Compute gradients
a.backward(torch.ones_like(a))
b.backward(torch.ones_like(b))

# Compute the sum of gradients
sum_of_gradients = torch.sum([p.grad  for p in [x, y, z] if p.grad is not None])
print(sum_of_gradients)
