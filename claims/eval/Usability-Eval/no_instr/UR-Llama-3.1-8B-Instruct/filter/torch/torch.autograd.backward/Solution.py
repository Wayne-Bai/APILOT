import torch

def compute_gradients_sum(tensors):
    """
    This function computes the sum of gradients of given tensors with respect to graph leaves.

    Args:
        tensors (list of torch.Tensor): List of tensors.

    Returns:
        torch.Tensor: The sum of gradients of given tensors.
    """
    # Initialize variables to keep track of the sum of gradients
    total_grad = 0.0

    # Iterate over each tensor in the input list
    for tensor in tensors:
        # Compute the sum of gradients for the current tensor using grad() method
        # If a tensor has an None gradient, use grad.default to return a tensor with the same shape and data type as the input.
        if tensor.grad is not None:
            total_grad += torch.sum(tensor.grad)

    return total_grad

# Example usage
if __name__ == "__main__":
    # Initialize tensors and compute their gradients
    tensors = [torch.tensor(2.0, requires_grad=True), torch.tensor(3.0, requires_grad=True)]
    loss = 5.0 * (tensors[0] + tensors[1])
    loss.backward()

    result = compute_gradients_sum(tensors)
    print(result)
