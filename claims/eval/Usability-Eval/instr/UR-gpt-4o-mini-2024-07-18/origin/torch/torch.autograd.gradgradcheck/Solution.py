import torch

def check_gradients(func, inputs, grad_outputs, epsilon=1e-5):
    # Ensure the inputs are tensors with requires_grad=True
    for inp in inputs:
        inp.requires_grad_(True)

    # Compute analytical gradients using Torch's autograd
    outputs = func(*inputs)
    outputs.sum().backward()

    analytic_grads = [inp.grad for inp in inputs]
    
    # Clear gradients for the next calculation
    for inp in inputs:
        inp.grad = None

    finite_diff_grads = []
    
    for i in range(len(inputs)):
        # Get the input tensor
        inp = inputs[i]
        
        # Compute the finite difference gradient
        plus_epsilon = inp.clone() + epsilon
        minus_epsilon = inp.clone() - epsilon
        
        # Calculate the function outputs for perturbed inputs
        outputs_plus = func(*(inputs[:i] + (plus_epsilon,) + inputs[i+1:]))
        outputs_minus = func(*(inputs[:i] + (minus_epsilon,) + inputs[i+1:]))
        
        # Compute finite difference gradient
        finite_diff_grad = (outputs_plus.sum() - outputs_minus.sum()) / (2 * epsilon)
        finite_diff_grads.append(finite_diff_grad)

    return analytic_grads, finite_diff_grads

# Example usage:
def example_function(x, y):
    return x * y

# Defining inputs with requires_grad=True
x = torch.tensor([2.0], requires_grad=True)
y = torch.tensor([3.0], requires_grad=True)

analytic_grads, finite_diff_grads = check_gradients(example_function, [x, y], None)

print("Analytical Gradients:", [grad.item() for grad in analytic_grads])
print("Finite Difference Gradients:", [grad.item() for grad in finite_diff_grads])
