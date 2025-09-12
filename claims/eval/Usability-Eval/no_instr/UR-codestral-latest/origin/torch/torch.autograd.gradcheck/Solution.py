import torch
import numpy as np

# Function to compute small finite differences
def compute_fd_grad(func, x, eps=1e-6):
    grad = torch.zeros_like(x)
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        ix = it.multi_index
        oldval = x[ix].item()
        x[ix] = oldval + eps
        f_pos = func(x)
        x[ix] = oldval - eps
        f_neg = func(x)
        grad[ix] = (f_pos - f_neg) / (2*eps)
        x[ix] = oldval
        it.iternext()
    return grad

# Use a simple function for demonstration
def func(x):
    return x**2

# Randomly initialize a tensor that requires gradient
x = torch.rand(5, dtype=torch.float64, requires_grad=True)

# Compute analytical gradients
y = func(x)
y.backward()
analytical_grad = x.grad.data

# Compute gradients via small finite differences
fd_grad = compute_fd_grad(func, x)

# Check difference between two results
print("Difference between analytical and finite difference gradients:")
print(analytical_grad - fd_grad)
