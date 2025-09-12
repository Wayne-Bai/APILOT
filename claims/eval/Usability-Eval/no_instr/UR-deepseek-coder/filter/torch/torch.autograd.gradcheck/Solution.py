import torch

def finite_difference_gradients(func, inputs, epsilon=1e-6):
    """
    Compute gradients via finite differences.

    Args:
        func (callable): The function to compute gradients for.
        inputs (torch.Tensor): The input tensor with requires_grad=True.
        epsilon (float): The small perturbation for finite differences.

    Returns:
        torch.Tensor: The computed finite difference gradients.
    """
    inputs = inputs.detach().requires_grad_(True)
    outputs = func(inputs)
    grad_outputs = torch.ones_like(outputs, requires_grad=False)
    analytical_grads = torch.autograd.grad(outputs, inputs, grad_outputs=grad_outputs, create_graph=True)[0]

    # Compute finite difference gradients
    inputs_perturbed = inputs.detach().clone()
    inputs_perturbed.requires_grad_(False)
    finite_diff_grads = torch.zeros_like(inputs)

    for i in range(inputs.numel()):
        inputs_perturbed.view(-1)[i] += epsilon
        outputs_perturbed = func(inputs_perturbed)
        finite_diff_grads.view(-1)[i] = (outputs_perturbed - outputs) / epsilon
        inputs_perturbed.view(-1)[i] -= epsilon

    return finite_diff_grads, analytical_grads

def check_gradients(func, inputs, epsilon=1e-6, tolerance=1e-5):
    """
    Check gradients computed via small finite differences against analytical gradients.

    Args:
        func (callable): The function to compute gradients for.
        inputs (torch.Tensor): The input tensor with requires_grad=True.
        epsilon (float): The small perturbation for finite differences.
        tolerance (float): The tolerance for gradient comparison.

    Returns:
        bool: True if the gradients match within the tolerance, False otherwise.
    """
    finite_diff_grads, analytical_grads = finite_difference_gradients(func, inputs, epsilon)
    return torch.allclose(finite_diff_grads, analytical_grads, atol=tolerance, rtol=tolerance)

# Example usage:
def example_function(x):
    return x.sin() + x.cos()

inputs = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
print(check_gradients(example_function, inputs))
