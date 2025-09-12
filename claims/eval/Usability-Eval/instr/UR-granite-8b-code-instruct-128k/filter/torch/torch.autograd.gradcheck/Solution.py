import torch

def check_gradients(tensor, grad_fn, *args, **kwargs):
    tensor.requires_grad_(True)
    output = grad_fn(tensor, *args, **kwargs)
    output.backward()
    analytical_grad = tensor.grad
    finite_diff_grad = (tensor.clone() + 1e-5).grad
    return torch.allclose(analytical_grad, finite_diff_grad)
