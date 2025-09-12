import torch

def finite_difference_grad(func, inputs, eps=1e-6):
    """
    Compute gradients using finite differences.
    
    Args:
    - func: The function to compute gradients for.
    - inputs: The input tensors.
    - eps: The small epsilon value for finite differences.
    
    Returns:
    - grads: The computed gradients using finite differences.
    """
    grads = []
    for input in inputs:
        if input.requires_grad and (input.is_floating_point() or input.is_complex()):
            input_flat = input.view(-1)
            grad_flat = torch.zeros_like(input_flat)
            for i in range(input_flat.numel()):
                input_flat[i] += eps
                y_plus = func(*inputs).sum()
                input_flat[i] -= 2 * eps
                y_minus = func(*inputs).sum()
                input_flat[i] += eps
                grad_flat[i] = (y_plus - y_minus) / (2 * eps)
            grads.append(grad_flat.view_as(input))
        else:
            grads.append(None)
    return grads

def check_gradients(func, inputs, atol=1e-5, rtol=1e-3):
    """
    Check gradients computed via small finite differences against analytical gradients.
    
    Args:
    - func: The function to compute gradients for.
    - inputs: The input tensors.
    - atol: Absolute tolerance for gradient comparison.
    - rtol: Relative tolerance for gradient comparison.
    
    Returns:
    - is_correct: A boolean indicating if the gradients match within the tolerance.
    """
    inputs = [input.clone().detach().requires_grad_(True) for input in inputs]
    outputs = func(*inputs)
    outputs.sum().backward()
    
    analytical_grads = [input.grad if input.requires_grad else None for input in inputs]
    finite_diff_grads = finite_difference_grad(func, inputs)
    
    is_correct = True
    for a_grad, f_grad in zip(analytical_grads, finite_diff_grads):
        if a_grad is not None and f_grad is not None:
            if not torch.allclose(a_grad, f_grad, atol=atol, rtol=rtol):
                is_correct = False
                break
    
    return is_correct

# Example usage:
def example_func(x, y):
    return x * y + x.sin()

x = torch.tensor([1.0, 2.0], requires_grad=True)
y = torch.tensor([3.0, 4.0], requires_grad=True)

print(check_gradients(example_func, [x, y]))  # Should print True if gradients are correct
