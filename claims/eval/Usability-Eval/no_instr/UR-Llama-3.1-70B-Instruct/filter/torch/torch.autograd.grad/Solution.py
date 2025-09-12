import torch

def compute_sum_of_gradients(inputs, outputs):
    """
    Computes and returns the sum of gradients of outputs with respect to the inputs.
    
    Args:
    inputs (torch.Tensor): The input tensor.
    outputs (torch.Tensor): The output tensor.
    
    Returns:
    torch.Tensor: The sum of gradients of outputs with respect to the inputs.
    """
    
    # Require gradients for inputs
    inputs.requires_grad = True
    
    # Zero gradients
    inputs.grad = None
    
    # Backward pass
    outputs.sum().backward()
    
    # Compute the sum of gradients
    sum_of_gradients = inputs.grad.sum()
    
    return sum_of_gradients

# Example usage
if __name__ == "__main__":
    # Create a tensor for inputs
    inputs = torch.randn(3, 3, requires_grad=True)
    
    # Create a tensor for outputs
    outputs = inputs ** 2
    
    # Compute the sum of gradients
    sum_of_gradients = compute_sum_of_gradients(inputs, outputs)
    
    print("Sum of Gradients:", sum_of_gradients)
