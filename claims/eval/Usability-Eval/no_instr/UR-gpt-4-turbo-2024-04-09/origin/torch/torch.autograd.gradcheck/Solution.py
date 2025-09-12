import torch

# Function to approximate gradient via small finite differences
def finite_difference_grad(func, inputs, eps=1e-6):
    inputs = [inp.clone().requires_grad_(True) for inp in inputs if inp.requires_grad]

    out = func(*inputs)
    grads_fd = []
    
    for i, inp in enumerate(inputs):
        grad_approx = []
        for j in range(inp.numel()):
            original = inp.flatten()[j].item()
            
            # Increment by eps
            inp.flatten()[j] = original + eps
            out1 = func(*inputs)
            
            # Decrement by eps
            inp.flatten()[j] = original - eps
            out2 = func(*inputs)
            
            # Finite difference approximation
            grad_approx_elem = ((out1 - out2) / (2 * eps)).detach()
            grad_approx.append(grad_approx_elem)
            
            # Reset the value
            inp.flatten()[j] = original

        grad_approx_tensor = torch.tensor(grad_approx).reshape(inp.shape)
        grads_fd.append(grad_approx_tensor)

    return grads_fd

# Analytical gradients computation using autograd
def analytical_grad(func, inputs):
    inputs = [inp.clone().requires_grad_(True) for inp in inputs if inp.requires_grad]
    
    out = func(*inputs)
    out.backward()
    
    grads_analytical = [inp.grad for inp in inputs]
    return grads_analytical

# Example Function and Input
def example_function(x, y):
    return x * x * y + y * torch.sin(x)

# Example inputs
x = torch.randn(3, 3, dtype=torch.float32, requires_grad=True)
y = torch.randn(3, 3, dtype=torch.float32, requires_grad=True)
inputs = [x, y]

# Compute gradients
grads_fd = finite_difference_grad(example_function, inputs)
grads_analytical = analytical_grad(example_function, inputs)

# Print results
print("Finite Difference Gradients:", grads_fd)
print("Analytical Gradients:", grads_analytical)
