import torch

def finite_difference_gradients(func, inputs, grad_outputs, epsilon=1e-6):
    """
    Compute gradients via small finite differences.
    
    Args:
    - func: The function to compute gradients for.
    - inputs: The input tensors.
    - grad_outputs: The gradient outputs.
    - epsilon: Small perturbation for finite differences.
    
    Returns:
    - Finite difference gradients.
    """
    grads = []
    for i in range(len(inputs)):
        input_perturbed = [inp.clone() for inp in inputs]
        input_perturbed[i] += epsilon
        output_perturbed = func(*input_perturbed)
        grad_perturbed = torch.autograd.grad(output_perturbed, inputs, grad_outputs=grad_outputs, create_graph=True)[0]
        
        input_perturbed = [inp.clone() for inp in inputs]
        input_perturbed[i] -= epsilon
        output_perturbed = func(*input_perturbed)
        grad_perturbed_neg = torch.autograd.grad(output_perturbed, inputs, grad_outputs=grad_outputs, create_graph=True)[0]
        
        grads.append((grad_perturbed - grad_perturbed_neg) / (2 * epsilon))
    
    return grads

def check_gradients(func, inputs, grad_outputs, epsilon=1e-6, atol=1e-5, rtol=1e-3):
    """
    Check gradients of gradients computed via small finite differences against analytical gradients.
    
    Args:
    - func: The function to compute gradients for.
    - inputs: The input tensors.
    - grad_outputs: The gradient outputs.
    - epsilon: Small perturbation for finite differences.
    - atol: Absolute tolerance for comparison.
    - rtol: Relative tolerance for comparison.
    
    Returns:
    - Boolean indicating whether the gradients match within the specified tolerances.
    """
    # Compute analytical gradients
    outputs = func(*inputs)
    analytical_grads = torch.autograd.grad(outputs, inputs, grad_outputs=grad_outputs, create_graph=True)
    
    # Compute finite difference gradients
    finite_diff_grads = finite_difference_gradients(func, inputs, grad_outputs, epsilon)
    
    # Compare gradients
    for analytical_grad, finite_diff_grad in zip(analytical_grads, finite_diff_grads):
        if not torch.allclose(analytical_grad, finite_diff_grad, atol=atol, rtol=rtol):
            return False
    
    return True

# Example usage
def example_func(x, y):
    return x * y + x.sin()

x = torch.tensor([1.0, 2.0], requires_grad=True)
y = torch.tensor([3.0, 4.0], requires_grad=True)
grad_outputs = torch.tensor([1.0, 1.0])

print(check_gradients(example_func, [x, y], grad_outputs))
