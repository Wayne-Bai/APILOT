import torch

# Create a tensor
tensor = torch.randn(5, requires_grad=True)
print("Original Tensor: ", tensor)
print("Original Tensor Grad: ", tensor.grad_fn)

# Detach the tensor from the graph
detached_tensor = tensor.detach()
print("\nDetached Tensor: ", detached_tensor)
print("Detached Tensor Grad: ", detached_tensor.grad_fn)

# Change the value of the original tensor
tensor[0] = 100

# Print the values of both tensors
print("\nAfter Changing Original Tensor:")
print("Original Tensor: ", tensor)
print("Detached Tensor: ", detached_tensor)

# Create a view of the original tensor
view = tensor.view(-1)
print("\nView of Original Tensor: ", view)
print("View Grad: ", view.grad_fn)

# Try to detach the view in-place
try:
    view.detach_()
except RuntimeError as e:
    print("\nError Detaching View: ", e)
