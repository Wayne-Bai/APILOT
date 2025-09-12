import torch

def finite_difference_gradients(inputs, grad_outputs, epsilon=1e-6):
    """
    Compute gradients via small finite differences.
    
    Args:
    - inputs (torch.Tensor): Input tensor with requires_grad=True.
    - grad_outputs (torch.Tensor): Gradients with respect to the output.
    - epsilon (float): Small perturbation for finite differences.
    
    Returns:
    - torch.Tensor: Gradients computed via finite differences.
    """
    inputs = inputs.detach().requires_grad_(True)
    grad_outputs = grad_outputs.detach()
    
    # Compute the original output
    outputs = torch.sum(inputs * grad_outputs)
    outputs.backward(retain_graph=True)
    analytical_grads = inputs.grad.clone()
    
    # Compute gradients via finite differences
    finite_diff_grads = torch.zeros_like(inputs)
    for i in range(inputs.numel()):
        inputs_perturbed = inputs.clone().detach()
        inputs_perturbed.requires_grad_(True)
        inputs_perturbed.view(-1)[i] += epsilon
        
        outputs_perturbed = torch.sum(inputs_perturbed * grad_outputs)
        outputs_perturbed.backward(retain_graph=True)
        finite_diff_grads.view(-1)[i] = (outputs_perturbed.item() - outputs.item()) / epsilon
    
    return finite_diff_grads, analytical_grads

def check_gradients(inputs, grad_outputs, epsilon=1e-6, tolerance=1e-5):
    """
    Check gradients of gradients computed via small finite differences against analytical gradients.
    
    Args:
    - inputs (torch.Tensor): Input tensor with requires_grad=True.
    - grad_outputs (torch.Tensor): Gradients with respect to the output.
    - epsilon (float): Small perturbation for finite differences.
    - tolerance (float): Tolerance for gradient comparison.
    
    Returns:
    - bool: True if gradients match within tolerance, False otherwise.
    """
    finite_diff_grads, analytical_grads = finite_difference_gradients(inputs, grad_outputs, epsilon)
    
    # Compare finite difference gradients with analytical gradients
    grad_diff = torch.abs(finite_diff_grads - analytical_grads)
    max_diff = torch.max(grad_diff)
    
    if max_diff > tolerance:
        print(f"Gradients do not match! Maximum difference: {max_diff}")
        return False
    else:
        print(f"Gradients match within tolerance. Maximum difference: {max_diff}")
        return True

# Example usage
inputs = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
grad_outputs = torch.tensor([0.1, 0.2, 0.3])

check_gradients(inputs, grad_outputs)
