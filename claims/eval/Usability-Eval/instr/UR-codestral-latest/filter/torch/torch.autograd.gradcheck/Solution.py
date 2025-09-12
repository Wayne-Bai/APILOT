import torch

def check_gradients(func, input):
    # Forward pass
    output = func(input)
    output.backward()

    # Analytical gradient
    analytical_grad = input.grad.data.clone()

    # Reset gradient
    input.grad.data.zero_()

    # Compute numerical gradient
    h = 1e-4
    eps = torch.randn(input.shape) * h

    output_plus_eps = func(input + eps)
    output_minus_eps = func(input - eps)

    numerical_grad = (output_plus_eps - output_minus_eps) / (2*h)

    # Compare
    diff = torch.abs(numerical_grad - analytical_grad).sum()
    print('Gradient difference:', diff)

    return diff

# Example usage
def func(x):
    return x.pow(2).sum()

input = torch.randn((10,), requires_grad=True)
diff = check_gradients(func, input)
