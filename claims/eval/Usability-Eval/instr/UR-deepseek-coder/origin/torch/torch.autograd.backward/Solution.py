import torch

def sum_of_gradients(tensors):
    # Ensure all tensors require gradients
    for t in tensors:
        t.requires_grad_(True)

    # Compute the sum of the tensors
    sum_tensor = sum(tensors)

    # Compute the gradients
    sum_tensor.backward()

    # Collect the gradients of the leaf nodes
    gradients = [t.grad for t in tensors if t.grad is not None]

    # Sum the gradients
    total_gradient = sum(gradients)

    return total_gradient

# Example usage
tensor1 = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
tensor2 = torch.tensor([4.0, 5.0, 6.0], requires_grad=True)

result = sum_of_gradients([tensor1, tensor2])
print(result)
