import torch

def check_analytical_gradients(f, x):
    # Compute analytical gradient
    analytical_grad = torch.autograd.grad(f(x), x, create_graph=True)[0]

    # Compute gradient via small finite differences
    h = torch.tensor(1e-7, dtype=x.dtype)
    numerical_grad = torch.autograd.grad(f(x + h).sum(), x, create_graph=True)[0] - torch.autograd.grad(f(x - h).sum(), x, create_graph=True)[0]

    return analytical_grad, numerical_grad

# Example usage
def f(x):
    return x**2 + 3*x + 2

x = torch.tensor([1.0], requires_grad=True, dtype=torch.float32)

analytical, numerical = check_analytical_gradients(f, x)
print("Analytical Gradient:", analytical.item())
print("Numerical Gradient:", numerical.item())
