import torch

def check_gradients(tensors, grad_outputs, grad_gradients):
    inputs = (tensors,) if not isinstance(tensors, tuple) else tensors
    grad_outputs = (grad_outputs,) if not isinstance(grad_outputs, tuple) else grad_outputs

    for inp, grad_output in zip(inputs, grad_outputs):
        inp.requires_grad = True
        grad = torch.autograd.grad(grad_output, inp, create_graph=True)[0]

        for inp_tensor in inp:
            finite_diff_grad = (inp_tensor + 1e-6).requires_grad_(True).backward(retain_graph=True)[0] - (inp_tensor - 1e-6).requires_grad_(True).backward(retain_graph=True)[0]
            assert torch.allclose(grad, finite_diff_grad, rtol=1e-5, atol=1e-5)
            print(f"Gradient of gradient w.r.t {id(inp_tensor)} computed via finite differences: {finite_diff_grad}")
            print(f"Analytical gradient w.r.t {id(inp_tensor)}: {grad}")

    grad_gradients = (grad_gradients,) if not isinstance(grad_gradients, tuple) else grad_gradients
    for grad_grad in grad_gradients:
        grad_grad.requires_grad = True
        finite_diff_grad_grad = (grad_grad + 1e-6).backward()[0] - (grad_grad - 1e-6).backward()[0]
        assert torch.allclose(grad, finite_diff_grad_grad, rtol=1e-5, atol=1e-5)
        print(f"Gradient of gradient computed via finite differences: {finite_diff_grad_grad}")
        print(f"Analytical gradient: {grad}")

# Example usage:
tensors = torch.randn(1, requires_grad=True)
grad_outputs = torch.randn(1, requires_grad=True)
grad_gradients = torch.randn(1, requires_grad=True)
check_gradients(tensors, grad_outputs, grad_gradients)
