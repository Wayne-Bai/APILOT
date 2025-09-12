import torch

def compute_gradient_sum(tensors):
    grad_sum = 0
    for tensor in tensors:
        # Check if the tensor requires gradient computation
        if tensor.requires_grad:
            grad_sum += tensor.grad.data.sum()
    return grad_sum

# Example usage:
# Create some tensors with requires_grad=True
x = torch.tensor([2.0], requires_grad=True)
y = torch.tensor([3.0], requires_grad=True)

# Perform some operations to generate gradients
z = x**2 * y
z.backward()

# Compute the sum of gradient of given tensors
grad_sum = compute_gradient_sum([x, y])
print(grad_sum)
