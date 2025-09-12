import torch

def check_gradients(input, grad_output, eps=1e-5):
    # Check gradients of inputs
    input_grad = torch.autograd.grad(input, input, grad_output, retain_graph=True, create_graph=True)
    input_grad_finite_diff = (input_grad[0] - torch.autograd.grad(input, input, torch.zeros_like(grad_output), retain_graph=True, create_graph=True, eps=eps))[0]
    assert torch.allclose(input_grad_finite_diff, torch.zeros_like(input), atol=1e-5)

    # Check gradients of grad_outputs
    grad_output_grad = torch.autograd.grad(grad_output, grad_output, input, retain_graph=True, create_graph=True)
    grad_output_grad_finite_diff = (grad_output_grad[0] - torch.autograd.grad(grad_output, grad_output, torch.zeros_like(input), retain_graph=True, create_graph=True, eps=eps)[0])
    assert torch.allclose(grad_output_grad_finite_diff, torch.zeros_like(grad_output), atol=1e-5)

# Example usage
input = torch.randn(10, requires_grad=True)
grad_output = torch.randn(10, requires_grad=True)
check_gradients(input, grad_output)
