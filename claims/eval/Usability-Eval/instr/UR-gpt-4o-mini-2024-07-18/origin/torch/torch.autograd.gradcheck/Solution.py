import torch

def check_gradients(func, inputs, epsilon=1e-5):
    """
    Check gradients computed via finite differences against analytical gradients.
    
    Parameters:
    - func: The function for which to compute gradients.
    - inputs: A tuple of input tensors with requires_grad=True.
    - epsilon: The finite difference step size.
    """
    
    # Enable gradients computation
    for input in inputs:
        input.requires_grad = True
    
    # Compute analytical gradients
    analytical_gradients = torch.autograd.grad(func(*inputs), inputs)

    # Finite difference approximation
    finite_diffs = []
    for i, input in enumerate(inputs):
        # Create a tensor for finite difference
        input_plus = input.clone().detach()
        input_plus += epsilon
        input_plus.requires_grad = True

        input_minus = input.clone().detach()
        input_minus -= epsilon
        input_minus.requires_grad = True
        
        # Compute function values
        f_plus = func(*inputs[:i] + (input_plus,) + inputs[i+1:])
        f_minus = func(*inputs[:i] + (input_minus,) + inputs[i+1:])

        # Calculate the finite difference gradient
        finite_diff = (f_plus - f_minus) / (2 * epsilon)
        finite_diffs.append(finite_diff)

    # Compare analytical with finite difference gradients
    for analytical, finite in zip(analytical_gradients, finite_diffs):
        if analytical is not None:
            print(f"Analytical gradient: {analytical}")
            print(f"Finite difference gradient: {finite}")
            print(f"Difference: {torch.abs(analytical - finite).max()}")

# Example usage
def example_func(x, y):
    return torch.sum(x ** 2) + torch.sum(y ** 2)

x = torch.tensor([1.0, 2.0], requires_grad=True)
y = torch.tensor([3.0, 4.0], requires_grad=True)

check_gradients(example_func, (x, y))
