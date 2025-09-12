import torch

def grad_check(func, *args, eps=1e-6, atol=1e-4):
    # Compute analytical gradients using autograd
    args = [arg.detach().requires_grad_() for arg in args]
    out = func(*args)
    grad_outputs = torch.ones_like(out)
    grads = torch.autograd.grad(out, args, grad_outputs=grad_outputs, create_graph=True)

    # Compute gradients of gradients using finite differences
    grad2_est = []
    for i, arg in enumerate(args):
        grad2_i = torch.zeros_like(arg)
        for j in range(arg.nelement()):
            eps_ij = torch.zeros_like(arg)
            eps_ij.view(-1)[j] += eps
            out1 = func(*(arg + eps_ij for arg in args))
            out2 = func(*(arg - eps_ij for arg in args))
            grad2_ij = (out1.grad_fn(grad_outputs) - out2.grad_fn(grad_outputs)) / (2.0 * eps)
            grad2_i.view(-1)[j] = grad2_ij.view(-1)[j]
        grad2_est.append(grad2_i)

    # Compare analytical and estimated gradients of gradients
    for grad_est, grad_analytic in zip(grad2_est, grads):
        assert torch.allclose(grad_est, grad_analytic, atol=atol), \
            "Gradients are different: {} vs {}".format(grad_est, grad_analytic)

# Test the function with a simple function: f(x) = x^2
func = lambda x: x ** 2
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
grad_check(func, x)
