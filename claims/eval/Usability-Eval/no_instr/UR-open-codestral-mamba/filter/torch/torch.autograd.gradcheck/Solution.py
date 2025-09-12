import torch
import numpy as np

def check_finite_difference(f, params, eps=1e-8):
    """Checks analytical gradient against finite difference gradients."""
    grad = torch.autograd.grad(f, params, create_graph=True)
    numeric_grad = []
    for p in params:
        if p.requires_grad:
            p_num = p.detach().clone().requires_grad_(True)
            f_num = torch.sum(f(p_num), p.requires_grad)
            numeric_grad.append(torch.autograd.grad(f_num, p_num)[0])
    return all(torch.allclose(g, n, eps) for g, n in zip(grad, numeric_grad))
