import torch

# Define the function to check gradients
def check_gradients(tensor, grad_output):
    # Compute gradients using small finite differences
    numerical_grad = (tensor + 0.0001 * torch.randn_like(tensor)).sum()

    # Analytical gradient
    analytical_grad = torch.autograd.grad(tensor, grad_output, create_graph=True)[0]

    # Check if the gradients are equal
    if torch.allclose(numerical_grad, analytical_grad):
        print("Gradients are equal")
    else:
        print("Gradients are not equal")

# Define the tensor and grad_output
tensor = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
grad_output = torch.tensor([0.1, 0.2, 0.3])

# Check the gradients
check_gradients(tensor, grad_output)