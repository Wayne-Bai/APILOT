
import torch

def gradient_sum(tensors, variables):
    """
    Computes the sum of gradients of given tensors with respect to graph leaves.

    Args:
        tensors (list): List of tensors to compute the gradients for.
        variables (list): List of graph leaf variables.

    Returns:
        list: List of summed gradients for each tensor in `tensors`.
    """
    # Compute the gradients of each tensor with respect to the variables
    grads = [torch.autograd.grad(tensor, variables) for tensor in tensors]
    # Sum the gradients along the first dimension (number of tensors)
    return [sum(grad) for grad in zip(*grads)]
