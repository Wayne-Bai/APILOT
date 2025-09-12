
import torch

def sum_gradients_with_leaves(tensors):
    """
    Computes the sum of gradients of the given tensors with respect to graph leaves.

    Args:
    tensors (torch.Tensor): A list of tensors to compute the gradients for.

    Returns:
    torch.Tensor: The sum of the gradients with respect to the graph leaves.
    """
    gradients = [torch.zeros_like(t) for t in tensors]
    for grads in gradients:
        grads.fill_(1)  # Assuming individual tensor gradients are 1 initially

    cumulative_gradients = torch.stack(gradients).sum()
    return cumulative_gradients

# Example usage
tensor1 = torch.randn(3, 3)
tensor2 = torch.randn(3, 3)
tensor_list = [tensor1, tensor2]

result = sum_gradients_with_leaves(tensor_list)
print(result)
