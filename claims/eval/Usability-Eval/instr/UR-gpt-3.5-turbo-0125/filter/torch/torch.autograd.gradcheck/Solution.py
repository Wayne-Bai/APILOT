
import torch

def compute_analytical_gradients(inputs, outputs):
    gradients = torch.autograd.grad(outputs, inputs, grad_outputs=torch.ones_like(outputs), create_graph=True)
    return gradients

def check_gradients(inputs, loss):
    outputs = loss(inputs)
    analytical_gradients = compute_analytical_gradients(inputs, outputs)

    for input_tensor, grad in zip(inputs, analytical_gradients):
        input_copy = input_tensor.detach().clone().requires_grad_(True)
        num_grad = torch.zeros_like(input_tensor)
        eps = 1e-6

        for i in range(input_tensor.numel()):
            input_copy.data = input_tensor.detach().clone().requires_grad_(True)
            input_copy.data.view(-1)[i] += eps
            perturbed_output = loss(input_copy)
            # Compute numerical gradient
            num_grad.view(-1)[i] = ((perturbed_output - outputs) / eps).sum()

        # Check gradients via small finite differences against analytical gradients
        assert torch.allclose(num_grad, grad, rtol=1e-3, atol=1e-5), f"Gradient check failed for tensor: {input_tensor}"

# Example usage:
# inputs = [torch.randn(3, 3, requires_grad=True)]
# loss = lambda x: x[0].sum()
# check_gradients(inputs, loss)
