import torch

def sum_of_gradients(tensors):
    # Ensure all tensors require gradients
    for t in tensors:
        t.requires_grad_(True)

    # Compute the sum of the tensors
    sum_tensor = sum(tensors)

    # Perform a backward pass to compute gradients
    sum_tensor.backward()

    # Collect the gradients of the leaf nodes
    gradients = [t.grad for t in tensors]

    # Compute the sum of the gradients
    total_gradient_sum = sum(gradients)

    return total_gradient_sum

# Example usage
if __name__ == "__main__":
    tensor1 = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
    tensor2 = torch.tensor([4.0, 5.0, 6.0], requires_grad=True)

    tensors = [tensor1, tensor2]
    result = sum_of_gradients(tensors)
    print("Sum of gradients:", result)
