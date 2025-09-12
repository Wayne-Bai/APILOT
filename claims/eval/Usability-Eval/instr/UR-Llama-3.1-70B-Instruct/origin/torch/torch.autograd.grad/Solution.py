import torch

def sum_of_gradients(input_tensor, output_tensor):
    """
    Computes and returns the sum of gradients of outputs with respect to the inputs.

    Args:
        input_tensor (torch.Tensor): The input tensor.
        output_tensor (torch.Tensor): The output tensor.

    Returns:
        torch.Tensor: The sum of gradients of outputs with respect to the inputs.
    """

    # Check if the input and output tensors require gradients
    if not input_tensor.requires_grad or not output_tensor.requires_grad:
        raise ValueError("Both input and output tensors should require gradients.")

    # Create a new graph to compute gradients
    output_tensor = output_tensor.detach().requires_grad_(True)
    input_tensor = input_tensor.detach().requires_grad_(True)

    # Compute the gradients of the output with respect to the input
    gradients = torch.autograd.grad(output_tensor, input_tensor, torch.ones_like(output_tensor))[0]

    # Compute the sum of the gradients
    sum_of_gradients = torch.sum(gradients)

    return sum_of_gradients


# Example usage:
if __name__ == "__main__":
    # Create a dummy input tensor
    input_tensor = torch.randn(3, 5, requires_grad=True)

    # Create a dummy output tensor
    output_tensor = torch.randn(3, 5, requires_grad=True)

    # Define a simple model to compute the output from the input
    model = torch.nn.Linear(5, 5)
    model_output = model(input_tensor)

    # Compute the sum of gradients
    sum_of_gradients = sum_of_gradients(input_tensor, model_output)

    print(sum_of_gradients)
