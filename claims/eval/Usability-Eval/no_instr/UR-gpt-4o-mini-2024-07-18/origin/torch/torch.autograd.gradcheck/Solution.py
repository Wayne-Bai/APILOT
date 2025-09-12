import torch

def compute_analytical_gradient(func, inputs):
    # Compute the analytical gradient using autograd
    inputs.requires_grad_(True)
    output = func(*inputs)
    output.backward()
    return [input.grad.clone() for input in inputs]

def compute_finite_difference_gradient(func, inputs, epsilon=1e-6):
    gradients = []
    for i in range(len(inputs)):
        original_value = inputs[i].clone()

        # Create a small perturbation
        inputs[i] = original_value + epsilon
        output_plus = func(*inputs)

        inputs[i] = original_value - epsilon
        output_minus = func(*inputs)

        # Calculate the finite difference gradient
        grad = (output_plus - output_minus) / (2 * epsilon)
        gradients.append(grad)

        # Restore the original value
        inputs[i] = original_value

    return gradients

# Example function
def example_func(x, y):
    return x**2 + y**3

# Define inputs
x = torch.tensor(1.0, dtype=torch.float32, requires_grad=True)
y = torch.tensor(2.0, dtype=torch.float32, requires_grad=True)

# Compute gradients
analytical_grad = compute_analytical_gradient(example_func, [x, y])
finite_diff_grad = compute_finite_difference_gradient(example_func, [x, y])

# Print results
for i in range(len(analytical_grad)):
    print(f'Analytical Gradient {i}: {analytical_grad[i]}')
    print(f'Finite Difference Gradient {i}: {finite_diff_grad[i]}')
