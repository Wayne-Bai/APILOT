import torch

# Define a simple neural network with one input and one output layer
model = torch.nn.Sequential(
    torch.nn.Linear(5, 3),
    torch.nn.ReLU(),
    torch.nn.Linear(3, 2)
)

# Define the inputs and outputs for the model
inputs = torch.randn(10, 5)
outputs = model(inputs)

# Compute the gradients of the outputs with respect to the inputs
gradients = torch.autograd.grad(outputs, inputs)

# Print the gradients
print(gradients)
