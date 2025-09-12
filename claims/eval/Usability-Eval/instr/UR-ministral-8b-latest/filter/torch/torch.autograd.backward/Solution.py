import torch

def compute_grad_sum(tensors):
    # Compute the gradients of each tensor with respect to their inputs
    gradients = [torch.autograd.grad(outputs=tensor, inputs=tensor, retain_graph=True)[0] for tensor in tensors]

    # Sum all the gradients
    grad_sum = sum(gradients)

    return grad_sum

# Example usage
x = torch.tensor([1.0], requires_grad=True)
y = torch.tensor([2.0], requires_grad=True)

# A symbolic computation
z = x + y

# Compute the gradient of z with respect to x and y
grad_x, grad_y = torch.autograd.grad(outputs=[z], inputs=[x, y])

# Summing up the individual gradients
grad_sum = compute_grad_sum([grad_x, grad_y])

print(f"Sum of gradients: {grad_sum}")
