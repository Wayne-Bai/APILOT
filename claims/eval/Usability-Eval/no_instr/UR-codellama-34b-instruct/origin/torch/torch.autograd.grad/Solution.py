import torch
from torch import nn, optim

class GradientSum(nn.Module):
    def __init__(self):
        super(GradientSum, self).__init__()
        # Initialize gradient accumulator with zeros
        self.grad_acc = torch.zeros_like(self.input)

    def forward(self, input, output):
        # Compute the gradients of outputs with respect to inputs
        gradients = torch.autograd.grad(outputs=output, inputs=input, grad_outputs=torch.ones_like(output), create_graph=True)
        # Accumulate the gradients
        self.grad_acc += gradients[0]
        return output

    def backward(self, input, output):
        # Return the accumulated gradients
        return self.grad_acc
