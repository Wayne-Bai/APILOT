import torch

def sum_of_gradients(inputs, network):
    # Forward pass
    outputs = network(inputs)

    # Zero the gradients
    torch.autograd.set_grad_enabled(True)
    outputs = outputs.detach()
    outputs.requires_grad_(True)

    # Compute the gradient
    gradients = torch.autograd.grad(outputs, inputs, create_graph=True)

    # Sum the gradients
    grad_sum = torch.sum(torch.abs(gradients[0])).item()

    return grad_sum

# Example usage:
inputs = torch.tensor([1.0, 2.0, 3.0], require_grad=True)
network = torch.nn.Sequential(
    torch.nn.Linear(3, 1),
    torch.nn.ReLU()
)
outputs = network(inputs)

# Compute the sum of gradients
sum_gradients = sum_of_gradients(inputs, network)
print("Sum of gradients:", sum_gradients)
