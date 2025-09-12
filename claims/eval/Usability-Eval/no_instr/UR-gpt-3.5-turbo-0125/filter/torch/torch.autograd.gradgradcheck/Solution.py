
import torch

# Create tensor variables with requires_grad=True
inputs = torch.randn(3, requires_grad=True)
grad_outputs = torch.randn(3, requires_grad=True)

# Obtain gradients of gradients computed via small finite differences
torch.autograd.grad(
    torch.autograd.grad(inputs, inputs, grad_outputs=grad_outputs, create_graph=True, retain_graph=True),
    inputs
)
