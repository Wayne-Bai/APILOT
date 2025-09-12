import torch

def compute_sum_of_gradients(tensors, grad_tensors):
    # Ensure all tensors require gradient calculation
    for tensor in tensors:
        tensor.requires_grad_(True)

    # Compute the gradient for each tensor with respect to the grad_tensors
    grads = torch.autograd.grad(outputs=tensors, inputs=grad_tensors, grad_outputs=[torch.ones_like(t) for t in tensors], create_graph=True)

    # Sum the gradients
    grad_sum = sum(grads)

    return grad_sum

# Example usage:
# Define some tensors
x = torch.tensor(1.0, requires_grad=True)
y = torch.tensor(2.0, requires_grad=True)
z = torch.tensor(3.0, requires_grad=True)

# Function for computing
result = compute_sum_of_gradients([x ** 2, y ** 3, z ** 4], [x, y, z])
print(result)  # Output the result of the gradient computation
