
import torch

# Define a custom autograd function
class SumGrad(torch.autograd.Function):
    @staticmethod
    def forward(ctx, inputs):
        # Store information needed to compute gradients in ctx
        ctx.inputs = inputs
        return inputs

    @staticmethod
    def backward(ctx, grad_output):
        # Retrieve the input tensor and its gradient from context
        inputs = ctx.inputs
        grad_input = grad_output * torch.ones_like(inputs)
        return grad_input

# Define a test function that takes two tensors as input and computes their sum using the custom autograd function
def sum_grad(t1, t2):
    with torch.enable_grad():
        # Create a tensor that stores the result of the sum
        output = SumGrad.apply(torch.add(t1, t2))
        # Compute the gradient of the sum with respect to the input tensors
        grads = torch.autograd.grad(output, [t1, t2], retain_graph=True)
    return grads[0] + grads[1]

# Test the function
t1 = torch.randn(2, 3, requires_grad=True)
t2 = torch.randn(2, 3, requires_grad=True)
result = sum_grad(t1, t2)
print(result)
