import torch

# Create a tensor with requires_grad=True which means that PyTorch will store gradients with respect to this tensor
x = torch.tensor([1., 2., 3.], requires_grad=True)

# Perform some operations on this tensor
y = x**2
z = y.sum()

# Compute gradients. By default, gradients are not computed for Tensor with requires_grad=True, that's why we need to call .backward()
z.backward()

# x.grad now holds the sum of gradients of outputs with respect to the inputs
sum_of_gradients = x.grad.sum()

print(sum_of_gradients)
