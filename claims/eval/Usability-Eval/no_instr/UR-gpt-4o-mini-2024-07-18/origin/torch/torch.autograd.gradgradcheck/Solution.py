import torch

def check_gradients(model, input_tensors, grad_outputs, epsilon=1e-5):
    """
    Check gradients of gradients computed via small finite differences against analytical gradients.
    
    Parameters:
    model: The model or function whose gradients are being computed.
    input_tensors: A list of input tensors with requires_grad=True.
    grad_outputs: A tensor for gradient output.
    epsilon: A small value for finite differences.
    
    Returns:
    None
    """
    # Ensure that inputs are tensors with gradient tracking enabled
    for tensor in input_tensors:
        assert tensor.requires_grad, "Input tensors must have requires_grad=True"
    
    # Compute analytical gradients
    model.zero_grad()
    output = model(*input_tensors)
    output.backward(grad_outputs)
    
    analytical_grads = [tensor.grad.clone() for tensor in input_tensors]
    
    # Clear the gradients
    for tensor in input_tensors:
        tensor.grad.data.zero_()
    
    # Compute gradients using finite differences
    finite_diffs_grads = []
    
    for i, tensor in enumerate(input_tensors):
        # Create a tensor for perturbation
        perturbation = torch.tensor(epsilon, dtype=tensor.dtype, device=tensor.device)
        
        # f(x + h)
        output_plus = model(*(t.clone() if j != i else t + perturbation for j, t in enumerate(input_tensors)))
        
        # f(x - h)
        output_minus = model(*(t.clone() if j != i else t - perturbation for j, t in enumerate(input_tensors)))
        
        # Central difference to estimate the gradient
        finite_grad = (output_plus - output_minus) / (2 * epsilon)
        
        finite_diffs_grads.append(finite_grad)
    
    # Compare gradients
    for i, (analytical_grad, finite_grad) in enumerate(zip(analytical_grads, finite_diffs_grads)):
        # Check if the gradients are similar
        if torch.allclose(analytical_grad, finite_grad, atol=1e-5):
            print(f"Gradients match for input tensor {i}.")
        else:
            print(f"Gradients do not match for input tensor {i}.")
            print(f"Analytical gradient: {analytical_grad}")
            print(f"Finite difference gradient: {finite_grad}")

# Example usage:
# model = ...  # define your model
# input_tensors = [torch.randn(2, 2, requires_grad=True, dtype=torch.float32)]
# grad_outputs = torch.ones_like(model(*input_tensors))
# check_gradients(model, input_tensors, grad_outputs)
