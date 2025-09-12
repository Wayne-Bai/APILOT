import torch

def check_grad(f, inputs, grad_outputs, threshold=1e-5):
    """
    Check gradients of gradients computed via small finite differences against analytical gradients.

    Args:
        f (function): The function to compute gradients for.
        inputs (tuple): The inputs to the function.
        grad_outputs (tuple): The gradients of the outputs with respect to the inputs.
        threshold (float): The threshold for the difference between the finite difference and analytical gradients.

    Returns:
        bool: True if the gradients are close enough, False otherwise.
    """
    # Compute finite difference gradients
    finite_diff_grads = []
    for i in range(len(inputs)):
        input_tensor = inputs[i]
        grad_output = grad_outputs[i]
        h = 1e-5
        grad_input_fd = (f(input_tensor + h * grad_output) - f(input_tensor - h * grad_output)) / (2 * h)
        finite_diff_grads.append(grad_input_fd)

    # Compute analytical gradients
    analytical_grads = torch.autograd.grad(f(*inputs), inputs, grad_outputs)

    # Check if the gradients are close enough
    close_enough = True
    for i in range(len(inputs)):
        if torch.abs(finite_diff_grads[i] - analytical_grads[i]).item() > threshold:
            close_enough = False
            break

    return close_enough
