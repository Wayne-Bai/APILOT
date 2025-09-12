import torch

# Set the seed for reproducibility
torch.manual_seed(0)

# Function to check gradients
def check_gradients(func, inputs, grad_outputs=None, grad_inputs=None, eps=1e-6):
    outputs = func(*inputs)
    num_inputs = len(inputs)
    for i in range(num_inputs):
        if inputs[i].is_complex() or inputs[i].dtype in [torch.float16, torch.float32, torch.float64]:
            if inputs[i].requires_grad:
                if grad_outputs is None:
                    grad_outputs = [torch.ones_like(outputs)]
                flat_grad = torch.reshape(grad_outputs[0], [-1])
                num_params = flat_grad.numel()
                flat_input = torch.reshape(inputs[i], [-1])
                for j in range(num_params):
                    inputs_copy = list(inputs)
                    inputs_copy[i] = inputs[i].clone().detach().requires_grad_()
                    outputs_copy = func(*inputs_copy)
                    outputs_copy_flat = torch.reshape(outputs_copy, [-1])
                    inputs_copy[i].data = inputs_copy[i].data.clone() + eps * torch.ones_like(inputs_copy[i].data) * flat_input[j]
                    outputs_copy_perturb = func(*inputs_copy)
                    outputs_copy_perturb_flat = torch.reshape(outputs_copy_perturb, [-1])
                    grad_fd = (outputs_copy_perturb_flat - outputs_copy_flat) / eps
                    outputs_copy.backward(grad_outputs[0], retain_graph=True)
                    inputs_copy[i].grad.data = inputs_copy[i].grad.data.squeeze()
                    grad_analytical = inputs_copy[i].grad
                    assert torch.allclose(grad_analytical.squeeze(), grad_fd.squeeze(), atol=5 * eps), "Gradient mismatch"

# Test the function
def func(input1, input2):
    return input1.sum() + input2.sum()

inputs = [torch.randn(2, 2, requires_grad=True), torch.randn(2, 2, requires_grad=True)]
check_gradients(func, inputs)

inputs = [torch.randn(2, 2, dtype=torch.complex64, requires_grad=True), torch.randn(2, 2, dtype=torch.complex64, requires_grad=True)]
check_gradients(func, inputs)
