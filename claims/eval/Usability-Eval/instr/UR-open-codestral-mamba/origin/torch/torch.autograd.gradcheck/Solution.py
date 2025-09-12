import torch

def check_gradients(model, inputs, targets):
    """
    This function checks the gradients computed via small finite differences against analytical gradients
    for input tensors that require gradient computation.

    Args:
    model (torch.nn.Module): The neural network model.
    inputs (list of torch.Tensor): The input tensors.
    targets (torch.Tensor): The target tensor.

    Returns:
    None
    """
    # Set the gradient tensors to zero
    for input_tensor in inputs:
        if input_tensor.requires_grad:
            input_tensor.grad = torch.zeros_like(input_tensor)

    # Compute the output
    output = model(inputs)

    # Compute the loss
    loss = torch.nn.functional.mse_loss(output, targets)

    # Compute the gradients
    loss.backward()

    # Check the gradients computed via small finite differences against the analytical gradients
    epsilon = 1e-7
    for input_tensor in inputs:
        if input_tensor.requires_grad:
            numerical_grad = torch.zeros_like(input_tensor)
            analytical_grad = input_tensor.grad

            for i in range(input_tensor.numel()):
                temp_val = input_tensor.data.flatten()[i]

                # f(x+e)
                input_tensor.data.flatten()[i] = temp_val + epsilon
                fx_plus_e = model(inputs)

                # f(x-e)
                input_tensor.data.flatten()[i] = temp_val - epsilon
                fx_minus_e = model(inputs)

                # Gradient approximation with finite differences
                numerical_grad.data.flatten()[i] = (fx_plus_e.sum() - fx_minus_e.sum()) / (2 * epsilon)

                # Restore the original value
                input_tensor.data.flatten()[i] = temp_val

            # Compare the numerical and analytical gradients
            assert torch.allclose(numerical_grad, analytical_grad, rtol=1e-3, atol=1e-5), "Numerical and analytical gradients do not match"

# Example usage:
# Define the model
model = MyModel()

# Define the inputs and targets
inputs = [torch.randn(2, 2, requires_grad=True), torch.randn(3, 3, requires_grad=True)]
targets = torch.randn(2, requires_grad=True)

# Check the gradients
check_gradients(model, inputs, targets)
