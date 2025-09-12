import torch

def check_gradients(inputs, grad_outputs, eps=1e-5):
    for input, grad_output in zip(inputs, grad_outputs):
        if input.requires_grad:
            input.grad = None
            f = lambda: (input * grad_output).sum()
            f_prime = lambda: grad_output.sum()

            f_prime_numerical = (f(input + eps) - f(input)) / eps
            f_prime_analytical = f_prime(input)

            assert torch.isclose(f_prime_numerical, f_prime_analytical, atol=1e-3), \
                f"Gradient of gradient is not close to analytical gradient. Input: {input}, Grad_output: {grad_output}"

# Example usage:
inputs = [torch.tensor([1.0, 2.0], requires_grad=True), torch.tensor([3.0, 4.0], requires_grad=True)]
grad_outputs = [torch.tensor([5.0, 6.0]), torch.tensor([7.0, 8.0])]
check_gradients(inputs, grad_outputs)
