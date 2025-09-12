import torch

def check_gradients(tensor, grad_output):
    tensor.requires_grad_(True)
    grad_output.requires_grad_(True)
    tensor.backward(grad_output)
    analytical_gradients = tensor.grad
    finite_differences_gradients = (tensor - tensor.clone().detach() + 1e-6 * grad_output).grad
    return torch.allclose(analytical_gradients, finite_differences_gradients)
