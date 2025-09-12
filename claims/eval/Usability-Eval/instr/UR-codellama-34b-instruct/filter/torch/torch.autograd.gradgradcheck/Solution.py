
import torch
import numpy as np

def check_gradients(model, inputs, grad_outputs):
    # Calculate the analytical gradients for the tensors in inputs and grad_outputs
    analytical_gradients = model.backward(inputs, grad_outputs)

    # Calculate the finite difference gradients for the tensors in inputs and grad_outputs
    epsilon = 1e-6
    h = np.sqrt(epsilon)
    gradients = []
    for input in inputs:
        # Create a copy of the input tensor with a small perturbation added to it
        perturbed_input = input + torch.tensor(h, requires_grad=True)
        # Calculate the loss using the perturbed input and the original grad_outputs
        perturbed_loss = model(perturbed_input, grad_outputs).sum()
        # Calculate the gradient of the loss with respect to the input tensor
        gradient = torch.autograd.grad(perturbed_loss, perturbed_input, create_graph=True)[0]
        # Add the calculated gradient to the list of gradients
        gradients.append(gradient)

    # Check if the analytical and finite difference gradients are close enough
    for i in range(len(analytical_gradients)):
        analytical_gradient = analytical_gradients[i]
        finite_difference_gradient = gradients[i]
        max_error = np.max(np.abs(analytical_gradient - finite_difference_gradient))
        if max_error > 1e-6:
            print(f"Gradient {i} is not close enough! Max error: {max_error}")

# Example usage
model = torch.nn.Linear(5, 3)
inputs = [torch.randn(4, requires_grad=True), torch.randn(5, requires_grad=True)]
grad_outputs = model(inputs[0], inputs[1])
check_gradients(model, inputs, grad_outputs)
