import torch

def sum_gradients(tensors):
    """
    Computes the sum of gradients of given tensors with respect to graph leaves.

    Args:
        tensors (list of torch.Tensor): List of tensors for which gradients need to be computed.

    Returns:
        torch.Tensor: Sum of the gradients.
    """
    grad_sum = None
    for tensor in tensors:
        # Ensure tensor requires gradients
        tensor.requires_grad_(True)
        
        # Compute gradients using autograd.grad
        grads = torch.autograd.grad(tensor, tensor, retain_graph=True)
        
        # Flatten and sum the gradients
        flattened_grad = torch.flatten(grads[0])
        if grad_sum is None:
            grad_sum = flattened_grad
        else:
            grad_sum += flattened_grad
            
    return grad_sum

# Example usage:
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = torch.tensor([4.0, 5.0, 6.0], requires_grad=True)
z = x * y

tensors_to_grad = [z]

result = sum_gradients(tensors_to_grad)
print(result)
